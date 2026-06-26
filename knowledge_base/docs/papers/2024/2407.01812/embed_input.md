<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Equivariant Diffusion Policy

Topics include Diffusion models, Generalization, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent work has shown diffusion models are an effective approach to learning the multimodal distributions arising from demonstration data in behavior cloning. However, a drawback of this approach is the need to learn a denoising function, which is significantly more complex than learning an explicit policy. In this work, we propose Equivariant Diffusion Policy, a novel diffusion policy learning method that leverages domain symmetries to obtain better sample efficiency and generalization in the denoising function. We theoretically analyze the SO symmetry of full 6-DoF control and characterize when a diffusion model is SO-equivariant. We furthermore evaluate the method empirically on a set of 12 simulation tasks in MimicGen, and show that it obtains a success rate that is, on average, 21.9% higher than the baseline Diffusion Policy. We also evaluate the method on a real-world system to show that effective policies can be learned with relatively few training samples, whereas the baseline Diffusion Policy cannot.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recently proposed Diffusion Policy formulates robotic manipulation action prediction as a diffusion model that denoises the action conditioned on the observation, thereby better capturing the multimodal action distribution of the demonstration data in Behavior Cloning (BC). Although Diffusion Policy often outperforms baselines on benchmarks, a key drawback is that the denoising function is more complex than a standard policy function. In particular, for a single state-action pair ( s, a ), the denoising process uses a mapping ( s, a + ε k, k ) ↦→ ε k for all possible k and ε k, where ε k is Gaussian noise conditioned on step k, which is harder to train compared with an explicit BC s ↦→ a.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we leverage equivariant neural models to embed task symmetry as an inductive bias in the diffusion process, making the denois- Figure 1: Equivariance in diffusion policy. Top left: a randomly sampled trajectory. Top right: a valid trajectory after denoising. If the state and the random trajectory are both rotated (bottom left), and we rotate the noise accordingly in the denoising process, we will end up with a successful trajectory in the rotated state (bottom right). ing function easier to learn. Although equivariant diffusion models have been studied by a number of prior works, our paper is the first to study the idea in the context of visuomotor policy learning. As illustrated in Figure 1, rotation of a state and noisy trajectory action about the gravity axis (i.e., rotated on the tabletop) results in a corresponding rotation of the denoised trajec- tory. As a result of this symmetry, our model is more data efficient and generalizes better than the non-symmetric baselines, mitigating the high data costs typically associated with diffusion.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

∗ Part of the work was done as an intern at the Boston Dynamics AI Institute Our contributions are as follows: 1) we propose Equivariant Diffusion Policy, a novel BC approach based on equivariant diffusion, 2) we analyze the conditions under which the denoising function is equivariant, 3) we theoretically demonstrate the use of SO -equivariance in the context of 6-DoF control for robotic manipulation, which prior methods leveraged in a less expressive SE action space, and 4) we provide a thorough demonstration of our method in both simulated and physical systems. In simulation, we evaluate on 12 manipulation tasks in the MimicGen benchmark and outperform the baseline Diffusion Policy by an average success rate of 21.9% when trained with 100 demos. On hardware, we show that successful policies can be learned with a small number (between 20 and 60) of demonstrations for six different manipulation tasks, including a long-horizon bagel baking task, while the original Diffusion Policy performs poorly in this low-data regime.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Theory of Equivariant Diffusion Policy", "weight": 1.0} -->

The main contribution of this paper is a method that incorporates equivariance in the diffusion process for policy learning. As theoretical justification, we first analyze the noise prediction function and show that it is equivariant any time the expert policy that is being modeled is equivariant. This implies equivariant neural networks have the correct inductive bias to model this function.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Theory of Equivariant Diffusion Policy", "weight": 1.0} -->

Let π: o ↦→ a be the expert policy function, and let ε: ( o, a k, k ) ↦→ ε k be the ground truth noise prediction function associated with the expert policy such that ε k = ε ( o, π ( o ) + ε k, k ). Assume g ∈ SO acts upon the noise ε k in the same way as it acts upon the action a.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Theory of Equivariant Diffusion Policy", "weight": 1.0} -->

Proposition 1. The noise prediction function ε is equivariant, i.e., ε ( g o, g a k, k ) = gε ( o, a k, k ), g ∈ SO, when the expert policy function is SO -equivariant, i.e., π ( g o ) = gπ ( o ), g ∈ SO.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Theory of Equivariant Diffusion Policy", "weight": 1.0} -->

