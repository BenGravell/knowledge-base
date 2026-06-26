<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Informative Input Design for Dynamic Mode Decomposition

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Efficiently estimating system dynamics from data is essential for minimizing data collection costs and improving model performance. This work addresses the challenge of designing future control inputs to maximize information gain, thereby improving the efficiency of the system identification process. We propose an approach that integrates informative input design into the Dynamic Mode Decomposition with control (DMDc) framework, which is well-suited for high-dimensional systems. By formulating an approximate convex optimization problem that minimizes the trace of the estimation error covariance matrix, we are able to efficiently reduce uncertainty in the model parameters while respecting constraints on the system states and control inputs. This method outperforms traditional techniques like Pseudo-Random Binary Sequences (PRBS) and orthogonal multisines, which do not adapt to the current system model and often gather redundant information. We validate our approach using aircraft and fluid dynamics simulations to demonstrate the practical applicability and effectiveness of our method. Our results show that strategically planning control inputs based on the current model enhances the accuracy of system identification while requiring less data. Furthermore, we provide our implementation and simulation interfaces as an open-source software package, facilitating further research development and use by industry practitioners.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Estimating system dynamics from data is a fundamental problem in control theory and systems engineering \[ljung1998system, tangirala2018principles, keesman2011system, kostelich1992problems, vandenberghe2012convex\]. Rapidly learning from limited measurements in high-dimensional systems can significantly reduce the cost associated with expensive real-world data collection while yielding more accurate models. Optimizing the actuation input sequence to gather informative measurements while respecting constraints on the state and control inputs remains an open challenge \[kaiser2018sparse\]. From the perspective of experimental design, designing future input signals to aid in the identification of the dynamical system can be framed as an information maximization problem \[uy2009optimization, wahlberg2010optimal\]. This involves perturbing the system in directions that provide high-value information, thereby enhancing the efficiency of the learning process.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

