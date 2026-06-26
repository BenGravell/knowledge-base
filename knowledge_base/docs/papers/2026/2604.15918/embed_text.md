## Introduction

The future of PID control was correctly predicted in an article 25 years ago [aastrom2001future]: it is still the most prevalent control strategy in real world applications. PID is a superior strategy when assessed in terms of performance, tuning, ease of use and maintenance, resulting in a good solution for many process dynamics.

Then and now, the PID implementation has been buried in proprietary archives of control technology suppliers. From Mathwork’s Matlab implementations to automotive, flight control, process control systems, etc: the PID controller is generally implemented as a black box, and the inside workings are not disclosed to the user. In some instances, the archives are not well maintained and the PID controller is poorly implemented with serious problems. The knowledge of how to implement the PID control law correctly is neither communicated nor developed.

The classical PID control law in the form $$u(t)=K\left(e(t)+\frac{1}{T_i}\,\int_0^t e(\tau)\, d\tau+T_d\frac{de(t)}{dt}\right)$$ is easy to implement in hardware and software [hagglund2024give]. While it is possible to implement the PID algorithm in analogue electronic circuits, mechanics, pneumatics and even biological systems, the most prevalent implementation is in programming code. The ease of implementation may explain why there appears to be only one publication solely dedicated to PID implementation [clarke1984pid], covering some basic steps focusing on the $z$-Domain. Several textbooks cover some basic aspects, too, e.g., [shin94], [shin96], [ast+haggISA2006] and [Visioli2006].

A quick online search shows that in recent years, the void of PID implementation publications has been filled with a large number of internet educational resources providing implementations of the PID controller in various languages (C, C++, Python or Matlab). Unfortunately, these implementation resources realise eq:pidTimeDomainbut rarely include the practical considerations that are required when implementing a real-world PID controller.

Some publications describe student projects or experimental setups that implement the PID controller, see [bhandari2022digital], [uzunovic2010implementation], [krejcar2011implementation]. A clear description of how to implement the real-world PID controller is not available.

Some efforts have been made to standardise the PID controller. The IEC has published a standard for evaluating the performance of PID control [IEC60546]. The International Society of Automation (ISA) has issued a technical report on PID algorithms and performance that standardises PID control, focusing on nomenclature [ISAPID2022]. There currently is no standard covering the implementation of the PID controller.

These circumstances make it difficult for control engineering professionals to find a concise and thoroughly explained reference implementation. As a result, PID implementations in commercial solutions are often ad hoc and may not include important features required to deal with practical problems. Anecdotally, the authors have heard of several industrial controllers without anti-windup that could not be used during process startup.

There are numerous extensions to the standard controller, including fractional-order controllers, PID controllers that additionally consider the second derivative of the error [HUBA2018954], etc. These fall outside the scope of this work. Neither do we consider PID tuning.

There are two alternative implementation forms: positional and incremental, the latter also referred to as velocity form [clarke1984pid]. Both are explained in detail in sec:digimp. sec:features first describes the most common problems found in practice, extending the basic discretisation of the PID control law to deal with all of them effectively. The result is the reference implementation given in sec:CombinedPID, which combines both positional and incremental form as the solution to all these practical problems, this being the main contribution of this paper. The reference implementation is provided in pseudo-code discussing line-by-line aided by a graphical representation of the code. While this means that the code cannot be taken directly into one development environment such as Matlab, C, or Python, the readability is improved because the code provides a clearer description of the algorithm, without any distractions. sec:closedloopimp introduces additional implementation considerations such as the state initialisation, the execution interval and the runtime environment. The most common problems that were described in sec:features are then simulated in sec:basicexamples to show the benefit of extending the basic PID algorithm to practical working code. The simulation codes are available in a GitHub repository by [PIDcodeGithub].

## Digital PID implementation

To implement the controller in a computer, eq:pidTimeDomain must be converted to a discrete time version. The principle of discrete time sampling is explained in this section. Both the integral and the derivative parts of the PID controller must be approximated for the conversion. There are two alternative implementations of the PID controller: the positional form and the incremental form, [clarke1984pid]. Both will be described in the following. The positional form is more intuitive, but the incremental form has important practical advantages. The implementation presented in this paper will be based on a combination of the two to exploit the advantages of each form.

The naming of variables and parameters in this implementation is based on the standard form described in eq:pidTimeDomain where $u(t)$ is the control signal and $e(t)=r(t)-y(t)$ is the control error, that is, the difference between the setpoint $r(t)$ and the measured process variable $y(t)$.

The basic control loop is depicted in fig:BasicLoop. Note that setpoint $r(t)$ and process variable $y(t)$ enter the PID block instead of control error $e(t)$. The reason for this depiction will become apparent in the following sections.

The basic control loop.

The parameters of the PID controller in eq:pidTimeDomain are controller gain $K$, integral time $T_i$, and derivative time $T_d$. The equation for the PID controller can be written in several different forms. We have chosen the linear parameterisation of eq:posForm1, with parameters $k_p=K$, $k_i=K/T_i$, and $k_d=K\ T_d$, since it is more general in the sense that it allows for $T_i=0$ in eq:pidTimeDomain without causing a division-y-zero error. If other forms are preferred, such as the series implementation [ast+haggISA2006], the implementation codes presented in this paper can be easily adapted.

### Discrete time sampling

Time series sampling is the prerequisite for digital implementation of eq:pidTimeDomain. The continuous-time process variable $y(t)$ and the continuous-time setpoint $r(t)$ have to be sampled at discrete time intervals $\Delta t$. The discrete-time control error is then with $t=n \Delta t$, where $n$ is the discrete time index. The control signal $u(t)$ is then calculated at discrete times $n\Delta t$. eq:pidTimeDomain contains the integral and the derivative of the control error $e(t)$. A common way of discretising integral and derivative is to approximate the integral with a sum and the derivative with a difference such that \int_{0}^{t} e(\tau)\,d\tau &\approx \Delta t \sum_{j=0}^{n} e(j\Delta t),\\[2pt] &\approx \frac{e(t)-e(t-\Delta t)}{\Delta t} = \frac{\Delta e(t)}{\Delta t}.

These approximations are illustrated in fig:Discretization. The integral is approximated using the forward rectangular rule, and the derivative is approximated using the forward difference approximation. Note that also other approximations such as backward difference or tangent line approximation can be considered without affecting the results presented in this paper.

Approximations of the integral and the derivative.

### Positional form

Introducing the approximations from eq:approximations in eq:pidTimeDomain, the discrete version of the PID controller results in the positional form $$u(t) = k_p\, e(t) + k_i \Delta t \sum^{n}_{j=0}e(j\Delta t) + k_d\ \frac{e(t) - e(t-\Delta t)}{\Delta t},$$ where the controller parameters $k_p=K$, $k_i=K/T_i$, and $k_d=KT_d$ have been introduced and are known as proportional gain $k_p$, integral gain $k_i$, and derivative gain $k_d$. Introducing the following notations for the three terms in the controller, eq:posForm1 becomes where $u_p(t)$, $u_i(t)$, and $u_d(t)$ represent the proportional, integral, and derivative terms, respectively. A more efficient way to implement the PID controller is to update the integral $u_i(t)$ recursively, and rewrite the individual terms as follows u_d(t) &= k_d \, \dfrac{e(t)-e(t-\Delta t)}{\Delta t} = k_d\frac{\Delta e(t)}{\Delta t}.

