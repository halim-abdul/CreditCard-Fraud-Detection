# Splitting Strategy

## Beginner baseline
Use a stratified train/test split so both partitions retain the rare fraud class.

## Better validation
Use train/validation/test partitions: train fits parameters, validation selects models and thresholds, test is touched once for final reporting.

## Production-like validation
When timestamps are available, train on earlier transactions and evaluate on later transactions. This better reflects deployment and exposes drift.

Never oversample before splitting; resampling belongs inside the training fold only.
