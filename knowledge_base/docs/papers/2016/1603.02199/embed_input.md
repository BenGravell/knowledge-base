<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Hand-Eye Coordination for Robotic Grasping with Deep Learning and Large-Scale Data Collection

Topics include Robotics, Neural networks, Deep learning, Convolutional networks, Real-time systems, Control, Learning, Greedy randomized adaptive search procedure, Convolutional neural network.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe a learning-based approach to hand-eye coordination for robotic grasping from monocular images. To learn hand-eye coordination for grasping, we trained a large convolutional neural network to predict the probability that task-space motion of the gripper will result in successful grasps, using only monocular camera images and independently of camera calibration or the current robot pose. This requires the network to observe the spatial relationship between the gripper and objects in the scene, thus learning hand-eye coordination. We then use this network to servo the gripper in real time to achieve successful grasps. To train our network, we collected over 800,000 grasp attempts over the course of two months, using between 6 and 14 robotic manipulators at any given time, with differences in camera placement and hardware. Our experimental evaluation demonstrates that our method achieves effective real-time control, can successfully grasp novel objects, and corrects mistakes by continuous servoing.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

When humans and animals engage in object manipulation behaviors, the interaction inherently involves a fast feedback loop between perception and action. Even complex manipulation tasks, such as extracting a single object from a cluttered bin, can be performed with hardly any advance planning, relying instead on feedback from touch and vision. In contrast, robotic manipulation often (though not always) relies more heavily on advance planning and analysis, with relatively simple feedback, such as trajectory following, to ensure stability during execution. Part of the reason for this is that incorporating complex sensory inputs such as vision directly into a feedback controller is exceedingly challenging. Techniques such as visual servoing perform continuous feedback on visual features, but typically require the features to be specified by hand, and both open loop perception and feedback (e.g. via visual servoing) requires manual or automatic calibration to determine the precise geometric relationship between the camera and the robot's end-effector.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a learning-based approach to hand-eye coordination, which we demonstrate on a robotic grasping task. Our approach is data-driven and goal-centric: our method learns to servo a robotic gripper to poses that are likely to produce successful grasps, with end-to-end training directly from image pixels to task-space gripper motion. By continuously recomputing the most promising motor commands, our method continuously integrates sensory cues from the environment, allowing it to react to perturbations and adjust the grasp to maximize the probability of success. Furthermore, the motor commands are issued in the frame of the robot, which is not known to the model at test time. This means that the model does not require the camera to be precisely calibrated with respect to the end-effector, but instead uses visual cues to determine the spatial relationship between the gripper and graspable objects in the scene.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method consists of two components: a grasp success predictor, which uses a deep convolutional neural network (CNN) to determine how likely a given motion is to produce a successful grasp, and a continuous servoing mechanism that uses the CNN to continuously update the robot's motor commands. By continuously choosing the best predicted path to a successful grasp, the servoing mechanism provides the robot with fast feedback to perturbations and object motion, as well as robustness to inaccurate actuation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The grasp prediction CNN was trained using a dataset of over 800,000 grasp attempts, collected using a cluster of similar (but not identical) robotic manipulators, shown in Figure 1, over the course of several months. Although the hardware parameters of each robot were initially identical, each unit experienced different wear and tear over the course of data collection, interacted with different objects, and used a slightly different camera pose relative to the robot base. These differences provided a diverse dataset for learning continuous hand-eye coordination for grasping.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of this work are a method for learning continuous visual servoing for robotic grasping from monocular cameras, a novel convolutional neural network architecture for learning to predict the outcome of a grasp attempt, and a large-scale data collection framework for robotic grasps. Our experimental evaluation demonstrates that our convolutional neural network grasping controller achieves a high success rate when grasping in clutter on a wide range of objects, including objects that are large, small, hard, soft, deformable, and translucent. Supplemental videos of our grasping system show that the robot employs continuous feedback to constantly adjust its grasp, accounting for motion of the objects and inaccurate actuation commands. We also compare our approach to open-loop variants to demonstrate the importance of continuous feedback, as well as a hand-engineering grasping baseline that uses manual hand-to-eye calibration and depth sensing. Our method achieves the highest success rates in our experiments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Overview", "weight": 1.0} -->

