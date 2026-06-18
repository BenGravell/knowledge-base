Towards Open-Source and Modular Space Systems with ATMOS

In the near future, autonomous space systems will compose many of the deployed spacecraft. Their tasks will involve autonomous rendezvous and proximity operations with large structures, such as inspections, assembly, and maintenance of orbiting space stations, as well as human-assistance tasks over shared workspaces. To promote replicable and reliable scientific results for autonomous control of spacecraft, we present the design of a space robotics laboratory based on open-source and modular software and hardware. The simulation software provides a software-in-the-loop architecture that seamlessly transfers simulated results to the hardware. Our results provide an insight into such a system, including comparisons of hardware and software results, as well as control and planning methodologies for controlling free-flying platforms.

## Introduction

The space sector has experienced significant growth in the last decade. Such growth is not only due to the decreased cost of access to space through multiple commercial operators, but also due to the maturation of existing technologies and, consequently, reduced pricing for equipment. In the last twenty to thirty years, a few academic and industrial research facilities have been created to test space systems by replicating motion in microgravity on Earth. These facilities primarily rely on granite tables, resin floors, or other flat-calibrated surfaces such as optic tables.

The remainder of the article is divided as follows: in Sec. 2, we introduce the available facilities. Sections 3 and detail the hardware and software of the proposed modular and open-source platform, ATMOS, while Sec. 5 discusses its autonomy capabilities. Ending the manuscript, Sec. 6 provides preliminary results of the proposed hardware and software package along with a small discussion on these. Section 7 concludes the article.

## Discussion and Conclusions

An overview of existing space robotics research facilities and the different strategies used to achieve frictionless motion has been presented, as well as platform limitations. Based on these works, we created the KTH Space Robotics Laboratory with its modular free-flying ATMOS platforms and multiple support systems.

As a significant component of our contribution is the open-source availability of both the hardware and the software of this facility, it is important to qualitatively assess its potential impact on the community. To this end, we are maintaining an open repository of laboratories using ATMOS or PX4Space, available in Due to the flexibility of PX4Space, adapting the software to other free-flyers requires only parameter adjustments regarding thruster placement and inertial parameters. It is also possible to adjust PX4Space to propeller-based actuation using the control and metric allocation modules developed in our software stack.
