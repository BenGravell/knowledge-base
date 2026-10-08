<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Receding Horizon Control of Nonlinear Systems: A Control Lyapunov Function Approach

Topics include Nonlinear model predictive control, Control Lyapunov functions, Stability, Region of attraction, Trajectory generation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops stability and region-of-attraction guarantees for nonlinear receding-horizon control with control Lyapunov terminal costs, and applies trajectory morphing to aggressive ducted-fan maneuvers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

With the advent of faster and cheaper computers, optimization based control methodologies have become a viable candidate for control of nonlinear systems. Over the past twenty years, a group of such control schemes have been successfully used in the process control industry where the processes are either intrinsically stable or have very large time constants. The purpose of this thesis is to provide a theoretical framework for synthesis of a class of optimization based control schemes, known as receding horizon control techniques for nonlinear systems such as unmanned aerial vehicles. It is well known that unconstrained infinite horizon optimal control may be used to construct a stabilizing controller for a nonlinear system. In this thesis, we show that similar stabilization results may be achieved using unconstrained finite horizon optimal control. The key idea is to approximate the tail of the infinite horizon cost-to-go using, as terminal cost, an appropriate control Lyapunov function (CLF). A CLF can be thought of as generalization of the concept of a Lyapunov function to systems with inputs. Roughly speaking, the terminal CLF should provide an (incremental) upper bound on the cost.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this fashion, important stability characteristics may be retained without the use of terminal constraints such as those employed by a number of other researchers. The absence of constraints allows a significant speedup in computation. Furthermore, it is shown that in order to guarantee stability, it suffices to satisfy an improvement property, thereby relaxing the requirement that truly optimal trajectories be found. We provide a complete analysis of the stability and region of attraction/operation properties of receding horizon control strategies that utilize finite horizon approximations in the proposed class. It is shown that the guaranteed region of operation contains that of the CLF controller and may be made as large as desired by increasing the optimization horizon (restricted, of course, to the infinite horizon domain). Moreover, it is easily seen that both CLF and infinite horizon optimal control approaches are limiting cases of our receding horizon strategy. The key results are illustrated using a familiar example, the inverted pendulum, as well as models of the Caltech ducted fan at hover and forward flight, where significant improvements in guaranteed region of operation and cost are noted.

<!-- chunk {"id": "abstract-0005", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We also develop an optimization based scheme for generation of aggressive trajectories for hover and forward flight models of the Caltech ducted fan experiment, using a technique known as trajectory morphing. The main idea behind trajectory morphing is to develop a simplified model of the nonlinear system and solve the trajectory generation problem for that model. The resulting trajectory is then used as a reference in a receding horizon optimization scheme to generate trajectories of the original nonlinear system. Several aggressive trajectories are obtained in this fashion for the forward flight model of the Caltech ducted fan experiment.
