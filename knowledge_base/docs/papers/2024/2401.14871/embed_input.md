<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Direct data-driven design methods for the linear quadratic regulator (LQR) mainly use offline or episodic data batches, and their online adaptation has been acknowledged as an open problem. In this paper, we propose a direct adaptive method to learn the LQR from online closed-loop data. First, we propose a new policy parameterization based on the sample covariance to formulate a direct data-driven LQR problem, which is shown to be equivalent to the certainty-equivalence LQR with optimal non-asymptotic guarantees. Second, we design a novel data-enabled policy optimization (DeePO) method to directly update the policy, where the gradient is explicitly computed using only a batch of persistently exciting (PE) data. Third, we establish its global convergence via a projected gradient dominance property. Importantly, we efficiently use DeePO to adaptively learn the LQR by performing only one-step projected gradient descent per sample of the closed-loop system, which also leads to an explicit recursive update of the policy.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Under PE inputs and for bounded noise, we show that the average regret of the LQR cost is upper-bounded by two terms signifying a sublinear decrease in time O(1/sqrt(T)) plus a bias scaling inversely with signal-to-noise ratio (SNR), which are independent of the noise statistics. Finally, we perform simulations to validate the theoretical results and demonstrate the computational and sample efficiency of our method.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a cornerstone of modern control theory, the linear quadratic regulator (LQR) design has been widely studied in data-driven control, where no model but only raw data is available. The manifold approaches to data-driven LQR design can be broadly categorized as indirect, i.e., based on system identification (SysID) followed by model-based control design, versus direct when bypassing the identification step. Another classification is episodic when obtaining the control policy from one episode of data or by alternating episodes of data collection and control (see Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), versus adaptive when updating the control policy from online closed-loop data (see Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The indirect data-driven LQR design has a rich history with well-understood tools for identification and control. Representative approaches include optimism-in-face-of-uncertainty, robust control, certainty-equivalence control, and adaptive dynamic programming. Most of them are episodic in that they either estimate the system dynamics from a single episode of offline data, or update their estimate only after an episode is completed. This is due to their requirement of statistically independent data and regret analysis methods. Notable adaptive methods are rooted on certainty-equivalence LQR: a system is first identified by ordinary least-squares from closed-loop data, and then a certainty-equivalence LQR is obtained with Riccati equations by treating the estimated system as the ground-truth. By alternating identification and certainty-equivalence LQR, they guarantee convergence to the optimal LQR gain. In particular, the work takes the first step towards indirect adaptive control with asymptotic convergence guarantees by regularizing the identification objective with the LQR cost. Recent works have shown that certainty-equivalence control with explorative input ensuring persistency of excitation meets optimal non-asymptotic guarantees.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Different from the indirect design, direct methods entirely by-pass models; see for a discussion of the trade-offs. An emerging line of direct methods obtains the LQR directly from a single episode of persistently exciting (PE) data. It is inspired by subspace methods and the fundamental lemma in behavioral system theory. Using subspace relations, the works show that the closed-loop system can be parameterized by state-space data, leading to direct data-driven formulations of the LQR problem. By a change of variables, they can be reformulated as semi-definite programs (SDPs) parameterized by raw data matrices. In the presence of noise, regularization is introduced for direct LQR design to promote certainty-equivalence or robustness. There are also works developing matrix S-lemma or combining prior knowledge for robust LQR design, while they are inherently conservative. Though these methods only use a single episode of offline data, the dimension of their formulations usually scales with the data length. Since adaptation of their policy to the latest data may not improve control performance, they cannot use online closed-loop data to achieve adaptive learning of the LQR.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In fact, their real-time adaptation is acknowledged as an open problem in the data-driven control field.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A potential path towards direct and online adaptive control is policy optimization (PO), a direct design framework where the policy is parameterized and recursively updated to minimize a cost function. Dating back to the adaptive control of aircraft in the 1950s, the concept of direct PO has a long history in control theory. However, due to the non-convexity of PO formulations, it is usually challenging to obtain strong performance guarantees. Recently, there have been resurgent interests in studying theoretical properties of zeroth-order PO, which is also an essential approach of modern reinforcement learning. It improves the policy by gradient methods, where the gradient is estimated from observations of the cost. For the LQR learning problem, zeroth-order PO meets global linear convergence thanks to a gradient dominance property. However, zeroth-order PO is intrinsically unsuitable for adaptive control since (a) the cost used for gradient estimate can be obtained only after observing an entire trajectory, (b) the trajectory needs to be sufficiently long to reduce the estimation error, and (c) it requires numerous trajectories to find an optimal policy.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Different from zeroth-order PO, our recent work has proposed a data-enabled PO (DeePO) method for the LQR, where the gradient is computed directly from a single trajectory of finite length, and shown global convergence. This is achieved by adopting the data-based policy parameterization. While this DeePO method is based on offline data, it paves the way to applying PO for direct and online adaptive control.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following, this paper proposes a novel DeePO method for direct adaptive learning of the LQR, where the policy is directly updated by gradient methods from online closed-loop data; see Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") for an illustration. Hence, we provide a promising solution to the open problem. Our contributions are summarized below.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a new policy parameterization for the LQR based on sample covariance, which is a key ingredient in SysID, filtering, and data-driven control parameterizations. Compared with the existing parameterization, it has two salient features that enable online adaptation of DeePO. First, the dimension of the parameterized policy remains constant depending only on the system dimension. Second, the resulting direct LQR is shown to be equivalent to the indirect certainty-equivalence LQR, which usually requires regularized formulations and methods. In view of, this equivalence implies that our covariance parameterization enables sample-efficient online learning. The covariance parameterization can also be used to solve other control problems in a direct data-driven fashion.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a DeePO method to solve the covariance-parameterized LQR problem with offline data and show global convergence. The key to our analysis is a projected gradient dominance property, which is distinguished from the usual gradient dominance in PO literature.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We use DeePO to adaptively learn the optimal LQR gain from online closed-loop data, starting from an initial stabilizing gain learned from offline data. The proposed approach is direct, online, and has an explicit recursive update of the policy. Moreover, it can be extended straightforwardly to time-varying systems by adding a forgetting factor to the covariance parameterization.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide non-asymptotic guarantees of DeePO for adaptive learning of the LQR, which are independent of noise statistics. Our focus is on the convergence of the policy instead of stability, which is in line with the RL perspective and the definition of adaptive control by Zames. Under PE inputs and bounded noise, we show that the average regret of the LQR cost is upper-bounded by two terms signifying a sublinear decrease in time $\mathcal{O}{({1/\sqrt{T}})}$ plus a bias scaling inversely as signal-to-noise ratio (SNR). This convergence result improves over single batch methods, whose performance also depends on SNR but does not decay over time. Our sublinear decrease rate aligns with that of first-order methods in online convex optimization of smooth functions, even though our considered LQR problem is non-convex. This sublinear rate shows the sample efficiency of DeePO to learn from online data.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the simulations, we validate the global convergence of DeePO. Moreover, we compare DeePO with the indirect adaptive approach and zeroth-order PO for the benchmark problem. The simulations demonstrate favorable computational and sample efficiency of DeePO.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Data-driven formulations and adaptive learning of the LQR", "weight": 1.0} -->

