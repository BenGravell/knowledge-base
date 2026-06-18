<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PyTorch: An Imperative Style, High-Performance Deep Learning Library

Topics include Deep learning, Benchmarks, Control, Learning, PyTorch, Programming style.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep learning frameworks have often focused on either usability or speed, but not both. PyTorch is a machine learning library that shows that these two goals are in fact compatible: it provides an imperative and Pythonic programming style that supports code as a model, makes debugging easy and is consistent with other popular scientific computing libraries, while remaining efficient and supporting hardware accelerators such as GPUs. In this paper, we detail the principles that drove the implementation of PyTorch and how they are reflected in its architecture. We emphasize that every aspect of PyTorch is a regular Python program under the full control of its user. We also explain how the careful and pragmatic implementation of the key components of its runtime enables them to work together to achieve compelling performance. We demonstrate the efficiency of individual subsystems, as well as the overall speed of PyTorch on several common benchmarks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

With the increased interest in deep learning in recent years, there has been an explosion of machine learning tools. Many popular frameworks such as Caffe, CNTK, TensorFlow, and Theano, construct a static dataflow graph that represents the computation and which can then be applied repeatedly to batches of data. This approach provides visibility into the whole computation ahead of time, and can theoretically be leveraged to improve performance and scalability. However, it comes at the cost of ease of use, ease of debugging, and flexibility of the types of computation that can be represented.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior work has recognized the value of dynamic eager execution for deep learning, and some recent frameworks implement this define-by-run approach, but do so either at the cost of performance (Chainer ) or using a less expressive, faster language (Torch, DyNet ), which limits their applicability.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, with careful implementation and design choices, dynamic eager execution can be achieved largely without sacrificing performance. This paper introduces PyTorch, a Python library that performs immediate execution of dynamic tensor computations with automatic differentiation and GPU acceleration, and does so while maintaining performance comparable to the fastest current libraries for deep learning. This combination has turned out to be very popular in the research community, for instance, 296 ICLR 2019 submissions mentioning PyTorch.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Design principles", "weight": 1.0} -->

PyTorch's success stems from weaving previous ideas into a design that balances speed and ease of use.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Design principles", "weight": 1.0} -->

Be Pythonic Data scientists are familiar with the Python language, its programming model, and its tools. PyTorch should be a first-class member of that ecosystem. It follows the commonly established design goals of keeping interfaces simple and consistent, ideally with one idiomatic way of doing things. It also integrates naturally with standard plotting, debugging, and data processing tools.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Design principles", "weight": 1.0} -->

Put researchers first PyTorch strives to make writing models, data loaders, and optimizers as easy and productive as possible. The complexity inherent to machine learning should be handled internally by the PyTorch library and hidden behind intuitive APIs free of side-effects and unexpected performance cliffs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Design principles", "weight": 1.0} -->

Provide pragmatic performance To be useful, PyTorch needs to deliver compelling performance, although not at the expense of simplicity and ease of use. Trading 10% of speed for a significantly simpler to use model is acceptable; 100% is not. Therefore, its *implementation* accepts added complexity in order to deliver that performance. Additionally, providing tools that allow researchers to manually control the execution of their code will empower them to find their own performance improvements independent of those that the library provides automatically.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Design principles", "weight": 1.0} -->

Worse is better Given a fixed amount of engineering resources, and all else being equal, the time saved by keeping the internal implementation of PyTorch simple can be used to implement additional features, adapt to new situations, and keep up with the fast pace of progress in the field of AI. Therefore it is better to have a simple but slightly incomplete solution than a comprehensive but complex and hard to maintain design.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Deep learning models are just Python programs", "weight": 1.0} -->

In a surprisingly short amount of time, machine learning grew from recognizing individual digits into autonomously playing StarCraft. Consequently, the neural networks themselves evolved rapidly from simple sequences of feed forward layers into incredibly varied numerical programs often composed of many loops and recursive functions. To support this growing complexity, PyTorch foregoes the potential benefits of a graph-metaprogramming based approach to preserve the imperative programming model of Python. This design was pioneered for model authoring by Chainer and Dynet. PyTorch extends this to all aspects of deep learning workflows. Defining layers, composing models, loading data, running optimizers, and parallelizing the training process are all expressed using the familiar concepts developed for general purpose programming.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Deep learning models are just Python programs", "weight": 1.0} -->

