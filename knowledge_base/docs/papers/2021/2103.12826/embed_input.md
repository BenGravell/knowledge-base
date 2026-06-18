Robowflex: Robot Motion Planning with MoveIt Made Easy

Robowflex is a software library for robot motion planning in industrial and research applications, leveraging the popular MoveIt library and Robot Operating System (ROS) middleware. Robowflex provides an augmented API for crafting and manipulating motion planning queries within a single program, making motion planning with MoveIt easy. Robowflex's high-level API simplifies many common use-cases while still providing low-level access to the MoveIt library when needed. Robowflex is particularly useful for 1) developing new motion planners, 2) evaluating motion planners, and 3) complex problems that use motion planning as a subroutine (e.g., task and motion planning). Robowflex also provides visualization capabilities, integrations to other robotics libraries (e.g., DART and Tesseract), and is complementary to other robotics packages. With our library, the user does not need to be an expert at ROS or MoveIt to set up motion planning queries, extract information from results, and directly interface with a variety of software components. We demonstrate its efficacy through several example use-cases.

## Introduction

A core component of any autonomous system is *motion planning*, which finds feasible motions that satisfy task requirements (e.g., reaching the goal, satisfying some motion constraint, etc.). There are many motion planning software system for general manipulators; a popular library for motion planning is MoveIt, which is built on top of the ubiquitous Robot Operating System (ros) framework....

This paper introduces *Robowflex*, a software library designed to simplify the use of MoveIt for industrial and research applications of motion planning. *Robowflex* is a high-level api to easily manipulate robots, collision environments, planning requests, and motion planners. *Robowflex* "wraps" the underlying MoveIt library within a c++ interface that provides many utilities that simplify the use and evaluation of motion planners. Moreover, *Robowflex* provides direct access to the implementation (that is, not through ros messaging)....

## Discussion

We have presented *Robowflex*, a c++ library that enables the use of MoveIt in an easier, more flexible way for the creation of advanced robot software for industry, research, and education. The core advantage that *Robowflex* provides over the default distribution of MoveIt is the ability to easily access and modify core data structures within the program itself, rather than through ros messages to the provided MoveGroup program. This also enables the use of motion planning within more complex algorithms, such as task and motion planning approaches....

Note that many scenes can be loaded simultaneously, can be copied and modified, and saved and loaded to and from disk.

Many ros programs rely on the parameter server, a distributed key-value store available in ros. As a result, it is sometimes difficult to have multiple programs running simultaneously that require similar parameters, leading to issues with managing namespaces. By default, *Robowflex* uses an anonymous namespace so that many instances of *Robowflex* code can simultaneously run. Moreover, there is support to load yaml files onto the parameter server, which is typically only available through ros launch, making it easy to have scripts load their parameters.

The *Robowflex* dart module provides an alternative to MoveIt, by modeling robots and scenes in the dart framework with bidirectional conversion to/from MoveIt constructs....
