Theano: A Python Framework for Fast Computation of Mathematical Expressions

Theano is a Python library that allows to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. Since its introduction, it has been one of the most used CPU and GPU mathematical compilers - especially in the machine learning community - and has shown steady performance improvements. Theano is being actively and continuously developed since 2008, multiple frameworks have been built on top of it and it has been used to produce many state-of-the-art machine learning models. The present article is structured as follows. Section I provides an overview of the Theano software and its community. Section II presents the principal features of Theano and how to use them, and compares them with other similar projects. Section III focuses on recently-introduced functionalities and improvements. Section IV compares the performance of Theano against Torch7 and TensorFlow on several machine learning models. Section V discusses current limitations of Theano and potential ways of improving it.

## Abstract

Theano is a Python library that allows to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. Since its introduction in Bergstra *et al.* it has been one of the most used CPU and GPU mathematical compilers -- especially in the machine learning community Bergstra *et al.* -- and has shown steady performance improvements Bastien *et al.*. Theano is being actively and continuously developed since 2008, multiple frameworks have been built on top of it and it has been used to produce many state-of-the-art machine learning models.

The present article is structured as follows. Section I provides an overview of the Theano software and its community. Section II presents the principal features of Theano and how to use them, and compares them with other similar projects. Section III focuses on recently-introduced functionalities and improvements. Section IV compares the performance of Theano against Torch7 Collobert *et al.* and TensorFlow Abadi *et al.* on several machine learning models. Section V discusses current limitations of Theano and potential ways of improving it.

## Limitations and challenges

Despite the progress made in recent years and our best efforts, there remain some limitations or shortcomings in Theano. Some of these issues have been addressed by competing frameworks mentioned in Section II.5, and by other projects like CGT (Computation Graph Toolkit).^1818^18

## Limitations from Python

Since Theano uses Python as its core language, and uses NumPy arrays and other Python objects to store values, it is affected by Python's limitations. The main one is the Python GIL, that limits concurrent execution of threads. We have seen that it is possible to make single-threaded execution fast by compiling binary modules that are then loaded in Python (Sections II.2.3 and II.3), and it would also be possible to release the GIL during the execution of these functions. However, the GIL has to be acquired again each time references to Python objects are added or removed, when using the C API of Python and NumPy.
