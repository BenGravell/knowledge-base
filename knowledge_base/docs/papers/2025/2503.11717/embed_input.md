<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Low-pass Sampling in Model Predictive Path Integral Control

Topics include Model predictive path integral control, Trajectory optimization, Sampling-based control, Action smoothing, Low-pass filter.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Applies a low-pass filter to Gaussian noise before using it as sampled action sequences in MPPI, a heuristic that produces smoother trajectories and can improve exploration quality with minimal computational overhead.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model Predictive Path Integral (MPPI) control is a widely used sampling-based approach for real-time control, valued for its flexibility in handling arbitrary dynamics and cost functions. However, it often suffers from high-frequency noise in the sampled control trajectories, which hinders the search for optimal controls and transfers to the applied controls, leading to actuator wear. In this work, we introduce Low-Pass Model Predictive Path Integral Control (LP-MPPI), which integrates low-pass filtering into the sampling process to eliminate detrimental high-frequency components and enhance the algorithm's efficiency. Unlike prior approaches, LP-MPPI provides direct and interpretable control over the frequency spectrum of sampled control trajectory perturbations, leading to more efficient sampling and smoother control. Through extensive evaluations in Gymnasium environments, simulated quadruped locomotion, and real-world F1TENTH autonomous racing, we demonstrate that LP-MPPI consistently outperforms state-of-the-art MPPI variants, achieving significant performance improvements while reducing control signal chattering.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

One of the key abilities of the autonomous system is to determine the best actions given a certain goal, i.e. real-time motion planning and control. If the model of the controlled system is available, one of the best performing approaches is Model Predictive Control (MPC), which has proven its capabilities to solve many challenging tasks, such as autonomous racing, off-road driving, agile drone flight, and legged locomotion.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In general, there are two main approaches to MPC: sampling-based and optimization-based. Optimization-based MPC algorithms provide an efficient way to find optimal control sequences using dynamics and cost function gradients. However, they typically impose requirements on the dynamics model or cost function formulations, such as differentiability or continuity. An interesting alternative is sampling-based MPC. One of the main benefits of this approach is that the dynamics and cost functions can be arbitrary, and the only requirement is to evaluate them relatively fast. The two algorithms within this group, which have proven their effectiveness in numerous tasks, such as off-road driving, drone flight, and control of high-dimensional simulated systems (humanoids, dexterous hands, manipulators), are the Cross Entropy Method (CEM) and Model Predictive Path Integral Control (MPPI).

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The core of both MPPI and CEM approaches is to evaluate the performance of the control trajectories sampled from a sequence of Gaussian distributions. This approach results in a potential lack of temporal correlation within individual trajectories. In fact, control trajectory perturbations are approximately white noise signals, i.e., they are evenly composed of all possible frequencies. This, in turn, results in the overrepresentation of the high-frequency components when compared to the expected optimal behaviors in most robotic systems. Moreover, the dynamics of most robots naturally dampen these components, so their impact on the resulting performance is minimal. Thus, they do not contribute to the efficient search for optimal control signals but instead result in chattering of the applied controls and wear out of the actuators.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To address these issues, researchers proposed several interesting approaches, such as spline interpolation of control signals or input-lifting. However, they offer only an indirect and coarse control over the control signal frequency spectrum. A more direct approach, inspired by the iCEM algorithm, was proposed, where colored noise was used in MPPI instead of the white one. However, colored noise damps the signal components proportionally to the inverse of their frequency, or its powers, which may not be desired, especially for tasks that require frequent repetitiveness, e.g., legged locomotion, stirring, or chopping.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper, we address these issues by extending the MPPI algorithm with a low-pass filter applied to the sampled control perturbations. Our method, called Low-Pass Model Predictive Path Integral control (LP-MPPI), is presented schematically in Figure. Our approach eliminates the harmful and ineffective high-frequency components of the control signal perturbations, increasing the efficiency of the MPPI algorithm and smoothing the resultant control signal without sacrificing its responsiveness. Moreover, unlike colored noise, it does not bias the control signal frequencies in the filter's passband, enabling an effective search for high-performing trajectories across the admissible frequency range. Our method introduces only two interpretable parameters with clear physical meaning, allowing intuitive tuning. They directly control the frequency range in which the search for the optimal control trajectory is focused and the damping characteristics beyond it. Finally, LP-MPPI is easy to implement and adds negligible computational overhead compared to the MPPI algorithm.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We conduct an extensive experimental evaluation of the proposed method against the State-of-the-Art variants of the MPPI in three Gymnasium environments, over a wide range of MPPI parameters. The results demonstrate that our approach consistently outperforms the considered baselines, improving their results by 24% on average, while significantly reducing chattering in the applied control signals. To further assess its applicability, we integrate LP-MPPI with the recently developed Dial-MPC and evaluate the resulting LP-Dial-MPC on quadruped robots. This experiment highlights the ease and effectiveness with which our method can be combined with other MPPI-based approaches, yielding an average performance gain of over 32% compared to Dial-MPC. Finally, we validate our approach in real-world autonomous F1TENTH racing, where it outperforms all baselines, most of them by a large margin.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We propose a Low-Pass Model Predictive Path Integral algorithm, which enables shaping the frequency spectrum of the control trajectories' perturbations distribution, improving search efficiency and reducing the high-frequency noise in the applied control signal.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We conduct a thorough experimental analysis of the proposed approach in several simulated environments, showing that the proposed method consistently outperforms the state-of-the-art MPPI-based control approaches, while reducing the amount of high-frequency components in the applied control signals (see Tab. I).

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We highlight the practicality of the proposed solution, that is, the ease of implementation of our method and its integration with the latest sampling-based MPC methods, the physical interpretability of its parameters, and the intuitiveness of tuning them.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Model Predictive Path Integral Control", "weight": 1.0} -->

