"""Automated suite for TicketHub. Traceable to TC IDs and REQ IDs."""
import importlib, os, sys
from decimal import Decimal as D
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
th = importlib.import_module("tickethub")
Order, InvalidTransitionError = th.Order, th.InvalidTransitionError


# REQ-F1 quantity (TC-01..TC-08)
@pytest.mark.parametrize("q", [1, 2, 4, 9, 10], ids=lambda q: f"TC-q{q}")
def test_TC01_quantity_valid(q):
    assert th.calculate_total(q, "PUBLIC") > 0

@pytest.mark.parametrize("q", [0, -1, 11, 100])
def test_TC06_quantity_out_of_range(q):
    with pytest.raises(ValueError):
        th.calculate_total(q, "PUBLIC")

@pytest.mark.parametrize("q", [2.5, "3", None, True], ids=["float", "str", "none", "bool"])
def test_TC07_quantity_wrong_type(q):
    with pytest.raises(TypeError):
        th.calculate_total(q, "PUBLIC")


# REQ-F2 customer type (TC-09..TC-12)
@pytest.mark.parametrize("t", ["student", "ALUMNI", "", None])
def test_TC09_invalid_customer_type(t):
    with pytest.raises(ValueError):
        th.calculate_total(1, t)


# REQ-F4 discount rules (TC-15..TC-27)
@pytest.mark.parametrize("q,t,promo,rate", [
    (4, "STUDENT", None, "0.20"),
    (7, "STUDENT", None, "0.25"),
    (4, "STUDENT", "SAVE10", "0.25"),
    (4, "STAFF", None, "0.10"),
    (7, "STAFF", None, "0.15"),
    (7, "STAFF", "SAVE10", "0.20"),
    (4, "PUBLIC", None, "0"),
    (7, "PUBLIC", None, "0.05"),
    (4, "PUBLIC", "SAVE10", "0.10"),
])
def test_TC15_discount_rules(q, t, promo, rate):
    assert th.calculate_discount(q, t, promo) == D(rate)

def test_TC24_bulk_threshold_5():
    assert th.calculate_discount(5, "PUBLIC") == D("0.05")
    assert th.calculate_discount(4, "PUBLIC") == D("0")

def test_TC25_cap_25_percent():
    assert th.calculate_discount(4, "STUDENT", "SAVE10") == D("0.25")

def test_TC26_promo_and_bulk_do_not_stack():
    assert th.calculate_discount(5, "PUBLIC", "SAVE10") == D("0.10")
    assert th.calculate_discount(7, "STAFF", "SAVE10") == D("0.20")
    assert th.calculate_discount(7, "STUDENT", "SAVE10") == D("0.25")


# REQ-F5 totals and rounding (TC-28..TC-31)
@pytest.mark.parametrize("q,t,promo,total", [
    (1, "PUBLIC", None, "19.99"),
    (4, "PUBLIC", None, "79.96"),
    (3, "STAFF", None, "53.97"),
])
def test_TC28_totals_exact(q, t, promo, total):
    assert th.calculate_total(q, t, promo) == D(total)

def test_TC31_rounding_half_up():
    assert th.calculate_total(3, "STUDENT") == D("47.98")
    assert th.calculate_total(5, "PUBLIC") == D("94.95")
    assert th.calculate_total(5, "STUDENT") == D("74.96")


# REQ-F6 promo case-sensitivity (TC-32..TC-35)
@pytest.mark.parametrize("code", ["BADCODE", "", "SAVE20"])
def test_TC32_invalid_promo(code):
    with pytest.raises(ValueError):
        th.calculate_total(1, "PUBLIC", code)

def test_TC33_promo_case_sensitive():
    with pytest.raises(ValueError):
        th.calculate_total(1, "PUBLIC", "save10")


# REQ-F7 state transitions (TC-36..TC-60)
def _order_in(state):
    o = Order(1, "PUBLIC")
    path = {"CREATED": [], "PAID": ["pay"], "CANCELLED": ["cancel"],
            "COLLECTED": ["pay", "collect"],
            "REFUND_PENDING": ["pay", "cancel"],
            "REFUNDED": ["pay", "cancel", "complete_refund"]}[state]
    for ev in path:
        getattr(o, ev)()
    return o

VALID = [("CREATED", "pay", "PAID"), ("CREATED", "cancel", "CANCELLED"),
         ("PAID", "cancel", "REFUND_PENDING"),
         ("PAID", "collect", "COLLECTED"),
         ("REFUND_PENDING", "complete_refund", "REFUNDED")]

@pytest.mark.parametrize("s,ev,nxt", VALID)
def test_TC36_valid_transitions(s, ev, nxt):
    o = _order_in(s)
    getattr(o, ev)()
    assert o.state == nxt

STATES = ["CREATED", "PAID", "COLLECTED", "REFUND_PENDING", "REFUNDED", "CANCELLED"]
EVENTS = ["pay", "cancel", "collect", "complete_refund"]
VALID_PAIRS = {("CREATED", "pay"), ("CREATED", "cancel"), ("PAID", "cancel"),
               ("PAID", "collect"), ("REFUND_PENDING", "complete_refund")}

@pytest.mark.parametrize("s", STATES)
@pytest.mark.parametrize("ev", EVENTS)
def test_TC41_invalid_transitions(s, ev):
    if (s, ev) in VALID_PAIRS:
        pytest.skip("valid pair")
    o = _order_in(s)
    with pytest.raises(InvalidTransitionError):
        getattr(o, ev)()
    assert o.state == s

def test_TC60a_path_pay_collect():
    o = Order(1, "PUBLIC"); o.pay(); o.collect()
    assert o.state == "COLLECTED"

def test_TC60b_path_pay_cancel_refund():
    o = Order(1, "PUBLIC"); o.pay(); o.cancel(); o.complete_refund()
    assert o.state == "REFUNDED"