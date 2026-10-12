\# DEF-02: Bulk discount applies at quantity 6, not 5

\- \*\*REQ violated:\*\* REQ-F4 (bulk threshold = 5)

\- \*\*Environment:\*\* Python 3.14.8

\- \*\*Steps:\*\* `calculate\_discount(5, "PUBLIC")`

\- \*\*Expected:\*\* Decimal("0.05")

\- \*\*Actual:\*\* Decimal("0")

\- \*\*Severity:\*\* High — undercharge at threshold

\- \*\*Priority:\*\* High

\- \*\*Evidence:\*\* test\_TC24\_bulk\_threshold\_5

\- \*\*Suspected root cause:\*\* `quantity > BULK\_THRESHOLD` should be `quantity >= BULK\_THRESHOLD`

\- \*\*Related tests:\*\* TC-24