Our proposed method, Low-Pass Model Predictive Path Integral Control (LP-MPPI), is based strongly on the original MPPI algorithm. Therefore, we recall its pseudocode in Algorithm. In general, the idea is to (i) draw multiple control trajectories around the current nominal control trajectory, (ii) simulate them using the model of the system, (iii) compute their costs, and finally (iv) update the nominal trajectory based on the costs obtained by the perturbed controls. In this paper, we focus on the commonly overlooked aspect of the MPPI algorithm -- drawing random control perturbations. In fact, the only part of the algorithm that we would like to analyze and improve is located in line. To do so, we will analyze the original MPPI algorithm and its recent extension from a frequency domain perspective.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Model Predictive Path Integral Control", "weight": 1.0} -->

1:Nominal control sequence U, current state xt, System dynamics model f, step and terminal cost functions c, cf, number of rollouts N, control sequence horizon H, temperature parameter λ, noise covariance matrix Σ 2:Updated nominal control sequence U 3:for i = 1 to N do ⊳ Sample N trajectories 4: Sample noise sequence ϵi, 1: H from 𝒩 (0,Σ) 5: Generate control sequence Ui = U + ϵi 6: Compute trajectory xi, t: t + H + 1 using system dynamics xi, t + h + 1 = f (xi, t + h,ui, h) 9:Compute importance weights $w_{i} = \frac{e^{- {\lambdaJ_{i}}}}{\sum_{j = 1}^{N}e^{- {\lambdaJ_{j}}}}$ 10:Update controls $U = {\sum_{i = 1}^{N}{w_{i}U_{i}}}$ 11:Apply first control input u1 to the system 12:Shift control sequence: U ← {u2, …, uH, uH

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Model Predictive Path Integral Control", "weight": 1.0} -->

+ 1} Algorithm 1 Model Path Integral Control (MPPI)

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-C Spectral analysis", "weight": 1.0} -->

