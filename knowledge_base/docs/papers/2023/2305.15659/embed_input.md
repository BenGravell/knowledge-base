How to Escape Sharp Minima with Random Perturbations

Modern machine learning applications have witnessed the remarkable success of optimization algorithms that are designed to find flat minima. Motivated by this design choice, we undertake a formal study that (i) formulates the notion of flat minima, and (ii) studies the complexity of finding them. Specifically, we adopt the trace of the Hessian of the cost function as a measure of flatness, and use it to formally define the notion of approximate flat minima. Under this notion, we then analyze algorithms that find approximate flat minima efficiently. For general cost functions, we discuss a gradient-based algorithm that finds an approximate flat local minimum efficiently. The main component of the algorithm is to use gradients computed from randomly perturbed iterates to estimate a direction that leads to flatter minima. For the setting where the cost function is an empirical risk over training data, we present a faster algorithm that is inspired by a recently proposed practical algorithm called sharpness-aware minimization, supporting its success in practice.

## Introduction

In modern machine learning applications, the training loss function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ to be optimized often has a continuum of local/global minima, and the central question is which minima lead to good prediction performance. Among many different properties for minima, "flatness" of minima has been a promising candidate extensively studied in the literature (Hochreiter and Schmidhuber Keskar et al. Dinh et al. Dziugaite and Roy Neyshabur et al. Sagun et al. Yao et al. Chaudhari et al. He et al. Mulayoff and Michaeli Tsuzuku et al. Xie et al., ).

Recently, there has been a resurgence of interest in flat minima due to various advances in both empirical and theoretical domains. Motivated by the extensive research on flat minima, this work undertakes a formal study that

delineates a clear definition for flat minima, and

studies the upper complexity bounds of finding them.
