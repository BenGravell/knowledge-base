<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Motion Perceiver: Real-Time Occupancy Forecasting for Embedded Systems

Topics include Occupancy forecasting, Motion prediction, Autonomous driving, Transformers, Recursive state estimation, Embedded systems, Real-time inference.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

MotionPerceiver maintains a recursive latent scene state using attention to assimilate streaming observations and forecast future occupancy. Local position queries avoid generating full occupancy grids, enabling real-time embedded inference while improving Soft IOU on the Waymo Open Motion Dataset.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work introduces a novel and adaptable architecture designed for real-time occupancy forecasting that outperforms existing state-of-the-art models on the Waymo Open Motion Dataset in Soft IOU. The proposed model uses recursive latent state estimation with learned transformer-based functions to effectively update and evolve the state. This enables highly efficient real-time inference on embedded systems, as profiled on an Nvidia Xavier AGX. Our model, MotionPerceiver, achieves this by encoding a scene into a latent state that evolves in time through self-attention mechanisms. Additionally, it incorporates relevant scene observations, such as traffic signals, road topology and agent detections, through cross-attention mechanisms. This forms an efficient data-streaming architecture, that contrasts with the expensive, fixed-sequence input common in existing models. The architecture also offers the distinct advantage of generating occupancy predictions through localized querying based on a point-of-interest, as opposed to generating fixed-size occupancy images that render potentially irrelevant regions.