In the original MPPI, all elements of the noise sequences are sampled from the Gaussian distribution with some constant covariance matrix $\Sigma$. This results in a lack of correlation between the subsequent elements of the noise sequence. In general, this may be seen as an advantage, as perturbing the system with white noise is a well-known technique in system identification, which ensures that the system dynamics are excited with all possible control frequencies. In the context of MPC, similar implications should also be true for the cost function $J$, which depends on both controls and state trajectories. However, in the context of robotic applications, it is pretty uncommon to control systems that require an excitation with high-frequency noise, as most robots filter it out. Therefore, control trajectories with high-frequency noise and low-frequency noise result in similar costs, which may result in frequent changes of the following actions, and thus jittering in the real system. Moreover, we expect that for most robotic systems, the spectrum of frequencies of the optimal control trajectories is not uniformly distributed, so the use of white noise may reduce the search efficiency and result in a performance decrease.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C Spectral analysis", "weight": 1.0} -->

In fact, using the uncorrelated noise distributions corresponds to the maximum exploration in the frequency spectrum.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C Spectral analysis", "weight": 1.0} -->

To limit the amount of high-frequency noise in the sampled controls, the authors of proposed biasing the spectrum of the control trajectory perturbations towards low frequencies. As a result, they obtained a strategy that puts most of the signal energy in the lowest possible frequencies and gradually reduces the energy of the higher-frequency components. In turn, in this paper, we analyze an alternative approach based on low-pass filtered noise, which balances the bias toward lower frequencies with efficient exploration of the admissible spectrum, and enables explicit control of this trade-off through adjustable parameters -- cutoff frequency and filter order.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Spectral analysis", "weight": 1.0} -->

To analyze each of the aforementioned control sampling strategies and provide the rationale for the approach proposed in this paper, we conducted an experiment. We compared the power density spectra of (i) white noise, (ii) colored noise, and (iii) low-pass filtered white noise, to the spectrum of the control signals generated by a trained RL policy from the StableBaselines3-zoo library for two sample environments, Ant-v3 and Humanoid-v3. We chose the RL agent controls spectrum as a reference, as it may be considered to be very close to the frequency statistics of the optimal behaviors in these environments. To present the results in a compact form, we averaged the spectra of the individual joints for the RL agent. In addition, we averaged the spectra over 100 seeds to reduce noise. Moreover, to ensure a fair comparison between the analyzed sampling distributions, we optimized their parameters to minimize the norm between their and the RL agent action spectra. The results of this comparison are presented in Figure.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Spectral analysis", "weight": 1.0} -->

One can see that in the considered locomotion tasks, the RL agent does not perform high-frequency actions; however, following only the lowest frequencies is also far from optimal, as it ignores the frequency bumps that occur around $2\ {Hz}$. In fact, the spectrum that best matches the RL agent is the low-pass-filtered white noise, as it does not damp the signal at the most important frequencies. Moreover, what is also important in the context of MPPI, it allows for efficient exploration in the assumed bandwidth.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-D Low-pass Model Predictive Path Integral Control", "weight": 1.0} -->

Following the observations made in the previous section, we introduce the Low-pass Model Predictive Path Integral Control (LP-MPPI). The core of the proposed algorithm is the introduction of a temporal correlation between the subsequent control perturbations by using a low-pass filter on them. The proposed approach is formalized in Algorithm, where the changes with respect to the original MPPI algorithm are marked in blue. Our method introduces a subtle yet important modification that (i) biases the search for optimal control trajectories toward low-frequency signals and (ii) allows the user to control the frequency spectrum within which the algorithm searches for candidate trajectory updates. These features can be precisely controlled by tuning the parameters of the low-pass filter, which we describe in detail in Section III-E. Importantly, the proposed modifications do not introduce significant computational overhead to the MPPI algorithm, as filtering typically requires a small number of multiplications proportional to the horizon length $H$ and, in most cases, is significantly cheaper than evaluating the system's dynamics.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-D Low-pass Model Predictive Path Integral Control", "weight": 1.0} -->

