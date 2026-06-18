## Introduction

Humans develop a mental model of the world based on what they are able to perceive with their limited senses. The decisions and actions we make are based on this internal model. Jay Wright Forrester, the father of system dynamics, described a mental model as:

The image of the world around us, which we carry in our head, is just a model. Nobody in his head imagines all the world, government or country. He has only selected concepts, and relationships between them, and uses those to represent the real system.

Figure 1: A World Model, from Scott McCloud’s Understanding Comics.

To handle the vast amount of information that flows through our daily lives, our brain learns an abstract representation of both spatial and temporal aspects of this information. We are able to observe a scene and remember an abstract description thereof. Evidence also suggests that what we perceive at any given moment is governed by our brain's prediction of the future based on our internal model.

One way of understanding the predictive model inside of our brains is that it might not be about just predicting the future in general, but predicting future sensory data given our current motor actions. We are able to instinctively act on this predictive model and perform fast reflexive behaviours when we face danger, without the need to consciously plan out a course of action.

Take baseball for example. A batter has milliseconds to decide how they should swing the bat -- shorter than the time it takes for visual signals to reach our brain. The reason we are able to hit a 100 mph fastball is due to our ability to instinctively predict when and where the ball will go. For professional players, this all happens subconsciously. Their muscles reflexively swing the bat at the right time and location in line with their internal models' predictions. They can quickly act on their predictions of the future without the need to consciously roll out possible future scenarios to form a plan.

Figure 2: What we see is based on our brain’s prediction of the future.

In many reinforcement learning (RL) problems, an artificial agent also benefits from having a good representation of past and present states, and a good predictive model of the future, preferably a powerful predictive model implemented on a general purpose computer such as a recurrent neural network (RNN).

Figure 3: In this work, we build probabilistic generative models of OpenAI Gym environments. The RNN-based world models are trained using collected observations recorded from the actual game environment. After training the world models, we can use them mimic the complete environment and train agents using them.

Large RNNs are highly expressive models that can learn rich spatial and temporal representations of data. However, many model-free RL methods in the literature often only use small neural networks with few parameters. The RL algorithm is often bottlenecked by the credit assignment problem, which makes it hard for traditional RL algorithms to learn millions of weights of a large model, hence in practice, smaller networks are used as they iterate faster to a good policy during training.

Ideally, we would like to be able to efficiently train large RNN-based agents. The backpropagation algorithm can be used to train large neural networks efficiently. In this work we look at training a large neural network^11^1Typical model-free RL models have in the order of $10^{3}$ to $10^{6}$ model parameters. We look at training models in the order of $10^{7}$ parameters, which is still rather small compared to state-of-the-art deep learning models with $10^{8}$ to even $10^{9}$ parameters. In principle, the procedure described in this article can take advantage of these larger networks if we wanted to use them. to tackle RL tasks, by dividing the agent into a large world model and a small controller model. We first train a large neural network to learn a model of the agent's world in an unsupervised manner, and then train the smaller controller model to learn to perform a task using this world model. A small controller lets the training algorithm focus on the credit assignment problem on a small search space, while not sacrificing capacity and expressiveness via the larger world model. By training the agent through the lens of its world model, we show that it can learn a highly compact policy to perform its task.

Although there is a large body of research relating to model-based reinforcement learning, this article is not meant to be a review of the current state of the field. Instead, the goal of this article is to distill several key concepts from a series of papers 1990--2015 on combinations of RNN-based world models and controllers. We will also discuss other related works in the literature that share similar ideas of learning a world model and training an agent using this model.

In this article, we present a simplified framework that we can use to experimentally demonstrate some of the key concepts from these papers, and also suggest further insights to effectively apply these ideas to various RL environments. We use similar terminology and notation as On Learning to Think: Algorithmic Information Theory for Novel Combinations of RL Controllers and RNN World Models when describing our methodology and experiments.

## Agent Model

We present a simple model inspired by our own cognitive system. In this model, our agent has a visual sensory component that compresses what it sees into a small representative code. It also has a memory component that makes predictions about future codes based on historical information. Finally, our agent has a decision-making component that decides what actions to take based only on the representations created by its vision and memory components.

Figure 4: Our agent consists of three components that work closely together: Vision (V), Memory (M), and Controller (C)

### VAE (V) Model

The environment provides our agent with a high dimensional input observation at each time step. This input is usually a 2D image frame that is part of a video sequence. The role of the V model is to learn an abstract, compressed representation of each observed input frame.

