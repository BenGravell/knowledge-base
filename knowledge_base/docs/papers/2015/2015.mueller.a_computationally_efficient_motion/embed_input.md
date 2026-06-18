<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Computationally Efficient Motion Primitive for Quadrocopter Trajectory Generation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A method is presented for the rapid generation and feasibility verification of motion primitives for quadrocopters and similar multirotor vehicles. The motion primitives are defined by the quadrocopter's initial state, the desired motion duration, and any combination of components of the quadrocopter's position, velocity, and acceleration at the motion's end. Closed-form solutions for the primitives are given, which minimize a cost function related to input aggressiveness. Computationally efficient tests are presented to allow for rapid feasibility verification. Conditions are given under which the existence of feasible primitives can be guaranteed a priori. The algorithm may be incorporated in a high-level trajectory generator, which can then rapidly search over a large number of motion primitives which would achieve some given high-level goal. It is shown that a million motion primitives may be evaluated and compared per second on a standard laptop computer. The motion primitive generation algorithm is experimentally demonstrated by tasking a quadrocopter with an attached net to catch a thrown ball, evaluating thousands of different possible motions to catch the ball.