One of the crucial design choices is to decide which signals should be smoothed in order to improve efficiency and reduce chattering without sacrificing controller reactiveness or violating system constraints. In the proposed approach, we apply low-pass filtering to sampled noise sequences, i.e. control trajectory perturbations. This way, we strongly bias the search for control trajectories towards low frequencies, but we do not constrain the applied control signal frequency spectrum. The first control may change rapidly, but the change of the entire control trajectory is correlated. Thus, the search is biased, but the applied control signal maintains its reactiveness. Moreover, unlike existing filtering approaches, such as MPPI(SGF), our approach improves search efficiency by evaluating only smoothed constraint-compliant perturbations and does not introduce any phase shift to the applied control signal, as if the filtering were applied directly to it.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-D Low-pass Model Predictive Path Integral Control", "weight": 1.0} -->

In our software implementation, we utilized a simple and computationally efficient digital implementation of the Butterworth filter. This type of filter is maximally flat in the passband, which prevents introducing biases to specific frequencies within the desired range. In turn, its frequency spectrum is not as steep as, for example, that of Chebyshev filters; however, as can be seen in Figure, this property is not necessarily needed in the context of sampling performant control trajectories. Similarly, the relatively high phase shift introduced by the Butterworth filter is not problematic in our approach, since temporally uncorrelated perturbations remain unaffected by such shifts.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Low-pass Model Predictive Path Integral Control", "weight": 1.0} -->

1:Nominal control sequence U, current state xt, System dynamics model f, step and terminal cost functions c, cf, number of rollouts N, control sequence horizon H, temperature parameter λ, noise covariance matrix Σ, low-pass filter cutoff frequency fc and order oLPF 2:Updated nominal control sequence U 3:for i = 1 to N do ⊳ Sample N trajectories 4: Sample noise sequence ϵi, 1: H from 𝒩 (0,Σ) 5: Filter noise sequence ϵiLP = LPFilter(ϵi,fc,oLPF) using low-pass filter 6: Generate control sequence Ui = U + ϵiLP 7: Compute trajectory xi, t: t + H + 1 using system dynamics xi, t + h + 1 = f (xi, t + h,ui, h) 10:Compute importance weights $w_{i} = \frac{e^{- {\lambdaJ_{i}}}}{\sum_{j = 1}^{N}e^{- {\lambdaJ_{j}}}}$ 11:Update controls $U = {\sum_{i =

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Low-pass Model Predictive Path Integral Control", "weight": 1.0} -->

1}^{N}{w_{i}U_{i}}}$ 12:Apply first control input u1 to the system 13:Shift control sequence: U ← {u2, …, uH, uH + 1} Algorithm 2 Low-pass Model Path Integral Control (LP-MPPI)

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-E Parameters of LP-MPPI", "weight": 1.0} -->

Our proposed algorithm, LP-MPPI, does not introduce any additional parameters beyond those of a low-pass filter. Therefore, in our case, the parameters of the LP-MPPI are the parameters of the Butterworth filter itself -- cutoff frequency $f_{c}$ and order $o_{\text{LPF}}$. The cutoff frequency controls the width of the passband, which affects the range of frequencies with the highest power density in the drawn control signal perturbations. A lower $f_{c}$ results in a greater bias at lower frequencies and an increased use of low-frequency signals. In turn, a higher $f_{c}$ reduces the bias on low frequencies and allows searching in a wider range of signals. The second parameter of the Butterworth filter is its order $o_{\text{LPF}}$, which controls the slope of the power density spectrum in the stopband -- roll-off, i.e., how much the attenuation of the signal components grows with the growth of the frequency. The higher the order, the lesser the exploration outside the passband, and the greater the bias towards low frequencies.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-E Parameters of LP-MPPI", "weight": 1.0} -->

To better visualize these dependencies, in Figure we present the impact of the filter cutoff frequency $f_{c}$ and its order $o_{\text{LPF}}$ on the magnitude of the frequency response and on the signals in the time domain.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-E Parameters of LP-MPPI", "weight": 1.0} -->