See Appendix A for the proof. Figure 2 illustrates the equivariance property of ε. If we infer ε for all actions in the action space, we effectively acquire a gradient field towards the expert trajectory. The figure shows that such a gradient field is equivariant when the expert policy is equivariant, thus the function ε is also equivariant. Notice that the figure shows the average of all action time steps.

<!-- chunk {"id": "body-0010", "role": "body", "section": "SO Representation on 6DoF Action", "weight": 1.0} -->

A key step in defining an Equivariant Diffusion Policy is to define how actions a t transform under rotation. We describe this transformation in terms of irreducible SO representations, which allows us to build the equivariance constraint into the denoising network.

<!-- chunk {"id": "body-0011", "role": "body", "section": "SO Representation on 6DoF Action", "weight": 1.0} -->

Proposition 2. There exist irreducible representations that describe how SO acts on an SE gripper action a t. In absolute pose control, let a t = Vec c ( A t ) where Vec c flattens an SE pose A t ∈ R 4 × 4 into a vector by column, g a t = ( ρ 1 ⊕ ρ 2 0 ) 4 ( g ) a t. In relative pose control, let a t = Vec r ( A t ) where Vec r flattens A t into a vector by row, g a t = P -1 [ ( ρ 6 0 ⊕ ρ 4 1 ⊕ ρ 2 )( g ) ] P a t, where P is a fixed change-of-basis matrix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "SO Representation on 6DoF Action", "weight": 1.0} -->

Absolute Control We first consider absolute pose control, i.e., T t +1 = A t. Let T g be the transformation matrix corresponding to the SO rotation along the z -axis of the world frame, T g = (cos g -sin g 0 0 sin g cos g 0 0 0 0 1 0 0 0 0 1) = (ρ 1 (g) ρ 0 (g) ρ 0 (g)), where ρ 1 (g) = (cos g -sin g sin g cos g). The SO action on A t is g A t = T g A t = (ρ 1 ⊕ ρ 2 0)(g) A t. Vectorizing A t by column gives a t = Vec c (A t) = [A 1 T t, A 2 T t, A 3 T t, A 4 T t] T where A i t is the i th column of A t. By the rule of matrix multiplication, we have g A i t = (ρ 1 ⊕ ρ 2 0)(g) A i t and g a t = (ρ 1 ⊕ ρ 2 0) 4 (g) a t.

<!-- chunk {"id": "body-0013", "role": "body", "section": "SO Representation on 6DoF Action", "weight": 1.0} -->

Since the gripper open width is invariant, gw t = ρ 0 ( g ) w t, we can append w t to a t and add an extra ρ 0 to the representation. We can also simplify the representation by removing the constants in the transformation matrix and removing the last row in the rotation part of the transformation matrix (i.e., the 6D rotation representation ). The resulting action vector would be a t ∈ R 6 × R 3 × R, where the first six elements are the 6D rotation, the following three elements are the translation, and the last element is the gripper open width. In such a case, we have g a t = ( ρ 3 1 ⊕ ( ρ 1 ⊕ ρ 0 ) ⊕ ρ 0 )( g ) a t.

<!-- chunk {"id": "body-0014", "role": "body", "section": "SO Representation on 6DoF Action", "weight": 1.0} -->

Relative Control For relative gripper pose, i.e., T t +1 = A t T t, the group action on A t satisfies ( g A t ) T g T t = T g ( A t T t ) (because the rotation g ∈ SO applies to both the current pose and the change of pose). Solving for g A t we get g A t = T g A t T -1 g. Let a t = Vec r ( A t ) where Vec r: R n × m → R ( n · m ) flattens a matrix into a vector by row. Here we want to find a linear action ρ A that satisfies g a t = ρ A ( g )Vec r ( A t ) = Vec r ( T g A t T -1 g ). After solving for ρ A ∈ R 16 × 16 and calculating a change-of-basis matrix P such that Pρ A P -1 is a block diagonal matrix consisting of irreducible representations, we have g a t = P -1 [ ( ρ 6 0 ⊕ ρ 4 1 ⊕ ρ 2 )( g ) ] P a t (see Appendix B for details).

<!-- chunk {"id": "body-0015", "role": "body", "section": "SO Representation on 6DoF Action", "weight": 1.0} -->

For easier implementation, we add a ρ 0 for the gripper action w t, remove the constants in the transformation matrix, and decompose SE = SO × R 3. See Appendix C.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Implementation of Equivariant Diffusion Policy", "weight": 1.0} -->

