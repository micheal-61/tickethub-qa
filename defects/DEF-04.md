\# DEF-04: Promo code is case-insensitive

\- \*\*REQ violated:\*\* REQ-F6 (SAVE10 is case-sensitive)

\- \*\*Environment:\*\* Python 3.14.8

\- \*\*Steps:\*\* `calculate\_total(1, "PUBLIC", "save10")`

\- \*\*Expected:\*\* ValueError

\- \*\*Actual:\*\* accepted, returns Decimal("17.99")

\- \*\*Severity:\*\* Medium — invalid input silently accepted

\- \*\*Priority:\*\* Medium

\- \*\*Evidence:\*\* test\_TC33\_promo\_case\_sensitive

\- \*\*Suspected root cause:\*\* `promo\_code.upper()` folds case before comparison

\- \*\*Related tests:\*\* TC-33

