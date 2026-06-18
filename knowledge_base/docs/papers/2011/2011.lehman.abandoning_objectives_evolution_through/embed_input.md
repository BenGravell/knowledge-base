<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Abandoning Objectives: Evolution through the Search for Novelty Alone

Topics include Novelty search, Evolutionary algorithms, Quality diversity, Open-ended evolution, Deception, Behavioral diversity, Neuroevolution.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Argues that objective functions can actively mislead evolutionary search and proposes novelty search as an alternative pressure based on behavioral difference. The paper is influential because it shows that ignoring the explicit objective can outperform objective-based fitness on deceptive maze-navigation and biped-walking domains, reframing exploration as a first-class search objective.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In evolutionary computation, the fitness function normally measures progress toward an objective in the search space, effectively acting as an objective function. Through deception, such objective functions may actually prevent the objective from being reached. While methods exist to mitigate deception, they leave the underlying pathology untreated: Objective functions themselves may actively misdirect search toward dead ends. This paper proposes an approach to circumventing deception that also yields a new perspective on open-ended evolution. Instead of either explicitly seeking an objective or modeling natural evolution to capture open-endedness, the idea is to simply search for behavioral novelty. Even in an objective-based problem, such novelty search ignores the objective. Because many points in the search space collapse to a single behavior, the search for novelty is often feasible. Furthermore, because there are only so many simple behaviors, the search for novelty leads to increasing complexity. By decoupling open-ended search from artificial life worlds, the search for novelty is applicable to real world problems. Counterintuitively, in the maze navigation and biped walking tasks in this paper, novelty search significantly outperforms objective-based search, suggesting the strange conclusion that some problems are best solved by methods that ignore the objective.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The main lesson is the inherent limitation of the objective-based paradigm and the unexploited opportunity to guide search through other means.