Figure 5: Flow diagram of a Variational Autoencoder (VAE).

Here, we use a simple Variational Autoencoder as our V model to compress each image frame into a small latent vector $z$.

### MDN-RNN (M) Model

While it is the role of the V model to compress what the agent sees at each time frame, we also want to compress what happens over time. For this purpose, the role of the M model is to predict the future. The M model serves as a predictive model of the future $z$ vectors that V is expected to produce. Since many complex environments are stochastic in nature, we train our RNN to output a probability density function $p{(z)}$ instead of a deterministic prediction of $z$.

Figure 6: RNN with a Mixture Density Network output layer. The MDN outputs the parameters of a mixture of Gaussian distribution used to sample a prediction of the next latent vector z.

In our approach, we approximate $p{(z)}$ as a mixture of Gaussian distribution, and train the RNN to output the probability distribution of the next latent vector $z_{t + 1}$ given the current and past information made available to it.

More specifically, the RNN will model $P{(\left. z_{t + 1} \middle| {a_{t},z_{t},h_{t}} \right.)}$, where $a_{t}$ is the action taken at time $t$ and $h_{t}$ is the hidden state of the RNN at time $t$. During sampling, we can adjust a temperature parameter $\tau$ to control model uncertainty, as done in -- we will find adjusting $\tau$ to be useful for training our controller later on.

Figure 7: SketchRNN is an example of a MDN-RNN used to predict the next pen strokes of a sketch drawing. We use a similar model to predict the next latent vector zt.

This approach is known as a Mixture Density Network combined with a RNN (MDN-RNN), and has been applied in the past for sequence generation problems such as generating handwriting and sketches.

### Controller (C) Model

The Controller (C) model is responsible for determining the course of actions to take in order to maximize the expected cumulative reward of the agent during a rollout of the environment. In our experiments, we deliberately make C as simple and small as possible, and trained separately from V and M, so that most of our agent's complexity resides in the world model (V and M).

C is a simple single layer linear model that maps $z_{t}$ and $h_{t}$ directly to action $a_{t}$ at each time step:

In this linear model, $W_{c}$ and $b_{c}$ are the weight matrix and bias vector that maps the concatenated input vector $\lbrack{z_{t}h_{t}}\rbrack$ to the output action vector $a_{t}$.

### Putting V, M, and C Together

The following flow diagram illustrates how V, M, and C interacts with the environment:

Figure 8: Flow diagram of our Agent model. The raw observation is first processed by V at each time step t to produce zt. The input into C is this latent vector zt concatenated with M’s hidden state ht at each time step. C will then output an action vector at for motor control, and will affect the environment. M will then take the current zt and action at as an input to update its own hidden state to produce ht + 1 to be used at time t + 1.

Below is the pseudocode for how our agent model is used in the OpenAI Gym environment:

def rollout(controller):
’’’ env, rnn, vae are ’’’
obs = env.reset()
h = rnn.initial_state()
while not done:
z = vae.encode(obs)
obs, reward, done = env.step(a)
cumulative_reward += reward
return cumulative_reward

Running this function on a given controller C will return the cumulative reward during a rollout.

This minimal design for C also offers important practical benefits. Advances in deep learning provided us with the tools to train large, sophisticated models efficiently, provided we can define a well-behaved, differentiable loss function. Our V and M models are designed to be trained efficiently with the backpropagation algorithm using modern GPU accelerators, so we would like most of the model's complexity, and model parameters to reside in V and M. The number of parameters of C, a linear model, is minimal in comparison. This choice allows us to explore more unconventional ways to train C -- for example, even using evolution strategies (ES) to tackle more challenging RL tasks where the credit assignment problem is difficult.

To optimize the parameters of C, we chose the Covariance-Matrix Adaptation Evolution Strategy (CMA-ES) as our optimization algorithm since it is known to work well for solution spaces of up to a few thousand parameters. We evolve parameters of C on a single machine with multiple CPU cores running multiple rollouts of the environment in parallel.

For more specific information about the models, training procedures, and environments used in our experiments, please refer to the Appendix section.

## Car Racing Experiment

In this section, we describe how we can train the Agent model described earlier to solve a car racing task. To our knowledge, our agent is the first known solution to achieve the score required to solve this task.^22^2We find this task interesting because although it is not difficult to train an agent to wobble around randomly generated tracks and obtain a mediocre score, CarRacing-v0 defines solving as getting average reward of 900 over 100 consecutive trials, which means the agent can only afford very few driving mistakes.