In this section, we first recapitulate indirect certainty-equivalence LQR (least-square SysID followed by model-based LQR design), direct LQR design using data-based policy parameterization, and policy optimization (PO) of the LQR based on zeroth-order gradient estimate. Then, we formalize our adaptive learning problem.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

where $t \in {\mathbb{N}}$, $x_{t} \in {\mathbb{R}}^{n}$ is the state, $u_{t} \in {\mathbb{R}}^{m}$ is the control input, $w_{t} \in {\mathbb{R}}^{n}$ is the noise, and $z_{t}$ is the performance signal of interest. We assume that $(A,B)$ are controllable and the weighting matrices $(Q,R)$ are positive definite. Throughout the paper, we do not assume any statistics of the noise $w_{t}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

The LQR problem is phrased as finding a state-feedback gain $K \in {\mathbb{R}}^{m \times n}$ that minimizes the $\mathcal{H}_{2}$-norm of the transfer function ${\mathcal{T}{(K)}}:{w\rightarrow z}$ of the closed-loop system

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

where $\Sigma_{K}$ is the closed-loop state covariance matrix obtained as the positive definite solution to the Lyapunov equation

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

We refer to $C{(K)}$ as the LQR cost and to ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) as a policy parameterization of the LQR.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

There are alternative formulations to find the optimal LQR gain $K^{\ast}:={{\arg{\min_{K}C}}{(K)}}$ of ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-( and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), e.g., via the celebrated Riccati equation with known $(A,B)$. For unknown $(A,B)$, there is a plethora of data-driven control methods to find $K^{\ast}$, some of which we recapitulate below.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

This conventional approach to data-driven LQR design follows the certainty-equivalence principle: it first identifies a system $(A,B)$ from data, and then solves the LQR problem regarding the identified model as the ground-truth. The SysID step is based on subspace relations among the state-space data. Consider a $t$-long time series^11^1The time series do not have to be consecutive. All results in Sections II and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")-IV and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") also hold when each column in ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is obtained from independent experiments or even averaged data sets. of states, inputs, noises, and successor states

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

which satisfy the system dynamics

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

We assume that the data is persistently exciting (PE), i.e., the block matrix of input and state data

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

This PE condition is necessary for the data-driven LQR design.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

Based on the subspace relations ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) and the rank condition ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), an estimate $(\hat{A},\hat{B})$ of the system can be obtained as the unique solution to the ordinary least-squares problem

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

Following the certainty-equivalence principle, the system $(A,B)$ is replaced with its estimate $(\hat{A},\hat{B})$ in ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-( and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), and the LQR problem can be reformulated as a bi-level program

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

The problem ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is termed certainty-equivalence and indirect data-driven LQR design. By alternating between solving ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) and using the resulting policy to collect online closed-loop data, it achieves adaptive learning of the LQR with optimal non-asymptotic guarantees.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

In contrast to the SysID-followed-by-control approach ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the direct data-driven LQR design aims to find $K^{\ast}$ bypassing the identification step ( and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), which we recapitulate as follows. It uses a data-based policy parameterization: by the rank condition ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), there exists a matrix $G \in {\mathbb{R}}^{T \times n}$ that satisfies

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

for any given $K$. Together with the subspace relation ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the closed-loop matrix can be written as

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

Since $W_{0}$ is unknown and unmeasurable, it is disregarded and $X_{1}G$ is used as the closed-loop matrix. Following the certainty-equivalence principle, we substitute $A + {BK}$ with $X_{1}G$ in ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-( and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), and together with ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0043", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) the LQR problem becomes

