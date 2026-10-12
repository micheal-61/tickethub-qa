\# DEF-06: Wrong rounding mode (ROUND\_DOWN instead of ROUND\_HALF\_UP)

\- \*\*REQ violated:\*\* REQ-F5

\- \*\*Environment:\*\* Python 3.14.8

\- \*\*Steps:\*\* `calculate\_total(3, "STUDENT")`

\- \*\*Expected:\*\* Decimal("47.98")

\- \*\*Actual:\*\* Decimal("47.97")

\- \*\*Severity:\*\* Medium — systematic undercharge

\- \*\*Priority:\*\* Medium

\- \*\*Evidence:\*\* test\_TC31\_rounding\_half\_up

\- \*\*Suspected root cause:\*\* `rounding=ROUND\_DOWN` should be `ROUND\_HALF\_UP`

\- \*\*Related tests:\*\* TC-31