PID controllers are often implemented based on the positional discrete representation of eq:PIDterms and eq:posForm2. This representation is also sometimes called the direct form. In each iteration, the control signal is computed from the two most recent setpoint and process variable values, with previous value of the error $e(t-\Delta t)$ and the previous value of the error integral $u_i(t-\Delta t)$as controller states.

### Incremental form

The incremental form, also called the velocity form [clarke1984pid], computes the control signal increment since the last iteration, and uses the control signal itself to store the controller state. The control law of the incremental form is where $\Delta u(t)$ represents the increment of the following signal between the indexed time, and an instance $\Delta t$ earlier. In general, a signal increment from one time step to the next is denoted with $\Delta$, for example, The control signal increment $\Delta u(t)$ can be split into the individual terms $$\Delta u = \Delta u_p(t) + \Delta u_i(t) + \Delta u_d(t),$$ which can be obtained from eq:posForm2 as \Delta u_d(t) &= k_d\, \Big(\dfrac{\Delta e(t)}{\Delta t} - \dfrac{\Delta e(t-\Delta t)}{\Delta t}\Big), where $\Delta e(t-\Delta t)=e(t-\Delta t)-e(t-2\Delta t)$. In each iteration, the term increments are calculated according to eq:incformLong from the three most recent error values, with the actual control signal itself, $u(t)$, saved as a controller state between iterations.

### Incremental versus positional form

The incremental form has two important advantages over the positional form relating to practical implementation: bumpless transfer and clamping antiw-windup strategies can be implemented with ease.

Bumpless transfer refers to changing between manual and automatic mode, between tracking and automatic mode, or when changing parameters of the controller, without the controller output $u$ resulting in large jumps. Bumpless transfer is a requirement in most applications. In positional form implementations, this can be achieved by keeping track of when such changes occur, and changing the integrator state to a value that results in bumpless transfer. In the incremental form, the controller output is only changed by increment $\Delta u$and there is therefore no need for such checks and adjustments.

The integral part of the PID controller can result in a problem called integral windup. Integral windup occurs when the actuator and process cannot achieve the desired setpoint, resulting in a persistent control error. The persistent error may then cause a continued increase of the control signal beyond the physical limitations of the actuators. There are three common ways to avoid integral windup in PID controllers: control signal clamping, back calculation and integrator clamping. In practice, they can both work, but back calculation requires an additional parameter, a tracking-time constant, that has to be tuned. When the incremental form is used, control signal clamping is obtained simply by forcing the control signal to stay inside the control limits.

On the other hand, the incremental form requires the use of the integral term, which means that it cannot be used when the controller is a P- or PD-controller. In these cases, the positional form must be implemented. This will be discussed and handled in the implementation presented in sec:CombinedPID. This restriction is a minor drawback, since neither anti-windup nor bumpless transfer are relevant when there is no integral action in the controller.

Pseudo-code for the two forms, based on eq:posForm2 and eq:incformLong are presented in code:position and code:incremental, respectively. In the reference implementation, we drop the index for the current time, replacing $u(t)$ with u, etc. Since some increments manipulate the previous values of variables or signals, we denote these by the prefix x. For example, $e(t-\Delta t)$ is written as xe. In the code, the Greek letter $\Delta$ is denoted by the capital letter D. As a results, $\Delta e(t) = e(t)-e(t-\Delta t)$ will become De=e-xe. The pseduo-code language is explained in detail in sec:language. caption=Basic positional form., label=code:position]code/position.txt caption=Basic incremental form., label=code:incremental]code/incremental.txt

## Implementation features

Implementing the basic form of the PID controller is easy, but practical problems complicate the basic code. These problems often only become apparent during development and are usually not taught in a course or included in textbooks. Some but not all problems may occur simultaneously. Conversely, not all adjustments may be necessary. However, there is no major downside in any of the discussed modifications. tab:problems gives an overview of the problems that are addressed in the reference implementation presented in sec:CombinedPIDand are discussed in the remainder of this section.

Overview of practical implementation problems and their solutions addressed in sec:features.

| Problem | Solution | Section |

### Control without integral action

The PID implementation must be able to handle the situation of a PID control law without integral action, such as pure P- or PD-control. As discussed earlier, the incremental form cannot be used for controllers without integral action because the incremental form results in a non-changing control signal when the error is constant. To see this phenomenon, observe eq:incrementLaw,eq:DeltaUTerms,eq:incformLong when $k_i=0$ and the error is constant. Then $\Delta u(t)$ is zero, no matter the value of the control signal $u(t)$ and the constant error $e(t)$. We therefore risk to get stuck far from $e(t)=0$. Also, consider a parameter update of $k_p$for a P-controller when the error is constant, but non-zero. On incremental form, the control action stays the same after the update, and the stationary error of the P-controller is unaffected, which should not be the case.

Therefore, the desired strategy for our PID implementation to handle P- and PD-control is to operate the controller in positional form whenever $k_i=0$. This is illustrated in the example given in sec:example2. A bias term $u_0$ must be added to reduce stationary errors, see e.g. [ast+haggISA2006]. The bias term is nothing more than a constant control signal, that is normally adjusted to the control signal corresponding to zero error. This is illustrated in fig:PControl for a P-controller, which shows how the value of $u_0$ encodes the offset from $u(t)=0$ when the error is zero. The slope in the figure corresponds to the proportional gain $k_p$, and the limits $u_{\min}$ and $u_{\max}$ represent the actuator limitations.

Relationship between control error $e(t)$ and control signal $u(t)$ for a P-controller.

Thus, when there is no integral action in the controller, the integral term $u_i(t)$ is replaced by $u_0$, such that the control signal in this situation becomes

### Setpoint handling

With the position form control laws of eq:pidTimeDomain,eq:posForm1, a step in the setpoint $r(t)$ results in a corresponding step in the control error $e(t)=r(t)-y(t)$ and a therefore a large impulse in the derivative of the control error $de(t)/dt=dr(t)/dt-dy(t)/dt$. This is illustrated in fig:SetpointStep, from which it easily can be seen that we directly after the setpoint change get a large spike in the control signal, sometimes referred to as derivative kick.

Responses resulting from a step change in the setpoint.

This behavior is normally not desired, so to obtain a smoother control signal, it is common to introduce setpoint weights in the proportional and derivative parts, so that the control error in the proportional part is replaced by $b\ r(t)-y(t)$ and the error in the derivative part by $c\ dr(t)/dt-dy(t)/dt$. The setpoint weights $b$ and $c$ are restricted to $0 \le b \le 1$ and $0 \le c \le 1$. With these modifications, eq:pidTimeDomain becomes $$u(t) = K \left(b\ r(t)-y(t) + \frac{1}{T_i} \int_{0}^{t} e(\tau) \, d\tau + T_d \left(c\ \frac{dr(t)}{dt}-\frac{dy(t)}{dt}\right)\right),$$ and implementations eq:posForm2 and eq:incformLong are u_d(t) &= k_d \,\left(c\,\dfrac{\Delta r(t)}{\Delta t} - \dfrac{\Delta y(t)}{\Delta t}\right). for the positional form, and \Delta u_p(t) &= k_p\,(b\Delta r(t)-\Delta y(t)),\\[8pt] c\,\dfrac{\Delta r(t)-\Delta r(t-\Delta t)}{\Delta t} - \dfrac{\Delta y(t)-\Delta y(t-\Delta t)}{\Delta t} for the incremental form.

