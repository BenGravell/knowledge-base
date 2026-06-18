<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PUMA: Planning under Uncertainty with Macro-Actions

Topics include POMDPs, Macro-actions, Planning under uncertainty, Forward search, Anytime planning, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces PUMA, an online POMDP planner that constructs and evaluates open-loop macro-actions to search farther ahead under partial observability. The method reduces branching by committing over macro-action intervals while retaining refinement toward shorter decisions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Planning in large, partially observable domains is challenging, especially when a long-horizon lookahead is necessary to obtain a good policy. Traditional POMDP planners that plan a different potential action for each future observation can be prohibitively expensive when planning many steps ahead. An efficient solution for planning far into the future in fully observable domains is to use temporally-extended sequences of actions, or "macro-actions." In this paper, we present a POMDP algorithm for planning under uncertainty with macro-actions (PUMA) that automatically constructs and evaluates open-loop macro-actions within forward-search planning, where the planner branches on observations only at the end of each macro-action. Additionally, we show how to incrementally refine the plan over time, resulting in an anytime algorithm that provably converges to an epsilon-optimal policy. In experiments on several large POMDP problems which require a long horizon lookahead, PUMA outperforms existing state-of-the art solvers.