Our approach to learning hand-eye coordination for grasping consists of two parts. The first part is a prediction network $g{(\mathbf{I}_{t},\mathbf{v}_{t})}$ that accepts visual input $\mathbf{I}_{t}$ and a task-space motion command $\mathbf{v}_{t}$, and outputs the predicted probability that executing the command $\mathbf{v}_{t}$ will produce a successful grasp. The second part is a servoing function $f{(\mathbf{I}_{t})}$ that uses the prediction network to continuously control the robot to servo the gripper to a success grasp. We describe each of these components below: Section 4.1 formally defines the task solved by the prediction network and describes the network architecture, Section 4.2 describes how the servoing function can use the prediction network to perform continuous control.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Overview", "weight": 1.0} -->

By breaking up the hand-eye coordination system into components, we can train the CNN grasp predictor using a standard supervised learning objective, and design the servoing mechanism to utilize this predictor to optimize grasp performance. The resulting method can be interpreted as a type of reinforcement learning, and we discuss this interpretation, together with the underlying assumptions, in Section 4.3.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Overview", "weight": 1.0} -->

In order to train our prediction network, we collected over 800,000 grasp attempts using a set of similar (but not identical) robotic manipulators, shown in Figure 1. We discuss the details of our hardware setup in Section 5.1, and discuss the data collection process in Section 5.2. To ensure generalization of the learned prediction network, the specific parameters of each robot varied in terms of the camera pose relative to the robot, providing independence to camera calibration. Furthermore, uneven wear and tear on each robot resulted in differences in the shape of the gripper fingers. Although accurately predicting optimal motion vectors in open-loop is not possible with this degree of variation, as demonstrated in our experiments, our continuous servoing method can correct mistakes by observing the outcomes of its past actions, achieving a high success rate even without knowledge of the precise camera calibration.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Grasping with Convolutional Networks and Continuous Servoing", "weight": 1.0} -->

In this section, we discuss each component of our approach, including a description of the neural network architecture and the servoing mechanism, and conclude with an interpretation of the method as a form of reinforcement learning, including the corresponding assumptions on the structure of the decision problem.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Grasp Success Prediction with Convolutional Neural Networks", "weight": 1.0} -->

The grasp prediction network $g{(\mathbf{I}_{t},\mathbf{v}_{t})}$ is trained to predict whether a given task-space motion $\mathbf{v}_{t}$ will result in a successful grasp, based on the current camera observation $\mathbf{I}_{t}$. In order to make accurate predictions, $g{(\mathbf{I}_{t},\mathbf{v}_{t})}$ must be able to parse the current camera image, locate the gripper, and determine whether moving the gripper according to $\mathbf{v}_{t}$ will put it in a position where closing the fingers will pick up an object. This is a complex spatial reasoning task that requires not only the ability to parse the geometry of the scene from monocular images, but also the ability to interpret material properties and spatial relationships between objects, which strongly affect the success of a given grasp. A pair of example input images for the network is shown in Figure 2, overlaid with lines colored accordingly to the inferred grasp success probabilities.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Grasp Success Prediction with Convolutional Neural Networks", "weight": 1.0} -->

Importantly, the movement vectors provided to the network are not transformed into the frame of the camera, which means that the method does not require hand-to-eye camera calibration. However, this also means that the network must itself infer the outcome of a task-space motor command by determining the orientation and position of the robot and gripper.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Grasp Success Prediction with Convolutional Neural Networks", "weight": 1.0} -->

