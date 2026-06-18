<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Swing-up Control of Inverted Pendulum Using Pseudo-State Feedback

Topics include Inverted pendulum, Swing-up control, Nonlinear control, Bang-bang control, Robust control, Underactuated systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes a robust swing-up controller for an inverted pendulum using a projected pseudo-state rather than a purely feedforward optimal trajectory. The method partitions the pseudo-state to produce a bang-bang input and demonstrates the controller experimentally on the TI Tech pendulum, helping establish swing-up as a benchmark nonlinear control problem.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Swing-up control, that is the transfer of a pendulum from a pendant state to the inverted one, is a good laboratory experiment of optimal control theory for non-linear control systems. The optimal control can be determined by the maximum principle and obtained as a function of time. Since the control is, however, determined in a feedforward fashion, the control is not robust to disturbances and uncertainties of the system, and the transfer of the state of the pendulum is not assured. In the paper, a robust swing-up control using a subspace projected from the whole state space is proposed. Based on the projected state space or pseudo-state, the control input is determined depending on the partitioning of the state as a bang-bang type control. The control algorithm is applied for a new type of pendulum (TI Tech pendulum), and the effectiveness and robustness of the proposed control are examined by experiments.