Note also that for controllers without integral action there will normally be stationary control errors. To minimise these, the choice $b=1$ is recommended to make the P part act on the true control error. When integral action is considered, the parameter $b$ can be used to reduce the impact of sudden changes in the setpoint signal on the control action, mitigating overshoot without compromising the performance of the disturbance rejection. Use of setpoint weighting is illustrated in the example given in sec:example3. For the PID reference implementation proposed in this article, setpoint weights are included, as well as the choice $b=1$when no integral action is present.

### Feed-forward control

Feed-forward control is a complementary control strategy to the feedback strategy used in PID-control to compensate measurable load disturbances, as illustrated in fig:FeedForward. For several reasons including anti-windup treatment, the feed-forward control signal should be added to the feedback control signal inside the PID controller, since it should affect anti-windup in the same way as other control signal terms; see [guz+hagg2024].

PID controller with feed-forward from load disturbance $v(t)$.

The feed-forward input signal can be used for other purposes than load disturbance compensation. It can for instance be used for improved setpoint handling and for decoupling in MIMO systems (see [liu2019review]). For a PID implementation on incremental form, the desired behavior is that feed-forward enters with the increments such that the total update equation for the control signal becomes $$\Delta u(t) = \Delta u_p(t) + \Delta u_i(t) + \Delta u_d(t) + \Delta u_{ff}(t).$$ In scenarios in which the positional form is used, the feed-forward signal then enters as a direct signal, and not through increments. Feed-forward control is illustrated in the example given in sec:example4.

### Control signal limitation

In almost all PID control systems, the controller output is limited due to actuator constraints. In many cases, the lower bound is $u_{\min}=0~\%$, which reflects a motor being turned off or a valve being fully closed, and the upper bound is $u_{\max}=100~\%$, which reflects the motor running at maximum speed or the valve being fully open. The values of these limits depend on the actuator for each particular control problem, and the limitation is expressed as $$u_{\min}\leq u(t) \leq u_{\max}.$$ In some PID control systems, the rate at which the control signal is allowed to change may also be limited due to safety or due to windup, if the actuator is slow. This puts the restriction $$\dot{u}_{\min}\leq \dot{u}(t) \leq \dot{u}_{\max},$$ which is normally referred to as rate limitation.

The amplitude and rate constraints can be combined at every sampling instant to form an effective interval for the control signal. The rate limitation implies that the control signal at the current instant must satisfy $$u(t-\Delta t) + \Delta t\,\dot{u}_{\min} \le u(t) \le u(t-\Delta t) + \Delta t\,\dot{u}_{\max}.$$ This interval is intersected with the actuator saturation limits. The resulting admissible bounds used by the controller are therefore $$u_{s,\min} = \max\!\left(u_{\min},\, u(t-\Delta t) + \Delta t\,\dot{u}_{\min}\right),$$ $$u_{s,\max} = \min\!\left(u_{\max},\, u(t-\Delta t) + \Delta t\,\dot{u}_{\max}\right).$$ The control signal is finally constrained to satisfy &u_{s,\max} \quad \quad \quad \, \, \text{if} \quad u(t) > u_{s,\max}, \\&u_{s,\min} \quad \quad \quad \, \, \, \text{if} \quad u(t) < u_{s,\min}, \\& u(t) \quad \quad \quad\quad \,\,\text{else}.

This procedure ensures that the control signal simultaneously respects the actuator saturation limits and the maximum allowed rate of change between consecutive sampling instants. Saturation handling is illustrated in the examples given in sec:example2 and sec:example4.

### Integrator anti-windup

Enforcing limits on the control signal means that the saturated control signal $u_s(t)$ may differ from the calculated nominal control signal $u(t)$. This gives rise to the well-understood phenomenon of integrator wind-up, as explained in e.g., [ast+haggISA2006]. There are several established strategies to address integrator wind-up [bohn+2002,dasilva+2018,hoyo+2023,visioli2003], but since naming of anti-windup strategies is somewhat ambiguous in the literature, we list here the terminology used throughout this article of the most commonly used anti-windup strategies, and what those strategies mean for an incremental form implementation:

- Control signal clamping: If the calculated control signal falls outside the interval [$u_{s,\min}$, $u_{s,\max}$], it is adjusted to the saturated value, i.e., $u(t)=u_s(t)$. - Back calculation: The calculated control signal $u$ is dynamically adjusted such that the saturation error $u(t)-u_s(t)$ decays as a first-order process with a time constant $T_t$, whenever the control signal is saturated. The time constant $T_t$ is typically set to the integral time $T_i$. - Integrator clamping: In its simplest form, integrator clamping entails not updating the integrating part whenever there is saturation. In incremental form, this corresponds to setting $\Delta u_i(t)=0$ whenever the control signal saturates.

As stated in sec:incvcpos, control signal clamping results naturally with the incremental form by saturation of the control signal according to eq:uIncSat. However, we propose back calculation for this article due to its flexibility. In this context, flexibility means that with $T_t=\Delta t$ we have control signal clamping, but by adjusting $T_t$, different anti-windup behaviours can be obtained. As discussed in sec:ulims, enforcing the saturation limits achieves both absolute control signal limits and rate limitations. The rate limitations prevent windup inherently.

In a large majority of use cases, the suggested anti-windup scheme is an appropriate choice. Nevertheless, an advanced strategy can be implemented to deal with more complex cases. This advanced strategy, referred to as combined anti-windup in this work, combines the previously described strategies as follows: Consider the situation where the control signal $u(t)$ is saturated, but not the control signal without $\Delta u_i(t)$. Then the desired behavior is to integrate to the limit. Thus, $\Delta u_i(t)$ is reduced. - Allow integration in the right direction: When $u(t)>u_{\max}$ then integration further into saturation ($\Delta u_i(t) > 0$) is not allowed, but integration away from saturation ($\Delta u_i(t) < 0$) is. In this case, $\Delta u_i(t)$ is not set to zero, but remains as calculated in integration. Of course, the corresponding logic applies to the lower limit $u_{\min}$. - Back calculation: The saturation error is updated according to the description of Back calculation above.

Anti-windup is illustrated in the example given in

### External signal tracking

There are situations in which the controller output should track an external signal instead of trying to make the process variable follow a setpoint. Examples are override control, where another controller may take over the control, often handled by selectors, and gain scheduling using several controllers. In these instances, the controller, which currently does not affect the process, must enter tracking mode (track) to avoid windup and bumps; see [Hagglund+2023]. A tracking example including a simulation when tracking is desired is provided in sec:example7.

In tracking mode, the controller assumes that the control signal currently applied to the actuator was produced by itself, even if it was not. In other words, the controller updates its internal states so that its computed output is consistent with the actual actuator signal. This means that the control signal is calculated by $$u(t)=u_{track}(t)+\Delta u_p(t) + \Delta u_i(t) + \Delta u_d(t) + \Delta u_{ff}(t),$$ where $u_{track}$ is the control signal from the controller that was actually in control of the actuator in the last iteration. The reference implementation should inherit this functionality. Controller output tracking is illustrated in the examples given in sec:example6 and sec:example7.

### Bumpless mode and parameter changes