This solution ensures that any new potential neural network architecture can be easily implemented with PyTorch. For instance, layers (which in modern machine learning should really be understood as stateful functions with implicit parameters) are typically expressed as Python classes whose constructors create and initialize their parameters, and whose forward methods process an input activation. Similarly, models are usually represented as classes that compose individual layers, but let us state again that nothing forces the user to structure their code in that way. Listing 1 demonstrates how an entire model can be created by composing functionality provided by PyTorch such as 2d convolution, matrix multiplication, dropout, and softmax to classify gray-scale images. Note that linear layers are of course part of the library, but we show an example implementation to highlight how simple it is.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Deep learning models are just Python programs", "weight": 1.0} -->

[⬇](data:text/plain;base64,CmNsYXNzIExpbmVhckxheWVyKE1vZHVsZSk6CmRlZiBfX2luaXRfXyhzZWxmLCBpbl9zeiwgb3V0X3N6KToKc3VwZXIoKS5fX2luaXRfXygpCnQxID0gdG9yY2gucmFuZG4oaW5fc3osIG91dF9zeikKc2VsZi53ID0gbm4uUGFyYW1ldGVyKHQxKQp0MiA9IHRvcmNoLnJhbmRuKG91dF9zeikKc2VsZi5iID0gbm4uUGFyYW1ldGVyKHQyKQpccGFyZGVmIGZvcndhcmQoc2VsZiwgYWN0aXZhdGlvbnMpOgp0ID0gdG9yY2gubW0oYWN0aXZhdGlvbnMsIHNlbGYudykKcmV0dXJuIHQgKyBzZWxmLmIK){download=""}

<!-- chunk {"id": "body-0014", "role": "body", "section": "Deep learning models are just Python programs", "weight": 1.0} -->

[⬇](data:text/plain;base64,CmNsYXNzIEZ1bGxCYXNpY01vZGVsKG5uLk1vZHVsZSk6CmRlZiBfX2luaXRfXyhzZWxmKToKc3VwZXIoKS5fX2luaXRfXygpCnNlbGYuY29udiA9IG5uLkNvbnYyZCgxLCAxMjgsIDMpCnNlbGYuZmMgPSBMaW5lYXJMYXllcigxMjgsIDEwKQpccGFyZGVmIGZvcndhcmQoc2VsZiwgeCk6CnQxID0gc2VsZi5jb252KHgpCnQyID0gbm4uZnVuY3Rpb25hbC5yZWx1KHQxKQp0MyA9IHNlbGYuZmModDEpCnJldHVybiBubi5mdW5jdGlvbmFsLnNvZnRtYXgodDMpCg==){download=""}

<!-- chunk {"id": "body-0015", "role": "body", "section": "Deep learning models are just Python programs", "weight": 1.0} -->

A custom layer used as a building block for a simple but complete neural network.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Deep learning models are just Python programs", "weight": 1.0} -->

This "everything is a just a program" philosophy is not limited to just the models, and applies to optimizers and data loaders as well. This facilitates the experimentation of new training techniques. For example, to implement the very popular generative adversarial networks, one needs to specify two separate models (the generator and the discriminator), and two loss functions that depend on both models at the same time. Rigid APIs would struggle with this setup, but the simple design employed in PyTorch easily adapts to this setting as shown in Listing 2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Deep learning models are just Python programs", "weight": 1.0} -->