<!-- chunk {"id": "body-0044", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

with the gain matrix $K = {U_{0}G}$, which can be reformulated as an SDP. The LQR parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is direct data-driven, as it does not involve any explicit SysID.

<!-- chunk {"id": "body-0045", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

However, the LQR parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is not robust to noise and requires regularization. Moreover, its dimension scales linearly with $t$, and it is unclear how to turn ( and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0046", "role": "body", "section": "II-C Direct LQR with data-based policy parameterization", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) into a recursive formulation for online closed-loop adaptation. These issues are naturally addressed with the covariance parameterization in the sequel.

<!-- chunk {"id": "body-0047", "role": "body", "section": "II-D PO of the LQR using zeroth-order gradient estimate", "weight": 1.0} -->

As an essential approach of modern reinforcement learning, zeroth-order PO finds $K^{\ast}$ by iterating the gradient descent for the policy parameterization of the LQR ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-( and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0048", "role": "body", "section": "II-D PO of the LQR using zeroth-order gradient estimate", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")):

<!-- chunk {"id": "body-0049", "role": "body", "section": "II-D PO of the LQR using zeroth-order gradient estimate", "weight": 1.0} -->

The PO ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is initialized with a stabilizing gain, $\eta > 0$ is a constant stepsize, and $\hat{{\nabla C}⁢{(K)}}$ is the gradient estimate from zeroth-order information, e.g., the two-point gradient estimate

<!-- chunk {"id": "body-0050", "role": "body", "section": "II-D PO of the LQR using zeroth-order gradient estimate", "weight": 1.0} -->

where $r > 0$ is the smoothing radius, $F$ is uniformly sampled from the unit sphere ${\mathbb{S}}^{{mn} - 1}$, and $\hat{C}$ is the approximated cost observed from a single realization of a $T$-long trajectory of system ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0051", "role": "body", "section": "II-D PO of the LQR using zeroth-order gradient estimate", "weight": 1.0} -->

While zeroth-order PO has a recursive policy update, it requires to sample a large number of long trajectories to find $K^{\ast}$, which is inherently unsuitable for online adaptive control.

<!-- chunk {"id": "body-0052", "role": "body", "section": "II-E Direct adaptive learning for the LQR with online closed-loop data", "weight": 1.0} -->

All the aforementioned data-driven LQR design methods either lack a recursive policy update, or are unsuitable for adaptive control with online closed-loop data.

<!-- chunk {"id": "body-0053", "role": "body", "section": "II-E Direct adaptive learning for the LQR with online closed-loop data", "weight": 1.0} -->

Problem: design a recursive direct method based on online closed-loop data such that the control policy converges to the optimal LQR gain.

<!-- chunk {"id": "body-0054", "role": "body", "section": "II-E Direct adaptive learning for the LQR with online closed-loop data", "weight": 1.0} -->

Our objective concerns the optimality of the policy whereas traditional adaptive control focuses on stability. Our perspective is in line with the RL perspective and the essence of adaptive control by Zames, namely, improving over the best control with a prior information. Following, we start with a direct data-driven LQR formulation but with a new policy parameterization. Then, we take an iterative PO perspective to the direct LQR as in our previous work, and use gradient methods to achieve adaptive learning of the LQR with online closed-loop data.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Direct data-driven LQR with a new policy parameterization", "weight": 1.0} -->

In this section, we first propose a new policy parameterization based on the sample covariance to formulate the direct data-driven LQR problem. Then, we establish its equivalence to the indirect certainty-equivalence LQR problem.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-A A new policy parameterization using sample covariance", "weight": 1.0} -->

To efficiently use data, we propose a new policy parameterization based on the sample covariance of input-state data

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-A A new policy parameterization using sample covariance", "weight": 1.0} -->

which plays an important role in SysID, filtering, and data-driven control parameterizations. Under the PE rank condition ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the sample covariance $\Phi$ is positive definite, and there exists a unique solution $V \in {\mathbb{R}}^{{({n + m})} \times n}$ to

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-A A new policy parameterization using sample covariance", "weight": 1.0} -->

for any given $K$. We refer to ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) as the covariance parameterization of the policy. In contrast to the parameterization in ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-A A new policy parameterization using sample covariance", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the dimension of $V$ is independent of the data length.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The covariance parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) can also be derived from ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 1", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). Since $D_{0}$ does not necessarily have full column rank, there is a considerable nullspace in the solution of ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 1", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")),

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 1", "weight": 1.0} -->

with $V \in {\mathbb{R}}^{{({n + m})} \times n}$. If we remove the nullspace $\mathcal{N}{(D_{0})}$ in ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), then the parameterization ( and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 1", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) reduces to ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 1", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). Note that the nullspace is undesirable, and regularization methods are usually used to single out a favorable solution.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Analogous to ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), we disregard the uncertainty ${\overline{W}}_{0}$ in the parameterized closed-loop matrix and formulate the direct data-driven LQR problem using $(X_{0},U_{0},X_{1})$ as

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 1", "weight": 1.0} -->

with the gain matrix $K = {{\overline{U}}_{0}V}$. We refer to ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) as the LQR problem with covariance parameterization.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In comparison with ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the covariance parameterization can well display and partially mitigate the effects of stochastic noise. Let $\{ w_{t}\}$ be additive white noise.

<!-- chunk {"id": "body-0069", "role": "body", "section": "III-B The equivalence between the covariance parameterization of the LQR and the indirect certainty-equivalence LQR", "weight": 1.0} -->

We now show that the data-driven covariance parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is equivalent to the indirect certainty-equivalence LQR ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0070", "role": "body", "section": "III-B The equivalence between the covariance parameterization of the LQR and the indirect certainty-equivalence LQR", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) in the sense that their solutions coincide. Let $J^{\ast}$ and $C_{\text{CE}}^{\ast}$ be the optimum of ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0071", "role": "body", "section": "III-B The equivalence between the covariance parameterization of the LQR and the indirect certainty-equivalence LQR", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) and ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0072", "role": "body", "section": "III-B The equivalence between the covariance parameterization of the LQR and the indirect certainty-equivalence LQR", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), respectively. Then, we have the following result.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 3 (Implicit regularization)", "weight": 1.0} -->

