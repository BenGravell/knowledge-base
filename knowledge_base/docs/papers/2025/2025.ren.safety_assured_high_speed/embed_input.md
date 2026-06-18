<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safety-assured High-speed Navigation for MAVs

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Micro air vehicles (MAVs) capable of high-speed autonomous navigation in unknown environments have the potential to improve applications like search and rescue and disaster relief, where timely and safe navigation is critical. However, achieving autonomous, safe, and high-speed MAV navigation faces systematic challenges, necessitating reduced vehicle weight and size for high-speed maneuvering, strong sensing capability for detecting obstacles at a distance, and advanced planning and control algorithms maximizing flight speed while ensuring obstacle avoidance. Here, we present the safety-assured high-speed aerial robot (SUPER), a compact MAV with a 280-millimeter wheelbase and a thrust-to-weight ratio greater than 5.0, enabling agile flight in cluttered environments. SUPER uses a lightweight three-dimensional light detection and ranging (LIDAR) sensor for accurate, long-range obstacle detection. To ensure high-speed flight while maintaining safety, we introduced an efficient planning framework that directly plans trajectories using LIDAR point clouds. In each replanning cycle, two trajectories were generated: one in known free spaces to ensure safety and another in both known and unknown spaces to maximize speed.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Compared with baseline methods, this framework reduced failure rates by 35.9 times while flying faster and with half the planning time. In real-world tests, SUPER achieved autonomous flights at speeds exceeding 20 meters per second, successfully avoiding thin obstacles and navigating narrow spaces. SUPER represents a milestone in autonomous MAV systems, bridging the gap from laboratory research to real-world applications.
