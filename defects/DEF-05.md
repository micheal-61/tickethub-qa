\# DEF-05: Promo and bulk discounts stack

\- \*\*REQ violated:\*\* REQ-F4 ("promo and bulk never combine")

\- \*\*Environment:\*\* Python 3.14.8

\- \*\*Steps:\*\* `calculate\_discount(7, "STAFF", "SAVE10")`

\- \*\*Expected:\*\* Decimal("0.20")

\- \*\*Actual:\*\* Decimal("0.25")

\- \*\*Severity:\*\* Critical — over-discount

\- \*\*Priority:\*\* High

\- \*\*Evidence:\*\* test\_TC26\_promo\_and\_bulk\_do\_not\_stack

\- \*\*Suspected root cause:\*\* promo and bulk added unconditionally

\- \*\*Related tests:\*\* TC-26, TC-15\[STAFF-SAVE10]