This equivalence has also been shown for the LQR parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) with a sufficiently large certainty-equivalence regularizer, i.e.,

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 3 (Implicit regularization)", "weight": 1.0} -->

with the gain $K = {U_{0}G}$ \[, Corollary 3.2\]. Thus, the covariance parametrization of the LQR ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is implicitly regularized as it achieves this equivalence without any regularization.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 3 (Implicit regularization)", "weight": 1.0} -->

An implicit regularization property is also established in the PO of ( ‣ III-B The equivalence between the covariance parameterization of the LQR and the indirect certainty-equivalence LQR ‣ III Direct data-driven LQR with a new policy parameterization ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Remark 3 (Implicit regularization)", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")) in the absence of noise \[, Theorem 2\].

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remark 3 (Implicit regularization)", "weight": 1.0} -->

While the LQR problem with covariance parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) can be reformulated into an SDP as, our subsequent solution will not make use of that. Instead, the next section solves ( and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 3 (Implicit regularization)", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) via an iterative PO method with convergence guarantees.

<!-- chunk {"id": "body-0079", "role": "body", "section": "DeePO for the LQR with covariance parameterization using offline data", "weight": 1.0} -->

In this section, we first present our novel PO method to solve the LQR problem with covariance parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) given offline data $(X_{0},U_{0},X_{1})$. Then, we show its global convergence by proving a projected gradient dominance property.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IV-A Data-enabled policy optimization to solve the LQR problem with covariance parameterization (18 and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)\"))", "weight": 1.0} -->

We assume the feasibility of ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The covariance parameterization of the LQR problem in ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 4", "weight": 1.0} -->

By Lemma ‣ III-B The equivalence between the covariance parameterization of the LQR and the indirect certainty-equivalence LQR ‣ III Direct data-driven LQR with a new policy parameterization ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Remark 4", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)"), Assumption and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") is equivalent to the feasibility of the certainty-equivalence LQR problem ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Remark 4", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), and hence is necessary also for indirect control.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Remark 4", "weight": 1.0} -->

where $P_{V} \succ 0$ is the unique solution to the Lyapunov equation

<!-- chunk {"id": "body-0086", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Then, the closed-form expression for ${\nabla J}{(V)}$ is given as follows.

<!-- chunk {"id": "body-0087", "role": "body", "section": "IV-B Projected gradient dominance of the LQR cost", "weight": 1.0} -->

We first define the projected gradient dominance property.

<!-- chunk {"id": "body-0088", "role": "body", "section": "IV-C Global convergence of DeePO", "weight": 1.0} -->

As in the LQR parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0089", "role": "body", "section": "IV-C Global convergence of DeePO", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the cost $J{(V)}$ here tends to infinity as $V$ approaches the boundary $\partial\mathcal{S}$. Thus, it is only locally smooth over a sublevel set.

<!-- chunk {"id": "body-0090", "role": "body", "section": "DeePO for direct, adaptive, and recursive learning of the LQR with online closed-loop data", "weight": 1.0} -->

In this section, we first use DeePO to adaptively and recursively learn the optimal LQR gain from online closed-loop data. Then, we provide non-asymptotic convergence guarantees for DeePO.

<!-- chunk {"id": "body-0091", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

In the adaptive control setting, we collect online closed-loop data $x_{t},u_{t},x_{t + 1}$ at time $t$ that constitutes the data matrices $(X_{0,{t + 1}},U_{0,{t + 1}},X_{1,{t + 1}})$^22^2Since the closed-loop data grows with time in the adaptive control setting, we use $X_{0,t},U_{0,t},W_{0,t},X_{1,t}$ to denote the data series of length $t$ in ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0092", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). We also add a subscript $t$ to other notations to highlight the time dependence. Under the new notations, all the results in Sections II and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0093", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)"), III and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"), IV and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0094", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") still hold.. The goal is to use DeePO to learn the optimal LQR gain $K^{\ast}$ directly from online closed-loop data. Our key idea is to first use $(X_{0,{t + 1}},U_{0,{t + 1}},X_{1,{t + 1}})$ to perform only one-step projected gradient descent for the parameterized policy at time $t$, then use the updated policy to control the system, and repeat. The details are presented in Algorithm and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0095", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"), which is both direct and adaptive.