Data for training the CNN grasp predictor is obtained by attempting grasps using real physical robots. Each grasp consists of $T$ time steps. At each time step, the robot records the current image $\mathbf{I}_{t}^{i}$ and the current pose $\mathbf{p}_{t}^{i}$, and then chooses a direction along which to move the gripper. At the final time step $T$, the robot closes the gripper and evaluates the success of the grasp (as described in Appendix B), producing a label $\ell_{i}$. Each grasp attempt results in $T$ training samples, given by $(\mathbf{I}_{t}^{i},{\mathbf{p}_{T}^{i} - \mathbf{p}_{t}^{i}},\ell_{i})$. That is, each sample includes the image observed at that time step, the vector from the current pose to the one that is eventually reached, and the success of the entire grasp.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Grasp Success Prediction with Convolutional Neural Networks", "weight": 1.0} -->

This process is illustrated in Figure 3. This procedure trains the network to predict whether moving a gripper along a given vector and then grasping will produce a successful grasp. Note that this differs from the standard reinforcement-learning setting, where the prediction is based on the current state and motor command, which in this case is given by $\mathbf{p}_{t + 1} - \mathbf{p}_{t}$. We discuss the interpretation of this approach in the context of reinforcement learning in Section 4.3.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Grasp Success Prediction with Convolutional Neural Networks", "weight": 1.0} -->

The architecture of our grasp prediction CNN is shown in Figure 4. The network takes the current image $\mathbf{I}_{t}$ as input, as well as an additional image $\mathbf{I}_{0}$ that is recorded before the grasp begins, and does not contain the gripper. This additional image provides an unoccluded view of the scene. The two input images are concatenated and processed by 5 convolutional layers with batch normalization, following by max pooling. After the $5^{\text{th}}$ layer, we provide the vector $\mathbf{v}_{t}$ as input to the network. The vector is represented by 5 values: a 3D translation vector, and a sine-cosine encoding of the change in orientation of the gripper about the vertical axis.^11^1In this work, we only consider vertical pinch grasps, though extensions to other grasp parameterizations would be straightforward.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Grasp Success Prediction with Convolutional Neural Networks", "weight": 1.0} -->

To provide this vector to the convolutional network, we pass it through one fully connected layer and replicate it over the spatial dimensions of the response map after layer 5, concatenating it with the output of the pooling layer. After this concatenation, further convolution and pooling operations are applied, as described in Figure 4, followed by a set of small fully connected layers that output the probability of grasp success, trained with a cross-entropy loss to match $\ell_{i}$, causing the network to output $p{({\ell_{i} = 1})}$. The input matches are $512 \times 512$ pixels, and we randomly crop the images to a $472 \times 472$ region during training to provide for translation invariance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Grasp Success Prediction with Convolutional Neural Networks", "weight": 1.0} -->

Once trained the network $g{(\mathbf{I}_{t},\mathbf{v}_{t})}$ can predict the probability of success of a given motor command, independently of the exact camera pose. In the next section, we discuss how this grasp success predictor can be used to continuous servo the gripper to a graspable object.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Continuous Servoing", "weight": 1.0} -->

In this section, we describe the servoing mechanism $f{(\mathbf{I}_{t})}$ that uses the grasp prediction network to choose the motor commands for the robot that will maximize the probability of a success grasp. The most basic operation for the servoing mechanism is to perform inference in the grasp predictor, in order to determine the motor command $\mathbf{v}_{t}$ given an image $\mathbf{I}_{t}$. The simplest way of doing this is to randomly sample a set of candidate motor commands $\mathbf{v}_{t}$ and then evaluate $g{(\mathbf{I}_{t},\mathbf{v}_{t})}$, taking the command with the highest probability of success. However, we can obtain better results by running a small optimization on $\mathbf{v}_{t}$, which we perform using the cross-entropy method (CEM).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Continuous Servoing", "weight": 1.0} -->

