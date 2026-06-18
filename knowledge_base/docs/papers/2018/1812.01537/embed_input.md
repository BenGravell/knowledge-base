A Micro Lie Theory for State Estimation in Robotics

A Lie group is an old mathematical abstract object dating back to the XIX century, when mathematician Sophus Lie laid the foundations of the theory of continuous transformation groups. As it often happens, its usage has spread over diverse areas of science and technology many years later. In robotics, we are recently experiencing an important trend in its usage, at least in the fields of estimation, and particularly in motion estimation for navigation. Yet for a vast majority of roboticians, Lie groups are highly abstract constructions and therefore difficult to understand and to use. This may be due to the fact that most of the literature on Lie theory is written by and for mathematicians and physicists, who might be more used than us to the deep abstractions this theory deals . In estimation for robotics it is often not necessary to exploit the full capacity of the theory, and therefore an effort of selection of materials is required. In this paper, we will walk through the most basic principles of the Lie theory, with the aim of conveying clear and useful ideas, and leave a significant corpus of the Lie theory behind.

## Introduction

There has been a remarkable effort in the last years in the robotics community to formulate estimation problems properly. This is motivated by an increasing demand for precision, consistency and stability of the solutions. Indeed, proper modeling of the states and measurements, the functions relating them, and their uncertainties, is crucial to achieving these goals. This has led to designs involving what has been known as 'manifolds', which in this context are no less than the smooth topologic surfaces of the Lie groups where the state representations evolve.

Lie theory is by no means simple. To grasp a minimum idea of what LT can be, we may consider the following three references. First, Abbaspour's *"Basic Lie theory"* comprises more than 400 pages. With a similar title, Howe's *"Very basic Lie theory"* comprises 24 (dense) pages, and is sometimes considered a must-read introduction. Finally, the more modern and often celebrated Stillwell's *"Naive Lie theory"* comprises more than 200 pages. With such precedents labeled as 'basic', 'very basic' and 'naive', the aim of this paper at merely LABEL:LastPage pages is to simplify Lie theory even more (thus our adjective 'micro' in the title).

Our effort is in line with other recent works on the subject, which have also identified this need of bringing the LT closer to the roboticist. Our approach aims at appearing familiar to the target audience of this paper: an audience that is skilled in state estimation (Kalman filtering, graph-based optimization, and the like), but not yet familiar with the theoretical corpus of the Lie theory. We have for this taken some initiatives concerning notation, especially in the definition of the derivative, bringing it close to the vectorial counterparts, thus making the chain rule clearly visible.

## Conclusion

We have presented the essential of Lie theory in a form that should be useful for an audience skilled in state estimation, with a focus on robotics applications.

First, a selection of materials that avoids abstract mathematical concepts as much as possible. This helps to focus Lie theory to make its tools easier to understand and to use.
