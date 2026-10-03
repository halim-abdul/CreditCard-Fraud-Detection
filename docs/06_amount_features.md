# Amount Features

Transaction amounts are usually right-skewed. Tree models can often work with raw values, while linear models benefit from transformed/scaled features.

Recommended candidates: raw amount, `log1p(amount)`, square root amount, percentile/rank within a training reference set, and deviation from an account's past median when entity history exists.