Now that we have the theoretical grounding of the equivariance in the noise prediction function ε, this section will introduce the network architecture of our Equivariant Diffusion Policy. As is shown in Figure 3, our network consists of three main parts: encoding (white box), denoising (yellow box), and decoding (gray box). We implement our network using the escnn library. First, an equivariant observation encoder and an equivariant action encoder take inputs o and a k, respectively, to create equivariant embeddings e o and e a k. The embeddings will be in the form of a regular representation of the subgroup C u ⊂ SO (where u is the number of discrete rotations in the group). The embeddings have shape e o ∈ R u × d o and e a k ∈ R u × d a, where each of the d o or d a dimensional vectors encodes the features for a specific group element (i.e., a rotation angle).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Implementation of Equivariant Diffusion Policy", "weight": 1.0} -->

Second, in the denoising step, let e g o ∈ R d o and e g a k ∈ R d a be a pair of partial embeddings corresponding to the same group element g. We process each pair with a 1D Temporal U-Net (adopted from the prior works ) to calculate an equivariant noise embedding. Specifically, letting k be the denoising step, U the U-Net, and z its output, we have z g = U ( e g o, e g a k, k ). Since the same network is applied for all g ∈ C u, the output is an equivariant embedding of the noise in the regular representation. Finally, an equivariant decoder will decode the noise ε k. See Appendix D for details.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Simulation Experiment", "weight": 1.0} -->

Experimental Settings We first evaluate our Equivariant Diffusion Policy (EquiDiff) with either image (Im) or voxel (Vo) input on 12 manipulation tasks from MimicGen (Figure 4). We define the rotation of the observation as a voxel grid rotation or an image rotation. Notice that in the image version of our method, there is a mismatch between the rotation of the agent view image and the rotation of the ground truth state since the agent view is not orthogonally top-down. Although topdown observations could be captured, we use the observation settings in the published dataset from MimicGen to demonstrate the generalizability of our method 1. On the other hand, the voxel version eliminates this symmetry mismatch as the rotation of the voxel grid aligns with the rotation of the ground truth state. To better leverage the equivariance, we also add a rotation augmentation in the voxel version of our method following our analysis in Section 4.1-4.2. We compare our method with the following baselines: 1) DiffPo-C: the original diffusion policy trained with the 1D Temporal UNet.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Simulation Experiment", "weight": 1.0} -->

Notice that the baseline shares the same UNet architecture as our method, but it does not have any equivariant structure. 2) DiffPo-T: same as above, but trained with a transformer. 3) DP3: the 3D diffusion policy trained with a point net encoder. 4) ACT: the Action Chunking Transformer trained as a conditional V AE. 5) BC RNN: a recurrent architecture. Notice that the voxel version of our method and DP3 utilizes the 3D inputs constructed from four cameras, while the image version of our method and the other baselines directly use the RGB images from two cameras. As our main baseline, we evaluate DiffPo-C in both absolute and relative pose control. We evaluate the other baselines in the same control mode as in the original work (absolute for DiffPo-T, DP3 and ACT, and relative for BC RNN). See Appendix E and F for the details.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Simulation Experiment", "weight": 1.0} -->

1 Prior work demonstrate that the equivariant CNN is still able to capture symmetry in such a scenario.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Simulation Experiment", "weight": 1.0} -->

| | | | Stack D1 | Stack D1 | Stack D1 | Stack Three D1 | Stack Three D1 | Stack Three D1 | Square D2 | Square D2 | Square D2 | Threading D2 | Threading D2 | Threading D2 | Threading D2 | Threading D2 | Threading D2 | Threading D2 | Threading D2 | Threading D2 | Threading D2 | Results Table 1 shows the experimental result in terms of the maximum success rate among 50 evaluations throughout the training. First, with absolute pose control, our Equivariant Diffusion Policy with voxel input achieves the best overall performance, outperforming the baselines in 11 out of the 12 environments (Hammer Cleanup D1 being the exception). With RGB image inputs, our method outperforms all RGB baselines in all environments except for Kitchen D1. Second, in relative control, our method with voxel input achieves the best performance, while our method with RGB input is only marginally better than the baselines. Third, our method appears to perform particularly well in the low- data regime (i.e., with 100 or 200 demos).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Simulation Experiment", "weight": 1.0} -->

