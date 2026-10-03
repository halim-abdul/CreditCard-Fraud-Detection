# Leakage Prevention

Fraud models fail silently when training data contains information that would not exist at authorization time.

## Common leakage sources
- chargeback outcome fields;
- manually reviewed labels generated after the transaction;
- aggregates computed using future transactions;
- random splitting when the same card/customer appears in both train and test;
- preprocessing fitted on the full dataset.

## Rules
Fit every transformer only on training data, preserve transaction chronology where possible, and compute rolling features using past-only windows.
