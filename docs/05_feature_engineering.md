# Feature Engineering for Fraud

Useful fraud features summarize transaction context rather than memorizing identities.

- log-transform highly skewed `Amount`;
- encode time cyclically with sine/cosine;
- build past-only velocity counts when entity IDs exist;
- compare a transaction with a customer's historical baseline;
- prefer robust statistics such as median and MAD for heavy-tailed data.

Feature engineering must be fitted or computed without future information.
