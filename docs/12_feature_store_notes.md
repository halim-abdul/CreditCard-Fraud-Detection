# Feature Store Notes

A real-time fraud system often needs the same feature definitions offline and online. A feature store can centralize transformations, point-in-time correctness, entity keys, freshness, and monitoring.

For this repository, keep feature functions deterministic and side-effect free so they can later be moved behind batch or streaming feature services without rewriting model logic.