### World Model for Feature Extraction

A predictive world model can help us extract useful representations of space and time. By using these features as inputs of a controller, we can train a compact and minimal controller to perform a continuous control task, such as learning to drive from pixel inputs for a top-down car racing environment called CarRacing-v0.

Figure 9: Our agent learning to navigate in CarRacing-v0.

In this environment, the tracks are randomly generated for each trial, and our agent is rewarded for visiting as many tiles as possible in the least amount of time. The agent controls three continuous actions: steering left/right, acceleration, and brake.

To train our V model, we first collect a dataset of 10,000 random rollouts of the environment. We have first an agent acting randomly to explore the environment multiple times, and record the random actions $a_{t}$ taken and the resulting observations from the environment. We use this dataset to train V to learn a latent space of each frame observed. We train our VAE to encode each frame into low dimensional latent vector $z$ by minimizing the difference between a given frame and the reconstructed version of the frame produced by the decoder from $z$.

We can now use our trained V model to pre-process each frame at time $t$ into $z_{t}$ to train our M model. Using this pre-processed data, along with the recorded random actions $a_{t}$ taken, our MDN-RNN can now be trained to model $P{(\left. z_{t + 1} \middle| {a_{t},z_{t},h_{t}} \right.)}$ as a mixture of Gaussians.^33^3In principle, we can train both models together in an end-to-end manner, although we found that training each separately is more practical, and also achieves satisfactory results. Training each model only required less than an hour of computation time on a single GPU. We can also train individual VAE and MDN-RNN models without having to exhaustively tune hyperparameters.

In this experiment, the world model (V and M) has no knowledge about the actual reward signals from the environment. Its task is simply to compress and predict the sequence of image frames observed. Only the Controller (C) Model has access to the reward information from the environment. Since there are a mere 867 parameters inside the linear controller model, evolutionary algorithms such as CMA-ES are well suited for this optimization task.

We can use the VAE to reconstruct each frame using $z_{t}$ at each time step to visualize the quality of the information the agent actually sees during a rollout. The figure below is a VAE model trained on screenshots from CarRacing-v0.

Figure 10: Despite losing details during this lossy compression process, latent vector z captures the essence of each image frame.

In the online version of this article, one can load randomly chosen screenshots to be encoded into a small latent vector $z$, which is used to reconstruct the original screenshot. One can also experiment with adjusting the values of the $z$ vector using the slider bars to see how it affects the reconstruction, or randomize $z$ to observe the space of possible screenshots.

### Procedure

To summarize the Car Racing experiment, below are the steps taken:

Collect 10,000 rollouts from a random policy.

Train VAE (V) to encode frames into $z \in \mathcal{R}^{32}$.

Train MDN-RNN (M) to model $P{(\left. z_{t + 1} \middle| {a_{t},z_{t},h_{t}} \right.)}$.

Define Controller (C) as $a_{t} = {{W_{c}{\lbrack{z_{t}h_{t}}\rbrack}} + b_{c}}$.

Use CMA-ES to solve for a $W_{c}$ and $b_{c}$ that maximizes the expected cumulative reward.

### Experiment Results

Training an agent to drive is not a difficult task if we have a good representation of the observation. Previous works have shown that with a good set of hand-engineered information about the observation, such as LIDAR information, angles, positions and velocities, one can easily train a small feed-forward network to take this hand-engineered input and output a satisfactory navigation policy. For this reason, we first want to test our agent by handicapping C to only have access to V but not M, so we define our controller as $a_{t} = {{W_{c}z_{t}} + b_{c}}$.

Figure 11: Limiting our controller to see only zt, but not ht results in wobbly and unstable driving behaviours.

Although the agent is still able to navigate the race track in this setting, we notice it wobbles around and misses the tracks on sharper corners. This handicapped agent achieved an average score of 632 $\pm$ 251 over 100 random trials, in line with the performance of other agents on OpenAI Gym's leaderboard and traditional Deep RL methods such as A3C. Adding a hidden layer to C's policy network helps to improve the results to 788 $\pm$ 141, but not quite enough to solve this environment.

Full World Model (V and M)

The representation $z_{t}$ provided by our V model only captures a representation at a moment in time and does not have much predictive power. In contrast, M is trained to do one thing, and to do it really well, which is to predict $z_{t + 1}$. Since M's prediction of $z_{t + 1}$ is produced from the RNN's hidden state $h_{t}$ at time $t$, this vector is a good candidate for the set of learned features we can give to our agent. Combining $z_{t}$ with $h_{t}$ gives our controller C a good representation of both the current observation, and what to expect in the future.

