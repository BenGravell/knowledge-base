<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Procedural Generation of Complex Roundabouts for Autonomous Vehicle Testing

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

High-definition roads are an essential component of realistic driving scenario simulation for autonomous vehicle testing. Roundabouts are one of the key road segments that have not been thoroughly investigated. Based on the geometric constraints of the nearby road structure, this work presents a novel method for procedurally building roundabouts. The suggested method can result in roundabout lanes that are not perfectly circular and resemble real-world roundabouts by allowing approaching roadways to be connected to a roundabout at any angle. One can easily incorporate the roundabout in their HD road generation process or use the standalone roundabouts in scenario-based testing of autonomous driving.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-definition (HD) maps consist of roads, lanes, signs, buildings, and other road objects, essential in creating a realistic world in a simulator for autonomous vehicles (AV). Using HD maps in simulation-based testing improves the generalizability of test results to the real world because HD maps are detailed, accurate, extensive, and photo-realistic, thereby permitting an AV to use multiple sensors to build a 3D world model. An essential aspect of HD maps is road geometries' overall realism and variation. Due to their complexity, roundabouts are often omitted from procedural road network generators, yet they do occur in the real world. In some cities, they are very common. Since there are roundabouts of various shapes and sizes, an AV needs to have access to a wide variety of roundabout shapes for thorough simulation-based testing.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Roundabouts in HD maps can be generated manually (e.g., using a tool like RoadRunner) or via extraction from digital maps like OpenStreetMap(OSM). Manual authoring of roundabouts is time-consuming and labor-intensive, typically limiting the number and variety of instances that are created. Roundabouts extracted from digital maps may require manual cleanup and are challenging to modify. Procedural generation of roundabouts addresses the problems with manual and extractive approaches -- it is fast, scalable, and can produce realistic yet different outputs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While existing approaches produce roundabouts with fixed structures that cannot be adapted to surrounding road structures, the approach described in this paper takes the surrounding information as constraints and produces roundabouts consistent with these constraints. This ensures the lanes and direction of the approaching roads to the roundabout area mold the roundabout. In addition to flexibly producing roundabouts, the method outputs the roads in OpenDRIVE format, a standard language to describe road geometries. OpenDRIVE roads can easily be imported into driving simulators such as CARLA.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This study is motivated by the restrictive design of existing roundabout generation methods. Our first finding is that current approaches frequently only permit connections at right angles and do not permit approaching roads to be joined at other angles. Realistic roundabouts, however, permit approaching roads to be joined at a variety of angles (see Figure 9). Our second observation is that the lanes inside a roundabout are not always perfectly circular. Driving is more difficult due to the inside lanes' changing curvature. Our major contributions target these findings and develop methods to address them. Moreover, our generator can also produce Turbo Roundabouts, which are not seen in any other generator.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we formalize the method that can capture the variability of a roundabout's angles and semicircular shapes. We provide the expressive range analysis of our output.

<!-- chunk {"id": "body-0008", "role": "body", "section": "METHODS FOR ROUNDABOUT GENERATION", "weight": 1.0} -->

In this section, we present our approach for creating two types of roundabouts: (a) classical roundabout, (b) turbo roundabout.

<!-- chunk {"id": "body-0009", "role": "body", "section": "METHODS FOR ROUNDABOUT GENERATION", "weight": 1.0} -->

Fig. 1: (a) Randomly generated classic roundabout with 4 incident roads, (b) Randomly generated turbo roundabout with 4 incident roads A roundabout is a set of roads of two types: circular roads and incident roads. Vehicles approach and leave the roundabout through one of the incident roads. Circular roads create the loop inside the roundabout and connect the incident roads. Furthermore, we define the incident road definition as a four-value tuple of (position, heading, numLeftLanes, numRightLanes). Each incident road definition corresponds to the incident point where an incident road is connected to the roundabout area. Given a set of incident road definitions, a roundabout is generated in three phases. In the first phase, we find a circle using the incident points. In the second phase, we create the circular roads. In the third phase, we create incident roads and connect them to circular roads using connection roads.

<!-- chunk {"id": "body-0010", "role": "body", "section": "METHODS FOR ROUNDABOUT GENERATION", "weight": 1.0} -->

In our work, we use the term classic roundabouts to describe standard multi-lane roundabouts. Turbo roundabouts refer to roundabouts with enhanced design for disallowing lane changing, which minimizes conflict points.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Classic Roundabout", "weight": 1.0} -->

This section discusses the three phases of classic roundabout generation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A1 Phase 1: Finding Maximal Circle Which Has No Incident Points Inside", "weight": 1.0} -->

Fig. 2: (a) Phase 1 finds maximal circle with input road definitions. (b) Phase 2 builds the skeleton by building circular roads. (c) Phase 3 adds incident roads to the skeleton built in Phase 2 and finishes the roundabout.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A1 Phase 1: Finding Maximal Circle Which Has No Incident Points Inside", "weight": 1.0} -->

