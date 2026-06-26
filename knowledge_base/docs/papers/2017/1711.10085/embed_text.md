## Introduction

UNMANNED aerial vehicle (UAV) research and development has been growing rapidly over the past decade. In academia, there are more than 60 UAV papers in IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) and IEEE International Conference on Robotics and Automation (ICRA) in 2016 alone. In the commercial sector, the annual Aerospace Forecast Report released by the United States Federal Aviation Administration (FAA) estimates that more than seven million UAVs will be purchased by 2020. Another recent report released by PricewaterhouseCoopers (PwC)---the second largest professional services firm in the world---estimates the global market for applications of UAVs at over \$127 billion in 2020.

Despite rapid growth, there is no survey paper that summarizes the background, latest developments, and trends of the UAV research. And, because the number of UAV papers has grown rapidly in recent years, researchers often find it hard to cite all related papers in a short paper. To date, there is no survey that attempt to list all the UAV papers in a systematic way. In this work, we systematically identify 1,318 UAV papers that appear in the top robotic journals/conferences since 2001. The identification process includes screening paper abstracts with a program script and eliminating non-UAV papers based on several criteria with meticulous human checks. We categorize the selected UAV papers in several ways, e.g., with regard to UAV types, research topics, onboard camera systems, off-board motion capture system, countries, years, etc. In addition, we provide a high-level view of UAV research since 2001 by summarizing various statistical information, including year, type, and topic distribution. We believe this survey list not only can help researchers to identify, study, and compare their works, but also is useful for understanding the research trends in the field.

From our survey results, we also find that the types of UAV are growing rapidly. There is a urgent need to have an overview on the UAV types and categories to enhance readers' understanding and to avoid potential confusion. With the UAV papers list, we outline the recent progress of several UAVs for each UAV type that we have surveyed in this work. These include quadcopter, hexacopter, fixed-wing, flapping-wing, ducted-fan, blimp, cyclocopter, spincopter, Coandǎ, and various others. To the best of our knowledge, there is no literature that summarizes as many types of UAV in a unified fashion. Along with the UAV figures, we also briefly describe the novelties (either new methods or applications) of each. We believe that the survey results could be a great source of inspiration and continue to push the boundary of UAV research.

The structure of this survey paper is as follows. In Section II, we first present the definition, types, categories, and topics of UAV research. In Section III, we review some survey works that are related to UAV research. Then, we explain our survey methodology in Section IV and summarizes our survey results in Section V. In Section VI, we outline all types of UAVs that we have surveyed in this work. Lastly, we present our discussion and final remarks in Section VII.

## UAV Overview

In this section, we define the term UAV formally and introduce a few types of UAVs based on a common classification. Then, we discuss two interesting ideas that have been proposed by UAV researchers to categorize UAVs and summarize the UAV topics briefly with a pie chart.

### II-A UAV Definition

Commonly known as a drone, a UAV is an aircraft that can perform flight missions autonomously without a human pilot onboard or can be tele-operated by a pilot from a ground station. The UAV's degree of autonomy varies but often has basic autonomy features such as "self-leveling" using an inertial measurement unit (IMU), "position-holding" using a global navigation satellite system (GNSS) sensor, and "altitude-holding" using a barometer or a distance sensor. UAVs with higher degrees of autonomy offer more functions like automatic take-off and landing, path planning, and obstacle avoidance. In general, a UAV can be viewed as a flying robot. In the literature and UAV communities, a UAV also has several other names like micro aerial vehicle (MAV), unmanned aerial system (UAS), vertical take-off and landing aircraft (VTOL), multicopter, rotorcraft, and aerial robot. In this work, we will use the phrases "UAV" and "drone" interchangeably.

### II-B UAV Types

Depending on the flying principle, UAVs can be classified into several types.^11^1 Refer to Section VI for a comprehensive list of UAV types, along with detailed descriptions and high-resolution figures for each type of UAV. Figure 1 illustrates one common classification method, where UAVs are first classified according to their vehicle mass. For example, "heavier-than-air" UAVs normally have substantial vehicle mass and rely on aerodynamic or propulsive thrust to fly. On the other hand, "lighter-than-air" UAVs like blimps and balloons normally rely on bouyancy force (e.g., using helium gas or heat air) to fly. "Heavier-than-air" UAVs can be further classified into "wing" or "rotor" type. "Wing" type UAVs, including fixed-wing, flying-wing, and flapping-wing UAVs, rely on their wings to generate aerodynamic lift; "rotor" type UAVs, including a plethora of multirotors, rely on multiple rotors and propellers that are pointing upwards to generate propulsive thrust.

Figure 1: Common UAV types. See text for details.

### II-C UAV Categories