Figure 12: Driving is more stable if we give our controller access to both zt and ht.

We see that allowing the agent to access the both $z_{t}$ and $h_{t}$ greatly improves its driving capability. The driving is more stable, and the agent is able to seemingly attack the sharp corners effectively. Furthermore, we see that in making these fast reflexive driving decisions during a car race, the agent does not need to plan ahead and roll out hypothetical scenarios of the future. Since $h_{t}$ contain information about the probability distribution of the future, the agent can just query the RNN instinctively to guide its action decisions. Like a seasoned Formula One driver or the baseball player discussed earlier, the agent can instinctively predict when and where to navigate in the heat of the moment.

ceobillionaire (Gym Leaderboard)

V model with hidden layer

Full World Model

Table 1: CarRacing-v0 scores achieved using various methods.

Our agent is able to achieve a score of 906 $\pm$ 21 over 100 random trials, effectively solving the task and obtaining new state of the art results. Previous attempts using Deep RL methods obtained average scores of 591--652 range, and the best reported solution on the leaderboard obtained an average score of 838 $\pm$ 11 over 100 random trials. Traditional Deep RL methods often require pre-processing of each frame, such as employing edge-detection, in addition to stacking a few recent frames into the input. In contrast, our world model takes in a stream of raw RGB pixel images and directly learns a spatial-temporal representation. To our knowledge, our method is the first reported solution to solve this task.

### Car Racing Dreams

Since our world model is able to model the future, we are also able to have it come up with hypothetical car racing scenarios on its own. We can ask it to produce the probability distribution of $z_{t + 1}$ given the current states, sample a $z_{t + 1}$ and use this sample as the real observation. We can put our trained C back into this hallucinated environment generated by M. The following image from an interactive demo in the online version of this article shows how our world model can be used to hallucinate the car racing environment:

Figure 13: Our agent driving inside of its own dream world. Here, we deploy our trained policy into a fake environment generated by the MDN-RNN, and rendered using the VAE’s decoder. In the demo, one can override the agent’s actions as well as adjust τ to control the uncertainty of the environment generated by M.

## VizDoom Experiment

### Learning Inside of a Dream

We have just seen that a policy learned inside of the real environment appears to somewhat function inside of the dream environment. This begs the question -- can we train our agent to learn inside of its own dream, and transfer this policy back to the actual environment?

If our world model is sufficiently accurate for its purpose, and complete enough for the problem at hand, we should be able to substitute the actual environment with this world model. After all, our agent does not directly observe the reality, but only sees what the world model lets it see. In this experiment, we train an agent inside the hallucination generated by its world model trained to mimic a VizDoom environment.

Figure 14: Our final agent solving VizDoom: Take Cover.

The agent must learn to avoid fireballs shot by monsters from the other side of the room with the sole intent of killing the agent. There are no explicit rewards in this environment, so to mimic natural selection, the cumulative reward can be defined to be the number of time steps the agent manages to stay alive during a rollout. Each rollout of the environment runs for a maximum of 2100 time steps ($\sim$ 60 seconds), and the task is considered solved if the average survival time over 100 consecutive rollouts is greater than 750 time steps ($\sim$ 20 seconds).

### Procedure

The setup of our VizDoom experiment is largely the same as the Car Racing task, except for a few key differences. In the Car Racing task, M is only trained to model the next $z_{t}$. Since we want to build a world model we can train our agent in, our M model here will also predict whether the agent dies in the next frame (as a binary event $done_{t}$, or $d_{t}$ for short), in addition to the next frame $z_{t}$.

Since the M model can predict the $done$ state in addition to the next observation, we now have all of the ingredients needed to make a full RL environment. We first build an OpenAI Gym environment interface by wrapping a gym.Env interface over our M if it were a real Gym environment, and then train our agent inside of this virtual environment instead of using the actual environment.

In this simulation, we do not need the V model to encode any real pixel frames during the hallucination process, so our agent will therefore only train entirely in a latent space environment. This has many advantages as we will see.

This virtual environment has an identical interface to the real environment, so after the agent learns a satisfactory policy in the virtual environment, we can easily deploy this policy back into the actual environment to see how well the policy transfers over.

To summarize the Take Cover experiment, below are the steps taken:

Collect 10,000 rollouts from a random policy.

Train VAE (V) to encode each frame into a latent vector $z \in \mathcal{R}^{64}$, and use V to convert the images collected from into the latent space representation.