There are three control modes: automatic or switched on (auto), tracking (track) as described in the previous section, and manual (man), where the control signal is specified by the user. Switching between these modes should not result in a large change or bump in the control signal $u(t)$. Bumpless transfer is a fundamental concept in PID control and is therefore a must in a good implementation. Bumpless transfer is desired for all controller mode changes (when possible) and for controller parameter updates.

A common implementation of bumpless transfer in positional form is to adjust the integral term to obtain the desired control signal. In incremental form, since the integral state is encoded into the control signal, bumpless transfer results naturally in many situations. However, there are some scenarios where bumpless transfer is not possible without large workarounds. For example, bumpless parameter updates when $k_i=0$ is usually neither possible nor desired. tab:bumplessReqdescribes when bumpless transfer is desired for the PID reference implementation and when not.

Bumpless transfer requirements during mode changes and parameter updates for our PID reference implementation. Tracking mode is described in sec:tracking.

| Change | $\mathbf{k_i}$ | Bumpless | Since bumpless transfer from manual mode to auto is desired, the manual control signal $u_{\text{man}}$ must enter the controller for this to be implementable; see fig:ManAuto.

Switching between manual and automatic mode.

It is often also desired to have bumpless transfer from automatic mode to manual mode. This can be accomplished outside the controller by setting $u_{\text{man}}$ to $u_{\text{auto}}$ at these mode transitions. Mode switching between man and auto is illustrated in sec:example1.

### Sampling rate and jitter

The sampling period $\Delta t$ is normally set to a constant value so that periodic sampling is obtained. Jitter is referred to as the deviation from this nominal execution period, whether it was introduced intentionally or accidentally. In most applications, the jitter is small and neglected in the calculations. However, in cases where the jitter is a problem or desired, for instance in event-based control, $\Delta t$ can be calculated as the actual time elapsed since the last execution. Therefore, the possibility to run a PID controller with jitter compensation is a required functionality for the reference PID controller implementation. Note that a large change in the sampling period $\Delta t$ also affects the rate limitations $\dot{u}_{\min}$ and $\dot{u}_{\max}$.

### Process variable and setpoint filtering

The process variable $y(t)$ is often corrupted by high-frequency noise or quantisation effects, which may cause undesired variations in the control signal $u(t)$. These variations are to some extent caused by the proportional term, $u_p(t)$, but more importantly by the derivative term, $u_d(t)$. The integral term $u_i(t)$averages the noise across samples, and thus serves as a low-pass filter, blocking noise propagation.

Our reference implementation uses the backward difference approximation $$\frac{dy}{dt} \approx \dfrac{y(t)-y(t-\Delta t)}{\Delta t},$$ with $dr/dt$ approximated in the same way, and used in controllers with setpoint derivative weight $c\neq 0$, as described in sec:setpoint.

To illustrate noise amplification of the derivative, let $n(t)$ be the additive noise term in $y(t)$. This means that while we consider $y(t)$ to be the process variable, the true, and unknown, process variable is in fact $y(t)-n(t)$. Letting $\Delta n = n(t)-v(t-\Delta t)$ we thus have a noise amplification of $\Delta n / \Delta t$, which is inversely proportional to the sampling period. For this reason, it is often necessary in practice to low-pass filter the noisy process variable $y(t)$ before computing the finite derivative approximation. This becomes increasingly important as the sampling period $\Delta t $decreases.

Similarly, while a true step function exhibits an unbounded derivative, a setpoint step of size $\Delta r$ results in a spike $\Delta r/\Delta t$ in our derivative approximation eq:derapprox.

To limit noise amplification, which may otherwise result in unnecessary actuator wear or excite resonant modes in the dynamics of the process, it is customary to low-pass filter the process variable. In situations where a setpoint weight $c>0$ is used in combination with possible abrupt (step) changes in the setpoint $r(t)$, it might also be adequate to low-pass filter $r(t)$.

While a first-order low-pass filter is most often used in existing implementations and textbooks alike, a second-order filter is advisable. This is because the latter results in derivative term noise amplification gain asymptotically approaching zero for high frequencies. This desired property is commoly referred to as high-frequency roll-off [ast+haggISA2006]. This strongly motivates the use of second-order filters, although they introduce slightly more phase-loss than their first-order counterparts.

For our reference implementation, we introduce a simple filter that approximates either of the first-order filter with transfer function or the second-order filter with transfer function in discrete time, with a sampling period $\Delta t$. The parameter $T_f$ is the filter time constant, meaning that the magnitude of the filter transfer function breaks down at $\omega_c=T_f^{-1}$, and thus effectively attenuates (noise) components in $y(t)$ with angular frequencies larger than $\omega_c$.

We use a discretisation that approximates zero-order-hold (ZOH) well, while being computationally beneficial, and allowing for a filter with bumpless output at changes in either of the filter time constant $T_f$ or the sampling period $\Delta t$. It is based on a cascaded Tustin approximation, further explained in sec:filterapp. The first-order filter eq:F1 then results in an update equation $$y_f(t)=y_f(t-\Delta t)+a\big(y(t)-y_f(t-\Delta t)\big),$$ $$a=\frac{\Delta t}{T_f+\Delta t/2},$$ where $y$ is the filter input and $y_f$ is the filter output. The second-order filter eq:F2 is approximated by cascading two first-order filters, as shown in code:filter. The incremental form of eq:dt\_filter allows for bumpless changes in $T_f$ and $\Delta t$ during operation. Note that there is no formal requirement that the filter run with the same sampling period as the controller. Noise filtering is illustrated in the example given in sec:example5.

## The combined form PID controller

In this section, we propose our reference implementation that implements all functionalities and features described in sec:features, comprising of the combined form controller of code:control, and associated signal filter of code:filter. The code is both generic and general. For example, if a PID controller will never be used in tracking mode, all tracking-specific code can be removed. Similarly, the code can be simplified if, for example, no derivative action or in other words a PI controller, is required.