Specifically, taking the average over all environments (as is shown in Table 2), our method with voxel input and absolute pose control trained with 100 demos outperforms the best baseline by 21.9%. When trained with 200 demos, it outperforms all baselines trained with 1000 demos, indicating the strong sample efficiency of our method. We also perform an ablation study in Appendix H, where we ablate the equivariant structure and the voxel input in our method. We show that though both of these items contribute to the performance improvement our method shows over the baseline, the equivariant structure is the more important factor.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Simulation Experiment", "weight": 1.0} -->

| | | Average over 12 Environments | Average over 12 Environments | Average over 12 Environments | Figure 5: (a) The three task groups are based on the level of equivariance and their initial object distribution. Images were generated by taking the average of five random initialization states. (b) The performance improvement of our Equivariant Diffusion Policy (Voxel) compared with the original diffusion policy in absolute pose control. Blue environments are high-equivariance tasks; green environments are intermediate-equivariance tasks; red environments are low-equivariance tasks.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Improvement with Different Levels of Equivariance", "weight": 1.0} -->

Wefurther analyze the performance improvement of our method when the tasks have different levels of equivariance. Since equivariant models generalize automatically across different object poses, equivariance should hypothetically be more useful when there is greater variance in the distribution of initial object poses. We qualitatively group the tasks into three levels: 1) high-equivariance tasks where the poses of the objects are initialized randomly within the workspace; 2) intermediateequivariance tasks where each object is initialized in a certain range, but with some randomness inside the range; 3) low-equivariance tasks where there is no randomness for the position and/or orientation of certain objects. Figure 5a shows the three task groups. We show the performance improvement of our Equivariant Diffusion Policy with voxel in absolute pose control compared with the standard diffusion policy in Figure 5b. Generally, the high-equivariance tasks benefit more from injecting symmetry in the network architecture.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Improvement with Different Levels of Equivariance", "weight": 1.0} -->

Moreover, our method's strong performance in the intermediate and low-equivariance tasks indicates its robustness and generalizability, as the model's symmetry is helpful even when the task is partially symmetric.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Real-Robot Experiment", "weight": 1.0} -->

Experimental Settings In this section, we evaluate our method on a real robot system containing a Franka Emika robot arm equipped with a pair of fin-ray fingers and three Intel Realsense D455 cameras. Demonstrations were gathered by an operator using a 6DoF 3DConnexion mouse. Observations and demonstration actions were recorded at 5Hz. Similarly to prior work, we use DDIM in this experiment to reduce the number of denoising steps to 16. Figure 6 shows the six tasks in this experiment. We compare our Equivariant Diffusion Policy with voxel input against a baseline Diffusion Policy, which uses the same voxel grid as the vision input and uses a non-equivariant 3D convolutional encoder with approximately the same number of trainable parameters as ours. As we show in the ablation study (Appendix H), this baseline works better than the original diffusion policy with image input.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Real-Robot Experiment", "weight": 1.0} -->

| | Oven Opening | Banana in Bowl | Letter Alignment | Trash Sweeping | Hammer to Drawer | Bagel Baking | Results We evaluate the trained models over 20 test trials for each task. The results are shown in Table 3. Our Equivariant Diffusion Policy can solve those tasks with only 20 to 60 demonstrations. Notably, our method achieves an 80% success rate in bagel baking, where the failures were all due to the joint limits of the robot. In comparison, the baseline performs poorly in all six tasks.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper studies the leveraging of symmetries in visuomotor policy learning. We propose the novel Equivariant Diffusion Policy method and provide a theoretical analysis identifying the conditions under which diffusion processes are equivariant. We also demonstrate a general framework for using SO -equivariance in the 6DoF control for robotic manipulation. We evaluate our method in both simulation and the real world and show in both cases that our method outperforms the baseline Diffusion Policy by a large margin.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conclusion", "weight": 1.5} -->

One limitation of this work is the partial utilization of the power of equivariance due to the symmetry mismatch in the vision system. Even with the voxel input, Factors like the arm's occasional presence in the voxel grid and camera noise could break symmetry. Future work could address this by designing a vision system free of symmetry corruption. Additionally, 'incorrect equivariance', as shown in prior work, may harm performance when the model's symmetry conflicts with the demonstration. Another limitation is that although the theory in Section 4.2 is not limited to diffusion policies and can apply to other policy learning pipelines as well, this is not demonstrated. Specifically, given the good performance of BC RNN with the relative pose control in Table 1, experimenting with an equivariant version of BC RNN could be beneficial. Finally, extending our method to other robotic tasks like navigation, locomotion, and mobile manipulation is a key future direction.
