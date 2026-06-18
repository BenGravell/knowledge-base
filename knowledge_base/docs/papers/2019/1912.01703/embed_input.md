PyTorch: An Imperative Style, High-Performance Deep Learning Library

Topics include Deep learning, Benchmarks, Control, Learning, PyTorch, Programming style.

Deep learning frameworks have often focused on either usability or speed, but not both. PyTorch is a machine learning library that shows that these two goals are in fact compatible: it provides an imperative and Pythonic programming style that supports code as a model, makes debugging easy and is consistent with other popular scientific computing libraries, while remaining efficient and supporting hardware accelerators such as GPUs. In this paper, we detail the principles that drove the implementation of PyTorch and how they are reflected in its architecture. We emphasize that every aspect of PyTorch is a regular Python program under the full control of its user. We also explain how the careful and pragmatic implementation of the key components of its runtime enables them to work together to achieve compelling performance. We demonstrate the efficiency of individual subsystems, as well as the overall speed of PyTorch on several common benchmarks.

## Introduction

With the increased interest in deep learning in recent years, there has been an explosion of machine learning tools. Many popular frameworks such as Caffe, CNTK, TensorFlow, and Theano, construct a static dataflow graph that represents the computation and which can then be applied repeatedly to batches of data. This approach provides visibility into the whole computation ahead of time, and can theoretically be leveraged to improve performance and scalability. However, it comes at the cost of ease of use, ease of debugging, and flexibility of the types of computation that can be represented.

Prior work has recognized the value of dynamic eager execution for deep learning, and some recent frameworks implement this define-by-run approach, but do so either at the cost of performance (Chainer ) or using a less expressive, faster language (Torch, DyNet ), which limits their applicability.

However, with careful implementation and design choices, dynamic eager execution can be achieved largely without sacrificing performance. This paper introduces PyTorch, a Python library that performs immediate execution of dynamic tensor computations with automatic differentiation and GPU acceleration, and does so while maintaining performance comparable to the fastest current libraries for deep learning. This combination has turned out to be very popular in the research community , for instance, 296 ICLR 2019 submissions mentioning PyTorch.

## Design principles

PyTorch's success stems from weaving previous ideas into a design that balances speed and ease of use.

## Conclusion and future work

PyTorch has become a popular tool in the deep learning research community by combining a focus on usability with careful performance considerations. In addition to continuing to support the latest trends and advances in deep learning, in the future we plan to continue to improve the speed and scalability of PyTorch. Most notably, we are working on the PyTorch JIT: a suite of tools that allow PyTorch programs to be executed outside of the Python interpreter where they can be further optimized.