The term `combined' comes from the controller making use of both the positional and incremental forms, described previously in sec:positionalsec:incvcpos. The essential idea is to use the incremental form whenever the controller has integral action. This ensures bumpless behavior at parameter and mode changes, and facilitates tracking of an exogenous control signal. However, for controllers without integral action, the positional form is needed to ensure the desired response in the control signal.

In the following sub-sections, we cover features of the proposed implementation to deal with the practical problems described in sec:features. The pseudo-code language we use is meant to be generic and focus on algorithmic aspects. For an in-depth explanation of it we refer to sec:language.

In the following, we go through our proposed implementation of the combined form PID controller (code:control), and the signal filter (code:filter) that was proposed in sec:filter. We also propose an implementation of the alternative anti-windup strategy that was introduced in sec:windup (code:anti-windup).

With the exception of the filter and alternative anti-windup strategy, we will use the schematic drawing of fig:controlschematic as a basis for introducing the code. The numbered blocks indicate the order in which the corresponding functionality appears in the implementation. Each block is described in a subsection (4.$x$) correspondingly numbered with $x$ referring to the block number in the fig:controlschematic(a). The core part of the implementation, including PID with the integral term and anti-windup techniques, is summarized in sec:code-integral and depicted in fig:controlschematic(b). code:control, the control function itself is invoked on lineline:controlfunction, and takes as its arguments:

- feed forward control signal uff, - manual control signal uman, - tracking control signal utrack, - operating mode mode.

The process variable y and setpoint r are assumed to be adequately filtered, as discussed in sec:filter, using for example our proposed filter implementation of sec:code-filter. The mode variable mode has two defined modes: manual mode "MAN" and external signal tracking mode "TRACK". It is assumed that the controller is in automatic mode whenever it is not in manual or tracking mode. Encoding of the mode is further discussed in sec:ControlMode. If no feed-forward action is desired, uff is simply set to zero. On a similar note, the values of uman and utrackare relevant when the controller is in manual and tracking mode, respectively.

The implementation also consists of both states and parameters. The parameters, e.g. controller gains and limits, are set externally by some language-dependent unspecified mechanism, further discussed in sec:closedloopimp. States are used to store controller values between executions. Complete lists of all arguments, parameters, and states are found in sec:nomenclature. [Schematic representation of code:control.] [Schematic representation of the PID with I block in fig:controlschematic1.]

Schematic overview of the combined-form PID controller. Block numbers reflect the order of appearance in our implementation and correspond to the numbered subsections referencing the relevant code lines in code:control. caption=Combined form PID controller., label=code:control]code/control.txt caption=Second-order signal filter., label=code:filter]code/filter.txt caption=Conditional integration anti-windup., label=code:anti-windup]code/anti-windup.txt

### Rate limits

The parameters umin and umax define the interval into which the control signal is saturated, cf. sec:code-saturation. The parameters dumin and dumax define a lower and upper rate limit for the change of the control signal. They are used together with the previous value of the saturated control signal, xus and the past sampling interval Dt to compute corresponding saturation bounds xus+Dt*dumin and xus+Dt*dumax (see sec:ulims).

Note that it is important that the previous saturated control signal xus, and not the previous nominal control signal xuis used to produce a correct rate limitation.

The actual saturation limits usmin and usmax are then chosen (using the min and max operations) to be the more conservative of the saturation limits umin and umax, and the ones resulting from the rate limitation, as described above as coded on Linesline:usminline:usmax.

### Derivative approximation

The derivatives used by controllers with derivative action are approximated using finite differences, as explained in sec:sampling. The difference between the current and previous process variable value y-xy is divided by the execution interval duration Dt, to produce the finite difference approximation dy on lineline:dy. The setpoint derivative approximation dr is computed in the same way on lineline:dr.

To avoid undesired jumps and noise amplification in the control signal, it is important that the process variable is adequately filtered, as described in sec:filter. In the case of nonzero setpoint weight c, the setpoint must also be adequately filtered.

### Tracking mode

Tracking of external signals, as explained in sec:tracking is implemented to overwrite the previous output xu with the signal to be tracked, utrack on lineline:tracku. Then the control signal increment is computed as normal, cf. sec:code-integral. Tracking mode is active when mode=="TRACK".

Note that tracking is only meaningful when there is integral action. In the case of no integral action, tracking mode and manual mode behave identically.

In our implementation feed-forward and integrator anti-windup behave the same way in tracking mode, as in automatic mode.

### Manual mode

The controller is in manual mode when mode=="MAN". In manual mode, the nominal control signal u takes on the externally provided value uman, as expressed on lineline:uman. The manual mode control signal is limited as explained in sec:code-ratelim. Feed-forward action is disabled in manual mode. Due to incremental form when we have integral action, the bumpless mode switches required in sec:manautois automatically obtained.

### Integral switch

The combined form switches between positional and incremental form based on whether the controller utilises integral action, as specified in sec:PandPD. This is achieved by checking for ki==0 on lineline:ifint. If the condition is true, position form is employed, as explained in sec:code-nointegral. Otherwise, the else block starting on lineline:intstart is executed, implementing incremental form as explained in sec:code-integral.

### PID without integral action

In the absence of integral action (ki==0), the positional form control signal is computed according to lineline:upos. The constant bias term u0 can be used to zero-offset the control signal to match the stationary operating point of consideration. The setpoint weighing with the weight parameters b and c are used for the proportional and derivative terms, respectively, as explained in sec:setpoint.

Feed-forward is enabled, and the control signal is saturated according to sec:code-ratelim, but since there is no integral action, no integrator anti-windup is applied.

Parameter and mode changes are not bumpless, as there is no integrator state that can be shifted to compensate for bumps.

### PID with integral action

With integral action (ki not zero), an incremental form PID control law is applied, which is summarised in fig:controlschematic(b) according to the code Linesline:Drline:uaw.

The setpoint and process variable increments Dr and Dy are computed on Linesline:Drline:Dy, followed by increments of their derivative approximations (see sec:code-derivatives) on Linesline:Ddrline:Ddy. Taking the process variable as example, the increment is simply computed as the current value y minus the previous value xy stored in the previous execution of the controlfunction.

The computed signal increments are then used to compute increments of the individual control signal termss on Linesline:Dupline:Duff. Since the derivatives are calculated from the actual time between executions, Dt, and that the integral increment also use Dt, we compensate for possible jitter according to sec:jitter. Weight parameters b and c are used for the proportional and derivative terms, respectively, to account for setpoint weighing as described in sec:setpoint. The rectangular integral approximation and finite difference derivative approximation utilised in computing Dui and Dud are described in sec:sampling.

The nominal (i.e., not yet saturated) control signal u is computed on lineline:unom by adding the increments from Linesline:Dupline:Duff to the previous nominal control signal xu. Note that the feed-forward signal must enter the signal increment here, as motivated in sec:FF.

Note that it is important that it is the nominal previous control signal xuthat is used, and not its saturated counterpart. Otherwise, it is not possible to implement integrator anti-windup strategies other than control signal clamping, as both conditional integration and back calculation rely on the possibility for the control signal to go outside of its unsaturated range. sec:windup, integrator anti-windup relies on knowing the difference between the nominal control signal u, and its saturated counterpart that we call us. To this end, the saturation limits computed on Linesline:usminline:usmax, as explained in sec:code-ratelim are applied on lineline:usminmax to obtain us.

The reference implementation of code:control implements the back calculation anti-windup strategy on lineline:uaw (with control signal clamping as a special case when Tt equals Dt).

A more general anti-windup implementation, that can serve as an in-place replacement lineline:uaw of code:control is provided in code:anti-windup. It fulfills the advanced anti-windup behaviours specified at the end of sec:windup.

For integrator clamping, it can be used as provided with Tt set to Inf, effectively translating lineline:uaw2 into u=u. Alternatively lineline:uaw2can be removed entirely when integrator clamping is desired.

Linesline:intcondline:awend in code:anti-windup have no purpose in control signal clamping, and if no other anti-windup mode needs to be supported, code:anti-windup can be replaced in its entirety by u=us (An even simpler alternative for this case is to move saving of the control signal state (xu=u) on lineline:xu of code:control to after saturating the control signal on lineline:usminmax, and removing the entire integrator anti-windup block on Linesline:usminmaxline:uaw; replacing xus by xu on Linesline:usminline:usmax, and removing lineline:xus).

### Saturate

Upon saving the nominal, unsaturated, control signal as xu on lineline:xu, the control signal is saturated on lineline:uminmax, as described in sec:code-ratelim. It is this saturated control signal that is eventually returned by the controlfunction.

### State update

As a final stage of the control function, the state variables are updated on Linesline:xusline:xuff (in addition to xu that was updated on lineline:xubefore saturating the control signal).

### Process variable and setpoint filtering

As discussed in sec:filter, the process variable, and sometimes the setpoint, need to be adequately low-pass filtered before being passed to the PID control algorithm of code:control. To this end, code:filter implements the low-pass filter introduced in sec:filter and further explained in sec:filterapp.

Lineline:a computes the filter parameter a from the filter time constant parameter Tf and execution interval Dt, as explained in sec:filterapp. If the filter runs at a constant sampling interval, there is no need to re-compute a at each invocation of the filter function. Instead, a can then be considered a parameter, computed outside the filterfunction and provided in the same fashion as other parameters.

The cascaded filter is implemented on Linesline:x1line:x2. If a first-order filter is desired, lineline:x2 can be removed, and xf2 changed to xf1 on lineline:filterfunction.

Note that the filter function must be instantiated separately for every signal being filtered, since each instance requires its own state variables

## Closed loop implementation

The PID control algorithm may be executed in a real-world, run-time environment or in a simulated environment, but always in closed loop. Both scenarios require more code than the function presented in sec:CombinedPID. This section first provides PID function execution details including initialisation, default parameter and discussions relating to the control mode. It then provides the code necessary for closed loop implementation as will be used in sec:basicexamples.

### PID function execution

The PID function call cannot be stand-alone but is embedded in an environment. The environment can take various forms and is usually application specific, but a number of common questions arise relating to the execution: how are states and signals initialised? How are parameters passed to the function? How do we loop the function call with the update of the signal reading? Answers to these questions are given in these sections.

### Initialisation

The state variables of the controller, as well as any signal filters, must be initialised to appropriate values before the control or filter functions of code:control and code:filter are invoked for the first time. The controller states are xr, xu, xus, xy, xdy, xdr and xuff. The latest available signal values can be used to initialise the controller states, so that, for example, xr=r, etc.

If the controller is started in manual mode, the initialisation of xu has no practical effect. If, instead, the controller is started in automatic or tracking mode, it is reasonable to initialise xu to the value that the actuator can be expected to have at startup. For this reason, setting xu=0 and xus=0is appropriate in many situations. However, other initialisations may be preferable depending on the application context. As with controller parameter tuning, such choices depend more on the specific use case than on the controller implementation itself, and are therefore not discussed further here.

A reasonable initialisation of the low-pass filter is to assign xf1 and xf2the latest available value of the corresponding unfiltered measurement. To avoid transient effects, it is advisable letting filters converge to their steady-state before placing the corresponding controller in automatic or tracking mode.

In the closed-loop simulation examples of this paper, the initial variables and subsequentially the controller states are are all set to zero by default.

### PID parameters

The parameters, which are orange in colour in the code, are listed in sec:nomenclature. If parameters are passed by reference, it is important to prevent them from changing while critical parts of the functions are executing. For example, switching to a new pair kp, ki should be done in a way that avoids a single invocation of code:control using the old kp value together with the new kivalue. This can be avoided in several ways. One approach is to pass all parameters by value as arguments to the function that uses them. Another approach is to call an update function that reads parameters from memory at the beginning of the function. A third option is to use thread-safety mechanisms such as locks or mutexes to prevent parameter updates while critical sections of the function are executing.

The reference implementation assumes a runtime capable of performing floating-point arithmetic, either natively through a floating-point unit or via emulation. Established methods exist for porting floating-point implementations to fixed-point architectures. We therefore do not delve further into this topic, but refer the interested reader to the introduction provided in One important aspect concerns how signals and parameters are passed to the controller, and how the computed control signal is actuated. In our reference implementation, signals are passed as arguments to the control and filter functions (see code:control and code:filter), while parameters (orange) and state variables (pink) are assumed to be provided through some unspecified mechanism.

It should be noted that the distinction between signals and parameters is not always clear-cut. For example, modecould just as well be regarded as a parameter. We deliberately refrain from prescribing how values are passed, since this depends on programming language and runtime environment.

In an object-oriented setting, it is natural to define a PID object with control and filter methods, together with appropriate constructors for initialisation, as the Matlab and Python implemenations provided in our GitHub repository [PIDcodeGithub]. However, the proposed algorithms can equally well be implemented without object-oriented constructs. For this reason, we focus on the algorithmic structure rather than on software architectural details.

### Control mode

The control mode key function is to allow the PID user or operator to switch the controller on or off, which is labeled automatic ("AUTO") and manual ("MAN"), respectively. As described in sec:manauto, the controller can be in tracking mode when the calculated control signal is not applied but the controller tracks another signal.

There is a risk that the controller defaults to automatic mode on lineline:intstart if mode holds a value other than "MAN" or "TRACK". This risk can be eliminated by introducing the fourth mode `Disabled'. The `Disabled' mode means that the control signal $u$is neither calculated nor applied.

