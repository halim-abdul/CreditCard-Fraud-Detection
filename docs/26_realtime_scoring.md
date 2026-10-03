# Real-Time Scoring

A production fraud service receives transaction features, applies exactly the same preprocessing used during training, returns a calibrated probability/risk score, and records enough metadata for monitoring and audit.

Keep network calls off the critical path where possible, validate feature schemas, enforce timeouts, and define safe behavior when the model or feature service is unavailable.
