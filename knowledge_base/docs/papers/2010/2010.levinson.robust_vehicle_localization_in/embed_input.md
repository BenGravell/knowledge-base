<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Vehicle Localization in Urban Environments Using Probabilistic Maps

Topics include Motion planning, Trajectory planning, Sampling-based planning, Robotics, Autonomous vehicles, Vehicle control, Simultaneous localization and mapping, State estimation, Robot perception, Factor graphs, Probabilistic modeling, Uncertainty quantification.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous vehicle navigation in dynamic urban environments requires localization accuracy exceeding that available from GPS-based inertial guidance systems. We have shown previously that GPS, IMU, and LIDAR data can be used to generate a high-resolution infrared remittance ground map that can be subsequently used for localization. We now propose an extension to this approach that yields substantial improvements over previous work in vehicle localization, including higher precision, the ability to learn and improve maps over time, and increased robustness to environment changes and dynamic obstacles. Specifically, we model the environment, instead of as a spatial grid of fixed infrared remittance values, as a probabilistic grid whereby every cell is represented as its own gaussian distribution over remittance values. Subsequently, Bayesian inference is able to preferentially weight parts of the map most likely to be stationary and of consistent angular reflectivity, thereby reducing uncertainty and catastrophic errors. Furthermore, by using offline SLAM to align multiple passes of the same environment, possibly separated in time by days or even months, it is possible to build an increasingly robust understanding of the world that can be then exploited for localization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We validate the effectiveness of our approach by using these algorithms to localize our vehicle against probabilistic maps in various dynamic environments, achieving RMS accuracy in the 10cm-range and thus outperforming previous work. Importantly, this approach has enabled us to autonomously drive our vehicle for hundreds of miles in dense traffic on narrow urban roads which were formerly unnavigable with previous localization methods.