<!-- chunk {"id": "body-0096", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

1:Offline data (X0, t0,U0, t0,X1, t0), an initial stabilizing policy Kt0, and a stepsize η.
3: Apply ut and observe xt + 1.
4: Given Kt, solve Vt + 1 via

<!-- chunk {"id": "body-0097", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

5: Perform one-step projected gradient descent

<!-- chunk {"id": "body-0098", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

where the gradient ∇Jt + 1(Vt + 1) is given by Lemma 2.
6: Update the control gain by

<!-- chunk {"id": "body-0099", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

Algorithm 1 DeePO for direct adaptive learning of the LQR

<!-- chunk {"id": "body-0100", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

An initial stabilizing gain is obtained from offline data $(X_{0,t_{0}},U_{0,t_{0}},X_{1,t_{0}})$, i.e., $K_{t_{0}} = {{\overline{U}}_{0,t_{0}}V_{t_{0}}^{\prime}}$ with $V_{t_{0}}^{\prime}$ the solution to ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0101", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). Alternatively, $K_{t_{0}}$ can be found via ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0102", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")) or ( ‣ III-B The equivalence between the covariance parameterization of the LQR and the indirect certainty-equivalence LQR ‣ III Direct data-driven LQR with a new policy parameterization ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0103", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")).

<!-- chunk {"id": "body-0104", "role": "body", "section": "V-A Direct adaptive learning of the LQR", "weight": 1.0} -->

At the online stage $t \geq t_{0}$, we make the following assumptions on $u_{t}$ to update the policy.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumption and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") adopts a quantitative notion of PE \[, Definition 2\] and implies the rank condition ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). Here, the constant $\gamma$ is used to quantify the PE level.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Since ${\mathcal{H}_{n + 1}{(U_{0,t})}\mathcal{H}_{n + 1}^{\top}{(U_{0,t})}}/t$ is the sample covariance of the input, the $\mathcal{O}{(\sqrt{t})}$ scaling in $\underset{¯}{\sigma}{({\mathcal{H}_{n + 1}{(U_{0,t})}})}$ implies constant covariance excitation. Note that the PE assumption is universal in adaptive control.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Assumption and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") imposes the uniform boundedness and sequential stability of the closed-loop system, i.e., the state does not blow up under the switching policy sequence.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Remark 5", "weight": 1.0} -->

We use Assumptions and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") and and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Remark 5", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") to decouple the convergence analysis and the input design problem. The latter concerns designing control inputs ensuring the excitation and boundedness assumptions, which is not the focus of this paper. Briefly, the input can be selected as

<!-- chunk {"id": "body-0111", "role": "body", "section": "Remark 5", "weight": 1.0} -->

where $\{ v_{t}\}$ is a probing noise sequence. In this case, Assumption and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") holds with high probability when $\{ v_{t}\}$ is i.i.d. Gaussian.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Alternatively, a simple linear algebraic manipulation can also determine $v_{t}$, as the feedback term $K_{t}x_{t}$ is known. Of course, either approach will degrade the closed-loop performance. Assumption and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") can possibly be circumnavigated by a more sophisticated sequential stability analysis.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Intuitively, proving sequential stability for ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) requires that (a) the LQR cost of the closed-loop system $A + {BK_{t}}$ is uniformly bounded, which can be achieved by our gradient methods; and (b) $K_{t}$ changes sufficiently slowly, which can be easily achieved by selecting a small stepsize $\eta$.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Remark 5", "weight": 1.0} -->

We leave a detailed investigation of the consequences of these assumptions and the input design problem to future work, and instead focus on the convergence analysis in this paper.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Finally, we assume that the process noise $w_{t}$ is bounded as, which does not necessarily follow any particular statistics and can even be adversarial and correlated.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The process noise $w_{t}$ is upper-bounded, i.e., ${\| w_{t}\|} \leq \delta$ for some constant $\delta \geq 0$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

To better interpret our analysis and main results, we refer to $\gamma/\delta$ as the signal-to-noise ratio (SNR) describing the ratio between the useful and useless information $D_{0,t}$ and $W_{0,t}$. Such a notion of SNR is slightly different from the commonly used power-based definition.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

While Algorithm and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)") requires to compute the sample covariance matrices ${\overline{X}}_{0,t},{\overline{U}}_{0,t},{\overline{X}}_{1,t}$ and $\Phi_{t}^{- 1}$, it does not need to store all the historical data $(X_{0,t},U_{0,t},X_{1,t})$ and can be implemented recursively, as shown in the next subsection.

<!-- chunk {"id": "body-0120", "role": "body", "section": "V-B Recursive implementation of Algorithm 1 and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)\")", "weight": 1.0} -->

We show how to efficiently implement Algorithm and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") via recursive rank-one update. First, the sample covariance matrices ${\overline{X}}_{0,t},{\overline{U}}_{0,t},{\overline{X}}_{1,t}$ are updated recursively.

<!-- chunk {"id": "body-0121", "role": "body", "section": "V-B Recursive implementation of Algorithm 1 and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)\")", "weight": 1.0} -->

where the first term is the weighted covariance matrix from the last iteration, and the second is a rank-one matrix. The other two matrices ${\overline{U}}_{0,t},{\overline{X}}_{1,t}$ can be updated accordingly.

<!-- chunk {"id": "body-0122", "role": "body", "section": "V-B Recursive implementation of Algorithm 1 and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)\")", "weight": 1.0} -->

Second, the covariance parameterization in ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) can also be implemented via rank-one update.

<!-- chunk {"id": "body-0123", "role": "body", "section": "V-B Recursive implementation of Algorithm 1 and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)\")", "weight": 1.0} -->

Then, ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) can be written as a rank-one update

<!-- chunk {"id": "body-0124", "role": "body", "section": "V-C Non-asymptotic convergence guarantees for Algorithm 1 and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)\")", "weight": 1.0} -->

Let Assumptions and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")- and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0125", "role": "body", "section": "V-C Non-asymptotic convergence guarantees for Algorithm 1 and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)\")", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") hold throughout this section. Let $T:={{t - t_{0}} + 1}$ denote the running time of Algorithm and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0126", "role": "body", "section": "V-C Non-asymptotic convergence guarantees for Algorithm 1 and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)\")", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") and $C^{\ast}:={{\min_{K}C}{(K)}}$. We use the optimality gap ${C{(K_{t})}} - C^{\ast}$ to quantify the convergence of $K_{t}$, which is aligned with the RL perspective and broader online optimization literature. Define the average regret as the time-average optimality gap of the policy sequence

