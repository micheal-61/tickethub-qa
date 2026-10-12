\# DEF-03: Discount cap is 30%, not 25%

\- \*\*REQ violated:\*\* REQ-F4 (cap = 25%)

\- \*\*Environment:\*\* Python 3.14.8

\- \*\*Steps:\*\* `calculate\_discount(4, "STUDENT", "SAVE10")`

\- \*\*Expected:\*\* Decimal("0.25")

\- \*\*Actual:\*\* Decimal("0.30")

\- \*\*Severity:\*\* Critical — over-discount, revenue loss

\- \*\*Priority:\*\* High

\- \*\*Evidence:\*\* test\_TC25\_cap\_25\_percent

\- \*\*Suspected root cause:\*\* `DISCOUNT\_CAP = Decimal("0.30")` should be 0.25

\- \*\*Related tests:\*\* TC-25, TC-15\[STUDENT-SAVE10]