System identification is relevant in almost every science and engineering discipline ranging from aircraft dynamics, to geothermal processes, to financial markets \[tangirala2018principles\]. When the state space of these real-world environments is very large, reduced order models can be used to capture the most prominent dynamics of the system of interest. One common approach to constructing reduced order models is through Dynamic Mode Decomposition (DMD), a data-driven technique that decomposes complex systems into a set of dynamic modes, capturing essential spatiotemporal patterns \[schmid2010dynamic, proctor2016dynamic\]. Efficiently reducing uncertainty in the system dynamics model results in less data required to achieve similar predictive model performance while also reducing the costs related to expensive real-world data collection.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Designing future control inputs to efficiently learn system dynamics is challenging because future state estimates depend on the current model \[rojas2007robust, bombois2006least, suzuki2007input, mu2018input\]. Minimizing uncertainty in the model derived from data requires understanding how control inputs will affect future states, which in turn requires a reliable model \[morelli2016aircraft\]. This interdependence might seem circular, but sequentially optimizing inputs significantly reduces model uncertainty more rapidly and with less data than using random input sequences while also satisfying constraints on the resulting states and control inputs \[barenthin2008complexity\]. While collecting data with random inputs can indeed improve the identification of the underlying model, strategically planning future control inputs based on the current system model often yields larger improvements with less data, enhancing the efficiency of the learning process while also remaining cognizant of constraints on the system states and control inputs \[brighenti2009input, fujimoto2018informative\].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Popular techniques for designing informative inputs such as Pseudo-Random Binary Sequences (PRBS) and orthogonal multisines \[rivera2009constrained, morelli2021optimal\] do not use the current understanding of the system model. As a result, they often waste time collecting redundant information. Ideally, we would use our current model to identify regions in the parameter space where variance is high. By tailoring future control inputs to our current model, we can more efficiently reduce uncertainty.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our proposed approach integrates informative input design into the Dynamic Mode Decomposition with control (DMDc) framework, significantly enhancing the accuracy and efficiency of system identification. By formulating an optimization problem that minimizes the trace of the model covariance matrix, we systematically reduce the uncertainty in our estimates of the model parameters while respecting constraints on the state and control variables. We directly compare our approach to the optimal input design method proposed by \ \[morelli2021optimal\].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main focus of our work is to design informative inputs while respecting state and input constraints using our current estimate of the model. For very large state spaces, we can reduce the state space size first through DMDc and then everything else works the same as before.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key contributions of this work include introducing a convex approximation of the optimal input design problem, extending our method to handle high-dimensional state spaces through reduced-order models using the DMDc framework, validating our approach with simulations using the WaterLily, Aerobench, and X-Plane aircraft dynamic simulators \[weymouth_waterlily, heidlauf2018verification\], and releasing our implementation and simulation interfaces as an open-source software package.^11^1Code is available at

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Given a linear dynamical system represented by where the state at time $t$ is $x_{t} \in \mathbf{R}^{n}$, the control input is $u_{t} \in \mathbf{R}^{m}$, $A \in \mathbf{R}^{n \times n}$, $B \in \mathbf{R}^{n \times m}$, and $v_{t} \sim {\mathcal{N}{(0,{\sigma^{2}I})}}$ with state constraints $x_{\ell} \leq x_{t} \leq x_{u}$ and control constraints $u_{\ell} \leq u_{t} \leq u_{u}$. Let where we collected state and control input data up to time step $k + 1$ and $k$ respectively. The linear system model is where $V \in \mathbf{R}^{n \times k}$ is the stacked noise matrix.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We can construct estimates of $A$ and $B$, which we denote $\hat{A}$ and $\hat{B}$, by solving the regression problem with the Frobenius norm: where $\hat{\Theta} = \begin{bmatrix} \end{bmatrix}$. This optimization problem can be solved using the least squares method, yielding: where $Z^{\dagger}$ is the pseudo-inverse of $Z$. If $\Gamma = {\sigma^{2}\left({ZZ^{\top}} \right)^{- 1}}$, the covariance of $\hat{\Theta}$ is given: as shown in section VIII and is equivalently the covariance of the least squares parameter estimate \[hastie2009elements\]. The trace of ${Cov}{(\hat{\Theta})}$ is a measure of the total variance of the estimates of $\hat{A}$ and $\hat{B}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Notice that minimizing the trace of ${Cov}{(\hat{\Theta})}$ is equivalent to minimizing the trace of $\Gamma$ as shown in section VIII. The root-mean-square-error (RMSE) between the estimated $\hat{\Theta}$ and the true $\Theta$ is given by where ${\mathbf{t}\mathbf{r}}{({{Cov}{(\hat{\Theta})}})}$ represents the trace of the covariance matrix. Since we have assumed that the process noise $v_{t}$ is zero mean Gaussian noise, we can compute the variance of forward propagating the dynamics into the future as This recursive equation allows us to estimate how uncertainty in the state evolves over time due to both the dynamics of the system and the influence of the process noise. We have $\sigma_{x_{t}}^{2} = {\text{diag}{(\Sigma_{x_{t}})}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

To minimize our uncertainty in these estimates, we pose the following optimization problem. Let $t = {1,\ldots,{k + 1}}$ denote the time steps for which we have collected data to construct estimates of $\hat{A}$ and $\hat{B}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The lower and upper constraints on the state and control inputs are ${u_{\ell},x_{\ell},u_{u}},$ and $x_{u}$ respectively. The standard deviation is scaled by $\beta$ for the upper and lower bound state constraints. Everything in eq. 9 is convex, except for the objective ${\mathbf{t}\mathbf{r}}{(\Gamma)}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The solution to this problem will guide the selection of control inputs that not only steer the system state in a desired manner but also do so in a way that maximally reduces the uncertainty in our estimates of system dynamics resulting in more efficient system identification.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Dynamic Mode Decomposition with Control", "weight": 1.0} -->

proctor2016dynamic presented Dynamic Mode Decomposition with control (DMDc) to produce a reduced order model motivated by the fact that when $n \gg 1$, computing the pseudo-inverse in eq. 5 can be computationally prohibitive \[proctor2016dynamic\].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Convex Approximation", "weight": 1.0} -->

As previously mentioned, eq. 9 and eq. 15 are convex, except for the objective. The convex-concave procedure (CCP) is a useful heuristic for finding a local optimum by iteratively solving convex optimization problems \[lipp2016variations, boyd2016mimo, lipp2016antagonistic\]. The CCP replaces concave terms with a convex upper bound, and then solves the resulting convex problem.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Convex Approximation", "weight": 1.0} -->

We can linearize the term $W = \Gamma^{- 1} = {\sigma^{- 2}ZZ^{\top}}$ around the current matrix $Z_{c}$ which gives: This is affine in $Z$, hence the variables $u,x$. We can then minimize ${\mathbf{t}\mathbf{r}}{({\hat{W}}^{- 1})}$ instead of ${\mathbf{t}\mathbf{r}}{(W^{- 1})}$ in each iteration of the CCP. The problem then becomes: where $\mathcal{X}$ and $\mathcal{U}$ represent the set of all feasible states and controls given by the constraints in eq. 9.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Convex Approximation", "weight": 1.0} -->

As a result, we can simply iterate solving the convex problem with objective ${\mathbf{t}\mathbf{r}}{({\hat{W}}^{- 1})}$ without the need to line search, update trust regions, or tune hyper parameters.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Linear Program", "weight": 1.0} -->

Alternatively, we can minimize $- {{\mathbf{t}\mathbf{r}}{(\hat{W})}}$, which converts the problem from a semidefinite program to a linear program, allowing for an even more efficient solution time. The $- {{\mathbf{t}\mathbf{r}}{(\hat{W})}}$ objective is not equivalent to minimizing ${\mathbf{t}\mathbf{r}}{({\hat{W}}^{- 1})}$; however, it has been shown to be a useful surrogate objective on large problems \[ott2024approximate\].

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Linear Program", "weight": 1.0} -->

It is important to note that minimizing ${\mathbf{t}\mathbf{r}}{(W^{- 1})}$ penalizes small eigenvalues of $W$, ensuring that estimation errors are balanced across all directions. In contrast, the $- {{\mathbf{t}\mathbf{r}}{(W)}}$ objective can result in a few large eigenvalues dominating the objective, while others remain small. As a result, this could concentrate information gain in a single direction, resulting in poor performance in orthogonal directions. However, our empirical results demonstrate that this is not an issue in practice as long as the small initial data set used to construct estimates of $\hat{A}$ and $\hat{B}$ have reasonable excitation across each of the control inputs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Linear Program", "weight": 1.0} -->

3: $\hat{\Theta} = \begin{bmatrix} \overset{\sim}{A} & \overset{\sim}{B} \end{bmatrix}$ ⊳ Equations eq. 12, eq. 13 8: Apply the optimized control inputs uk + 1: T 9: Collect new data Xnew, Xnew′, Υnew and update Algorithm 1 Informative Input Design

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Iterative Input Design", "weight": 1.0} -->

The iterative nature of the input design described in algorithm 1 is fundamental to the effectiveness of the procedure. Our method emphasizes continuous improvement through repeated system identification epochs. As illustrated in fig. 1, we can sequentially solve eq. 9 and eq. 15 as new data is collected online. At each iteration, we use the current estimates of $\hat{A}$ and $\hat{B}$ to generate a new control input trajectory. These inputs are then applied to the system, and the resulting data is used to update our estimates of $\hat{A}$ and $\hat{B}$. This process involves concatenating the most recent measurements with previous data, thereby refining our model iteratively. This iterative input design strategy ensures that we account for the most recent measurements to target areas of the parameter space with the greatest variance.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Results", "weight": 1.0} -->

We experimentally validated our method in three simulation environments and benchmarked against two common informative input design techniques. The first is the orthogonal multisine method, which generates inputs that are mutually orthogonal in both the time domain and the frequency domain by solving a nonlinear optimization problem \[morelli2021optimal\]. The second is a random input signal. Our methods are the Convex-Concave semidefinite program (SDP) that uses the linearized objective ${\mathbf{t}\mathbf{r}}{({\hat{W}}^{- 1})}$ and the linear program (LP) that uses the $- {{\mathbf{t}\mathbf{r}}{(\hat{W})}}$ objective.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Results", "weight": 1.0} -->

To achieve fair comparison between the three methods, we enforce the same amplitude and time constraints \[morelli2016aircraft\]. We determine the maximum change in control input $\delta_{\max}$ constraint based on the largest frequency used in the orthogonal multisine method. We then apply this $\delta_{\max}$ constraint to our method as well as the random input method. The random input method changes the input by $\delta_{\max}$ at each time step and is limited to the same amplitude constraint. We compared this random method against a classical filtered pseudo-random binary sequence (PRBS) and found that it performed better so we selected it as the second baseline.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A Fluid Flow Past a Cylinder", "weight": 1.0} -->

We use the WaterLily.jl fluid simulator to control the rotation of a cylinder in horizontal flow at a Reynold's number of $100$ \[weymouth_waterlily\]. The initial dataset collected at $10$ Hz uses a sinusoidal rotation pattern of the cylinder for $50$ seconds. The size of the vorticity field state space is $n = {51,200}$. The four methods then plan the future rotation angles of the cylinder for the next $50$ seconds.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Fluid Flow Past a Cylinder", "weight": 1.0} -->

We also show the predicted state of the vorticity field $10$ seconds into the future after collecting data with informative inputs designed by the SDP method.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-B F-16 Dynamics", "weight": 1.0} -->

To demonstrate the capability of designing informative inputs for multi-input multi-output systems, we use the Aerobench simulator to simulate the nonlinear dynamics of an F-16 based on the model by \ \[morelli1998global\]. The state space consists of the velocity, angle of attack, angle of sideslip, roll, pitch, yaw, roll rate, pitch rate, yaw rate, east position, north position, altitude, and engine power setting. The controls are the throttle percentage, elevator, aileron and rudder deflections.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-B F-16 Dynamics", "weight": 1.0} -->

The initial data consisted of $250$ seconds of simulated flight data collected at $15$ Hz. Figure 3 shows the control inputs created by each of the four methods. We also compare the objective value and runtime comparison over 100 simulation runs for each of the methods. The objective values were computed by taking the control inputs planned by each of the methods and then executing them in the Aerobench simulator to collect the true output data. The RMSE of $\hat{\Theta}$ was computed with eq. 7 after collecting the data with each of the informative input design methods.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-B F-16 Dynamics", "weight": 1.0} -->

We see that the SDP and LP methods outperform the other methods by consistently achieving lower RMSE values while performing relatively similarly to each other with notably less variance in the LP performance. We see that the LP method also achieves better runtime performance compared to the orthogonal multisine method. The random method performs the worst in terms of objective value, but has the lowest runtime. The key takeaway here is that the $- {{\mathbf{t}\mathbf{r}}{(\hat{W})}}$ objective appears to be a suitable surrogate for the ${\mathbf{t}\mathbf{r}}{({\hat{W}}^{- 1})}$ by providing similar performance while decreasing runtime by over $50\%$. Additionally, we see the importance of considering the current model when planning future control inputs in order to target regions of the state and control space where the model has larger variance.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-C Real-Time Example in X-Plane", "weight": 1.0} -->

Many real-world applications involve situations where the model needs to be updated in real time and new control inputs planned for and executed in an online fashion. To demonstrate the usefulness of our method in real-world situations, we have integrated our method with the X-Plane simulator. X-Plane is a highly realistic flight simulator widely used for both pilot training and research purposes. By interfacing our control input design methods with X-Plane, we were able to test the effectiveness of our approach in a dynamic environment. This integration allows for real-time updates and adjustments to control inputs based on the current state of the aircraft, showcasing the practical applicability of our method in scenarios that require adaptive and responsive control strategies. This example demonstrates the speed of our method to update the model estimate and replan while running onboard the aircraft.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-C Real-Time Example in X-Plane", "weight": 1.0} -->

The initial data was collected by having a human fly the airplane for $50$ seconds with data collected at $2$ Hz. The LP method was then run to plan control inputs $25$ seconds into the future. While executing the control inputs, the future state predictions were updated based on the current state of the aircraft. Once the control inputs were executed, the dynamics model was updated with the newly collected data and then a new sequence of control inputs were planned.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-C Real-Time Example in X-Plane", "weight": 1.0} -->

For this real-time demonstration, we added additional constraints so that the system would try to end each $25$ second maneuver back at the initial trim condition (zero roll, pitch, yaw, sideslip, etc.). This is consistent with the approach used by \ to avoid the aircraft from deviating too far from the flight region of interest. The average replanning time for the LP method during these experiments was 0.20 seconds. All of the results presented in this section were run on a computer with an M1 Max and 64 GB of RAM.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion", "weight": 1.5} -->

We demonstrated a powerful technique to efficiently design informative control inputs for dynamic system identification, with a particular focus on high dimensional systems. Our approach integrates informative input design into the Dynamic Mode Decomposition with control (DMDc) framework by formulating the problem as an approximate convex optimization problem. This formulation allows us to systematically reduce model uncertainty and improve predictive accuracy while adhering to practical constraints on the resulting state estimates, control input amplitudes, slew rates, trim conditions, as well as the possibility to extend to a variety of other practical constraints.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

We validated our methods through extensive experiments in three different simulation environments. In the fluid flow past a cylinder experiment, we demonstrated the ability of our method to handle high dimensional systems. In the Aerobench simulator with F-16 dynamics, we showcased the effectiveness of our approach in handling complex, multi-input multi-output control scenarios, highlighting the advantages of our proposed methods in terms of objective value performance and solution times. Finally, we integrated our method with the X-Plane simulator to demonstrate real-time applicability, emphasizing its potential for adaptive and responsive control in real-world environments.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

The results from these simulations underscore the practical utility of our approach in various real-world applications, from aircraft control to fluid dynamics. Our methods not only significantly reduce model uncertainty with less data, but also support real-time applications.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discussion", "weight": 1.5} -->

Future work will explore enhancements to our input design framework, including extensions to handle more complex nonlinear systems, and applications in other domains such as robotics, climate modeling, and financial systems. The integration of our methods with real-time control systems holds promise for advancing the state-of-the-art in system identification and control, paving the way for more intelligent, data-driven approaches to managing and understanding complex dynamical systems. As data continues to become more abundant, the question becomes not only what information is contained in your data, but often, and more importantly -- what is not. Our contribution provides a principled approach to maximally leverage the data that we have collected by informing what new data needs to be collected. In doing so, we believe this will allow for the development of better informed data driven models while also maintaining the efficiency required for real-time applications.