Previously, we have classified UAVs into several types based on their flying principles. In Fig. 2, Floreano and Wood and Liew provide insights on how UAVs can be categorized with two principal components.

Floreano and Wood categorize UAVs with two different principal components---flight time versus UAV mass. While they have surveyed 28 different fixed-wing, flapping-wing, and rotor-type UAVs, we simplify their original plot into a conceptual chart in Fig. 2 (right). In general, flapping-wing UAVs are usually small and have short flight time. Blimp/balloon UAVs are lightweight and have longer flight time. Rotor-type and fixed-wing UAVs are usually heavier. Assuming the same UAV mass and optimal design, fixed-wing UAVs would have longer flight time than rotor-type UAVs due to their higher aerodynamic efficiency.

On the other hand, Liew proposes to categorize UAVs based on the degree of autonomy and degree of sociability. Traditionally, UAVs are controlled manually by human operators and have low degrees of autonomy and sociability (remote control UAV). Gradually, along the vertical axis of degree of autonomy, researchers have been improving the autonomy aspects of UAVs, such as better reactive control with more sensors and better path planning algorithms (autonomous UAV). Essentially, autonomous UAVs are less dependent on human operators and are able to perform some simple flight tasks autonomously. On the other hand, along the horizontal axis of degree of sociability, researchers have been improving the social aspects of UAVs, such as designing UAVs that are safe for human-robot interaction (HRI), developing a UAV motion planning model that is more comfortable to humans, and building an intuitive communication interface for UAVs to understand humans (social UAV). Different from autonomous UAVs, social UAVs often have low degree of autonomy. Most HRI researchers solely focus on social aspects and manually control a UAV using Wizard of Oz experiments. Liew first coins the phrase "companion UAV", where he defines a companion UAV as one that possesses high degrees of both autonomy and sociability. In addition to the autonomy aspects, such as stabilization control and motion planning, companion UAVs must also focus on the sociability aspects such as safe HRI and intuitive communication interface for HRI.

Figure 2: Two UAV categorization methods found in the literature. Left: Flight time versus UAV mass (inspired by Floreano and Wood ). Right: Degree of autonomy versus degree of sociability (inspired by Liew )). See text for details.

### II-D UAV Topics

Focusing on four robotic conferences and four robotic journals, Liew analyzes the topic distribution of UAVs from 2006 to 2016.^22^2Refer to Section IV & V for a more comprehensive survey and results. For reference purposes, we simplify the pie chart summarized by Liew in Fig. 3. From the pie chart, we can observe that hardware and control papers contribute to more than 50% of the pie. In recent years, researchers start to focus on higher level tasks such as navigation and task planning in UAVs. In addition, researchers also pay attention to visual odometry, localization, and mapping, which are essential for UAVs to perform task planning effectively. More recently, researchers focus on HRI and tele-operation with UAVs. Lately, researchers work on obstacle or collision avoidance, which is an important topic of UAVs.

Figure 3: Topic distribution of UAV research in 2006–2016 (data taken from ). Best viewed in color. See text for details.

## Related Works on UAV Survey

In this section, we discuss several surveys in the UAV field, including surveys on quadcopter and flapping-wing UAVs. We also list several short papers that summarize UAV results in a video. Lastly, we refer to several resources that aim to summarize details of open-source flight controllers.

### III-A Quadcopter UAV

Focusing on a quadcopter platform, Kumar and Michael discuss topics on dynamic modeling, trajectory planning, and state estimation in their UAV research. In addition, they outline several challenges and opportunities of formation flight. Different from their work, we consider all types of UAV in this survey paper, including quadcopter, hexacopter, multirotor, fixed-wing, flapping-wing, cyclocopter, coaxial, ducted-fan, glider, blimp, parafoil, kite, Coandǎ, and ion-propelled aircrafts (Section VI).

### III-B Flapping-wing UAV

Wood *et al.* present their progress in developing an insect-scale UAV with flapping wings, including topics on dynamic modeling, actuation, control, fabrication, and power. In contrast to their work, we survey the UAV papers since 2001 and provide a general overview of the UAV research, e.g., the number of UAV papers over years (Section V-A), paper distribution by UAV type (Section V-B), and paper distribution by research topic (Section V-C), to readers who are interested in this field.

### III-C Flight Video

Ollero and Kondak present a video that summarizes the UAV results of four European projects. Similarly, Mellinger *et al.* present a video that summarizes some advanced control capabilities of their quadcopter together with a motion capture system, such as flying through a narrow window, robust perching, and cooperative manipulation. On the other hand, Lupashin *et al.* present a video that introduces their flying machine arena---an indoor testbed where they use quadcopters and a motion capture system to demonstrate adaptive aggressive flight, iterative learning, rhythmic flight, and balance of an inverted pendulum during flight.

