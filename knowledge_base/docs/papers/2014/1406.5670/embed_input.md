3D ShapeNets: A Deep Representation for Volumetric Shapes

Topics include Deep learning, Convolutional networks, Computer vision, Datasets, Planning, Learning, 3D ShapeNets, CAD.

3D shape is a crucial but heavily underutilized cue in today's computer vision systems, mostly due to the lack of a good generic shape representation. With the recent availability of inexpensive 2.5D depth sensors (e.g. Microsoft Kinect), it is becoming increasingly important to have a powerful 3D shape representation in the loop. Apart from category recognition, recovering full 3D shapes from view-based 2.5D depth maps is also a critical part of visual understanding. To this end, we propose to represent a geometric 3D shape as a probability distribution of binary variables on a 3D voxel grid, using a Convolutional Deep Belief Network. Our model, 3D ShapeNets, learns the distribution of complex 3D shapes across different object categories and arbitrary poses from raw CAD data, and discovers hierarchical compositional part representations automatically. It naturally supports joint object recognition and shape completion from 2.5D depth maps, and it enables active object recognition through view planning. To train our 3D deep learning model, we construct ModelNet - a large-scale 3D CAD model dataset....

## Introduction

Figure 1: Usages of 3D ShapeNets. Given a depth map of an object, we convert it into a volumetric representation and identify the observed surface, free space and occluded space. 3D ShapeNets can recognize object category, complete full 3D shape, and predict the next best view if the initial recognition is uncertain. Finally, 3D ShapeNets can integrate new views to recognize object jointly with all views.

Since the establishment of computer vision as a field five decades ago, 3D geometric shape has been considered to be one of the most important cues in object recognition. Even though there are many theories about 3D representation (e.g. ), the success of 3D-based methods has largely been limited to instance recognition (e.g. model-based keypoint matching to nearest neighbors ). For object category recognition, 3D shape is not used in any state-of-the-art recognition methods (e.g. ), mostly due to the lack of a good generic representation for 3D geometric shapes....

## Conclusion

To study 3D shape representation for objects, we propose a convolutional deep belief network to represent a geometric 3D shape as a probability distribution of binary variables on a 3D voxel grid. Our model can jointly recognize and reconstruct objects from a single-view 2.5D depth map (e.g. from popular RGB-D sensors). To train this 3D deep learning model, we construct ModelNet, a large-scale 3D CAD model dataset. Our model significantly outperforms existing approaches on a variety of recognition tasks, and it is also a promising approach for next-best-view planning. All source code and data set are available at our project website.

The inputs to our next-best-view system are observed voxels $\mathbf{x}_{o}$ of an unknown object captured by a depth camera from a single view, and a finite list of next-view candidates $\{\mathbf{V}^{i}\}$ representing the camera rotation and translation in 3D. An algorithm chooses the next-view from the list that has the highest potential to reduce the recognition uncertainty. Note that during this view planning process, we do not observe any new data, and hence there is no improvement on the confidence of $p{({\left. y \middle| \mathbf{x}_{o} \right. = x_{o}})}$.

A 3D shape is represented as a $24 \times 24 \times 24$ voxel grid with 3 extra cells of padding in both directions to reduce the convolution border artifacts....
