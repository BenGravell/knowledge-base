Gen3DSR: Generalizable 3D Scene Reconstruction via Divide and Conquer from a Single View

Single-view 3D reconstruction is currently approached from two dominant perspectives: reconstruction of scenes with limited diversity using 3D data supervision or reconstruction of diverse singular objects using large image priors. However, real-world scenarios are far more complex and exceed the capabilities of these methods. We therefore propose a hybrid method following a divide-and-conquer strategy. We first process the scene holistically, extracting depth and semantic information, and then leverage an object-level method for the detailed reconstruction of individual components. By splitting the problem into simpler tasks, our system is able to generalize to various types of scenes without retraining or fine-tuning. We purposely design our pipeline to be highly modular with independent, self-contained modules, to avoid the need for end-to-end training of the whole system. This enables the pipeline to naturally improve as future methods can replace the individual modules. We demonstrate the reconstruction performance of our approach on both synthetic and real-world scenes, comparing favorable against prior works.

## Introduction

Single-view 3D scene reconstruction refers to the problem of understanding and explaining all the visible components that assembled together create a 3D scene which closely reproduces the original 2D observation. The computer vision and graphics communities have long been interested in automating this task, yet its complexity still leaves room for many improvements. Successful single-view applications have been developed for specific purposes such as face reconstruction and hair modeling.

In general, even reconstructing one 3D object from a single image is a severely ill-posed problem, *e.g*. it is impossible to tell precisely how the back side of an object looks like if the input image only observes the front. Nonetheless, if the distribution of objects that are naturally present in our day-to-day lives is known, one can plausibly predict the shape and appearance of a 3D object from very limited information. Accordingly, various priors have been used in the context of particular object classes (such as simple shapes, or human faces ). However, modeling entire scenes is a significantly more challenging problem.

We develop the connecting links for integrating individually reconstructed 3D objects into the scene layout by exploiting single-view depth estimation.

We achieve an unmatched level of generalizability for real-world single-view 3D scene reconstruction, which we demonstrate through extensive evaluations.

## Limitations

The proposed method has certain shortcomings and there is significant room for improvement, especially for in-the-wild predictions. By design, the failure cases of the individual modules (depth estimation, camera calibration, elevation estimation, etc.) become limitations of our framework. Since we do not train an end-to-end system, errors can propagate from one stage to the next. Therefore, the performance of the overall pipeline is limited by its weakest link.

We believe that most of the current limitations can be overcome by improving the implementation of some of the particular modules in our framework and by enhancing their interoperability: using estimated depth in 3D object reconstruction or global image context for amodal completion. We further discuss the method's limitations and provide concrete examples in the Section of the supplementary material.