### III-D Flight Controller

Lim *et al.* present a survey of the publicly available open-source FCs such as Arducopter, Multiwii, Pixhawk, Aeroquad, OpenPilot, and Paparazzi for UAV. In addition to the hardware details of the FCs, they also discuss the state estimation method and controller structure of each FC. Interestingly, in less than five years, the community has grown very fast and more options are available. Readers who are interested in the latest development of open-source FCs available in the market are recommended to view two recent online articles.

## Our Survey Methodology

In this section, we discuss our survey methodology. We first explain the scope of this survey and detail the UAV papers identification process. After that, we describe our on-going plan to update this survey and share the results online.

### IV-A Scope of This Survey

We cover four top journals and four top conferences in the robotics field since 2001 in this survey. The journals include IEEE Transactions on Robotics (TRO)^33^3 Known as IEEE Transactions on Robotics and Automation prior to 2004., IEEE/ASME Transactions on Mechatronics (TME), The International Journal of Robotics Research (IJRR), and IAS Robotics and Autonomous Systems (RAS); the conferences include IEEE International Conference on Intelligent Robots and Systems (IROS), IEEE International Conference on Robotics and Automation (ICRA), ACM/IEEE International Conference on Human-Robot Interaction (HRI), and IEEE International Workshop on Robot and Human Communication (ROMAN).

### IV-B UAV Papers Identification

The UAV papers identification process involves three major steps. We first use a script to automatically collect more than thirty thousand instances of title and abstract from the mentioned eight journal/conference web pages since 2001, namely TRO, TME, IJRR, RAS, IROS, ICRA, ICUAS, HRI, and ROMAN. We also manually review the hard copies of the IROS and ICRA conferences' table of contents from 2001 to 2004, as we find that not all UAV papers in those years are listed on the website (IEEE Xplore).

At the second step, we design a list of keywords (Table I) to search drone papers systematically from the titles and abstracts collected in the first step. Note that we search for both the full name of each keyword (e.g., Unmanned Aerial Vehicle) and its abbreviation (i.e., UAV) with an automatic program script. The keywords include most of the words that describe a UAV. For example, the word "quadcopter" or "quadrotor" could be detected by the keyword "copter" or "rotor". As long as one of the keywords is detected, the paper will pass this automated screening process. micro aerial vehicle unmmaned aerial vehicle unmanned aircraft system vertical takeoff and landing MAV, UAV, UAS, VTOL TABLE I: 35 keywords used to search drone papers systematically from the collected titles and abstracts.

At the third step, we perform a manual screening to reject some non-drone papers. We read the abstract, section titles, related works, and experiment results of all the papers from the second step. If a paper passes all the five criteria below, we consider it a drone paper for this survey.

The paper must have more than two pages; we do not consider workshop and poster papers.

The paper must have at least one page of flight-related results. These can be either simulation/experiment results, prototyping/fabrication results, or insights/discussion/lesson learned. One exception is a survey/review paper, which normally does not present experiment results. Papers with details/photos of the UAV hardware are a plus. Note that the experiment results do not necessarily need to be a successful flight, e.g., flapping wing UAVs normally have on-the-bench test results.

In topics related to computer vision or image processing, the images must be collected from a UAV's onboard camera rather than a manually moving camera.

In topics related to computer vision or image processing, the images must be collected by the authors themselves. This is important, as authors who collect the dataset themselves often provide insights about their data collection and experiment results.

The paper which proposes a general method, e.g., path planning, must have related works and experiment results on drones. This is important, as some authors mention that their method can be applied to a UAV, but provide no experiment result to verify their statement.

It is interesting to note that using the keyword "air" in the second step increases the number of false entries (since the keyword is used in many contexts) but helps to identify some rare drone-related papers that have only the keyword "air" in the title and abstract. By manually filtering the list in the third step, we successfully identify two of these drone papers. Similarly, using the keyword "bee" can help to identify a rare drone paper. On the other hand, we chose not to use the keyword of "wing" because it causes many false entries like the case of "following", "knowing", etc.

### IV-C Survey Updates and Online Sharing