While strings are used to encode the modes in code:control and in our code at GitHub, it may be preferable to use numeric macros in a real implementation. For example, with a two-digit binary number, the following modes could be defined:

- 0b01: Manual (corresponding to "MAN"), - 0b11: Tracking (corresponding to "TRACK").

This provides a memory-efficient encoding.

### Basic closed-loop simulation

To illustrate how the code can be used for simulation purposes, code:basicloop shows the code for a basic control loop. Note that the simulation codes for this as well as the the examples in sec:basicexamples are available on GitHub.

The PID controller parameters, saturation limits, rate limits, sampling time, and filter time constant are set in lines 1 and 2, and the PID controller is created based on those parameters in code line 3. After that, the initial values for the different signals are given in line 4, also setting the controller mode to "AUTO". Then, these values are used in code line 5 to initialise the PID controller states by calling the initialization function according to the ideas described in sec:initialisation.

The control loop for a given simulation time Tsim is defined from code lines 6 to 17. Inside the loop, code line 11 simulates the process dynamics, a set-point change is configured in code lines 7-9, the process output is filtered in code line 12 using the filter function, and the controller action is calculated in code line 13 by calling the control function. The calculated control signal is sent to the plant in line 15, and loop waits for the next sampling time instant in code line 13. Unless otherwise stated, the initial conditions defined in lines 1-5 of code:basicloop are used as default values for all examples presented in the example of sec:basicexamples, and only the specific modifications are described in the corresponding sections. caption=Basic control loop., label=code:basicloop]code/basic\_loop.txt

## Simulation examples

This section presents seven simulation examples to show how the proposed code handles the different implementation features discussed in sec:features. The first three examples deal with switching between automatic and manual mode, switching the integral action on and off, and showing the effect of rate limitation, respectively. The fourth example is focused on analyzing the combination of the PID controller with a feed-forward compensator and different solutions to treat the control signal saturation problem. The measurement noise filtering capabilities are presented in the fifth example. Finally, the last two examples demonstrate the use of the basic PID functionality for the cases that involve tracking a control signal, in particular gain scheduling and selector/override control.

For most of the simulation examples, a first-order plus deadtime process model with transfer function is used and controlled with a PI-controller tuned using the Lambda method with $\lambda=T=1$, resulting in the controller C(s) &= K\left(1+\frac{1}{sT_i}\right)=0.667\left(1+\frac{1}{s}\right) = k_p+k_i\frac{1}{s}=0.667 + 0.667\frac{1}{s}.

When different process dynamics or controller parameters are required for some particular example, new information will be provided.

### Example 1: Man/Auto switching

In the proposed simulation, the system starts in manual mode at the beginning of the simulation and then switches to automatic mode in the middle of the simulation time. fig:example1 shows a simulation for this example in which the system starts in manual mode from $t=0$ to $t=10$, with a step control signal change from $u_{\text{man}}=0$ to $u_{\text{man}}=1$ at $t=1$, and switches from manual to automatic mode at time $t=10$. The set-point is fixed to $r=3$from the beginning of the simulation. As observed, the switch between manual and automatic mode is performed properly, and there is no bump at the switching time.