Train MDN-RNN (M) to model\
$P{(z_{t + 1},\left. d_{t + 1} \middle| {a_{t},z_{t},h_{t}} \right.)}$.

Define Controller (C) as $a_{t} = {W_{c}{\lbrack{z_{t}h_{t}}\rbrack}}$.

Use CMA-ES to solve for a $W_{c}$ that maximizes the expected survival time inside the virtual environment.

Use learned policy from on actual environment.

### Training Inside of the Dream

After some training, our controller learns to navigate around the dream environment and escape from deadly fireballs launched by monsters generated by M. Our agent achieved a score of $\sim$ 900 time steps in the virtual environment.

Figure 15: Our agent discovers a policy to avoid hallucinated fireballs. In the online version of this article, the reader can interact with the environment inside this demo.

Here, our RNN-based world model is trained to mimic a complete game environment designed by human programmers. By learning only from raw image data collected from random episodes, it learns how to simulate the essential aspects of the game -- such as the game logic, enemy behaviour, physics, and also the 3D graphics rendering.

For instance, if the agent selects the left action, the M model learns to move the agent to the left and adjust its internal representation of the game states accordingly. It also learns to block the agent from moving beyond the walls on both sides of the level if the agent attempts to move too far in either direction. Occasionally, the M model needs to keep track of multiple fireballs being shot from several different monsters and coherently move them along in their intended directions. It must also detect whether the agent has been killed by one of these fireballs.

Unlike the actual game environment, however, we note that it is possible to add extra uncertainty into the virtual environment, thus making the game more challenging in the dream environment. We can do this by increasing the temperature $\tau$ parameter during the sampling process of $z_{t + 1}$. By increasing the uncertainty, our dream environment becomes more difficult compared to the actual environment. The fireballs may move more randomly in a less predictable path compared to the actual game. Sometimes the agent may even die due to sheer misfortune, without explanation.

We find agents that perform well in higher temperature settings generally perform better in the normal setting. In fact, increasing $\tau$ helps prevent our controller from taking advantage of the imperfections of our world model -- we will discuss this in more depth later on.

### Transfer Policy to Actual Environment

Figure 16: Deploying our policy learned inside of the dream RNN environment back into the actual VizDoom environment.

We took the agent trained inside of the virtual environment and tested its performance on the original VizDoom scenario. The score over 100 random consecutive trials is $\sim$ 1100 time steps, far beyond the required score of 750 time steps, and also much higher than the score obtained inside the more difficult virtual environment.

Figure 17: An interactive VAE of Doom in the online article.

We see that even though the V model is not able to capture all of the details of each frame correctly, for instance, getting the number of monsters correct, the agent is still able to use the learned policy to navigate in the real environment. As the virtual environment cannot even keep track of the exact number of monsters in the first place, an agent that is able to survive the noisier and uncertain virtual nightmare environment will thrive in the original, cleaner environment.

### Cheating the World Model

In our childhood, we may have encountered ways to exploit video games in ways that were not intended by the original game designer. Players discover ways to collect unlimited lives or health, and by taking advantage of these exploits, they can easily complete an otherwise difficult game. However, in the process of doing so, they may have forfeited the opportunity to learn the skill required to master the game as intended by the game designer.

For instance, in our initial experiments, we noticed that our agent discovered an adversarial policy to move around in such a way so that the monsters in this virtual environment governed by the M model never shoots a single fireball during some rollouts. Even when there are signs of a fireball forming, the agent will move in a way to extinguish the fireballs magically as if it has superpowers in the environment.

Because our world model is only an approximate probabilistic model of the environment, it will occasionally generate trajectories that do not follow the laws governing the actual environment. As we saw previously, even the number of monsters on the other side of the room in the actual environment is not exactly reproduced by the world model. Like a child who learns that objects in the air usually fall to the ground, the child might also imagine unrealistic superheroes who fly across the sky. For this reason, our world model will be exploitable by the controller, even if in the actual environment such exploits do not exist.

And since we are using the M model to generate a virtual dream environment for our agent, we are also giving the controller access to all of the hidden states of M. This is essentially granting our agent access to all of the internal states and memory of the game engine, rather than only the game observations that the player gets to see. Therefore our agent can efficiently explore ways to directly manipulate the hidden states of the game engine in its quest to maximize its expected cumulative reward. The weakness of this approach of learning a policy inside a learned dynamics model is that our agent can easily find an adversarial policy that can fool our dynamics model -- it'll find a policy that looks good under our dynamics model, but will fail in the actual environment, usually because it visits states where the model is wrong because they are away from the training distribution.

