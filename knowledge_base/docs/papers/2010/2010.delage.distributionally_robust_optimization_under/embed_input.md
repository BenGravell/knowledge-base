<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Optimization under Moment Uncertainty with Application to Data-Driven Problems

Topics include Distributionally robust optimization, Moment uncertainty, Mean and covariance, Semidefinite programming, Statistical confidence regions, Portfolio selection, Data-driven optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops tractable distributionally robust stochastic programs whose ambiguity sets allow uncertainty in both distribution shape and estimated mean and covariance. Statistical confidence regions calibrate those sets from data, and portfolio experiments demonstrate improved out-of-sample performance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic programming can effectively describe many decision-making problems in uncertain environments. Unfortunately, such programs are often computationally demanding to solve. In addition, their solution can be misleading when there is ambiguity in the choice of a distribution for the random parameters. In this paper, we propose a model that describes uncertainty in both the distribution form (discrete, Gaussian, exponential, etc.) and moments (mean and covariance matrix). We demonstrate that for a wide range of cost functions the associated distributionally robust (or min-max) stochastic program can be solved efficiently. Furthermore, by deriving a new confidence region for the mean and the covariance matrix of a random vector, we provide probabilistic arguments for using our model in problems that rely heavily on historical data. These arguments are confirmed in a practical example of portfolio selection, where our framework leads to better-performing policies on the “true” distribution underlying the daily returns of financial assets.