CEM is a simple derivative-free optimization algorithm that samples a batch of $N$ values at each iteration, fits a Gaussian distribution to $M < N$ of these samples, and then samples a new batch of $N$ from this Gaussian. We use $N = 64$ and $M = 6$ in our implementation, and perform three iterations of CEM to determine the best available command $\mathbf{v}_{t}^{\star}$ and thus evaluate $f{(\mathbf{I}_{t})}$. New motor commands are issued as soon as the CEM optimization completes, and the controller runs at around 2 to 5 Hz.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Continuous Servoing", "weight": 1.0} -->

One appealing property of this sampling-based approach is that we can easily impose constraints on the types of grasps that are sampled. This can be used, for example, to incorporate user commands that require the robot to grasp in a particular location, keep the robot from grasping outside of the workspace, and obey joint limits. It also allows the servoing mechanism to control the height of the gripper during each move. It is often desirable to raise the gripper above the objects in the scene to reposition it to a new location, for example when the objects move (due to contacts) or if errors due to lack of camera calibration produce motions that do not position the gripper in a favorable configuration for grasping.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Continuous Servoing", "weight": 1.0} -->

We can use the predicted grasp success $p{({\ell = 1})}$ produced by the network to inform a heuristic for raising and lowering the gripper, as well as to choose when to stop moving and attempt a grasp. We use two heuristics in particular: first, we close the gripper whenever the network predicts that $(\mathbf{I}_{t},\varnothing)$, where $\varnothing$ corresponds to no motion, will succeed with a probability that is at least $90\%$ of the best inferred motion $\mathbf{v}_{t}^{\star}$. The rationale behind this is to stop the grasp early if closing the gripper is nearly as likely to produce a successful grasp as moving it. The second heuristic is to raise the gripper off the table when $(\mathbf{I}_{t},\varnothing)$ has a probability of success that is less than $50\%$ of $\mathbf{v}_{t}^{\star}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Continuous Servoing", "weight": 1.0} -->

The rationale behind this choice is that, if closing the gripper now is substantially worse than moving it, the gripper is most likely not positioned in a good configuration, and a large motion will be required. Therefore, raising the gripper off the table minimizes the chance of hitting other objects that are in the way. While these heuristics are somewhat ad-hoc, we found that they were effective for successfully grasping a wide range of objects in highly cluttered situations, as discussed in Section 6. Pseudocode for the servoing mechanism $f{(\mathbf{I}_{t})}$ is presented in Algorithm 1. Further details on the servoing mechanism are presented in Appendix A.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Continuous Servoing", "weight": 1.0} -->

1: Given current image It and network g. 2: Infer vt⋆ using g and CEM. 5: Output ⌀, close gripper. 7: Modify vt⋆ to raise gripper height and execute vt⋆. Algorithm 1 Servoing mechanism f (It)

<!-- chunk {"id": "body-0025", "role": "body", "section": "Interpretation as Reinforcement Learning", "weight": 1.0} -->

One interesting conceptual question raised by our approach is the relationship between training the grasp prediction network and reinforcement learning. In the case where $T = 2$, and only one decision is made by the servoing mechanism, the grasp network can be regarded as approximating the Q-function for the policy defined by the servoing mechanism $f{(\mathbf{I}_{t})}$ and a reward function that is $1$ when the grasp succeeds and $0$ otherwise. Repeatedly deploying the latest grasp network $g{(\mathbf{I}_{t},\mathbf{v}_{t})}$, collecting additional data, and refitting $g{(\mathbf{I}_{t},\mathbf{v}_{t})}$ can then be regarded as fitted Q iteration. However, what happens when $T > 2$?

<!-- chunk {"id": "body-0026", "role": "body", "section": "Interpretation as Reinforcement Learning", "weight": 1.0} -->

