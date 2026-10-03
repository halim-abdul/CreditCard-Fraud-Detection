# Velocity Features

Velocity features capture unusually rapid behavior: transactions per 5 minutes/hour/day, recent spend, merchant diversity, or repeated declines.

## Important rule
For a transaction at time `t`, aggregate only events strictly before `t`. A rolling window that includes the current/future row leaks information.

In production, these features usually come from a feature store or streaming state keyed by card/account/device.
