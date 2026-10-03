# Scaling and Normalization

Linear models and distance-based methods are sensitive to scale; boosted trees generally are not. `RobustScaler` is useful when numerical features contain extreme values because it centers by the median and scales with quantiles.

Fit scaling parameters on training data only. Keep preprocessing inside a scikit-learn pipeline so cross-validation cannot leak validation statistics into training.
