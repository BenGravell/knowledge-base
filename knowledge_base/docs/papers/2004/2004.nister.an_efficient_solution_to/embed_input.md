An Efficient Solution to the Five-Point Relative Pose Problem

Topics include Structure from motion, Relative pose, Essential matrix, Minimal solver, Calibrated cameras, Random sample consensus, Polynomial solver.

Provides a practical calibrated five-point relative-pose solver by reducing the minimal problem to a tenth-degree polynomial. The method became a standard minimal solver inside RANSAC-based structure-from-motion and visual-odometry systems.

An efficient algorithmic solution to the classical five-point relative pose problem is presented. The problem is to find the possible solutions for relative camera motion between two calibrated views given five corresponding points. The algorithm consists of computing the coefficients of a tenth degree polynomial and subsequently finding its roots. It is the first algorithm well suited for numerical implementation that also corresponds to the inherent complexity of the problem. The algorithm is used in a robust hypothesise-and-test framework to estimate structure and motion in real-time.