Last but not least, one of the benefits of the proposed approach is the interpretability of the cutoff frequency $f_{c}$ parameter, as it enables intuitive tuning. One of the natural approaches to choosing this parameter is to set it around the natural cutoff frequency of the system to be controlled with LP-MPPI, as inducing higher frequencies requires a significant effort to overcome the damping characteristics of the system itself. Moreover, one can often heuristically estimate the highest expected frequency of the system states necessary to maximize the reward or obtain the desired behavior. Furthermore, in some cases, the interpretability of the cutoff frequency may help regularize the system's behavior, e.g., preventing exploitation of the carelessly designed reward function.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-E Parameters of LP-MPPI", "weight": 1.0} -->

To sum up, the proposed LP-MPPI approach filters out the high-frequency components from the evaluated control signals within the MPPI loop, significantly reducing the high-frequency components in the obtained controls. This reduction is particularly important for robotic systems, as it decreases their wear and biases the search for high-performance control signals towards a more promising area. Finally, our approach enables one to effectively control the frequency spectrum of the control signal perturbations, while providing intuitive tuning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Gymnasium environments", "weight": 1.0} -->

Our first experiment is an optimal control task in 3 high-dimensional Gymnasium environments: Hopper-v5, Ant-v5, and HalfCheetah-v5. The goal of this experiment is to evaluate the efficiency of the proposed approach and relate it to the State-of-the-Art MPPI-based control algorithms.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Gymnasium environments", "weight": 1.0} -->

MPPI -- the original MPPI algorithm,

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Gymnasium environments", "weight": 1.0} -->

SMPPI -- smoothed MPPI by control space lifting,

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Gymnasium environments", "weight": 1.0} -->

ColoredMPPI -- MPPI with colored noise.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Gymnasium environments", "weight": 1.0} -->

In this experiment, we assumed the perfect knowledge of the system dynamics, i.e., we used the same simulated environments for MPPI rollouts and evaluation. As a cost function, we used the original rewards from the Gymnasium environments, taken with a minus sign. To ensure a fair comparison, we tuned the parameters of each algorithm using Optuna and 100 trials. In addition, we averaged the results over 100 episodes to reduce the impact of randomness.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Gymnasium environments", "weight": 1.0} -->

The results of our experiment are presented in Figure. We evaluated each of the method, in each environment, on a matrix of the common MPPI parameters, i.e., horizon length $H$ (vertical axis), and number of rollouts $N$ (horizontal axis). In the first column, one can see the rewards obtained by the LP-MPPI, while in the remaining columns the relative improvement of the LP-MPPI over the baselines. The superiority of the proposed approach can be seen by the dominance of the green color in the presented chart. In fact, except for very short horizons, LP-MPPI outperforms all baselines in all environments considered, no matter the number of rollouts. The scale of the improvement vary for different horizons and numbers of rollouts, but in general, the longer the horizon, the bigger the improvement. For Ant-v5 and HalfCheetah-v5 environments on can observe that the improvements are larger for a smaller number of evaluated rollouts, showing the increased sample efficiency introduced by low-pass filtering of samples, which may be critical in computationally restricted edge devices. Interestingly, the biggest improvements are observed w.r.t.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Gymnasium environments", "weight": 1.0} -->

SMPPI and SCP-MPPI approaches, on average 26% and 36%, which may be caused by the lack of fine-grained control due to action representation. The best performance among the baselines is observed for ColoredMPPI, which is still, on average, about 10% less performant than the proposed LP-MPPI. In turn, if we consider the results obtained for the best pair of horizon length and number of rollouts, then LP-MPPI outperforms it on average by 8.46%.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Gymnasium environments", "weight": 1.0} -->

Despite higher rewards, an important aspect of the control algorithm is the smoothness of the applied controls. To visualize the differences between the considered methods, we present the applied control trajectories for the Ant-v5 environment with $H = 15$ and $N = 100$ in Figure. For fairness of comparison, each algorithm was used with the optimal set of parameters, w.r.t. cumulative reward, determined with Optuna using 100 trials. One can see that the original MPPI algorithm generates undesirably sharp controls, while the remaining baselines produce significantly smoother controls, comparable to each other and to our proposed LP-MPPI. To quantitatively assess smoothness, we report Mean Squared Second Derivative (MSSD) and Mean Savitzky-Golay Filter Deviation (MSGFD) in Table I. The results indicate that our method attains very low MSSD and the smallest MSGFD, confirming that the control trajectories it generates are notably smooth.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Quadruped locomotion", "weight": 1.0} -->