<!-- chunk {"id": "body-0127", "role": "body", "section": "V-C Non-asymptotic convergence guarantees for Algorithm 1 and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)\")", "weight": 1.0} -->

The regret depends on $\{ w_{t}\}$ but is not a well-defined random variable, since we do not assume any particular statistics on the noise. Now, we provide an upper bound on the regret for any bounded $\{ w_{t}\}$ consistent with Assumption 4.

<!-- chunk {"id": "body-0128", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

The DeePO method in Algorithm and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") is adaptive and direct in that it learns from online closed-loop data without any explicit SysID. This is in contrast to the indirect adaptive control that involves an identification step, and the episodic methods using single or multiple alternating episodes of data collection and control.

<!-- chunk {"id": "body-0129", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

The DeePO method has a recursive policy update and is computationally efficient. In particular, Algorithm and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") performs only one-step projected gradient descent per time efficiently using online closed-loop data, and can be implemented recursively (see Section V-B and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0130", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). In comparison, the indirect adaptive control requires to solve one certainty-equivalence LQR problem ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0131", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) per time. While one can do one or a few Riccati iterations per time step to gain in terms of computation time, it remains unclear if such an iterative approach has provable theoretical guarantees.

<!-- chunk {"id": "body-0132", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

Our analysis of Theorem ‣ V-C Non-asymptotic convergence guarantees for Algorithm 1 ‣ V DeePO for direct, adaptive, and recursive learning of the LQR with online closed-loop data ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0133", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)") is non-asymptotic and independent of the noise statistics. It improves over single batch methods, where their performance also depends on SNR but does not decay over time \[, Theorem 4.1\]. Our sublinear decrease matches the attainable rate $\mathcal{O}{({1/\sqrt{T}})}$ of first-order methods in online convex optimization of smooth functions \[, Chapter 3\], even though our considered LQR problem ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0134", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is non-convex.

<!-- chunk {"id": "body-0135", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

This indicates a favorable sample efficiency of DeePO to learn from online closed-loop data. The regret bound also has a polynomial dependence on the optimal LQR cost $C^{\ast}$, which is a key system-theoretic parameter. This is in line with the scaling in terms of $C^{\ast}$ of the regret bounds in indirect adaptive control.

<!-- chunk {"id": "body-0136", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

While Theorem ‣ V-C Non-asymptotic convergence guarantees for Algorithm 1 ‣ V DeePO for direct, adaptive, and recursive learning of the LQR with online closed-loop data ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0137", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)") assumes the boundedness of noise, DeePO can handle stochastic noise as well. Suppose that $\{ w_{t}\}$ is white Gaussian, then the SNR has an explicit high-confidence bound, i.e., it decays inversely proportional to the square root of time. Together with Theorem 2, it can be shown that the regret converges sublinearly with high probability. A detailed investigation of the stochastic case is left to future work.

<!-- chunk {"id": "body-0138", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

Since the policy update of DeePO is end-to-end, we can enhance the adaptivity by using sliding window data or forgetting factor, which is useful in time-varying systems. For example, adding a forgetting factor $\beta \in {}$ to the sample covariance ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0139", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")) leads to $\Phi:={{D_{0}SD_{0}^{\top}}/t}$ with $S = {\text{diag}{(\beta^{t - 1},\beta^{t - 2},\cdots,1)}}$, and all results in Section V-C and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0140", "role": "body", "section": "V-D Discussion", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)") continue to hold. We defer a rigorous analysis of time-varying systems to future work.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Simulations", "weight": 1.0} -->

In this section, we first simulate over a randomly generated linear system to validate the convergence of DeePO for learning the LQR using offline and online closed-loop data, respectively. Then, we compare DeePO with indirect adaptive control and zeroth-order PO.

<!-- chunk {"id": "body-0142", "role": "body", "section": "VI-A Convergence of DeePO for the LQR with offline data", "weight": 1.0} -->

We randomly generate a controllable and open-loop stable system $(A,B)$ with ${n = 4},{m = 2}$ as

<!-- chunk {"id": "body-0143", "role": "body", "section": "VI-A Convergence of DeePO for the LQR with offline data", "weight": 1.0} -->

Let $Q = I_{4}$ and $R = I_{2}$. We generate PE data $X_{0},U_{0},W_{0}$ of length $8$ from a standard normal distribution and compute $X_{1}$ using the linear dynamics ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")).

<!-- chunk {"id": "body-0144", "role": "body", "section": "VI-A Convergence of DeePO for the LQR with offline data", "weight": 1.0} -->

The SNR (computed as ${\underset{¯}{\sigma}{(D_{0})}}/{\| W_{0}\|}$) is $- 0.12$ dB. We use only $(X_{0},U_{0},X_{1})$ to perform DeePO ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0145", "role": "body", "section": "VI-A Convergence of DeePO for the LQR with offline data", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")) to solve the LQR problem with covariance parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), which is feasible under the given set of PE data.

<!-- chunk {"id": "body-0146", "role": "body", "section": "VI-A Convergence of DeePO for the LQR with offline data", "weight": 1.0} -->

We set the stepsize to $\eta = 0.1$ and the initial policy to ${V^{0} = {\Phi^{- 1}{\lbrack 0,I_{4}\rbrack}^{\top}} \in \mathcal{S}}.$ Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0147", "role": "body", "section": "VI-A Convergence of DeePO for the LQR with offline data", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)") shows that the LQR cost converges to $J^{\ast}$ at a linear rate, which implies that the sublinear rate certified in Theorem ‣ IV-C Global convergence of DeePO ‣ IV DeePO for the LQR with covariance parameterization using offline data ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0148", "role": "body", "section": "VI-A Convergence of DeePO for the LQR with offline data", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") may be conservative.

