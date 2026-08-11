<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Challenges in Autonomous Vehicle Testing and Validation

Topics include Autonomous vehicles, Testing, Validation, Safety, ISO 26262, Edge cases, Assurance.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Frames why conventional V-model validation is strained by fully autonomous vehicles: no fallback driver, difficult requirements, nondeterminism, learning components, and fail-operational needs. The paper is a useful safety-engineering checklist for AV assurance arguments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Software testing is all too often simply a bug hunt rather than a well-considered exercise in ensuring quality. A more methodical approach than a simple cycle of system-level test-fail-patch-test will be required to deploy safe autonomous vehicles at scale. The ISO 26262 development V process sets up a framework that ties each type of testing to a corresponding design or requirement document, but presents challenges when adapted to deal with the sorts of novel testing problems that face autonomous vehicles. This paper identifies five major challenge areas in testing according to the V model for autonomous vehicles: driver out of the loop, complex requirements, non-deterministic algorithms, inductive learning algorithms, and fail-operational systems. General solution approaches that seem promising across these different challenge areas include: phased deployment using successively relaxed operational scenarios, use of a monitor/actuator pair architecture to separate the most complex autonomy functions from simpler safety functions, and fault injection as a way to perform more efficient edge case testing. While significant challenges remain in safety-certifying the type of algorithms that provide high-level autonomy themselves, it seems within reach to instead architect the system and its accompanying design process to be able to employ existing software safety approaches.