In the previous experiment, we showed that LP-MPPI outperforms the baselines for simplified abstract robots. Instead, in this one, we focus on the full-scale simulated quadrupeds with 12DoF. We consider a locomotion task with trot gait, imposed in the reward function to guide the search of the control signals, on two quadrupeds, i.e., Unitree Go2 and MAB Silver Badger.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Quadruped locomotion", "weight": 1.0} -->

Recently, it was shown that MPPI-based approaches can succeed in such complex control tasks by diffusion-style annealing of the standard deviation of the noise distribution and the use of spline interpolation, as it was done in the Dial-MPC approach. We would like to enhance the Dial-MPC with the proposed low-pass filtering (LP-Dial-MPC) to evaluate whether it applies to recent MPPI-based approaches and can improve their performance. Moreover, we would like to compare our method, in this setting, with the best-performing approach from the previous experiment -- ColoredMPPI. Thus, we extend the Dial-MPC with colored noise instead of the default white one.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Quadruped locomotion", "weight": 1.0} -->

In this experiment, we used the default settings of the Unitree Go2 trot experiment available in the code repository associated with the Dial-MPC paper. The goal is to follow the desired longitudinal velocity of 1 m/s with the center of the robot trunk while maintaining its default orientation and height above the ground. In addition, a cost function that imposes a specific foot-height trajectory encourages the robot to follow a trot gait. Moreover, we designed a very similar experiment for the MAB Silver Badger robot, with the same goals as for the Go2 but with additional cost terms regarding the energy consumption and the minimum required height of the calves, to encourage more natural looking robot posture. In both experiments, we set the horizon $H = 16$, number of rollouts $N = 256$, ${dt} = 20$ ms, temperature $\lambda = 0.05$, horizon and trajectory diffusion factors equal to $0.9$ and $0.5$, respectively, and the number of diffusion steps equal to $2$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Quadruped locomotion", "weight": 1.0} -->

In this experiment, to highlight the robustness of the proposed approach to the choice of its parameters, we do not perform the search with Optuna but instead report the performance for several intuitive parameter sets, i.e. cutoff frequency $f_{c} \in {\{ 2,3,4\}}$ for Unitree and $f_{c} \in {\{ 3,4,5\}}$ for MAB robot, and orders $o_{\text{LPF}} \in {\{ 2,3,4\}}$. We compared their performance with the two above-mentioned baselines, for which we found the sets of the best parameters using Optuna. The results of this experiment can be found in Figure. The proposed low-pass filtering approach implemented into the Dial-MPC framework consistently outperforms the default Dial-MPC, by 24% and 41% for the Unitree Go2 and MAB Silver Badger robots, respectively. We attribute these improvements to the more fine-grained control (higher number of decision variables) of the LP Dial-MPC and its ability to directly shape the frequency spectrum of the sampling distribution.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Quadruped locomotion", "weight": 1.0} -->

In turn, the spectrum shaping capabilities of the colored noise are relatively limited and bias only the lowest frequencies, which results in significantly worse performance (about two times lower rewards than ours).

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Real-world F1TENTH racing", "weight": 1.0} -->

In all previous experiments, we assumed that the models of the controlled systems are perfectly known and are used by the MPPI to search for the best control trajectories. In turn, in this task, we would like to use an analytical model of the F1TENTH car (dynamic single-track model with MF6.1 tire model ) and evaluate it under the real-world racing conditions. The goal of this task is to cover the highest possible distance around the track centerline in 30 s, on the $14.2\ m$ long $1\ m$ wide oval racetrack. We defined the cost function by

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Real-world F1TENTH racing", "weight": 1.0} -->