In phase 1 (Fig:2(a)), we find a circle defined by $(C_{x},C_{y},r)$. Given incident points, we find a circle that contains no incident points inside. This is important as the circle lays the foundation for the circular roads, which cannot overlap with any incident roads. To find out the center, we use the least square regression method for circle fitting. Once the center $(C_{x},C_{y})$ is found, the radius can be found by finding the minimum distance between the center and the incident points.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A2 Phase 2: Creating Circular Roads", "weight": 1.0} -->

Fig. 3: Segmenting the roundabout into small parts for incident road connectivity. Blue filled circles are incident points, black arcs are road segments created on the centerline from phase 1, and black filled circle denote the start/endpoints for the segments. (a) Roads can only be linked to start or end points, thus fewer segments lead to road overlap. (b)(c) Dividing the circle into tiny segments allows incident roads to be connected to spatially nearby segments only.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A2 Phase 2: Creating Circular Roads", "weight": 1.0} -->

We use the circle from phase 1 as the reference line of the circular road inside the roundabout. The creation of circular roads poses a significant challenge due to the specifications of ASAM OpenDRIVE. Circular roads can be built using only two half-circle segments. However, OpenDRIVE only permits roads to be linked to their start and end points. Hence, if incident roads are connected in the way shown in Fig:3(a), while the connection is valid, the geometry becomes invalid due to road overlap. We first break down the circle into small segments to solve this challenge. Then we find their starting points and heading. Then we either create perfectly circular roads by joining the points with circular segments (Fig:3(b)) or, to induce an irregular circular shape, we add Perlin noise to the points and finally join the points using connection roads (Fig:3(c)). A connection road is a parametric cubic road with lanes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

Phase 2 produces the body of a roundabout. Phase 3 extends incident roads from the incident points given by the input road definitions, so they join the roundabout (Fig:2(c)). While connecting incident roads to circular roads becomes easier due to the modification is done in phase 2, deciding which point to connect to becomes difficult because incident angles can differ. Thus, a trivial rule, such as finding the closest circular segment for connecting straight roads, can create invalid geometries. For example, in Fig:4(a), incident roads are connected to the right and left points of the closest point, and we can see that it causes connection roads to overlap with circular roads.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

Therefore, we introduce centerOffset in this phase (Fig.4(b)). centerOffset is the angular difference between the original heading of an incident point and the direction of the vector between the center of the roundabout and the incident point. It is essential for making two important decisions: Using centerOffset, we can decide which circular road segment to connect a straight road to. If this method was not used, it would always connect straight roads to circular road segments based on their starting point, leading to undesirable connections. centerOffset affects the length of a straight road. The variability of the straight roads widens the incident angle range of the generator.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

Finally, phase 3 has the following steps: Create straight roads from road definitions based on distance from an incident point to the center and the centerOffset of the incident point. The length of the road can be found by finding the smallest length for which the distance between the road endpoint and the center is minimum and the road does not overlap the circular roads.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

Calculate road connection points for each roads using $centerOffset_{startingPoint}$ (Fig:4(b)).

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

Join incident roads with their respective circular road segments.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

Fig. 4: (a) fixed connection rule leads to a bad connection (closest segment starting point for each incident points shown with dotted lines), (b) centerOffset

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B1 Phase 1: Finding Maximal Circle Which Has No Incident Points Inside", "weight": 1.0} -->

This phase is similar to phase 1 of Classic Roundabout Generation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B2 Phase 2: Creating Circular Roads", "weight": 1.0} -->

Fig. 5: (a)(b) Finding compatible point (compatible point shown with bigger radius), (c)(d) Creating Turbo Circular Roads, (e) Rotating structure to match compatible points Turbo roundabout circular road structure differs from the classic roundabout because of its spiral pattern. This pattern emerges from circular road segments being translated along one or many axes. For this work we discuss construction of one-translation-axis turbo roundabouts, the most popular variant. Since there is one axis translation, two half circular roads need to be created and translated along the chosen axis. Besides, in the intersection where half circular roads are translated, incident roads are connected differently as the incoming and outgoing incident lanes connect to two structures that belong to different circles. To capture these behaviors, we define spike as the road segments that connect the two half circular segments. Phase 2 has the following steps: Find a pair of optimal points which will characterize the translation axis for spike generation (Fig. 5(a),5(b)).

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B2 Phase 2: Creating Circular Roads", "weight": 1.0} -->

Using radius and center, create two half circular roads using multiple segments, translate them and connect them using straight roads (spike). (Fig. 5(c),5(d)) Rotate road system to the translation axis. (Fig. 5(e))

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

Fig. 6: (a) Connecting compatible points to the spike and other points to opmimum locations, (b) Adding connection roads.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

The only difference between this phase and that of the Classic Roundabout Generation is that in this phase, compatible points will be connected to spike (Fig:6(a)), so that the roads generated from it are smoothly connected (Fig:6(b)), resembling a turbo roundabout. We connect the rest of the incident points using centerOffset as shown in the Phase 3 of Classic Roundabout Generation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

