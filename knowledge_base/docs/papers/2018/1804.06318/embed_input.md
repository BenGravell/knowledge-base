Learning Awareness Models

We consider the setting of an agent with a fixed body interacting with an unknown and uncertain external world. We show that models trained to predict proprioceptive information about the agent's body come to represent objects in the external world. In spite of being trained with only internally available signals, these dynamic body models come to represent external objects through the necessity of predicting their effects on the agent's own body. That is, the model learns holistic persistent representations of objects in the world, even though the only training signals are body signals. Our dynamics model is able to successfully predict distributions over 132 sensor readings over 100 steps into the future and we demonstrate that even when the body is no longer in contact with an object, the latent variables of the dynamics model continue to represent its shape. We show that active data collection by maximizing the entropy of predictions about the body - touch sensors, proprioception and vestibular information - leads to learning of dynamic models that show superior performance when used for control....

## Introduction

> Situation awareness is the perception of the elements in the environment within a volume of time and space, and the comprehension of their meaning, and the projection of their status in the near future. --- Endsley

As artificial intelligence moves off of the server and out into the world at large; be this the virtual world, in the form of simulated walkers, climbers and other creatures, or the real world in the form of virtual assistants, self driving vehicles, and household robots; we are increasingly faced with the need to build systems that understand and reason about the world around them.

In this paper we showed that learning a forward predictive model of proprioception we obtain models that can be used to answer questions and reason about objects in the external world. We demonstrated this in simulation with a series of diagnostic tasks where we use the model features to identify properties of external objects, and also with a control task where we show that we can plan in the model to achieve objectives that were not seen during training.

We also showed that the same principles we applied to our simulated models are also successful in reality. We collected data from a real robotic platform and used the same modelling techniques to predict the orientation of a grasped block.

While the actors are collecting data, a single learner process samples batches of the collected trajectories from the buffer being written to by the actors. The learner trains the PreCo model by maximum likelihood as described in Section 4 Dynamics Model ‣ Learning Awareness Models"), and the updated model propagates back to the actors who continue to plan using the updated model. We implemented this using the framework of Horgan et al..

Separating the dynamics model into predictor and corrector components allows us to operate in single-step and multi-step prediction modes as Figure 3 Dynamics Model ‣ Learning Awareness Models") shows. The predictor can make action-conditional predictions using the hidden states from the corrector for single-step predictions as $h_{t,0}^{p} = {{Predictor}_{\theta}{(h_{t - 1}^{c},u_{t})}}$ or from itself for multi-step predictions as $h_{t,{i + 1}}^{p} = {{Predictor}_{\theta}{(h_{t,i}^{p},u_{t + i})}}$....

In this section we explore how different data collection strategies lead to models of different quality....