where $v_{f}$ is the velocity along the centerline, $n$ is the distance to the centerline, $T_{w}$ is the track width, $\alpha$ is the slip angle, $\theta$ is the vehicle orientation, and $T_{\theta}$ is the orientation of the centerline. We set the horizon $H = 30$, ${dt} = 50$ ms, control frequency to $30\ {Hz}$, and evaluated the algorithms for both $N = 10$ and $N = 50$ rollouts. We have chosen the number of rollouts and the horizon to meet real-time requirements with a single core of Intel Core i5-12500H CPU, while achieving reasonable driving performance (see video attachment). The parameters of all methods were chosen in simulation using Optuna with 50 trials.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Real-world F1TENTH racing", "weight": 1.0} -->

In Figure, we present the distances covered by the proposed LP-MPPI and the other considered MPPI variants in 15 runs of $30\ s$ each. One can see that in both considered setups, the proposed LP-MPPI approach significantly outperformed all baselines except SMPPI, which performed very close to the LP-MPPI for $N = 50$ and a bit worse for $N = 10$. Note that in the racing scenarios, even the $30\ {cm}$ of difference gained every $30\ s$ of the race (the difference between medians of LP-MPPI and SMPPI) may be considered a notable gap.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Computational overhead", "weight": 1.0} -->

An important aspect of every control method is its computational efficiency. Therefore, we evaluate how much computational overhead the proposed method introduces relative to the nominal MPPI and how it relates to the other considered baselines. To do so, we run all methods for 10 episodes in Ant-v5 (MuJoCo model, ${H = 15},{N = 100}$) and F1TENTH (compiled analytical model, ${H = 30},{N = 10}$) environments, using a single core of the Intel Core i5-12500H CPU. We compute the median of the control computation time and relate it to the one obtained by the MPPI. In Table II, we present the results of this experiment. One can see that all baselines introduce some notable computational overhead in the F1TENTH environment, since the compiled analytical model, which is responsible for most of the computations, is very fast. Note that the proposed method introduces the second smallest overhead of 2.4%.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Computational overhead", "weight": 1.0} -->

In turn, in the case of a relatively heavy dynamics model, e.g., Ant-v5 environment, we observe some counterintuitive results, like the decrease in the compute time for LP-MPPI and ColoredMPPI. We suppose that this may be caused by the variability in the timings, due to the use of a standard OS instead of a real-time one, or be an effect of filtering out the higher frequencies from the control signal, which may simplify the underlying physics simulation. In summary, a computationally intense dynamics evaluation causes the overhead introduced by the proposed method to be negligible.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this work, we introduced Low-Pass Model Predictive Path Integral Control (LP-MPPI), a novel and easy-to-implement enhancement to MPPI that incorporates low-pass filtering into the sampling process. By directly shaping the frequency spectrum of control trajectory perturbations, LP-MPPI eliminates harmful high-frequency noise and improves the efficiency of searching for optimal control trajectories. Unlike existing smoothing techniques or colored noise sampling, our approach offers intuitive fine-grained control over the optimal control search in the frequency domain, making it highly adaptable to various robotic systems.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Through extensive simulation and real-world experiments, we demonstrated the superiority of LP-MPPI over state-of-the-art MPPI-based methods in a variety of tasks, including simulated legged locomotion and real-world F1TENTH autonomous racing. Our results show that LP-MPPI consistently outperforms state-of-the-art methods by 10% in Gymnasium environments, 32% in simulated quadruped locomotion, and by $0.115\ s$ in a $30\ s$ long F1TENTH autonomous time trial. In addition, it significantly reduces the chattering of the control signal, leading to smoother and more reliable actuation. Moreover, LP-MPPI maintains computational efficiency, introducing only a negligible overhead compared to standard MPPI, making it practical for real-time applications.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusions", "weight": 1.0} -->

To sum up, LP-MPPI represents a simple yet powerful modification to MPPI, making it an attractive option for real-time robotic control tasks requiring both high-performance trajectory optimization and smooth, actuator-friendly control signals. Future work will explore adaptive filtering techniques to dynamically adjust the sampling distribution based on task demands and further integrate LP-MPPI with learning-based sampling strategies for improved adaptability.