Switching from manual to automatic mode in Example sec:example1. code:example1 shows the control loop code for this example. Before simulating the control loop, the following changes must be done in the initialisation section for parameters and states: kp=0.667, ki=0.667, and kd=0.0, mode="MAN", and r=3. As observed, the step control signal change for manual mode is done in code lines 3-5 setting uman=1, while the switch between manual and automatic modes is performed in code lines 6-8 setting mode="AUTO". caption=Example 1 code., label=code:example1]code/Examples/Example1\_new.txt

### Example 2: P- or PD-control, and rate limitation

This example shows how the proposed code can be used to implement P- or PD-controllers, that is, controllers without integral action. The rate limitation function is also illustrated. We use the process and controller given by eq:P and eq:C. For the P-controller the integral gain is set to $k_i=0$ and the bias term $u_0$ is introduced with $u_0=2$. fig:example2 shows the simulation results for this example.

Switching between PI- and P-control in Example sec:example2.

The simulation starts using the PI-controller for an operating point given by $y=1$ and $u=1$, and with a setpoint change from $r=1$ to $r=3$ at $t=1$. $t=10$, the controller is switched to a P-controller by setting $k_i=0$. Since the control error is zero at time $t=10$, the control signal will jump down to the bias term $u_0=2$, and stay there until the process delay has elapsed. The P-controller will then control the process variable to a new position, but since there is no integral action there will be a control error. $t=15$, another setpoint change is made, from $r=3$ to $r=1$. The P-controller behaves as expected, and the two setpoint responses are similar, showing that the transitions from PI to P works well. $t=21$we switch back to a PI-controller and the control error is eliminated, obtaining a bumpless transfer response.

For this example, the simulation code is not shown since it is similar to the code used in code:example1. The manual part in code:example1 is removed, the variable ki is set to ki=0 at time $t=10$ to introduce the P-controller, and it is set to ki=0.667 at $t=21$ to go back to the PI-controller again. At $t=1$ and $t=15$ setpoint changes are introduces by setting r=3 and r=1, respectively, in a similar way as shown in code:basicloop in code lines 15-18. Moreover, the following changes are required at the initialisation section: y=1.0, u=1.0, u0=2.0, r=1.0, and mode="AUTO".

This example is also used to evaluate the rate limitation option. fig:example2\_rate\_limitation shows the same simulation results presented in fig:example2 but for a rate limit of 0.1, which also corresponds to the sampling time used for this simulation. As observed at time instants $t=1$, $t=10$, and $t=15$, the changes of the control signal are now limited and thus a slower response is obtained according to the rate limitation imposed. For this simulation, rate limitation variables must be modified in the code by setting dumin=-0.1 and dumax=0.1in the initialisation section.

Rate limitation effect in Example sec:example2 for dumin=-0.1 and dumax=0.1.

### Example 3: Setpoint handling

As discussed in sec:setpoint, the code proposed in this paper include the capabilities for setpoint handling to obtain a smoother control signal when strong changes of setpoints (like step changes) are required.

To show this idea, in this example we use the process and controller given by As the aim of this example is to show the effect of the $b$ parameter on the responses of the control system, fig:example3 shows the simulation results for the cases with $b=0$, $b=0.5$, and $b=1$. As observed, the smother control signal is obtained for the case with $b=0$ and the more aggressive control signal for $b=1$. The $b$ factor will of course also influence the process variable response, where the slower and faster responses are obtained for $b=0$ and $b=1$, respectively. fig:example3 also shows the effect to the disturbance rejection for a step-like disturbance signal of amplitude 1 entering in the control signal at time $t=10$. As expected, identical responses are obtained for any value of $b$, as the setpoint handling is decoupled of the disturbance rejection problem.

For this example, the simulation code is not shown as it is the same code as used in code:example1 skipping the manual part at the beginning of the simulation and using different values for the $b$parameter.

Setpoint handling in Example sec:example3.

### Example 4: Feed-forward and saturation

This example focuses on analyzing the anti-windup solutions discussed in sec:windup for the control signal saturation problem, and also the combination of the PID controller with a feed-forward compensator to deal with measurable disturbances. The effect of anti-windup clamping and tracking solutions implemented in code:control will be analyzed and compared. Moreover, the capability of the new PID code that includes the feed-forward control signal inside the PID controller will also be explored. Notice that in classical implementations, the contribution of the feed-forward compensator is added to the output of the PID controller outside the controller code [guz+hagg2024], and in the proposed code the feed-forward control signal is considered part of the PID controller (see sec:FF).

For this example, the following process models are used: where $P_u$ represents the dynamics that relates the control signal with the process output and $P_v$represents the dynamics that relates the load disturbance with the process output.

In this case, a PID controller was designed using the Pade approximation for the time delay and using the Lambda method with $\lambda=0.3$, resulting in $K=2.83$, $T_i=3.25$ and $T_d=0.23$. The control signal limits are $u_{\min}=-3$ and $u_{\max}=3$, and the feed-forward compensator is designed as in the classical manner by dividing $P_v$ over $P_u$ with reversed sign: fig:example4 shows the simulation results for this example, where the cases without saturation limits (No saturation) and with saturation limits but without using anti-windup techniques (No anti-windup) are included for a better comparison. The simulation starts with a large set-point change from $r=0$ to $r=4.5$ at $t=1$. Then, the set-point value is set again to $r=0$ at $t=20$ and a step-like change is also included for the load disturbance from $v=0$ to $v=1.5$ at $t=45$. Notice that for the no-saturation case, the desired closed-loop response is perfectly achieved for the set-point changes, and the effect of the disturbance is completely removed. When actuator saturation is taken into account, differences among the evaluated strategies become evident. Between $t = 1$ and $t = 20$, following the first set-point change, no noticeable differences are observed, since the control signal in all simulated cases exceeds the saturation limit. However, after the second step change at $t = 20$, the impact for the no anti-windup case becomes apparent. In this case, the system performance is significantly degraded, as the controller requires a longer time to exit the saturation region and reach the new set-point due to the windup effect. The performance is also significantly degraded in the disturbance rejection scenario, where an undesirable overshoot is observed in the response due to the same underlying cause.

Feed-forward plus saturation in Example sec:example4.

When clamping and back calculation anti-windup techniques are used, the responses are improved in different manners, as observed in the dashed-line and black solid-line curves for clamping and back calculation cases, respectively. As commented in sec:windup, the PID code is the same for both techniques only changing the value of $T_t$, with $T_t=\Delta t=0.01$ for clamping and $T_t=T_i=3.25$ for back calculation in this example. When clamping is used, the saturation time is dramatically reduced as observed in the control signal plot. It can be seen that the control signal leaves the saturation quickly for both the tracking and disturbance rejection responses. However, this advantage from a saturation point of view results in a slow response at the process output for set-point tracking and disturbance rejection, as observed in the process output plot. On the other hand, when anti-windup back calculation is used, the saturation time is only slightly reduced, but the performance on the process output for set-point tracking and disturbance rejection cases is much closer to the ideal response without saturation limits. As discussed in sec:windup, in this paper a third anti-windup approach is proposed as a combination of clamping and tracking. fig:example4\_b shows the same previous example, where clamping, back calculation, and the combined solution (named Combined solution in the figure) are compared. As observed, an intermediate behavior is obtained in this case, where for set-point tracking the result is similar to the clamping solution, and for the disturbance rejection problem it is closest to the tracking solution. The main advantage of this third solution is that the calculated control signal is dynamically adjusted so that the saturation error decays exactly as a first-order process with a time constant $T_t$, whenever the control signal is saturated.