Figure 18: Agent discovers an adversarial policy to automatically extinguish fireballs after they are fired during some rollouts.

This weakness could be the reason that many previous works that learn dynamics models of RL environments but do not actually use those models to fully replace the actual environments. Like in the M model proposed in, the dynamics model is a deterministic model, making the model easily exploitable by the agent if it is not perfect. Using Bayesian models, as in PILCO, helps to address this issue with the uncertainty estimates to some extent, however, they do not fully solve the problem. Recent work combines the model-based approach with traditional model-free RL training by first initializing the policy network with the learned policy, but must subsequently rely on model-free methods to fine-tune this policy in the actual environment.

In Learning to Think, it is acceptable that the RNN M is not always a reliable predictor. A (potentially evolution-based) RNN C can in principle learn to ignore a flawed M, or exploit certain useful parts of M for arbitrary computational purposes including hierarchical planning etc. This is not what we do here though -- our present approach is still closer to some of the older systems, where a RNN M is used to predict and plan ahead step by step. Unlike this early work, however, we use evolution for C (like in Learning to Think) rather than traditional RL combined with RNNs, which has the advantage of both simplicity and generality.

To make it more difficult for our C model to exploit deficiencies of the M model, we chose to use the MDN-RNN as the dynamics model, which models the distribution of possible outcomes in the actual environment, rather than merely predicting a deterministic future. Even if the actual environment is deterministic, the MDN-RNN would in effect approximate it as a stochastic environment. This has the advantage of allowing us to train our C model inside a more stochastic version of any environment -- we can simply adjust the temperature parameter $\tau$ to control the amount of randomness in the M model, hence controlling the tradeoff between realism and exploitability.

Using a mixture of Gaussian model may seem like overkill given that the latent space encoded with the VAE model is just a single diagonal Gaussian distribution. However, the discrete modes in a mixture density model is useful for environments with random discrete events, such as whether a monster decides to shoot a fireball or stay put. While a single diagonal Gaussian might be sufficient to encode individual frames, a RNN with a mixture density output layer makes it easier to model the logic behind a more complicated environment with discrete random states.

For instance, if we set the temperature parameter to a very low value of $\tau = 0.1$, effectively training our C model with a M model that is almost identical to a deterministic LSTM, the monsters inside this dream environment fail to shoot fireballs, no matter what the agent does, due to mode collapse. The M model is not able to jump to another mode in the mixture of Gaussian model where fireballs are formed and shot. Whatever policy learned inside of this dream will achieve a perfect score of 2100 most of the time, but will obviously fail when unleashed into the harsh reality of the actual world, underperforming even a random policy.

Note again, however, that the simpler and more robust approach in Learning to Think does not insist on using M for step by step planning. Instead, C can learn to use M's subroutines (parts of M's weight matrix) for arbitrary computational purposes but can also learn to ignore M when M is useless and when ignoring M yields better performance. Nevertheless, at least in our present C--M variant, M's predictions are essential for teaching C, more like in some of the early C--M systems, but combined with evolution or black box optimization.

By making the temperature $\tau$ an adjustable parameter of the M model, we can see the effect of training the C model on hallucinated virtual environments with different levels of uncertainty, and see how well they transfer over to the actual environment. We experimented with varying the temperature of the virtual environment and observing the resulting average score over 100 random rollouts of the actual environment after training the agent inside of the virtual environment with a given temperature:

Table 2: Take Cover scores at various temperature settings.

We see that while increasing the temperature of the M model makes it more difficult for the C model to find adversarial policies, increasing it too much will make the virtual environment too difficult for the agent to learn anything, hence in practice it is a hyperparameter we can tune. The temperature also affects the types of strategies the agent discovers. For example, although the best score obtained is 1092 $\pm$ 556 with $\tau = 1.15$, increasing $\tau$ a notch to 1.30 results in a lower score but at the same time a less risky strategy with a lower variance of returns. For comparison, the best score on the OpenAI Gym leaderboard is 820 $\pm$ 58.

## Iterative Training Procedure

In our experiments, the tasks are relatively simple, so a reasonable world model can be trained using a dataset collected from a random policy. But what if our environments become more sophisticated? In any difficult environment, only parts of the world are made available to the agent only after it learns how to strategically navigate through its world.

For more complicated tasks, an iterative training procedure is required. We need our agent to be able to explore its world, and constantly collect new observations so that its world model can be improved and refined over time. An iterative training procedure is as follows:

