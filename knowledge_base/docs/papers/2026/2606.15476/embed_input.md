<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FARM: Find Anything Using Relational Spatial Memory

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robots operating in homes, warehouses, and other object-rich environments need memory systems that can find specific object instances on demand. Object-level memory alone is often insufficient: scenes contain many plausibly matching objects, and users refer to the target through relations to landmarks and surrounding objects (e.g. ``the tall lamp below the dartboard and to the left of the poster''), demanding a relational spatial memory that supports retrieval through semantic, appearance, and spatial predicates over objects. To achieve this, we present FARM (Find Anything using Relational Spatial Memory), which builds, in real time at 5-10 Hz, a compact, open-vocabulary, object-level memory with geometry, visual-language descriptors, and viewpoint evidence. At query time, FARM uses VLMs to parse the query and score visual evidence, while grounding spatial constraints explicitly through object symbols and relational predicates. This structured use of VLMs enables more accurate and robust retrieval than end-to-end reasoning over frame histories or scene-graph context.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In experiments on 44k language queries spanning 67 indoor and outdoor scenes, ranging from 15 to 15,000 m^2, FARM improves Recall@5 and Recall@10 over prior methods by 164% and 224%, and a final VLM reranking stage improves Accuracy@1 by 35%, while running in real time. We further demonstrate closed-loop deployment on a quadrupedal robot using onboard sensors and compute.