In that case, fitted Q iteration would correspond to learning to predict the final probability of success from tuples of the form $(\mathbf{I}_{t},{\mathbf{p}_{t + 1} - \mathbf{p}_{t}})$, which is substantially harder, since $\mathbf{p}_{t + 1} - \mathbf{p}_{t}$ doesn't tell us where the gripper will end up at the end, before closing (which is $\mathbf{p}_{T}$).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Interpretation as Reinforcement Learning", "weight": 1.0} -->

Using $\mathbf{p}_{T} - \mathbf{p}_{t}$ as the action representation in fitted Q iteration therefore implies an additional assumption on the form of the dynamics. The assumption is that the actions induce a transitive relation between states: that is, that moving from $\mathbf{p}_{1}$ to $\mathbf{p}_{2}$ and then to $\mathbf{p}_{3}$ is equivalent to moving from $\mathbf{p}_{1}$ to $\mathbf{p}_{3}$ directly. This assumption does not always hold in the case of grasping, since an intermediate motion might move objects in the scene, but it is a reasonable approximation that we found works quite well in practice. The major advantage of this approximation is that fitting the Q function reduces to a prediction problem, and avoids the usual instabilities associated with Q iteration, since the previous Q function does not appear in the regression. An interesting and promising direction for future work is to combine our approach with more standard reinforcement learning formulations that do consider the effects of intermediate actions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Interpretation as Reinforcement Learning", "weight": 1.0} -->

This could enable the robot, for example, to perform nonprehensile manipulations to intentionally reorient and reposition objects prior to grasping.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Large-Scale Data Collection", "weight": 1.0} -->

In order to collect training data to train the prediction network $g{(\mathbf{I}_{t},\mathbf{v}_{t})}$, we used between 6 and 14 robots at any given time. An illustration of our data collection setup is shown in Figure 1. This section describes the robots used in our data collection process, as well as the data collection procedure.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Hardware Setup", "weight": 1.0} -->

Our robotic manipulator platform consists of a lightweight 7 degree of freedom arm, a compliant, underactuated, two-finger gripper, and a camera mounted behind the arm looking over the shoulder. An illustration of a single robot is shown in Figure 5. The underactuated gripper provides some degree of compliance for oddly shaped objects, at the cost of producing a loose grip that is prone to slipping. An interesting property of this gripper was uneven wear and tear over the course of data collection, which lasted several months. Images of the grippers of various robots are shown in Figure 7, illustrating the range of variation in gripper wear and geometry. Furthermore, the cameras were mounted at slightly varying angles, providing a different viewpoint for each robot. The views from the cameras of all 14 robots during data collection are shown in Figure 6.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Data Collection", "weight": 1.0} -->

We collected about 800,000 grasp attempts over the course of two months, using between 6 and 14 robots at any given point in time, without any manual annotation or supervision. The only human intervention into the data collection process was to replace the object in the bins in front of the robots and turn on the system. The data collection process started with random motor command selection and $T = 2$.^22^2The last command is always $\mathbf{v}_{T} = \varnothing$ and corresponds to closing the gripper without moving. When executing completely random motor commands, the robots were successful on 10% - 30% of the grasp attempts, depending on the particular objects in front of them. About half of the dataset was collected using random grasps, and the rest used the latest network fitted to all of the data collected so far. Over the course of data collection, we updated the network 4 times, and increased the number of steps from $T = 2$ at the beginning to $T = 10$ at the end.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Data Collection", "weight": 1.0} -->

The objects for grasping were chosen among common household and office items, and ranged from a $4$ to $20$ cm in length along the longest axis. Some of these objects are shown in Figure 6. The objects were placed in front of the robots into metal bins with sloped sides to prevent the objects from becoming wedged into corners. The objects were periodically swapped out to increase the diversity of the training data.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Data Collection", "weight": 1.0} -->

Grasp success was evaluated using two methods: first, we marked a grasp as successful if the position reading on the gripper was greater than 1 cm, indicating that the fingers had not closed fully. However, this method often missed thin objects, and we also included a drop test, where the robot picked up the object, recorded an image of the bin, and then dropped any object that was in the gripper. By comparing the image before and after the drop, we could determine whether any object had been picked up.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

