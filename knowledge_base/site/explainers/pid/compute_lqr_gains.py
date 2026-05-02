"""
LQR gains for the cart-pole dual-PID controller.

Linearises the cart-pole dynamics at the upright equilibrium, then solves
the continuous-time LQR problem to find the optimal state-feedback gain K.

The resulting controller is:
    F = Kp*theta + Kd*thetadot + Kpx*x + Kdx*xdot

NOTE: the position gain Kpx is POSITIVE, meaning the force is applied in
the SAME direction as the cart position error.  This is counter-intuitive
but correct: pushing in the direction of x tips the pole toward the origin,
which the angle PID then corrects with a strong force that drags the cart
back.  A negative position gain (intuitive "push back") creates positive
feedback in the position loop and is unstable.
"""
import numpy as np
from scipy.linalg import solve_continuous_are

# ── System parameters (must match the JavaScript simulation) ──────────────────
M = 1.0    # cart mass (kg)
m = 0.1    # pole mass (kg)
l = 0.5    # pole half-length (m)
g = 9.81   # gravity (m/s²)

# ── Linearised dynamics at (x, xd, theta, thd) = (0, 0, 0, 0) ───────────────
alpha    = 1.0 / (l * (4/3 - m / (M + m)))
b_xadd  =  1/(M+m) + m*l*alpha / (M+m)**2   #  0.9756
b_thadd = -alpha / (M+m)                      # -1.4634

A = np.array([
    [0, 1,             0, 0],
    [0, 0, -m*l*alpha*g/(M+m), 0],
    [0, 0,             0, 1],
    [0, 0,       alpha*g, 0],
])
B = np.array([[0], [b_xadd], [0], [b_thadd]])

print("Linearised A:")
print(np.array2string(A, precision=4, suppress_small=True))
print(f"B: {B.T}")

rank = np.linalg.matrix_rank(
    np.hstack([B, A@B, A@A@B, A@A@A@B])
)
print(f"\nControllability rank: {rank}/4 -> {'fully controllable' if rank==4 else 'NOT controllable'}")

# ── LQR design ────────────────────────────────────────────────────────────────
# State cost weights: penalise position x and angle theta
# Control cost R: penalise large forces
Q = np.diag([1.0, 0.0, 10.0, 1.0])   # [x, xdot, theta, thetadot]
R = 0.1                                # force cost

P   = solve_continuous_are(A, B, Q, R)
K   = (1/R) * B.T @ P                 # F = -K @ state  (LQR convention)
K   = K.flatten()

# Translate: F = -K @ [x, xd, theta, thd]
#           = (-K[0])*x + (-K[1])*xd + (-K[2])*theta + (-K[3])*thd
Kpx = -K[0];  Kdx = -K[1]   # position gains (will be positive)
Kp  = -K[2];  Kd  = -K[3]   # angle gains (will be positive)

Acl  = A - B @ K.reshape(1, -1)
eigs = np.linalg.eigvals(Acl)

print("\n" + "=" * 55)
print("LQR result  (Q = diag(1,0,10,1),  R = 0.1)")
print("=" * 55)
print(f"  Angle:    Kp = {Kp:.2f},  Kd = {Kd:.2f}")
print(f"  Position: Kpx = {Kpx:.2f},  Kdx = {Kdx:.2f}")
print(f"  Closed-loop eigenvalues: {[f'{e.real:.3f}{e.imag:+.3f}j' for e in eigs]}")
print(f"  Stable: {all(e.real < 0 for e in eigs)}")

print()
print("=" * 55)
print("JavaScript constants (paste into pid.md):")
print("=" * 55)
print(f"  var PRESET_KP   = {round(Kp,  1)};")
print(f"  var PRESET_KI   = 0.0;")
print(f"  var PRESET_KD   = {round(Kd,  1)};")
print(f"  var PRESET_KP_X = {round(Kpx, 1)};")
print(f"  var PRESET_KI_X = 0.0;")
print(f"  var PRESET_KD_X = {round(Kdx, 1)};")
