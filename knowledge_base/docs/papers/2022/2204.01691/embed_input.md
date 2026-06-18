Do as I Can, Not as I Say: Grounding Language in Robotic Affordances

Topics include Robotics, Large language models, Language models, Natural language.

Large language models can encode a wealth of semantic knowledge about the world. Such knowledge could be extremely useful to robots aiming to act upon high-level, temporally extended instructions expressed in natural language. However, a significant weakness of language models is that they lack real-world experience, which makes it difficult to leverage them for decision making within a given embodiment. For example, asking a language model to describe how to clean a spill might result in a reasonable narrative, but it may not be applicable to a particular agent, such as a robot, that needs to perform this task in a particular environment. We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are both feasible and contextually appropriate. The robot can act as the language model's "hands and eyes," while the language model supplies high-level semantic knowledge about the task....

## Introduction

Recent progress in training large language models (LLMs) has led to systems that can generate complex text based on prompts, answer questions, or even engage in dialogue on a wide range of topics. These models absorb vast quantities of knowledge from text corpora mined from the web, and we might wonder whether knowledge of everyday tasks that is encoded in such models can be used by robots to perform complex tasks in the real world. But how can embodied agents extract and harness the knowledge of LLMs for physically grounded tasks?

This question poses a major challenge. LLMs are not grounded in the physical world and they do not observe the consequences of their generations on any physical process. This can lead LLMs to not only make mistakes that seem unreasonable or humorous to people, but also to interpret instructions in ways that are nonsensical or unsafe for a particular physical situation. Figure 1 shows an example -- a kitchen robot capable of executing skills such as "pick up the sponge" or "go to the table" may be asked for help cleaning up a spill ("I spilled my drink, can you help?")....

In the future, it is also interesting to examine whether natural language is the right ontology to use to program robots: natural language naturally incorporates contextual and semantic cues from the environment, and provides a level of abstraction which enables robots do decide on how to execute a strategy based on its own perception and affordances. At the same time, as opposed to, e.g., hindsight goal images, it requires supervision and it might not be the most descriptive medium for certain tasks.

Lastly, SayCan presents a particular way of connecting and factorizing the challenges of language understanding and robotics, and many further extensions can be proposed. Ideas such as combining robot planning and language, using language models as a pre-training mechanism for policies and many other ways of combining language and interaction are exciting avenues for future research.

(b) “I left out a coke, apple, and water, can you throw them away and then bring me a sponge to wipe the table?”

Experimental Setup. We evaluate SayCan with a mobile manipulator and a set of object manipulation and navigation skills in two office kitchen environments. Figure 4 shows the environment setup and the robot....
