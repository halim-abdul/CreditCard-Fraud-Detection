# Time Features

Fraud behavior often varies by hour and recency. For periodic time, encode phase continuously:

`sin(2πt/T)` and `cos(2πt/T)`.

This avoids an artificial jump between the end and beginning of a cycle. With event histories, also consider time since previous transaction and rolling activity counts, always using past-only windows.
