Internal Feedback in the Cortical Perception-action Loop Enables Fast and Accurate Behavior

Topics include State estimation, Attention mechanisms, Control.

Animals move smoothly and reliably in unpredictable environments. Models of sensorimotor control have assumed that sensory information from the environment leads to actions, which then act back on the environment, creating a single, unidirectional perception-action loop. This loop contains internal delays in sensory and motor pathways, which can lead to unstable control. We show here that these delays can be compensated by internal feedback signals that flow backwards, from motor towards sensory areas. Internal feedback is ubiquitous in neural sensorimotor systems and recent advances in control theory show how internal feedback compensates internal delays. This is accomplished by filtering out self-generated and other predictable changes in early sensory areas so that unpredicted, actionable information can be rapidly transmitted toward action by the fastest components. For example, fast, giant neurons are necessarily less accurate than smaller neurons, but they are crucial for fast and accurate behavior....

## Abstract

Animals move smoothly and reliably in unpredictable environments. Models of sensorimotor control have assumed that sensory information from the environment leads to actions, which then act back on the environment, creating a single, unidirectional perception-action loop. This loop contains internal delays in sensory and motor pathways, which can lead to unstable control. We show here that these delays can be compensated by internal feedback signals that flow backwards, from motor towards sensory areas....

### keywords

Attention has been studied primarily in the context of sensory processing. The importance of attentional signals for reducing time delays in making motor decisions adds a new direction for future experimental studies. Attention is linked to conscious awareness and rides atop the global representation of the body throughout the cortex. This makes internal feedback a candidate feature of the nervous system that helps explain the sense of unity that we experience, which would otherwise be difficult to achieve with a balkanized representation of body parts.

Stephen Lisberger helped clarify our discussion on visual pathways to the oculomotor system. J.C.D. and T.J.S. were supported by NSF NCS-FO 1735004. T.J.S. was supported by ONR N00014-16-1-282. J.S.L. was in part supported by NSERC PGSD3-557385-2021. This paper is based on the doctoral research of A.A.S. and J.S.L.

Figure 8: Localization of function within motor-related cortex: although different parts of the cortex control different parts of the body, these parts of the body are inherently mechanically coupled. As a result, internal feedback is useful and in some cases necessary to maintain localization of function. In simulations, we consider the problem of tracking a moving target over a two-dimensional space, varying the task difficulty. The ’Ideal’ controller is centralized (i.e. no delays between local controllers) and obtains the best performance. The localized controller with internal feedback achieves similar performance....

We now consider the case in which sensing is instantaneous, but imperfect. Consider the following system:

The first term represents error from delay and object movement, similar to. The second term represents a combination of quantization error from the fast communication pathway ($\beta_{f}$) and performance error of the slow pathway...
