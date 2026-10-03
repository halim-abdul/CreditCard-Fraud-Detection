# Hyperparameter Optimization

Use Optuna or another search framework on a validation set or cross-validation folds. Optimize a metric aligned with rare-event detection, such as average precision, recall at a controlled false-positive rate, or expected cost.

Keep the final test set untouched. Record the search space, random seed, trial count, best parameters, and validation metric for reproducibility.