The full survey results (with all raw information) is shared and updated frequently online via Google Sheets.^44^4 Tables with full survey results can be viewed on Major updates, such as additional drone papers from the latest conferences/journals, will be carried out once every three months. While Google Sheets contains all the survey results, we find that it is not possible to tag the papers, and it is also difficult to search multiple keywords in the long paper list effectively. To overcome these issues, we use an open-source file tagging and organization software called TagSpaces. Figure 4 shows a screenshot of TagSpaces. TagSpaces enables readers to search papers with multiple tags or/and keywords effectively. For example, to search all IROS papers in 2016 that are related to quadcopter, users only need to input "+IROS +2016 +Quadcopter" into the search column. Moreover, since original papers (PDF files) cannot be shared with readers due to copyright issues, for each paper entry, we create an HTML file that contains the most important information inside (such as abstract, keywords, country, paper URL link, and video URL link) for easier reference. To setup TagSpaces and download all the HTML files, refer to our website at Figure 4: A screenshot of TagSpaces with different categories of tags on the left hand side, list of drone papers that match the search criterion at the middle, and info of the selected paper in HTML format on the right hand side. Best viewed in color.

## Survey Results Overview

In this section, we give an overview of the survey results, including the year, UAV type, and topic distribution of the UAV papers. For more results, please refer to Appendix A.

### V-A Yearly Distribution of UAV Papers

Figure 5 plots the numbers of UAV papers identified from the top eight journals and conferences from 2001 to 2016. From the figure, we can observe that the number of UAV papers increases rapidly over the years. As mentioned in the introduction section, the rapid increase is supported by a few factors, such as easier control of the quadcopter configuration, and lower cost of processors and sensors. While there is a slight drop in the number of papers in 2016, with the current strong trends in the research, commercial, government, and hobbyist sectors, we believe that the number of drone papers within the next five years would continue to exceed 150 papers per year.

Figure 5: Numbers of UAV papers (dots) identified from the top eight journals/conferences over the years 2001–2016, with an exponential curve fitting plot.

### V-B UAV Types Distribution

TABLE II: Top twenty-five keywords from the identified drone papers.

Figure 6: The change of papers distribution by UAV types over the years (overview). Best viewed in color. See text for details.

Figure 6 shows the UAV types distribution of surveyed papers over different years. The most notable transition in the bar graphs is the number of quadcopter papers, where it increases from 7, 19, 142, to 377 over the past sixteen years. The number of fixed-wing and flapping-wing papers more gradually increases over the years.

The number of hexacopter papers is zero before 2008. In 2009--2012, it increases to 7; in 2013-2016, it further increases to 45. The number of octocopter papers has a similar pattern. It has zero entries before 2012 but in 2013-2016, the number sudden increases to 222. We believe that hexacopter and octocopter are gaining more attention from researchers, since it has several advantages over quadcopters. First, they have redundant actuation; they are still able to fly/land safely when one motor is malfunctioning without a complex control algorithm. Second, they can handle higher payloads and researchers can mount heavier hardware, such as a robotic arms for an aerial manipulation application, or a 3D lidar sensor for a mapping application. Third, with small modifications, they can perform holonomic flight (move horizontally without tilting motion), where the the UAV is able to achieve 3D force motion without complex coupled dynamic effect, is more robust against wind disturbance and is able to achieve higher flight precision at the same time.

On the other hand, we notice that since 2005-2008, the number of helicopter papers starts to drop gradually from 48, 38, to 28. The possible cause for this decrease is the difficulties of helicopter control (when compared to quadcopter). Interestingly, the variety of UAVs also increases substantially since 2001. In 2016, in addition to the major six types of UAV (quadcopter, fixed-wing, helicopter, flapping-wing, hexacopter, and blimp), UAV papers also involve topics on coaxial, octocopter, glider, ducted fan, tricopter, bicopter, balloon, ionic flyer, cyclocopter, spincopter, kite, Coandǎ, omnicopter, parafoil, projectile, and missile UAV.

### V-C UAV Topics Distribution

Table II summarizes the top twenty-five keywords in the surveyed UAV papers. From Table II, we note that system modeling and control papers are the most frequent keywords. This is not surprising, as most UAVs require system modeling for dynamic control. It has been shown that a simple model-free PID controller is good enough for the basic maneuvers of a UAV. For aggressive maneuvers or more complex dynamics with onboard manipulators, dynamic models are normally employed. With a precision indoor positioning system, current state-of-the-art methods have successfully demonstrated formation flights, flying inverted pendulum, pole acrobatics, ball juggling, cooperative operation, and failure recovery.

From Table II, we can also observe that there are large amount of hardware development papers since 2001, including papers on quadcopters, hexacopters, octocopters, coaxial helicopters, a helicopter, a tandem helicopter, a bicopter, a trirotor UAV, fixed-wing UAV, flapping-wing UAV, cyclocopter, and blimp UAVs.

In recent years, researchers focus on higher level tasks such as navigation and task planning in UAVs. In addition, researchers also pay attention to visual odometry, localization, and mapping applications of UAVs. More recently, researchers work on obstacle or collision avoidance, which are important topics for UAVs. Current state-of-the-art UAVs could perform robust image-based six Degrees-of-Freedom (DoF) localization, cooperate mapping, aggressive flight in dense indoor environment, and flying through a forest autonomously.