Fig. 7: Randomly generated classic roundabouts. In (a) we have three-lane incident roads, in (b) and (c) the incident lanes have either two lanes or three lanes.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B3 Phase 3: Creating Incident Roads", "weight": 1.0} -->

Fig. 8: Randomly generated turbo roundabouts.

<!-- chunk {"id": "body-0029", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

We first present a qualitative evaluation of our work. Classic and turbo roundabouts produced by Junction-Art, as seen in Fig. 7 and 8, vary in the number of incident roads, incident road angles, radius, lanes, etc. In Fig 9, an example of a real life roundabout is presented. It is apparent that the roundabout contains different numbers of lanes for different incident roads, which can also be seen in the output from our generator. In Feature 2, we can see the variable radius of the circular roads. Our work can produce similar results as well. Finally, in the real-world example, incident roads can have different incident angles, which is also reflected in our output.

<!-- chunk {"id": "body-0030", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

Fig. 9: Comparison of a real-world roundabout from 290 Pacific Ave in Santa Cruz, California and Junction-Art generated output. Feature 1 shows variable incident road lanes, Feature 2 shows semi circular shape, and Feature 3 shows variable incident road angles. Map data ©2023 Google Fig. 10: Random road definition generation process for evalution.

<!-- chunk {"id": "body-0031", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

Fig. 11: Normalized 3-way roundabouts superimposed on a circle. Thick black line resembles the circle.

<!-- chunk {"id": "body-0032", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

To show the diversity of the curvature captured by our generator, we present an expressive range analysis of our output. First we generate 20 n-way random roundabouts. The method requires us to first select a random circle with a radius of 35 to 45 meters and then randomly pick $n$ points. Then we randomize their heading, and pass them into our generator (Fig. 10).

<!-- chunk {"id": "body-0033", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

Fig. 11 shows the summary of the semicircular shape of the 3-way roundabouts. The radii distributions of the 3, 4, and 5-way generated roundabouts are presented in Fig. 12. As shown in Fig. 12(a), it is apparent that most distributions are centralized towards the 12 to 25 meter region, which is due to the radius choice of the randomized road-definition generator. Besides, most distributions are platykurtic, showing the variability of the radius in roundabouts. The central tendency and the flat nature of the distribution also persists in the 4 and 5-way roundabouts (Fig. 12(b) & 12(c)).

<!-- chunk {"id": "body-0034", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

Fig. 12: Distribution of radii in several (a) 3, (b) 4, (c) 5 ways roundabouts. Each line represents a roundabout’s radius at different points on its center line. Driving on a roundabout with wider spread is harder in general.

<!-- chunk {"id": "body-0035", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

Fig. 13: Distribution of the derivative of radii in several 3-way roundabouts.

<!-- chunk {"id": "body-0036", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

To further analyze the variability of radii, we present the distribution of the derivative of the radii for several 3-way roundabouts in Fig. 13. The distributions are generally centered towards 0, often slightly skewed, and leptokurtic. Hence, it is apparent that generated roundabouts, while keeping a circular resemblance, change radius smoothly.

<!-- chunk {"id": "body-0037", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

Fig. 14: Distribution of radii in several 3-way roundabouts generated from the same road definition. Each line represents a roundabout’s radius at different points on its center line.

<!-- chunk {"id": "body-0038", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

Fig. 15: Bivariate density estimation of radii and derivative of the radii in several 3-way roundabouts generated for (a)random road definitions (b) a fixed road definition.

<!-- chunk {"id": "body-0039", "role": "body", "section": "EVALUATION", "weight": 1.0} -->

Finally, to show that the variations are unaffected by input variety, We generate 30 3-way roundabouts with a fixed input. As shown in Fig. 14, the distribution of radii for each roundabout is different while centered at the same position, showing that the roundabouts have variations in shape while keeping the same circular structure. We also see a similar outcome in Fig. 15(a) and 15(b), which shows no notable bias in the derivative of radii regardless of a fixed input or randomized inputs.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Future Work", "weight": 1.5} -->

While variations in both roundabouts were thoroughly presented in this work, there are many variation in turbo roundabouts that still need to be addressed such as shape, number of spikes etc. Many roundabouts have slip roads that are adjacent to or even sometimes partially overlapping with the roundabout area. We left such designs for future scope. There are also room to improve the distortion algorithm. Algorithms that can generate different shapes could more naturally model real-world distortion distributions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

This paper details how JunctionArt can generate Classic and Turbo roundabouts. These roundabouts can adapt to the incident roads and hence are pluggable into existing HD road networks. We formulated a novel approach to connect approaching roads from any angle to roundabout lanes without violating the OpenDRIVE rules for describing roads. The roundabout lanes can take distorted circular shapes creating a variation in curvature. We present an expressive range analysis of the shapes and curvatures. We look forward to the inclusion of greater numbers of more varied roundabouts in future AV simulation based testing scenarios.Í