discriminator = create_discriminator
generator = create_generator
optimD = optim.Adam(discriminator.parameters)
optimG = optim.Adam(generator.parameters)
\pardef step(real_sample):
## Update Discriminator
errD_real = loss(discriminator(real_sample), real_label)
errD_real.backward
fake = generator(get_noise)
errD_fake = loss(discriminator(fake.detach, fake_label)
errD_fake.backward
## Update Generator
errG = loss(discriminator(fake), real_label)

<!-- chunk {"id": "body-0018", "role": "body", "section": "Deep learning models are just Python programs", "weight": 1.0} -->

Simplified training of a generative adversarial networks.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Deep learning models are just Python programs", "weight": 1.0} -->

Since PyTorch programs execute eagerly, all the features of Python are available throughout the whole design process. Print statements, standard debuggers, and common visualization tools like matplotlib all work as expected. Users do not have to wait for lengthy compilation before they can start running their programs, and more importantly intermediate computations can be observed to understand how a model works and whether its results are correct.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Interoperability and extensibility", "weight": 1.0} -->

Easy and efficient interoperability is one of the top priorities for PyTorch because it opens the possibility to leverage the rich ecosystem of Python libraries as part of user programs. Hence, PyTorch allows for bidirectional exchange of data with external libraries. For example, it provides a mechanism to convert between NumPy arrays and PyTorch tensors using the torch.from_numpy function and.numpy tensor method. Similar functionality is also available to exchange data stored using the DLPack format. Note that this exchange happens in both cases without any data copying -- objects on both sides only describe how to interpret a memory region which is shared among them. Hence, those operations are actually extremely cheap, and take constant time no matter how large the converted arrays are.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Interoperability and extensibility", "weight": 1.0} -->

Moreover, many of the critical systems are designed specifically to be extensible. For instance, the automatic differentiation system allows users to add support for custom differentiable functions. To do that users can define a new subclass of torch.autograd.Function that implements forward and backward methods, which specify the function and its derivative (or more formally the vector-Jacobian product). Similarly new datasets can be added by subclassing torch.utils.data.Dataset and implementing two methods: \_\_getitem\_\_ (the indexing operator) and \_\_len\_\_ (the length operator), making datasets behave like (possibly lazy) lists. How these work is completely up to the implementer, and many users leverage other Python packages for data loading. The DataLoader class consumes objects conforming to this interface and provides an iterator over the data which takes care of shuffling, batching, parallelization, and management of pinned CUDA memory to improve throughput.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Interoperability and extensibility", "weight": 1.0} -->

Most importantly, users are free to replace any component of PyTorch that does not meet the needs or performance requirements of their project. They are all designed to be completely interchangeable, and PyTorch takes great care not to impose any particular solution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

Since gradient based optimization is vital to deep learning, PyTorch must be able to automatically compute gradients of models specified by our users, and those can be arbitrary Python programs. However, Python is a dynamic programming language that allows changing most behaviors at runtime, making ahead of time source-to-source differentiation cumbersome. Instead, PyTorch uses the operator overloading approach, which builds up a representation of the computed function every time it is executed. In its current implementation, PyTorch performs reverse-mode automatic differentiation, which computes the gradient of a scalar output with respect to a multivariate input. Differentiating functions with more outputs than inputs is more efficiently executed using forward-mode automatic differentiation, but this use case is less common for machine learning applications. PyTorch can be easily extended to perform forward-mode differentiation using array-level dual numbers.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

Another interesting and uncommon feature of our system is that it can differentiate through code employing mutation on tensors, which is one of the basic building blocks of imperative programs. To ensure safety, we have implemented a versioning system for tensors, which lets us track their modifications and ensure that we always use the data we expect. One interesting tradeoff is that while we could utilize techniques like copy-on-write to support arbitrary programs, we chose to not go down this path, as performance-wise it is usually beneficial for the users to rewrite their code to ensure that no copies have to be performed. Hence, while most mutations are benign and can be handled automatically, the really complicated cases result in a user error, which lets them know that they likely want to restructure the program. This allows us to avoid introducing subtle and hard-to-find performance cliffs.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Performance focused implementation", "weight": 1.0} -->

Running deep learning algorithms efficiently from a Python interpreter is notoriously challenging: for instance, the global interpreter lock effectively ensures that only one of any number of concurrent threads is running at any given time. Deep learning frameworks based on the construction of a static data-flow graph sidestep this problem by deferring the evaluation of the computation to a custom interpreter.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Performance focused implementation", "weight": 1.0} -->

PyTorch solved the problem differently, by carefully optimizing every aspect of its execution while simultaneously empowering its users to easily leverage additional optimization strategies.

<!-- chunk {"id": "body-0027", "role": "body", "section": "An efficient C++ core", "weight": 1.0} -->

Despite being closely integrated in the Python ecosystem, most of PyTorch is written in C++ to achieve high performance. This core libtorch library implements the tensor data structure, the GPU and CPU operators, and basic parallel primitives. It also provides the automatic differentiation system, including the gradient formulas for most built-in functions. This ensures that the computation of the derivatives of functions composed of core PyTorch operators is executed entirely in a multithreaded evaluator which does not require holding the Python global interpreter lock. Python bindings are generated using YAML meta-data files. An interesting side-effect of this approach is that it allowed our community to quickly create bindings to multiple other languages resulting in projects like NimTorch, hasktorch and others.

<!-- chunk {"id": "body-0028", "role": "body", "section": "An efficient C++ core", "weight": 1.0} -->

This design also allowed us to create first-class C++ bindings and modeling libraries that can be used in places where Python is inconvenient, such as the game engine for Starcraft or on mobile platforms. It is even possible to take the Python code describing a PyTorch model and run it without Python using the TorchScript engine.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Separate control and data flow", "weight": 1.0} -->

PyTorch maintains a strict separation between its control (i.e. program branches, loops) and data flow (i.e. tensors and the operations performed on them). The resolution of the control flow is handled by Python and optimized C++ code executed on the host CPU, and result in a linear sequence of operator invocations on the device. Operators can be run either on CPU or on GPU.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Separate control and data flow", "weight": 1.0} -->

PyTorch is designed to execute operators asynchronously on GPU by leveraging the CUDA stream mechanism to queue CUDA kernel invocations to the GPUs hardware FIFO. This allows the system to overlap the execution of Python code on CPU with tensor operators on GPU. Because the tensor operations usually take a significant amount of time, this lets us saturate the GPU and reach peak performance even in an interpreted language with fairly high overhead like Python. Note that this mechanism is nearly invisible to the user. Unless they implement their own multi-stream primitives all of the CPU-GPU synchronization is handled by the library.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Separate control and data flow", "weight": 1.0} -->

PyTorch could leverage a similar mechanism to also execute operators asynchronously on the CPU. However the costs of cross-thread communication and synchronization would negate the performance benefit of such an optimization.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Custom caching tensor allocator", "weight": 1.0} -->

Almost every operator must dynamically allocate an output tensor to hold the result of its execution. It is therefore critical to optimize the speed of the dynamic memory allocators. PyTorch can rely on optimized libraries to handle this task on CPU. However, on GPU the cudaFree routine may block its caller until all previously queued work on all GPUs completes. To avoid this bottleneck, PyTorch implements a custom allocator which incrementally builds up a cache of CUDA memory and reassigns it to later allocations without further use of CUDA APIs. The incremental allocation is also crucial for better interoperability, because taking up all GPU memory ahead of time would prevent the user from utilizing other GPU-enabled Python packages.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Custom caching tensor allocator", "weight": 1.0} -->

To further improve its effectiveness, this allocator was tuned for the specific memory usage patterns of deep learning. For example, it rounds up allocations to multiples of 512 bytes to avoid fragmentation issues. Moreover, it maintains a distinct pool of memory for every CUDA stream (work queue).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Custom caching tensor allocator", "weight": 1.0} -->

The one-pool-per-stream design assumption simplifies the implementation and improves the performance of the allocator: because the CPU runs ahead of the GPU, memory is freed on the CPU before its last use on the GPU finishes. Since streams serialize execution, if the free precedes the reallocation on the CPU, the same order will occur on the GPU. So the allocator can reallocate memory freed on the CPU immediately as long as the new allocation is used on the same stream as the freed region. However, if an allocation was last used on one stream and then allocated on another, additional synchronization is needed.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Custom caching tensor allocator", "weight": 1.0} -->

The one-pool-per-stream design seems limiting since the allocations end up fragmented per stream, but in practice PyTorch almost never uses multiple streams. It is notoriously hard to write CUDA kernels in a way that would let them cooperatively share the GPU because exact scheduling is hardware controlled. In practice, kernel writers usually resort to monolithic kernels that combine multiple tasks. Data loading and distributed computing utilities are exceptions to the one stream design, and they carefully insert additional synchronization to avoid bad interactions with the allocator.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Custom caching tensor allocator", "weight": 1.0} -->

While this design is susceptible to certain corner cases, it almost never exhibits unwanted behaviors in practical code. Most of our users are not aware of its existence.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Multiprocessing", "weight": 1.0} -->

Due to the global interpreter lock (GIL) Python's default implementation does not allow concurrent threads to execute in parallel. To alleviate this problem, the Python community has established a standard `multiprocessing` module, containing a number of utilities that allow users to easily spawn child processes and implement basic inter-process communication primitives.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Multiprocessing", "weight": 1.0} -->

However, the implementation of the primitives uses the same form of serialization used for on-disk persistence, which is inefficient when dealing with large arrays. Hence, PyTorch extends the Python `multiprocessing` module into `torch.multiprocessing`, which is a drop-in replacement for the built in package and automatically moves the data of tensors sent to other processes to shared memory instead of sending it over the communication channel.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Multiprocessing", "weight": 1.0} -->

This design greatly improves performance and makes the process isolation weaker, resulting in a programming model which more closely resembles regular threaded programs. Users can easily implement heavily parallel programs that operate on independent GPUs but later synchronize gradients using all-reduce style primitives.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Multiprocessing", "weight": 1.0} -->

Another unique feature of this system is that it transparently handles sharing of CUDA tensors, making it easy to implement techniques like Hogwild.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Reference counting", "weight": 1.0} -->

Users often design their models to utilize all memory available during training, and increasing batch sizes is a common technique of speeding up the process. Therefore, to deliver great performance, PyTorch has to treat memory as a scarce resource that it needs to manage carefully.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Reference counting", "weight": 1.0} -->

Libraries with eager semantics have to manage tensor memory without knowing how it will be used in the future. Garbage collection is the typical way to handle this automatically because it has good amortized performance. In this approach, the runtime periodically investigates the state of the system, enumerates used objects and frees everything else. However, by deferring the deallocation, it causes the program to use more memory overall. Given the scarcity of GPU memory, these overheads are unacceptable. In fact, Torch7 utilized the garbage collector built into Lua, and a common anti-pattern among the users was to sprinkle the program with explicit triggers to the garbage collector, hoping that the memory errors go away.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Reference counting", "weight": 1.0} -->

PyTorch takes a different approach: it relies on a reference counting scheme to track the number of uses of each tensor, and frees the underlying memory *immediately* once this count reaches zero. Note that PyTorch tracks both references internal to the libtorch library and external references made by users in their Python code by integrating with Python's own reference counting mechanism. This ensures that memory is released exactly when tensors become unneeded.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Reference counting", "weight": 1.0} -->

One notable caveat is that we can only guarantee the desired performance characteristics in implementations of languages that either already utilize reference counting (CPython, Swift, but not PyPy or many scripting languages such as Lua), and those that allow for user-defined behavior for assignment, copies, and moves (e.g. C++, Rust). Bindings to implementations that do not satisfy those criteria will have to implement their own specialized memory management on top of PyTorch.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In this section we compare the performance of PyTorch with several other commonly-used deep learning libraries, and find that it achieves competitive performance across a range of tasks. All experiments were performed on a workstation with two Intel Xeon E5-2698 v4 CPUs and one NVIDIA Quadro GP100 GPU.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Asynchronous dataflow", "weight": 1.0} -->

We start by quantifying the ability of PyTorch to asynchronously execute dataflow on GPU. We use the built-in profiler to instrument various benchmarks and record a timeline of the execution of a single training step.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Memory management", "weight": 1.0} -->

We used the NVIDIA profiler to trace the execution of the CUDA runtime as well as the execution of the CUDA kernels launched during one training iteration of the ResNet-50 model. As shown in Figure 4, the behavior of the first iteration differs significantly from that of subsequent ones. At first, calls to the CUDA memory management functions (`cudaMalloc` and `cudaFree`) slow down the execution quite dramatically by blocking the CPU thread for long periods of time, hence lowering the utilization of the GPU. This effect disappears in subsequent iterations as the PyTorch caching memory allocator starts reusing previously allocated regions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Finally, we can get an overall sense of single-machine eager mode performance of PyTorch by comparing it to three popular graph-based deep learning frameworks (CNTK, MXNet and TensorFlow), a define-by-run framework (Chainer), and production oriented platform (PaddlePaddle). The Appendix details all the steps needed to reproduce our setup.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Our results are summarized in Table 1. On all the benchmarks, the performance of PyTorch is within 17% of that of of the fastest framework. We attribute this result to the fact that these tools offload most of the computation to the same version of the cuDNN and cuBLAS libraries.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Adoption", "weight": 1.0} -->

The validity of design decisions and their impact on ease-of-use is hard to measure. As a proxy, we tried to quantify how well the machine learning community received PyTorch by counting how often various machine learning tools (including Caffe, Chainer, CNTK, Keras, MXNet, PyTorch, TensorFlow, and Theano) are mentioned on arXiv e-Prints since the initial release of PyTorch in January 2017. In Figure 5 we report the monthly number of mentions of the word \"PyTorch\" as a percentage of all mentions among these deep learning frameworks. We counted tools mentioned multiple times in a given paper only once, and made the search case insensitive to account for various spellings.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

PyTorch has become a popular tool in the deep learning research community by combining a focus on usability with careful performance considerations. In addition to continuing to support the latest trends and advances in deep learning, in the future we plan to continue to improve the speed and scalability of PyTorch. Most notably, we are working on the PyTorch JIT: a suite of tools that allow PyTorch programs to be executed outside of the Python interpreter where they can be further optimized. We also intend to improve support for distributed computation by providing efficient primitives for data parallelism as well as a Pythonic library for model parallelism based around remote procedure calls.