Initialize M, C with random model parameters.

Rollout to actual environment $N$ times. Save all actions $a_{t}$ and observations $x_{t}$ during rollouts to storage.

Train M to model $P{(x_{t + 1},r_{t + 1},a_{t + 1},\left. d_{t + 1} \middle| {x_{t},a_{t},h_{t}} \right.)}$ and train C to optimize expected rewards inside of M.

Go back to if task has not been completed.

We have shown that one iteration of this training loop was enough to solve simple tasks. For more difficult tasks, we need our controller in Step 2 to actively explore parts of the environment that is beneficial to improve its world model. An exciting research direction is to look at ways to incorporate artificial curiosity and intrinsic motivation and information seeking abilities in an agent to encourage novel exploration. In particular, we can augment the reward function based on improvement in compression quality.

In the present approach, since M is a MDN-RNN that models a probability distribution for the next frame, if it does a poor job, then it means the agent has encountered parts of the world that it is not familiar with. Therefore we can adapt and reuse M's training loss function to encourage curiosity. By flipping the sign of M's loss function in the actual environment, the agent will be encouraged to explore parts of the world that it is not familiar with. The new data it collects may improve the world model.

The iterative training procedure requires the M model to not only predict the next observation $x$ and $done$, but also predict the action and reward for the next time step. This may be required for more difficult tasks. For instance, if our agent needs to learn complex motor skills to walk around its environment, the world model will learn to imitate its own C model that has already learned to walk. After difficult motor skills, such as walking, is absorbed into a large world model with lots of capacity, the smaller C model can rely on the motor skills already absorbed by the world model and focus on learning more higher level skills to navigate itself using the motor skills it had already learned.

Figure 19: How information becomes memory.

An interesting connection to the neuroscience literature is the work on hippocampal replay that examines how the brain replays recent experiences when an animal rests or sleeps. Replaying recent experiences plays an important role in memory consolidation -- where hippocampus-dependent memories become independent of the hippocampus over a period of time. As puts it, replay is less like dreaming and more like thought. We invite readers to read Replay Comes of Age for a detailed overview of replay from a neuroscience perspective with connections to theoretical reinforcement learning.

Iterative training could allow the C--M model to develop a natural hierarchical way to learn. Recent works about self-play in RL and PowerPlay also explores methods that lead to a natural curriculum learning, and we feel this is one of the more exciting research areas of reinforcement learning.

## Related Work

There is extensive literature on learning a dynamics model, and using this model to train a policy. Many concepts first explored in the 1980s for feed-forward neural networks (FNNs) and in the 1990s for RNNs laid some of the groundwork for Learning to Think. The more recent PILCO is a probabilistic model-based search policy method designed to solve difficult control problems. Using data collected from the environment, PILCO uses a Gaussian process (GP) model to learn the system dynamics, and then uses this model to sample many trajectories in order to train a controller to perform a desired task, such as swinging up a pendulum, or riding a unicycle.

Figure 20: A controller with internal RNN model of the world.

While Gaussian processes work well with a small set of low dimension data, their computational complexity makes them difficult to scale up to model a large history of high dimensional observations. Other recent works use Bayesian neural networks instead of GPs to learn a dynamics model. These methods have demonstrated promising results on challenging control tasks, where the states are known and well defined, and the observation is relatively low dimensional. Here we are interested in modelling dynamics observed from high dimensional visual data where our input is a sequence of raw pixel frames.

In robotic control applications, the ability to learn the dynamics of a system from observing only camera-based video inputs is a challenging but important problem. Early work on RL for active vision trained an FNN to take the current image frame of a video sequence to predict the next frame, and use this predictive model to train a fovea-shifting control network trying to find targets in a visual scene. To get around the difficulty of training a dynamical model to learn directly from high-dimensional pixel images, researchers explored using neural networks to first learn a compressed representation of the video frames. Recent work along these lines was able to train controllers using the bottleneck hidden layer of an autoencoder as low-dimensional feature vectors to control a pendulum from pixel inputs. Learning a model of the dynamics from a compressed latent space enable RL algorithms to be much more data-efficient. We invite readers to watch Finn's lecture on Model-Based RL to learn more.

Video game environments are also popular in model-based RL research as a testbed for new ideas. used a feed-forward convolutional neural network (CNN) to learn a forward simulation model of a video game. Learning to predict how different actions affect future states in the environment is useful for game-play agents, since if our agent can predict what happens in the future given its current state and action, it can simply select the best action that suits its goal. This has been demonstrated not only in early work (when compute was a million times more expensive than today) but also in recent studies on several competitive VizDoom environments.