More recently, researchers also focus on HRI and tele-operation of UAVs, including jogging UAVs, a flying humanoid robot, a hand-sized hovering ball, and various human-following UAVs.

## UAV Types

In Section II-B, we discuss the UAV type distribution within the surveyed papers. To enhance understanding and avoid confusion, in this section, we summarize all types of UAVs that have been proposed by researchers. Along with figures, we briefly describe the novelty of each example UAV, including quadcopter, hexacopter, fixed-wing, flapping-wing, single-rotor, coaxial, ducted-fan, octocopter, glider, blimp, ionic flyer, cyclocopter, spincopter, Coandǎ, parafoil, and kite UAVs.

### VI-A Quadcopters

Figure 7: Prototypes of quadcopters (in alphabetical order: ) appear in the reviewed papers. Note that 8 out of the 12 illustrated quadcopters have protective cases for safer operation and human-robot interaction. See text for details.

A quadcopter (Fig. 7 (a)--(l)) is a UAV with four rotors. Papachristos *et al.* first present an autonomous quadcopter (Fig. 7 (a)) with do-it-yourself (DIY) stereo perception unit that could track a moving target and perform collision-free navigation. With the goal of reducing quadcopter energy consumption, Kalantari *et al.* build a quadcopter (Fig. 7 (b)) that uses a novel adhesive gripper to autonomously perch and take-off on smooth vertical walls. Kalantari and Spenko build one of the first hybrid quadcopters (Fig. 7 (c)) that is capable of both aerial and ground locomotion. While this quadcopter can only rotate in one direction, Okada *et al.* present a quadcopter with a gimbal mechanism (Fig. 7 (d)) that enables the quadcopter to rotate freely in the 3D space. The developed quadcopter is good for inspection applications as the gimbal-like rotating shell helps the quadcopter fly safely in a confined environment with many obstacles.

To the best of our knowledge, Shen *et al.* is first to present an autonomous quadcopter (Fig. 7 (e)) that could fly robustly indoors and outdoors by integrating information from a stereo camera, a 2D lidar sensor, an IMU, a magnetometer, a pressure altimeter, and a GPS sensor. Aiming for application in search and rescue missions, Ishiki and Kumon present a quadcopter (Fig. 7 (f)) that is equipped with a microphone array to perform sound localization. While the hybrid quadcopter shown in Fig. 7 (c)) is designed to roll on flat ground, Latscha *et al.* combine a quadcopter with two snake-like mobile robots (Fig. 7 (g)), which make the resulting hybrid robot able to move effectively in disaster scenarios. To increase the safety and robustness of a swarm of quadcopter, Mulgaonkar *et al.* design a small quadcopter with a mass of merely twenty-five grams (Fig. 7 (h)).

Aiming for higher performance, Oosedo *et al.* develop an unique quadcopter (Fig. 7 (i)) that could hover stably at various pitch angles with four tiltable propellers. Abeywardena *et al.* present a quadcopter (Fig. 7 (j)) that uses an extended Kalman filter (EKF) to produce high-frequency odometry by fusing information from an IMU sensor and a monocular camera. Darivianakis *et al.* build a quadcopter (Fig. 7 (k)) that can physically interact with the infrastructures that are being inspected. Driessens and Pounds present a "Y4" quadcopter (Fig. 7 (l)) that combines the simplicity of a conventional quadcopter and the energy efficiency of a helicopter.

Figure 8: Prototypes of hexacopters (in alphabetical order: ) appear in the reviewed papers. See text for details.

### VI-B Hexacopters

A hexacopter (Fig. 8 (a)--(f)) is a UAV with six rotors. Burri *et al.* use a hexacopter (Fig. 8 (a)) to perform system identification study. Specifically, they collect information from an onboard IMU sensor, motor speeds, and hexacopter's pose to estimate the complex dynamic model (required for accurate positioning flight). In addition to the IMU sensor, Zhou *et al.* combine visual information from two downward-facing cameras to perform visual odometry in their hexacopter (Fig. 8 (b)). On the other hand, Yol *et al.* demonstrate a hexacopter (Fig. 8 (c)) that could perform vision-based localization by using a downward-looking camera and geo-referenced images. Navigation and obstacle avoidance are also important topics for UAVs. Nguyen *et al.* demonstrate their real-time path planning and obstacle avoidance algorithms with a commercial hexacopter (Fig. 8 (d)).

