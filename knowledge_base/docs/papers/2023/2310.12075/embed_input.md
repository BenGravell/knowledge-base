Monte Carlo Tree Search for Behavior Planning in Autonomous Driving

Topics include Autonomous driving, Behavior planning, Monte Carlo tree search, Tree search, Motion planning.

Applies Monte Carlo tree search to autonomous-driving behavior planning, using cost functions and search structure tailored to highway and urban decisions. It is a compact example of keeping decision-level planning explicit instead of replacing the behavior layer with a learned policy.

The integration of autonomous vehicles into urban and highway environments necessitates the development of robust and adaptable behavior planning systems. This study presents an innovative approach to address this challenge by utilizing a Monte-Carlo Tree Search (MCTS) based algorithm for autonomous driving behavior planning. The core objective is to leverage the balance between exploration and exploitation inherent in MCTS to facilitate intelligent driving decisions in complex scenarios. We introduce an MCTS-based algorithm tailored to the specific demands of autonomous driving. This involves the integration of carefully crafted cost functions, encompassing safety, comfort, and passability metrics, into the MCTS framework. The effectiveness of our approach is demonstrated by enabling autonomous vehicles to navigate intricate scenarios, such as intersections, unprotected left turns, cut-ins, and ramps, even under traffic congestion, in real-time. Qualitative instances illustrate the integration of diverse driving decisions, such as lane changes, acceleration, and deceleration, into the MCTS framework.

## Introduction

(a) An intricate urban intersection scenario, where an autonomous vehicle (blue) makes an unprotected left turn while interacting with other vehicles.

(b) An autonomous vehicle (blue) approaches a highway exit marked by a sudden traffic jam.

In a comprehensive autonomous driving system, various components work harmoniously to orchestrate the vehicle's movements. These include sensors for environment perception, high-definition maps for precise localization, route planners for efficient navigation, motion planners for trajectory generation, behavior planners for strategic decision-making, and control systems for precise execution. This paper emphasizes the behavior planner, which serves as the nexus between high-level intentions and low-level control actions, orchestrating the vehicle's behavior to align with both its objectives and safety requirements.

Central to our approach is the integration of the Monte-Carlo Tree Search (MCTS) algorithm into the realm of autonomous driving. Originating from game theory and artificial intelligence, MCTS has found application in various autonomous fields, showcasing its adaptability and robustness, such as the orienteering problem, sensor tasking, persistent monitoring, and autonomous driving. By adapting MCTS to autonomous driving behavior planning, we harness its intrinsic ability to balance exploration and exploitation, making it well-suited to the intricate, dynamic, and uncertain nature of real-world traffic scenarios.

## Conclusion and Future Directions

In this paper, we presented a Monte Carlo Tree Search (MCTS) based framework for decision-making in autonomous driving scenarios. With both qualitative and quantitative analyses, we demonstrated the efficacy and robustness of our MCTS approach across a wide range of driving scenarios, from highway exits to intricate urban intersections. The versatility of the framework was further emphasized by its ability to seamlessly handle diverse challenges like sudden cut-ins and unprotected left turns.
