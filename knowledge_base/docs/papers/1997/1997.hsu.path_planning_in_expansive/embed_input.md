<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Path Planning in Expansive Configuration Spaces

Topics include Motion planning, Expansive configuration spaces, Randomized planning, Configuration space, Sampling-based planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the Expansive Space Trees (EST) algorithm and the notion of "expansive" configuration spaces, characterizing when randomized sampling-based planners can efficiently capture connectivity. EST explores the configuration space by biasing sampling toward less explored regions, a complementary approach to RRT's goal-biased exploration.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The authors introduce the notion of expansiveness to characterize a family of robot configuration spaces whose connectivity can be effectively captured by a roadmap of randomly-sampled milestones. The analysis of expansive configuration spaces inspired them to develop a new randomized planning algorithm that tries to sample only the portion of the configuration space that is relevant to the current query, avoiding the cost of precomputing a roadmap for the entire configuration space.