<!-- chunk {"id": "body-0149", "role": "body", "section": "VI-B Convergence of DeePO for the adaptive learning of the LQR with online closed-loop data", "weight": 1.0} -->

In this subsection, we perform Algorithm and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0150", "role": "body", "section": "VI-B Convergence of DeePO for the adaptive learning of the LQR with online closed-loop data", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)") for the adaptive learning of the LQR with online closed-loop data to validate Theorem ‣ V-C Non-asymptotic convergence guarantees for Algorithm 1 ‣ V DeePO for direct, adaptive, and recursive learning of the LQR with online closed-loop data ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0151", "role": "body", "section": "VI-B Convergence of DeePO for the adaptive learning of the LQR with online closed-loop data", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"). We set $x_{0} = 0$ and $u_{t} \sim {\mathcal{N}{(0,I_{2})}}$ for $t < t_{0}$ with $t_{0} = 8$. For $t \geq t_{0}$, we set $u_{t} = {{K_{t}x_{t}} + v_{t}}$ with $v_{t} \sim {\mathcal{N}{(0,I_{2})}}$ to ensure persistency of excitation.

<!-- chunk {"id": "body-0152", "role": "body", "section": "VI-B Convergence of DeePO for the adaptive learning of the LQR with online closed-loop data", "weight": 1.0} -->

The white noise sequence $\{ w_{t}\}$ is drawn from a uniform distribution, where each element of $w_{t}$ is uniformly sampled from $\lbrack 0,\sigma\rbrack$. We consider three noise levels $\sigma \in {\{ 0.1,0.01,0.001\}}$, which correspond approximately to the SNR $\in {{\lbrack 0,5\rbrack},{\lbrack 10,15\rbrack},{\lbrack 20,25\rbrack}}$ dB (computed as ${\underset{¯}{\sigma}{(D_{0,t})}}/{\| W_{0,t}\|}$), respectively. Note that the SNR varies within a interval due to the random online sample of noise. We set the stepsize to $\eta = 0.01$.

<!-- chunk {"id": "body-0153", "role": "body", "section": "VI-B Convergence of DeePO for the adaptive learning of the LQR with online closed-loop data", "weight": 1.0} -->

Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0154", "role": "body", "section": "VI-B Convergence of DeePO for the adaptive learning of the LQR with online closed-loop data", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)") shows that average regret matches the expected sublinear decrease $\mathcal{O}{({1/\sqrt{T}})}$ in Theorem ‣ V-C Non-asymptotic convergence guarantees for Algorithm 1 ‣ V DeePO for direct, adaptive, and recursive learning of the LQR with online closed-loop data ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0155", "role": "body", "section": "VI-B Convergence of DeePO for the adaptive learning of the LQR with online closed-loop data", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"). Moreover, since the bounded noise $w_{t}$ has non-zero mean, the regret does not converge to zero. Roughly, the bias scales as SNR^-2^ rather than the expected SNR^-1/2^, which implies that our bound on the bias term certified in Theorem ‣ V-C Non-asymptotic convergence guarantees for Algorithm 1 ‣ V DeePO for direct, adaptive, and recursive learning of the LQR with online closed-loop data ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0156", "role": "body", "section": "VI-B Convergence of DeePO for the adaptive learning of the LQR with online closed-loop data", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") may be conservative. Bridging this gap requires tighter perturbation bounds.

<!-- chunk {"id": "body-0157", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

Consider the system proposed in \[, Section 6\]

<!-- chunk {"id": "body-0158", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

which corresponds to a discrete-time marginally unstable Laplacian system. Let $Q = R = I_{3}$. To verify that DeePO can handle unbounded noise, let $w_{t} \sim {\mathcal{N}{(0,{I_{3}/100})}}$ which corresponds to SNR $\in {\lbrack 0,5\rbrack}$ as in \[, Section VI\]. We compare Algorithm and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0159", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") with the indirect adaptive approach. Specifically, the indirect adaptive method alternates between finding the certainty-equivalence LQR gain $K_{t}$ ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0160", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")) every time step and using $u_{t} = {{K_{t}x_{t}} + v_{t}}$ with $v_{t} \sim {\mathcal{N}{(0,I_{2})}}$ to obtain the new state $x_{t + 1}$. For both methods, we use the solution to the LQR problem with covariance parameterization ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0161", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) based on $(X_{0,t_{0}},U_{0,t_{0}},X_{1,t_{0}})$ as the initial gain $K_{t_{0}}$.