Similar to a conventional quadcopter, a conventional hexacopter is a non-holonomic aircraft, which cannot move horizontally without changing its attitude. Ryll *et al.* present a hexacopter (Fig. 8 (e)) that could transform itself from a conventional hexacopter to a holonomic hexacopter, i.e., able to move horizontally without tilting the aircraft, by using a servo to tilt the six rotors simultaneously. Similarly, Park *et al.* design a special hexacopter with six asymmetrically aligned and bi-directional rotors, which enable the hexacopter (Fig. 8 (f)) to perform fully-actuated flight. While The holonomic capability of a hexacopter is not as energy-efficient as a conventional hexacopter, it has several merits such as robust to wind disturbance, precision flight, and intuitive human-drone interaction.

Figure 9: Prototypes of fixed-wing UAVs (in alphabetical order: ) appear in the reviewed papers. See text for details.

### VI-C Fixed-wing UAVs

A fixed-wing UAV (Fig. 9 (a)--(k)), also known as airplane, aeroplane, or simply a plane, is one of the most common aircrafts in the aviation history. Compared to a multi-rotor aircraft, a fixed-wing UAV generally has higher flight safety (still able to glide for a long time after engines break down in the air) and longer flight time (much more energy-efficient).

Figure 9 (a)--(c) show three typical fixed-wing UAVs. Bryson and Sukkarieh demonstrate a mapping application with their fixed-wing UAV by integrating information from an IMU sensor, a GPS sensor, and a downward-facing monocular camera (Fig. 9 (a)). Hemakumara and Sukkarieh focus on system identification topic and aim to learn the complex dynamic model of their fixed-wing UAV by using Gaussian processes (Fig. 9 (b)). Morton *et al.* focus on hardware development, where they detail the design and developments of their solar-powered and fixed-wing UAV (Fig. 9 (c)).

Compared to a multi-rotor UAV, a conventional fixed-wing UAV is more energy efficient during cruise flight but does not have the hovering capability, in which a fixed-wing UAV cannot maintains its position in the air and requires more space for take-off and landing. Bapst *et al.* aim to combine the merits of both types of UAVs, where they present their design, modeling, and control of a UAV that could vertically take-off and land (VTOL) like a multi-rotor UAV and perform cruise flight like a fixed-wing UAV (Fig. 9 (d)). Verling *et al.* present another design of this type of hybrid fixed-wing UAV based on a new modeling and controller approach, where they focus on the smooth and autonomous transition between the VTOL mode and cruise mode (Fig. 9 (e)).

Researchers have also explored topics on fixed-wing UAVs with transformable shapes. Daler *et al.* build a fixed-wing UAV that could fly in the air and walk on the ground by rotating its wings (Fig. 9 (f)). D'Sa *et al.* present a UAV that could fly in a fixed-wing configuration and perform VTOL in a quadcopter configuration (Fig. 9 (g)).

Alexis and Tzes present a hybrid UAV, where the UAV could perform cruise flight like a fixed-wing UAV and perform hovering flight like a bicopter (Fig. 9 (h)). Their key design lies on the hybrid wings/propellers' structures: in the fixed-wing configuration, the one-blade structures are fixed at the right positions and act as wings; in the bicopter configuration, the one-blade structures rotate and act as propellers. Papachristos *et al.* develop another type of hybrid UAV, where the UAV could perform cruise flight like a fixed-wing UAV and perform hovering flight like a tricopter (Fig. 9 (i)).

Several palm-sized fixed-wing UAVs have also been designed by researchers. Zufferey and Floreano design a small fixed-wing UAV that has only 30 grams and capable of navigating autonomously at an indoor environment (Fig. 9 (j)). Despite its small size, the 30-gram fixed-wing UAV can also avoid obstacle during flight by relying on optical flow techinique. Pounds and Singh present a novel and low-cost fixed-wing UAV by integrating electronics and lift-producing devices onto a paper aeroplane (Fig. 9 (k)).

### VI-D Flapping-wing UAVs

Figure 10: Prototypes of flapping-wing UAVs (in alphabetical order: ) appear in the reviewed papers. See text for details.

A flapping-wing UAV (Fig. 10 (a)--(g)), also known as ornithopter and usually in about a hand size, is a UAV that generate lifting and forward force by flapping its wings. Aiming for a better aerodynamic modeling, Rose and Fearing compare the flight data collected from a wind tunnel to flight data collected from a free flight condition by using their bird-shaped flapping-wing UAV---H^2^Bird (Fig. 10 (a)). They find atht the flight data collected from the wind tunnel is not accurate enough to predict the flight data during free flight and further experiments are required. Rose *et al.* develop a coordinated launching system for H^2^Bird by mounting it onto a hexapedal robot (Fig. 10 (b)). With the hexapedal robot's helps, H^2^Bird has a more steady launching velocity. Peterson and Fearing develop a flapping-wing UAV---BOLT that is capable of flying and walking on the ground like a bipedal robot (Fig. 10 (c)).