To evaluate our continuous grasping system, we conducted a series of quantitative experiments with novel objects that were not seen during training. The particular objects used in our evaluation are shown in Figure 8. This set of objects presents a challenging cross section of common office and household items, including objects that are heavy, such as staplers and tape dispensers, objects that are flat, such as post-it notes, as well as objects that are small, large, rigid, soft, and translucent.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The goal of our evaluation was to answer the following questions: does continuous servoing significantly improve grasping accuracy and success rate? how well does our learning-based system perform when compared to alternative approaches? To answer question, we compared our approach to an open-loop method that observes the scene prior to the grasp, extracts image patches, chooses the patch with the highest probability of a successful grasp, and then uses a known camera calibration to move the gripper to that location. This method is analogous to the approach proposed by Pinto & Gupta, but uses the same network architecture as our method and the same training set. We refer to this approach as "open loop," since it does not make use of continuous visual feedback. To answer question, we also compared our approach to a random baseline method, as well as a hand-engineered grasping system that uses depth images and heuristic positioning of the fingers. This hand-engineered system is described in Appendix C. Note that our method requires fewer assumptions than either of the two alternative methods: unlike Pinto & Gupta, we do not require knowledge of the camera to hand calibration, and unlike the hand-engineered system, we do not require either the calibration or depth images.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We evaluated the methods using two experimental protocols. In the first protocol, the objects were placed into a bin in front of the robot, and it was allowed to grasp objects for 100 attempts, placing any grasped object back into the bin after each attempt. Grasping with replacement tests the ability of the system to pick up objects in cluttered settings, but it also allows the robot to repeatedly pick up easy objects. To address this shortcoming of the replacement condition, we also tested each system without replacement, as shown in Figure 8, by having it remove objects from a bin. For this condition, which we refer to as "without replacement," we repeated each experiment 4 times, and we report success rates on the first 10, 20, and 30 grasp attempts.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Comparisons", "weight": 1.0} -->

The results are presented in Table 1. The success rate of our continuous servoing method exceeded the baseline and prior methods in all cases. For the evaluation without replacement, our method cleared the bin completely after 30 grasps on one of the 4 attempts, and had only one object left in the other 3 attempts (which was picked up on the $31^{\text{st}}$ grasp attempt in 2 of the three cases, thus clearing the bin). The hand-engineered baseline struggled to accurately resolve graspable objects in clutter, since the camera was positioned about a meter away from the table, and its performance also dropped in the non-replacement case as the bin was emptied, leaving only small, flat objects that could not be resolved by the depth camera. Many practical grasping systems use a wrist-mounted camera to address this issue. In contrast, our approach did not require any special hardware modifications. The open-loop baseline was also substantially less successful.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Comparisons", "weight": 1.0} -->

Although it benefited from the large dataset collected by our parallelized data collection setup, which was more than an order of magnitude larger than in prior work, it was unable to react to perturbations, movement of objects, and variability in actuation and gripper shape.^33^3The absolute performance of the open-loop method is lower than reported by Pinto & Gupta. This can be attributed to differences in the setup: different objects, grippers, and clutter.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Evaluating Data Requirements", "weight": 1.0} -->

In Table 2, we evaluate the performance of our model under the no replacement condition with varying amounts of data. We trained grasp prediction models using roughly the first $12\%$, $25\%$, and $50\%$ of the grasp attempts in our dataset, to simulate the effective performance of the model one eighth, one quarter, and one half of the way through the data collection process. Table 2 shows the size of each dataset in terms of the number of images. Note that the length of the trajectories changed over the course of data collection, increasing from $T = 2$ at the beginning to $T = 10$ at the end, so that the later datasets are substantially larger in terms of the total number of images. Furthermore, the success rate in the later grasp attempts was substantially higher, increasing from $10$ to $20\%$ in the beginning to around $70\%$ at the end (using $\epsilon$-greedy exploration with $\epsilon = 0.1$, meaning that one in ten decisions was taken at random). Nonetheless, these results can be informative for understanding the data requirements of the grasping task.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Evaluating Data Requirements", "weight": 1.0} -->

