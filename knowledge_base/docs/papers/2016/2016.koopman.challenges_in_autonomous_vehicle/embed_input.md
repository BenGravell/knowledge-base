<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Challenges in Autonomous Vehicle Testing and Validation

Topics include Autonomous vehicles, Testing, Validation, Safety, ISO 26262, Edge cases, Assurance.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Frames why conventional V-model validation is strained by fully autonomous vehicles: no fallback driver, difficult requirements, nondeterminism, learning components, and fail-operational needs. The paper is a useful safety-engineering checklist for AV assurance arguments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we explore some of the challenges that await developers who are attempting to qualify fully autonomous, NHTSA Level 4 vehicles for large-scale deployment. Thus, we skip past potential semi-automated approaches to address systems in which the driver is not responsible at all for safe vehicle operation. We further limit scope to consider how such vehicles might be designed and validated within the ISO 26262 V framework. This paper identifies five major challenge areas in testing according to the V model for autonomous vehicles: driver out of the loop, complex requirements, non-deterministic algorithms, inductive learning algorithms, and fail-operational systems. General solution approaches that seem promising across these different challenge areas include phased deployment using successively relaxed operational scenarios, use of a monitor/actuator pair architecture to separate the most complex autonomy functions from simpler safety functions, and fault injection as a way to perform more efficient edge case testing.