Inspired by birds, Paranjape *et al.* design a flapping-wing UAV that is able to perch naturally on a chair or human hand (Fig. 10 (d)). One of the unique features of their UAV is to control the flight path and heading angles by using wing articulation. on the other hand, Lamers *et al.* develop a flapping-wing UAV that has a mini monocular camera system (Fig. 10 (e)). By combining the camera and a proximity sensor, their UAV can achieve obstacle detection by applying a machine learning method.

Flapping-wing UAVs with insect shapes are also common. Ma *et al.* fabricate an bee-shaped flapping-wing UAV that has a mass of 380 mg by using novel methods (Fig. 10 (f)). After detailing their design and fabrication processes, they also demonstrate a hovering flight with the developed mini UAV. Rosen *et al.* develop another insect-scaled flapping-wing UAV that is capable of flapping and gliding flights (Fig. 10 (g)).

### VI-E Single-rotor, Coaxial, and Ducted-fan UAVs

Figure 11: Prototypes of single-rotor helicopters (Fig. (a)–(c)), coaxial helicopters (Fig. (d)–(f)), and ducted-fan UAV (Fig. (g)) appear in the reviewed papers. See text for details.

A single-rotor helicopter (Fig. 11 (a)--(c)) is a UAV that relies on a main rotor and a tail rotor to generate thrust for VTOL, hovering, forward, backward, and lateral flights. By using a lidar-based perception system, Merz and Kendoul demonstrate a helicopter that can perform obstacle avoidance and close-range infrastructure inspection. Backus *et al.* focus on the aerial manipulation of an helicopter. Specifically, they design a robotic hand for their helicopter to perform grasping and perching actions effectively. Laiacker *et al.* aim to optimize their visual servoing system on a helicopter that is equipped with a 7 DoF industrial manipulator.

On the other hand, a coaxial helicopter (Fig. 11 (d)--(f)) is a UAV that uses two contra-rotating rotors mounted on the same axis to generate thrust for VTOL, hovering, forward, backward, and lateral flights. Moore *et al.* implement a lightweight omnidirectional vision sensor for their mini coaxial helicopter to perform visual navigation. Conventionally, a helicopter requires additional servo motor and a mechanical device called swashplate for horizontal position control. Paulos and Yim present a novel coaxial helicopter that requires no servo motor and mechanical device for horizontal position control. In order to perform horizontal movement, the rotors are driven by a modulated signal in order to generate both lifting and lateral forces simultaneously. Instead of avoid obstacles like a conventional UAV, Briod *et al.* design a coaxial helicopter that uses force sensors around the UAV to detect obstacle and able to perform autonomous navigation safely without the high risks of collisions.

A ducted-fan UAV (Fig. 11 (g)) is a UAV that has similar rotors configuration with a coaxial helicopter but the rotors are mounted within a cylindrical duct. The duct helps to reduce thrust losses of the propellers and the ducted fans normally have rotational speeds. Pflimlin *et al.* present a ducted-fan UAV that can stabilize itself in wind gusts by using a two-level controller for position and attitude controls.

### VI-F Octocopter, Glider, Blimp, and Ionic Flyer UAVs

Figure 12: Prototypes of octocopters (Fig. (a)–(b)), multirotor (Fig. (c)), gliders (Fig. (d)–(e)), blimp (Fig. (f)), and Ionic Flyer (Fig. (g)) appear in the reviewed papers. See text for details.

An octocopter (Fig. 12 (a)--(b)) is a UAV with eight rotors. Schneider *et al.* demonstrate an octocopter with a multiple fisheye-camera system that can perform a simultaneous localization and mapping (SLAM) function (Fig. 12 (a)). Different from a conventional octocopter, Brescianini and D'Andrea build a octocopter that has eight rotors facing to eight different direction in the 3D space (Fig. 12 (b)). This unique configuration allows the UAV to have 6 DoF and to hover stably at any attitude. More importantly, the octocopter is able to control its force in the 3D space and is useful for applications such as aerial manipulation.

A multirotor is a UAV with more than one rotor and has simple rotors configuration for flight control. Oung and D'Andrea design a modular multirotor system, where each rotor aircraft has a hexagonal shape and can be assembled into a multirotor aircraft with different configuration. With a distributed state estimation algorithm and a parameterized control strategy, the multirotor is able to fly in any flight-feasible configuration both indoors and outdoors (Fig. 12 (c)).

