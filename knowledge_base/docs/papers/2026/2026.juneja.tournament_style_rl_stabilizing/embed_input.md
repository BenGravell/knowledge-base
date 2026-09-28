<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Tournament Style RL: Stabilizing Policy Optimization on Non Verifiable Problems

Topics include Reinforcement learning, Non-verifiable tasks, Pairwise preference, Reward design, Language models.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

TSRL trains language models for subjective tasks using the win rate against a fixed set of anchor responses as a reward. Aggregating pairwise judgments reduces reward noise and improves performance across four tasks compared with scalar and single-comparison rewards.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many real-world tasks are non-verifiable—there is no objective ground truth, and quality must be judged subjectively—making reward design for RL difficult. Existing approaches based on scalar rubric scores or single comparisons are often noisy, poorly calibrated, or provide sparse learning signals. We introduce Tournament Style RL (TSRL), which constructs rewards from rubric-guided pairwise judgments against a fixed set of anchor responses, using win-rate as the reward for policy optimization. This aggregation of comparisons against anchor responses yields a signal that is more robust to the judge noise by stabilizing the reference frame, reducing the variance in reward. We test across four non-verifiable tasks and two backbone LLMs, and find that TSRL improves average win-rate by +43.8 points over the base model and +22.8 points over the strongest baseline. TSRL scales with the number of anchors, remains robust under weak or partially corrupted judges, the results are supported by blinded human preference studies.
