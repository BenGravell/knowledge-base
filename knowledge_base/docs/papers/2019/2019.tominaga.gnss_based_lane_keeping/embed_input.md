<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GNSS Based Lane Keeping Assist System via Model Predictive Control

Topics include Lane keeping, Model predictive control, GNSS, Autonomous driving, Path tracking.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines precise satellite positioning and high-definition maps with model predictive steering control for lane keeping, evaluating performance in simulation and vehicle tests.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recently, the field of autonomous driving has been dramatically expanding, and some of the key technologies like the Lane Keeping Assist (LKA) system have begun to be applied to mass production vehicles. In general, mass-produced LKA systems use a lane detection camera as a means of keeping the lane. One of the common limitations of camera-based LKA systems is that the lane keeping performance significantly decreases when the camera cannot detect lane markings for various reasons such as snow coverage and sunlight. To overcome this limitation, we have developed a Global Navigation Satellite System (GNSS) based LKA system, which is not affected by the surrounding environment such as weather and lighting. Our LKA system uses centimeter-level augmentation service and high-definition maps, whereby the LKA system can accurately estimate its own position. This feature potentially enables our LKA system to show higher lane-keeping performance than camera-based LKA systems even when lane markings are undetectable. In our previous study, we proposed a GNSS based LKA system in which the target steering angle was calculated by means of a PID controller based on a look-ahead model.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Although there were a few problems such as oscillation of steering, the proposed system enabled a real vehicle to keep the lane even under conditions in which camera based LKA systems would probably not work well. In this paper, to aim at improving lane keeping performance, we proposed a GNSS based LKA system that calculates target steering angle via Model Predictive Control (MPC). We then validated the lane keeping performance of the LKA system using MPC in both a simulation and in real vehicle tests.
