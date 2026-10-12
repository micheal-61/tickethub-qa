\# DEF-07: PAID + cancel goes to CANCELLED, not REFUND\_PENDING

\- \*\*REQ violated:\*\* REQ-F7

\- \*\*Environment:\*\* Python 3.14.8

\- \*\*Steps:\*\* `o = Order(1,"PUBLIC"); o.pay(); o.cancel()`

\- \*\*Expected:\*\* state == "REFUND\_PENDING"

\- \*\*Actual:\*\* state == "CANCELLED"

\- \*\*Severity:\*\* Critical — money taken, no refund path

\- \*\*Priority:\*\* High

\- \*\*Evidence:\*\* test\_TC36\_valid\_transitions\[PAID-cancel-REFUND\_PENDING]

\- \*\*Suspected root cause:\*\* transition table maps ("PAID","cancel") -> "CANCELLED"

\- \*\*Related tests:\*\* TC-36, TC-38, TC-41 (many)