Thus, three different anti-windup options are available to deal with the saturation problem, clamping allowing to leave the saturation very fast but slowing down the process output response; back calculation allowing to obtain a trade-off between saturation time and process output performance; and the combination of the two approaches providing an intermediate behavior according to the trade-off between saturation time and process output performance. Therefore, the user can choose between these two solutions depending on each control problem.

Feed-forward plus saturation in Example sec:example4 comparing anti-windup techniques.

### Example 5: Noise filtering

An interesting feature of the implementation presented in this work is that measurement noise filtering is suggested to be combined with the PID controller, as described in sec:filter.

Noise filtering in Example sec:example5.

This example shows how the control signal can be properly filtered by tuning the $T_f$ parameter as input to the filter function. The process transfer function and PI-controller given by eq:P and eq:C, respectively, have been used for this simulation, where a white noise signal was added to the process output. fig:example5 shows the simulation result for three cases: without filter, corresponding to $T_f=0$, and with filter for $T_f=0.01T_i$ and $T_f=0.1T_i$, respectively. The simulation starts with the controller in manual mode with $u=0$. The setpoint is change from $r=0$ to $r=3$ at $t=1$. At time $t=1.25$the controller is switched to automatic mode.

As observed in the bottom plot, for the case with $T_f=0.01T_i$, the original control signal is mainly kept and only the very high frequency components of the signal are filtered. For the case with $T_f=0.1T_i$, the original control signal is highly filtered by cutting off high- and low-frequency components. Notice that for all three cases, almost the same process output responses are obtained, which means that the filter is mainly affecting only the control signal.

### Example 6: Gain scheduling

This example shows how to use the proposed code for the implementation of gain-scheduling approaches. We consider the classical tank level control problem, which process dynamics is given by the following differential equation: $$\frac{dy(t)}{dt}=-\frac{a}{A}\sqrt{2gy(t)}+\frac{u(t)}{A},$$ where $y$ is the tank level, $u$ is the inlet flow, $g=983$ $cm/s^2$ is the gravity constant, $a=2.15$ $cm^3$ is the cross section of the outlet hole, and $A=390$ $cm^2$is the cross section of the tank.

Since the process is nonlinear, it is divided into three different operating zones, where a linear model approximation is derived in each zone. The following three operating points are considered for this study: In each zone, the process is modeled as The model parameters are given in tab:gainscheduling.

Process and controller parameters for the gain scheduling Example sec:example6.

| | Zone 1 | Zone 2 | Zone 3 | The gain-scheduling control scheme can be implemented in two different ways: by running all the controllers in parallel and switching among them based on the current operating point; or by using a single controller and updating its parameters based on the current operating point. Both solutions have been used in this example, and code:example6a and code:example6b show the corresponding codes for the multiple controllers and single controller case, respectively. Notice that the initialisation of the variables was omitted and only the control loop is presented. In both cases, the set-point is initialised with a value of $r=22$ cm, and the process is initialised with a value of $y=4$ $cm$ and $u=190.66$ $cm^3/s$.

When using multiple controllers as presented in code:example6a, the key point is to correctly manage the mode status of the controllers, as observed from code lines 6-21. Once the corresponding controller is selected to be active ("mode=AUTO"), the rest of the controllers must be in tracking mode, and thus the corresponding variables mode must be set to "TRACK". Moreover, the tracking signal for all the controllers must be the actual input to the process in order to ensure bumpless transfer when switching among the controllers (see code line 22). In the case of using a single controller as presented in code:example6b, the key point is the adaptation of the controller parameters according to the corresponding operating point observed in code lines 4-16. Notice that in this case, the controller mode is set to "AUTO"since the beginning of the simulation.

Both implementations provide identical results. fig:example6shows the simulation results for both cases where the setpoint was changed along the operating points to force the switching among the different controllers. As observed, the same results are obtained in both implementations and the curves in the two upper plots overlap. It can also be seen how the same closed-loop behavior is obtained despite the changes on the operating range. Moreover, note that no bumps are observed in the control signal at the switching moments. The lower plot shows the number of active controllers, representing the switching state.

Gain scheduling control results for the tank level control problem in Example sec:example6 for codes code:example6a and code:example6b. caption=Parallel controllers in Example sec:example6., label=code:example6a]code/Examples/Example6a\_new.txt caption=Single controller in Example sec:example6., label=code:example6b]code/Examples/Example6b\_new.txt

### Example 7: Selector or override control

This is an example that shows how to handle the tracking state when using a selector control approach. The important thing here is to keep the P-part of the controllers as we need their current P-contribution to properly select (for instance, with MIN or MAX selectors) the current control signal.

To analyze this case, we use the example proposed in fig:selector\_scheme.

Selector control scheme The process has one input signal $u$ and two output variables, $y_1$ and $y_2$. The two output variables are input signals to the two controllers $C_1$ and $C_2$. Only one of the controllers is active at a time, in this case the controller with the smallest control signal. The control signal corresponding to the non-active controller is tracking the active control signal.

This structure is common for handling security constraints. One of the controllers is working in normal operation, but when a certain process variable becomes too small or too large, the other controller takes over, overrides, to ensure that the constraint is not violated. $P_1=P_2$ and $C_1=C_2$, where we use the process and controller given by eq:P and eq:C. The setpoint values are $r_1=0.3$ and $r_2=0.5$. fig:example7 shows the simulation results for this example. A disturbance signal $v$ is added to the input of $P_1$ to generate variations in the operating conditions. The graphic at the bottom represents the disturbance signal $v$. As observed from the third graphic from top (representing $u_1-u_2$), the MIN selector works properly. The active control signal is always the smallest one. Moreover, the controller which is in tracking state calculates the control signal as the current control signal plus its P-part.

Simulation results for the selector control scheme in Example sec:example7 and for code code:example7. code:example7 shows the code in which the handling of the tracking mode signals is observed based on the selector choice. As happened for the use of parallel controllers in Example [sec:example6], the tracking signal for the two controllers must be the actual input to the process to ensure bumpless transfer when switching among the controllers (see code line 15). caption=Simulation code for selector control approach., label=code:example7]code/Examples/Example7.txt

## Conclusions

This paper can be used as a practical guide to understand and implement a PID controller in a software environment. The proposed reference implementation is intended to be used as a standard for many applications from the process industry to medical, aeronautical and automotive applications. The contribution lies in the consideration of practical problems that will be encountered when dealing with real-world problems, all of which have been carefully considered and addressed.

The contribution further lies in the discussion of several simulated examples where the different features are tested in closed loop.

While we expect that small adjustments will have to be made for most applications, we believe that this reference implementation closes the book on PID implementation of the basic form and opens the next when comparing advanced control strategies. In particular, feed-forward control as well as strategies requiring tracking such as selectors or override, gain scheduling and cascade control can be studied in different ways.

We hope that this implementation will also make the use of advanced strategies more popular as these rely on the correct basic implementation, which is not always given in industrial settings.
