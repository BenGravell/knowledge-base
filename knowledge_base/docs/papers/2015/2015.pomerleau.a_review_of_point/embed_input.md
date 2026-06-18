<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Review of Point Cloud Registration Algorithms for Mobile Robotics

Topics include Point cloud registration, Iterative closest point, Geometric registration, Mobile robotics, Laser odometry, Robot localization, 3D reconstruction, Scan matching, Registration taxonomy, Survey.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Surveys point cloud registration for mobile robotics with ICP as the central historical and practical reference point. Its main value is the taxonomy: it decomposes geometric registration pipelines into configurable choices, making it easier to compare variants and choose an implementation for a given sensor, platform, and environment.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The topic of this review is geometric registration in robotics. Registration algorithms associate sets of data into a common coordinate system. They have been used extensively in object reconstruction, inspection, medical application, and localization of mobile robotics. We focus on mobile robotics applications in which point clouds are to be registered. While the underlying principle of those algorithms is simple, many variations have been proposed for many different applications. In this review, we give a historical perspective of the registration problem and show that the plethora of solutions can be organized and differentiated according to a few elements. Accordingly, we present a formalization of geometric registration and cast algorithms proposed in the literature into this framework. Finally, we review a few applications of this framework in mobile robotics that cover different kinds of platforms, environments, and tasks. These examples allow us to study the specific requirements of each use case and the necessary configuration choices leading to the registration implementation. Ultimately, the objective of this review is to provide guidelines for the choice of geometric registration configuration.
