<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Belief Roadmap: Efficient Planning in Belief Space by Factoring the Covariance

Topics include Belief-space planning, Motion planning, Uncertainty, Covariance planning, Roadmap, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the belief roadmap, which factors covariance evolution to make planning in belief space more efficient. The method lets robots reason about uncertainty along roadmap paths without paying the full cost of high-dimensional belief planning everywhere.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

When a mobile agent does not know its position perfectly, incorporating the predicted uncertainty of future position estimates into the planning process can lead to substantially better motion performance. However, planning in the space of probabilistic position estimates, or belief space, can incur a substantial computational cost. In this paper, we show that planning in belief space can be performed efficiently for linear Gaussian systems by using a factored form of the covariance matrix. This factored form allows several prediction and measurement steps to be combined into a single linear transfer function, leading to very efficient posterior belief prediction during planning. We give a belief-space variant of the probabilistic roadmap algorithm called the belief roadmap (BRM) and show that the BRM can compute plans substantially faster than conventional belief space planning. We conclude with performance results for an agent using ultra-wide bandwidth radio beacons to localize and show that we can efficiently generate plans that avoid failures due to loss of accurate position estimation.
