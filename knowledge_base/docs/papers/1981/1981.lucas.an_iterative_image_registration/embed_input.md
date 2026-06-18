An Iterative Image Registration Technique with an Application to Stereo Vision

Topics include Optical flow, Lucas-Kanade, Image registration, Stereo vision, Newton-raphson iteration, Gradient-based alignment, Local motion estimation.

Lucas and Kanade present the local gradient-based registration method that later became a standard sparse optical flow tracker. Its core idea is to estimate small image displacements by iteratively linearizing image alignment, making motion estimation practical for patches, features, and stereo correspondence.

Image registration finds a variety of applications in computer vision. Unfortunately, traditional image registration techniques tend to be costly. We present a new image registration technique that makes use of the spatial intensity gradient of the images to find a good match using a type of Newton-Raphson iteration. Our technique is faster because it examines far fewer potential matches between the images than existing techniques. Furthermore, this registration technique can be generalized to handle rotation, scaling and shearing. We show how our technique can be adapted for use in a stereo vision system.
