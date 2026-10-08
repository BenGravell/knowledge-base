<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally-Aware Exploration for CVaR Bandits

Topics include Multi-armed bandits, Conditional value at risk, Risk-sensitive learning, Optimism, Distributional exploration, Regret bounds.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Constructs optimistic sample distributions using Dvoretzky-Kiefer-Wolfowitz confidence bands before estimating each arm's CVaR. Provides regret guarantees and experiments showing that distribution-aware exploration improves on bonuses applied directly to scalar CVaR estimates.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Risk sensitive objectives are often desirable in settings like healthcare or finance, where agents are more sensitive to worst-case than average outcomes. However, current risk-sensitive algorithms for multi-armed bandits utilize exploration bonuses which do not adapt to the distributional nature of these objectives. In this paper, we consider multi-armed bandits with a popular risk-sensitive objective called the Conditional Value at Risk (CVaR). We present an novel optimism-based algorithm for this setting: instead of adding bonuses to the CVaR estimate of each arm, we apply optimism at the sample level, generating an optimistic set of samples for each arm and then computing CVaR estimates from them instead. We present regret bounds for our algorithm, along with experiments showing order-of-magnitude improvements over baselines and prior work. Further experiments demonstrate how sample-level optimism enables our algorithm to adapt to the shape of each arm distribution in ways that exploration bonuses do not.