First, the results suggest that the grasp success rate continued to improve as more data was accumulated, and a high success rate (exceeding the open-loop and hand-engineered baselines) was not observed until at least halfway through the data collection process. The results also suggest that collecting additional data could further improve the accuracy of the grasping system, and we plan to experiment with larger datasets in the future.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Qualitatively, our method exhibited some interesting behaviors. Figure 9 shows the grasps that were chosen for soft and hard objects. Our system preferred to grasp softer objects by embedding the finger into the center of the object, while harder objects were grasped by placing the fingers on either side. Our method was also able to grasp a variety of challenging objects, some of which are shown in Figure 10. Other interesting grasp strategies, corrections, and mistakes can be seen in our supplementary video: Figure 10: Examples of difficult objects grasped by our algorithm, including objects that are translucent, awkardly shaped, and heavy.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

We presented a method for learning hand-eye coordination for robotic grasping, using deep learning to build a grasp success prediction network, and a continuous servoing mechanism to use this network to continuously control a robotic manipulator. By training on over 800,000 grasp attempts from 14 distinct robotic manipulators with variation in camera pose, we can achieve invariance to camera calibration and small variations in the hardware. Unlike most grasping and visual servoing methods, our approach does not require calibration of the camera to the robot, instead using continuous feedback to correct any errors resulting from discrepancies in calibration. Our experimental results demonstrate that our method can effectively grasp a wide range of different objects, including novel objects not seen during training. Our results also show that our method can use continuous feedback to correct mistakes and reposition the gripper in response to perturbation and movement of objects in the scene.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

As with all learning-based methods, our approach assumes that the data distribution during training resembles the distribution at test-time. While this assumption is reasonable for a large and diverse training set, such as the one used in this work, structural regularities during data collection can limit generalization at test time. For example, although our method exhibits some robustness to small variations in gripper shape, it would not readily generalize to new robotic platforms that differ substantially from those used during training. Furthermore, since all of our training grasp attempts were executed on flat surfaces, the proposed method is unlikely to generalize well to grasping on shelves, narrow cubbies, or other drastically different settings. These issues can be mitigated by increasing the diversity of the training setup, which we plan to explore as future work.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

One of the most exciting aspects of the proposed grasping method is the ability of the learning algorithm to discover unconventional and non-obvious grasping strategies. We observed, for example, that the system tended to adopt a different approach for grasping soft objects, as opposed to hard ones. For hard objects, the fingers must be placed on either side of the object for a successful grasp. However, soft objects can be grasped simply by pinching into the object, which is most easily accomplished by placing one finger into the middle, and the other to the side. We observed this strategy for objects such as paper tissues and sponges. In future work, we plan to further explore the relationship between our self-supervised continuous grasping approach and reinforcement learning, in order to allow the methods to learn a wider variety of grasp strategies from large datasets of robotic experience.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

At a more general level, our work explores the implications of large-scale data collection across multiple robotic platforms, demonstrating the value of this type of automatic large dataset construction for real-world robotic tasks. Although all of the robots in our experiments were located in a controlled laboratory environment, in the long term, this class of methods is particularly compelling for robotic systems that are deployed in the real world, and therefore are naturally exposed to a wide variety of environments, objects, lighting conditions, and wear and tear. For self-supervised tasks such as grasping, data collected and shared by robots in the real world would be the most representative of test-time inputs, and would therefore be the best possible training data for improving the real-world performance of the system. So a particularly exciting avenue for future work is to explore how our method would need to change to apply it to large-scale data collection across a large number of deployed robots engaged in real world tasks, including grasping and other manipulation skills.