The works mentioned above use FNNs to predict the next video frame. We may want to use models that can capture longer term time dependencies. RNNs are powerful models suitable for sequence modelling. In a lecture called Hallucination with RNNs, Graves demonstrated the ability of RNNs to learn a probabilistic model of Atari game environments. He trained RNNs to learn the structure of such a game and then showed that they can hallucinate similar game levels on its own.

Using RNNs to develop internal models to reason about the future has been explored as early as 1990 in a paper called Making the World Differentiable, and then further explored in. A more recent paper called Learning to Think presented a unifying framework for building a RNN-based general problem solver that can learn a world model of its environment and also learn to reason about the future using this model. Subsequent works have used RNN-based models to generate many frames into the future, and also as an internal model to reason about the future.

In this work, we used evolution strategies to train our controller, as it offers many benefits. For instance, we only need to provide the optimizer with the final cumulative reward, rather than the entire history. ES is also easy to parallelize -- we can launch many instances of rollout with different solutions to many workers and quickly compute a set of cumulative rewards in parallel. Recent works have confirmed that ES is a viable alternative to traditional Deep RL methods on many strong baselines.

Before the popularity of Deep RL methods, evolution-based algorithms have been shown to be effective at solving RL tasks. Evolution-based algorithms have even been able to solve difficult RL tasks from high dimensional pixel inputs. More recent works combine VAE and ES, which is similar to our approach.

## Discussion

Figure 21: Ancient drawing of a RNN-based controller interacting with an environment.

We have demonstrated the possibility of training an agent to perform tasks entirely inside of its simulated latent space dream world. This approach offers many practical benefits. For instance, running computationally intensive game engines require using heavy compute resources for rendering the game states into image frames, or calculating physics not immediately relevant to the game. We may not want to waste cycles training an agent in the actual environment, but instead train the agent as many times as we want inside its simulated environment. Training agents in the real world is even more expensive, so world models that are trained incrementally to simulate reality may prove to be useful for transferring policies back to the real world. Our approach may complement sim2real approaches outlined in.

Furthermore, we can take advantage of deep learning frameworks to accelerate our world model simulations using GPUs in a distributed environment. The benefit of implementing the world model as a fully differentiable recurrent computation graph also means that we may be able to train our agents in the dream directly using the backpropagation algorithm to fine-tune its policy to maximize an objective function.

The choice of using a VAE for the V model and training it as a standalone model also has its limitations, since it may encode parts of the observations that are not relevant to a task. After all, unsupervised learning cannot, by definition, know what will be useful for the task at hand. For instance, it reproduced unimportant detailed brick tile patterns on the side walls in the Doom environment, but failed to reproduce task-relevant tiles on the road in the Car Racing environment. By training together with a M model that predicts rewards, the VAE may learn to focus on task-relevant areas of the image, but the tradeoff here is that we may not be able to reuse the VAE effectively for new tasks without retraining.

Learning task-relevant features has connections to neuroscience as well. Primary sensory neurons are released from inhibition when rewards are received, which suggests that they generally learn task-relevant features, rather than just any features, at least in adulthood.

Another concern is the limited capacity of our world model. While modern storage devices can store large amounts of historical data generated using the iterative training procedure, our LSTM -based world model may not be able to store all of the recorded information inside its weight connections. While the human brain can hold decades and even centuries of memories to some resolution, our neural networks trained with backpropagation have more limited capacity and suffer from issues such as catastrophic forgetting. Future work may explore replacing the small MDN-RNN network with higher capacity models, or incorporating an external memory module, if we want our agent to learn to explore more complicated worlds.

Like early RNN-based C--M systems, ours simulates possible futures time step by time step, without profiting from human-like hierarchical planning or abstract reasoning, which often ignores irrelevant spatial-temporal details. However, the more general Learning To Think approach is not limited to this rather naive approach. Instead it allows a recurrent C to learn to address subroutines of the recurrent M, and reuse them for problem solving in arbitrary computable ways, e.g., through hierarchical planning or other kinds of exploiting parts of M's program-like weight matrix. A recent One Big Net extension of the C--M approach collapses C and M into a single network, and uses PowerPlay-like behavioural replay (where the behaviour of a teacher net is compressed into a student net ) to avoid forgetting old prediction and control skills when learning new ones. Experiments with those more general approaches are left for future work.
