\# DEF-01: Quantity 10 wrongly rejected

\- \*\*REQ violated:\*\* REQ-F1 (1 to 10 inclusive)

\- \*\*Environment:\*\* Python 3.14.8

\- \*\*Steps:\*\* `calculate\_total(10, "PUBLIC")`

\- \*\*Expected:\*\* Decimal("189.91")

\- \*\*Actual:\*\* ValueError: quantity must be between 1 and 10

\- \*\*Severity:\*\* High — valid boundary rejected, revenue lost

\- \*\*Priority:\*\* High

\- \*\*Evidence:\*\* test\_TC01\_quantity\_valid\[TC-q10]

\- \*\*Suspected root cause:\*\* `quantity >= MAX\_QTY` should be `quantity > MAX\_QTY`

\- \*\*Related tests:\*\* TC-01 (q=10)