A glider (Fig. 12 (d)--(e)) is a UAV that uses its wings and aerodynamics to glide in the air. Glider normally has a outlook like a fixed-wing UAV but does not rely on an active propulsion system during gliding performance. For instance, Cobano *et al.* demonstrate multiple gliders that can glide cooperatively in the sky (Fig. 12 (d)). To glide for a long time in the sky without active propulsion control, the gliders detect thermal currents and exploit their energy to soar and continue to glide in the air. Inspired by a vampire bat, Woodward and Sitti build a different type of glider UAV, where their UAV can jump from the ground and then uses its wings to glide in the air (Fig. 12 (e)).

A blimp, also known as a non-rigid airship, is a lighter-than-air UAV that relies on helium gas inside an envelope to generate lifting force. Different from a Montgolfière or hot air balloon, a blimp keeps its envelope shape with the internal pressure of helium gas and has actuation units for motion control. By using a motion capture system, Müller and Burgard present an autonomous blimp that can navigate in an indoor environment with an online motion planning method (Fig. 12 (f)). Poon *et al.* aim to design a UAV that is noiseless and vibration-free by using ionic propulsion, where they call their UAV Inoic Flyer (Fig. 12 (g)). Instead of using rotors, they create a propulsion unit that has no moving mechanic parts and relies on high electrical voltage to create thrust by accelerating ions.

### VI-G Cyclocopter, Spincopter, Coandǎ, Parafoil, and Kite UAVs

Figure 13: Prototypes of cyclocopters (Fig. (a)–(b)), spincopters (Fig. (c)–(d)), Coandǎ UAV (Fig. (e)), parafoil UAV (Fig. (f)), and kite UAV (Fig. (g)) appear in the reviewed papers. See text for details.

A cyclocopter (Fig. 13 (a)--(b)) is a UAV that flies by rotating a cyclogyro wing with several wings positioned around the edge of a cylindrical structure. Generally, the wings' angles of attack are adjusted collectively by a servo motor to generate required forces. Tanaka *et al.* built a cyclocopter that can the angles of attack using a novel eccentric point mechanism without additional actuators (Fig. 13 (a)). Hara *et al.* developed a cyclocopter based on a pantograph structure, where diameters of the wings can be expanded or contracted (with reference to the rotational axis) for flight control (Fig. 13 (b)).

A spincopter (Fig. 13 (c)--(d)) is a UAV that spins itself during flight. Orsag *et al.* designed a spincopter that can spin the central wings (and the whole aircraft) using two small motors mounted at the edge of the virtual ring of the UAV (Fig. 13 (c)). The motors adjust their output thrust symmetrically/asymmetrically for vertical/horizontal motion control. By using a asymmetrical design and cascaded control strategy, Zhang *et al.* demonstrate a spincopter that has three translational DoF and two rotational DoF with only one rotor (Fig. 13 (d)).

A Coandǎ UAV is an aircraft that produces lifting force by utilizing the Coandǎ effect. Specifically, the Coandǎ effect is caused by the tendency of a jet of fluid to follow an adjacent surface and to attract the surrounding fluid. Thanks to the Bernoulli principle, in which pressure is low when speed is high, a Coandǎ UAV can generate enough lifting force to hover in the air when the Coandǎ effect is strong enough. Han *et al.* developed a Coandǎ UAV in a flying saucer shape (Fig. 13 (e)). By attaching additional servo motors onto the UAV for flap control, their Coandǎ UAV is able to perform VTOL and horizontal movements in the air.

Parafoil UAVs (Fig. 13 (f)) and kite UAVs (Fig. 13 (g)) resemble the shapes and flying principles of a parafoil or kite. For an aerial cargo delivery application, Cacan *et al.* improved the landing accuracy of an autonomous parafoil UAV with the assistance of a ground-based wind measurement system (Fig. 13 (f)) while Christoforou develop a robotic kite UAV that can surf automatically in the air (Fig. 13 (g)).

## Discussion and Final Remarks

While we have covered and selected more than one thousand UAV papers in several top journals and conferences since 2001, we focused on the robotic communities (TRO, TME, IJRR, RAS, IROS, ICRA, HRI, ROMAN). To extend the survey, we could expand into journals/conferences in the aerospace and aeronautics communities, such as International Journal of Robust and Nonlinear Control, Journal of Guidance, Control, and Dynamics, and International Conference on Unmanned Aircraft Systems. UAVs from the commercial sectors would also provide fertile ground. To name a few, the DJI Phantom 4 and YUNEEC Typhoon H ) appear to possess advanced path planning, human tracking, and obstacle avoidance algorithms. However, private companies often do not provide detailed technical information to the public.

In the Part II of this survey, we cover the trends in aerial robotics by discussing three emerging topics---(i) holonomic UAVs, a special type of UAV that can perform horizontal motions while maintaining orientation; (ii) localization and mapping with UAV; and (iii) human-drone interaction.
