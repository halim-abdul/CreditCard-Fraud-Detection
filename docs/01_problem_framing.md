# Fraud Detection Problem Framing

Credit-card fraud detection is a rare-event binary classification problem. The practical objective is not raw accuracy; it is to identify costly fraud while controlling false alarms and review workload.

## Core questions
- What is the positive class?
- What time window is used for training and evaluation?
- Which features exist at authorization time?
- What is the cost of a false negative versus a false positive?
- Is the output a label, a probability, or a ranked review queue?

## Recommended outputs
1. calibrated fraud probability;
2. operational risk score;
3. decision threshold selected from business cost or review capacity;
4. explanations for analyst review.
