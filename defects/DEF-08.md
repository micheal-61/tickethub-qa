\# DEF-08: COLLECTED + cancel is allowed

\- \*\*REQ violated:\*\* REQ-F7 (COLLECTED is final)

\- \*\*Environment:\*\* Python 3.14.8

\- \*\*Steps:\*\* `o = Order(1,"PUBLIC"); o.pay(); o.collect(); o.cancel()`

\- \*\*Expected:\*\* InvalidTransitionError

\- \*\*Actual:\*\* no exception raised

\- \*\*Severity:\*\* High — collected tickets can be refunded

\- \*\*Priority:\*\* High

\- \*\*Evidence:\*\* test\_TC41\_invalid\_transitions\[cancel-COLLECTED]

\- \*\*Suspected root cause:\*\* spurious ("COLLECTED","cancel") entry in transition table

\- \*\*Related tests:\*\* TC-41\[cancel-COLLECTED]