<!-- chunk {"id": "body-0162", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") shows that the optimality gap of both methods converges sublinearly to $10^{- 4}$ in $200$ time steps. By using online closed-loop data, both methods improve the performance over the initial gain. For $t \leq 20$, the indirect approach exhibits faster convergence than DeePO.

<!-- chunk {"id": "body-0163", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

This is because DeePO only performs one-step projected gradient descent per time, and hence requires more iterations to asymptotically approach the certainty-equivalence LQR. Indeed, they achieve similar performance for $t \geq 60$. Moreover, thanks to the recursive policy update, the curve of DeePO is significantly smoother.

<!-- chunk {"id": "body-0164", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

Next, we compare the finite-horizon cost $\sum_{k = 0}^{t - 1}{\| z_{k}\|}^{2}$ induced by DeePO and the indirect method, denoted by $C_{d}{(t)}$ and $C_{in}{(t)}$, respectively. Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0165", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)") reports the average finite-horizon cost from $50$ independent trials, showing that their performance is extremely close during the entire run time. Further, at the initial several steps, the DeePO method has slightly lower cost due to smoother switching of the policy. After that, the indirect method performs better but their relative cost approaches to zero asymptotically.

<!-- chunk {"id": "body-0166", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

Finally, we compare their efficiency in terms of real-time computation. For a fair comparison, we apply rank-one update for Algorithm and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") (see Section V-B and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0167", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) and recursive least squares for SysID ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0168", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). Let $Q$ and $R$ be identity matrices with proper dimension. With identified model, the certainty-equivalence LQR problem ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0169", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")) is solved using the dlqr function in MATLAB. First, we evaluate the computation time for systems with different dimensions during $100$ time steps. Let the dimension of the state and input be equal, and $n = m \in {\{ 10,20,30,40,50\}}$. For each instance, we perform $50$ independent trials, where each trial uses randomly generated stable state matrix $A$ and identity input matrix $B$. The box plot in Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0170", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") shows that DeePO is significantly more efficient than indirect methods, and their gap scales significantly with the dimension. Second, we also compare the computation time to achieve different optimality gap $\epsilon:={{({{C{(K)}} - C^{\ast}})}/C^{\ast}}$ for a fixed system dimension $n = 4$. Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0171", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") shows the results from $50$ independent trials. For a large optimality gap (e.g., $\epsilon = 10^{- 2}$), the computation time is similar for both methods. This reveals that while the indirect method converges faster at the beginning (see Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0172", "role": "body", "section": "VI-C Comparison with indirect certainty-equivalence adaptive control for adaptive learning of the LQR", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), its real-time computation is more time-consuming. For a small optimality gap (e.g., $\epsilon = 10^{- 5}$), DeePO requires significantly less computation time. Since a rank-one update has been applied in both methods, the difference of computational efficiency is due to DeePO only performing one-step gradient descent per time, but the indirect method needs to solve a Riccati equation.

<!-- chunk {"id": "body-0173", "role": "body", "section": "VI-D Comparison with zeroth-order PO", "weight": 1.0} -->

While the zeroth-order PO methods are episodic (see Fig. and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), we compare them with DeePO in Algorithm and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0174", "role": "body", "section": "VI-D Comparison with zeroth-order PO", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") to demonstrate our sample efficiency. We use the simulation model ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0175", "role": "body", "section": "VI-D Comparison with zeroth-order PO", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) with $Q = {10 \times I_{3}}$, $R = I_{3}$ and $w_{t} \sim {\mathcal{N}{(0,{0.01I_{n}})}}$. We adopt the zeroth-order PO method in ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0176", "role": "body", "section": "VI-D Comparison with zeroth-order PO", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) for comparison.

<!-- chunk {"id": "body-0177", "role": "body", "section": "VI-D Comparison with zeroth-order PO", "weight": 1.0} -->

In particular, we use a minibatch of $30$ zeroth-order samples for ( and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) to reduce the variance of gradient estimate. We set the smooth radius to $r = 0.02$, the stepsize to $\eta = 10^{- 3}$, and the length of the trajectory to $T = 50$. The setting for Algorithm and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0178", "role": "body", "section": "VI-D Comparison with zeroth-order PO", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") is the same as in Section VI-B and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0179", "role": "body", "section": "VI-D Comparison with zeroth-order PO", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"). For both methods, we use $- {0.15 \times I_{3}}$ as the initial stabilizing gain.

<!-- chunk {"id": "body-0180", "role": "body", "section": "VI-D Comparison with zeroth-order PO", "weight": 1.0} -->

Table I demonstrates the sample complexity of zeroth-order PO (in terms of number of trajectories) and DeePO (in terms of number of input-state pairs) to achieve different optimality gap. It indicates that the zeroth-order PO is vastly less efficient for solving the LQR problem, which is in line with the sample complexity discussion.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

This paper proposed DeePO for the direct adaptive learning of the LQR based on the covariance parameterization. The proposed method is direct, adaptive, with closed-loop data, and has a recursive implementation. Hence, we provided a viable angle of attack to the open problem.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

We believe that our paper leads to fruitful future works. As discussed in Remark and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"), input design, quantifying the effects of probing noise, and weakening Assumptions and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") and and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

(e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") are formidable problems worthy of further investigations. We believe that the sequential stability analysis would be the key to achieving this. As observed in the simulation, the sublinear rate in Theorem ‣ IV-C Global convergence of DeePO ‣ IV DeePO for the LQR with covariance parameterization using offline data ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China. (Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

(e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") and the dependence on the SNR in Theorem ‣ V-C Non-asymptotic convergence guarantees for Algorithm 1 ‣ V DeePO for direct, adaptive, and recursive learning of the LQR with online closed-loop data ‣ Data-Enabled Policy Optimization for Direct Adaptive Learning of the LQR Research of F. Zhao and K. You was supported by National Science and Technology Major Project of China (2022ZD0116700) and National Natural Science Foundation of China.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

(Corresponding author: Keyou You) F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. (e-mail: zhaofr18@tsinghua.org.cn, youky@tsinghua.edu.cn)F. Dörfler is with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") may be conservative, and their sharper analysis is an important future work.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

While this paper considers only the LQR problem, we believe that the covariance parameterization and DeePO can be extended for other objectives (e.g., output feedback control), performance indices (e.g., $\mathcal{H}_{\infty}$ norm), and system classes (e.g., time-varying systems). It is valuable to move beyond the bounded noise assumption and analyze the expected regret under stochastic noise. The adaptivity of DeePO can be further enhanced by using sliding data window and/or forgetting factor, and a rigorous analysis is also open.
