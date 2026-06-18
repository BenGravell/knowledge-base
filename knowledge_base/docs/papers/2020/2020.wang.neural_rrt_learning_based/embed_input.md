<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Neural RRT*: Learning-Based Optimal Path Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Rapidly random-exploring tree (RRT) and its variants are very popular due to their ability to quickly and efficiently explore the state space. However, they suffer sensitivity to the initial solution and slow convergence to the optimal solution, which means that they consume a lot of memory and time to find the optimal path. It is critical to quickly find a short path in many applications such as the autonomous vehicle with limited power/fuel. To overcome these limitations, we propose a novel optimal path planning algorithm based on the convolutional neural network (CNN), namely the neural RRT* (NRRT*). The NRRT* utilizes a nonuniform sampling distribution generated from a CNN model. The model is trained using quantities of successful path planning cases. In this article, we use the A* algorithm to generate the training data set consisting of the map information and the optimal path. For a given task, the proposed CNN model can predict the probability distribution of the optimal path on the map, which is used to guide the sampling process. The time cost and memory usage of the planned path are selected as the metric to demonstrate the effectiveness and efficiency of the NRRT*.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The simulation results reveal that the NRRT* can achieve convincing performance compared with the state-of-the-art path planning algorithms. Note to Practitioners—The motivation of this article stems from the need to develop a fast and efficient path planning algorithm for practical applications such as autonomous driving, warehouse robot, and countless others. Sampling-based algorithms are widely used in these areas due to their good scalability and high efficiency. However, the quality of the initial path is not guaranteed and it takes much time to converge to the optimal path. To quickly obtain a high-quality initial path and accelerate the convergence speed, we propose the NRRT*. It utilizes a nonuniform sampling distribution and achieves better performance. The NRRT* can be also applied to other sampling-based algorithms for improved results in different applications.
