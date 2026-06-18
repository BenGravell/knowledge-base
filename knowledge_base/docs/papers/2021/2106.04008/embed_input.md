<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Widening Access to Applied Machine Learning with TinyML

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Broadening access to both computational and educational resources is critical to diffusing machine-learning (ML) innovation. However, today, most ML resources and experts are siloed in a few countries and organizations. In this paper, we describe our pedagogical approach to increasing access to applied ML through a massive open online course (MOOC) on Tiny Machine Learning (TinyML). We suggest that TinyML, ML on resource-constrained embedded devices, is an attractive means to widen access because TinyML both leverages low-cost and globally accessible hardware, and encourages the development of complete, self-contained applications, from data collection to deployment. To this end, a collaboration between academia (Harvard University) and industry (Google) produced a four-part MOOC that provides application-oriented instruction on how to develop solutions using TinyML. The series is openly available on the edX MOOC platform, has no prerequisites beyond basic programming, and is designed for learners from a global variety of backgrounds.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It introduces pupils to real-world applications, ML algorithms, data-set engineering, and the ethical considerations of these technologies via hands-on programming and deployment of TinyML applications in both the cloud and their own microcontrollers. To facilitate continued learning, community building, and collaboration beyond the courses, we launched a standalone website, a forum, a chat, and an optional course-project competition. We also released the course materials publicly, hoping they will inspire the next generation of ML practitioners and educators and further broaden access to cutting-edge ML technologies.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The past two decades have seen machine learning (ML) progress dramatically from a purely academic discipline to a widespread commercial technology that serves a range of sectors. ML allows developers to improve business processes and human productivity through data-driven automation. Given applied ML's ubiquity and success, its commercial use should only increase. Existing ML applications cover a wide spectrum that includes digital assistants (mitchell1994experience digital-assistant-2, ), autonomous vehicles (ml-autonomous ml-autonomous-2, ), robotics (ml-tossing-bot, ), health care (ml-healthcare, ), transportation (ml-transport ml-transport-2, ), security (ml-security, ), and education (ml-education ml-education-2, ), with new application use cases continuously emerging every few days.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proliferation of this technology and associated jobs have great potential to improve society and uncover new opportunities for technological innovation, societal prosperity, and individual growth. But it all rests on the assumption that everyone, globally, has unfettered access to ML technologies, which isn't the case.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Expanding access to applied ML faces three challenges. First is a shortage of ML educators at all levels (brown_ai_2019 gagne_global_nodate, ). Second is insufficient resources, as training and running ML models often requires costly, high-performance hardware, especially as data sets continue to balloon. Third is a growing gap between industry and academia, as even the best academic institutions and research labs struggle to keep pace with industry's rapid progress. Addressing these critical issues requires innovative education and workforce training to prepare the next generation of applied-ML engineers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents a pedagogical approach, developed as an academic and industry collaboration led by Harvard University and Google, to address these challenges and thereby increase global access to applied ML. The resulting course, TinyML on edX, focuses not only on teaching the topic by exploring real-world TinyML applications running on low-cost embedded systems, but it also considers the ethical and life-cycle challenges of industrial product development and deployment (see Figure 1).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To improve accessibility we employ both cloud computing and low-cost hardware. We leverage Google's free, open-source TensorFlow and Colaboratory tools along with globally accessible inexpensive embedded devices from Arm and Arduino. We believe hands-on learning that transcends the underlying ML equations is essential. To this end, we focus our approach on TinyML.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Tiny Machine Learning (TinyML)*, a rapidly growing subfield of applied ML, is a prime candidate for enabling hands-on education globally. This budding area focuses on deploying simple yet powerful models on extremely low-power, low-cost microcontrollers at the network edge. TinyML models require relatively small amounts of data, and their training can employ simple procedures. Furthermore, as TinyML can run on microcontroller development boards with extensive hardware abstraction, such as Arduino products, deploying an application onto hardware is easy. TinyML enables a variety of always-on applications for battery-powered devices--for instance, environmental monitoring and industrial predictive-maintenance analytics. Moreover, the same cost and efficiency benefits open the door to distributed TinyML systems working in concert at the "edge" of the cloud-computing network.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since TinyML systems are becoming powerful enough for many commercial tasks, learners can acquire skills that can directly apply to their professional careers and future job prospects. The lessons of complete-TinyML-application design, development, deployment and management are also transferable to large-scale ML systems and applications, such as those in data centers and mobile devices. This technology thus provides an attractive entry into applied ML.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach to applied ML through the lens of TinyML provides experience with the complete industrial ML workflow, and it also explores the ethics of software deployment--crucial knowledge for the applied-ML workforce. Creating an ML system is a high-stakes endeavor since inaccurate or unpredictable model performance can erode consumer trust and reduce the chance of success. So understanding ethical reasoning is a crucial skill for ML engineers. To this end, we collaborated with the Harvard Embedded EthiCS program to develop and integrate a responsible-AI curriculum into each course, providing opportunities to practice identifying ethical challenges and thinking through potential solutions to concrete problems, many of which are based on real-world case studies.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

To broaden and widen access, we aimed to provide TinyML on a globally available platform that lets users benefit at no cost from instructional resources. We therefore deployed our pedagogical approach on edX, a MOOC provider created by Harvard and MIT that hosts university-level courses in many disciplines. Notably, professionals can choose to prove their newly earned skills with a certificate, available for a small fee, once they satisfy the testing requirements. To foster collaboration and continued learning beyond this edX course, we developed a standalone website, a Discourse forum, a Discord chat, and an optional course-project competition.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We launched the core TinyML edX series, comprising three sequential courses, between October 2020 and March 2021; an optional fourth course is under development. On average, more than 1,000 new students enroll each week. After eight months, over 40,000 have enrolled from 170 countries. They come from diverse backgrounds and experiences, ranging from complete novices to experts who want to master an emerging field. Feedback suggests this strong enrollment may owe to the unique collaborative structure we foster between students, teachers, and industry leaders. Shared ownership between Harvard faculty and staff and Google instructors and engineers appears to give participants confidence they are gaining skills that industry needs both today and tomorrow. Moreover, we recognize that opportunities to interact with experts is both encouraging and validating.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Focus on application-based pedagogy that covers all ML aspects. Instead of isolated theory and ML-model training, show how to physically design, develop, deploy, and manage trained ML models.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Work with industry and academic leaders to aid learners in developing the skills that industry requires today and will require in the foreseeable future.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Raise awareness of the ethical challenges associated with ML and familiarize learners with ethical-reasoning skills to identify and address these challenges.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prioritize open access to students worldwide by teaching TinyML at a global scale through a MOOC platform using low-cost hardware that is available anywhere.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Build community by providing a variety of platforms so participants can learn collaboratively and showcase their work no matter where they live.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

We hope the approach we devised brings ML to more people. As such we have open sourced our courseware materials which can be found at and note that this paper is part of a broader effort to enable activities such as TinyML4 Developing Countries (TinyML4D) and TinyML4 Science, Technology, Engineering, and Mathematics (TinyML4STEM).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

We have organized the rest of the paper as follows. It begins with a discussion of the criteria for increasing access to applied ML (Section 2). We then explain both why TinyML is a useful entry to practical ML and how our courses meet those criteria (Section 3). Next, the paper describes our series (Section 4) and how we integrated ethics throughout (Section 5). We then detail how we quickly and efficiently deployed TinyML by innovating in both multimedia production and the use of MOOCs as well as other online platforms (Section 6), in addition to analyzing early data on our courses' impact (Section 7). Finally, we introduce the TinyML Open Education Initiative: our effort to further broaden the courses' impact through activities such as TinyML4STEM (Section 8). To provide a balanced viewpoint, we discuss some limitations of our approach and suggest alternatives (Section 9). Finally, we conclude the paper with the main takeaways and the lessons learned (Section 10).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Challenges and Opportunities", "weight": 1.0} -->

We propose three criteria to empower applied-ML practitioners. First, no one size fits all with regard to interest, experience, and motivation, especially when broadening participation. Second, given ML innovation's breakneck pace, academic/industrial collaboration on cutting-edge technologies is paramount. Third, learners who wish to prepare for ML careers need experience with the entire development process from data collection to deployment, and they must understand the ethical implications of their designs before deploying them.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Student Background Diversity", "weight": 1.0} -->

A major challenge in expanding ML access is that participants begin applied-ML courses with diverse background knowledge, work experience, learning styles, and goals. Hence, we must provide multiple on-ramps to meet the needs of a varied population.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Student Background Diversity", "weight": 1.0} -->

Participants include high-school and university students who want to learn about AI for the first time. Not only will this knowledge empower them to develop cutting-edge applications, but it will also give them an edge in their careers, as many employers expect new hires to have some ML background.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Student Background Diversity", "weight": 1.0} -->

Other participants are industry veterans looking to either pivot their careers toward ML or study the landscape of the TinyML field. For example, some are computer-systems engineers who want to learn about ML in general. Others are ML engineers and data scientists who want to expand their skills by applying ML. Yet others are doctors, scientists, or environmentalists who are curious about how TinyML technology could transform their fields.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Student Background Diversity", "weight": 1.0} -->

Other participants are self-taught, makers, tinkerers, and hobbyists who want to build smart "things" based on emerging technologies. This group typically operates at the systems level, drawing on prior art, but they want to understand how different components or functional blocks fit together to create intelligent ML devices.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Student Background Diversity", "weight": 1.0} -->

Given this broad spectrum, we have a unique opportunity to enable inclusive learning for all despite differing backgrounds and expertise. But we must provide multiple on-ramps. Specifically, we chose to structure the course in a spiral that sequentially addresses the same concepts with increasing complexity (harden1999spiral, ). Doing so ensures that not only do participants reinforce fundamentals while picking up new details, but they also master important objectives at every stage. This approach has been shown to improve learning while meeting each individual's objectives (neumann2017robust, ).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Need for Academia/Industry Collaboration", "weight": 1.0} -->

Expanding ML access requires the expertise of academia and industry. Academia is strong in structured teaching: it creates in-depth, rigorous curricula to impart a deep understanding of a field. Conversely, industry is more pragmatic, developing the skills necessary for employment. These approaches are complementary.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Need for Academia/Industry Collaboration", "weight": 1.0} -->

Also, ML is moving rapidly thanks largely to industry's access to rich data. Analysis of ML-research publications at the NeurIPS ML conference suggests industry leads ML innovation (chuvpilo_2020, ). As such, industry has essential domain-specific knowledge that helps ground ML pedagogy in practical skills and real-world applications.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Need for Academia/Industry Collaboration", "weight": 1.0} -->

We belive that academia and industry must work in tandem to deliver high-quality, accessible, foundational, and skills-based ML content. Joining a strong academic institution and a industry leader in technology innovation, with a history of releasing free and accessible resources, makes students confident that they are learning the best skills from the best teachers.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Demand for Full-Stack ML Expertise", "weight": 1.0} -->

In ML, the "full stack"^11^1The term *full-stack* comes from historic career growth in web technologies and the Internet. It began as a series of loosely linked skills but now encompasses web development from the lowest level, the server, to the highest level, the web browser or mobile app. approach to building and using ML models is the core skill that will define future engineers. The engineers who bring long-term value to their industry are those who have the in-depth knowledge to innovate beyond well-known applications and scenarios. In fact, full-stack developers are now more numerous than all other developers combined, with 55% of developers identifying as full-stack in a 2020 report (stack_overflow, ).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Demand for Full-Stack ML Expertise", "weight": 1.0} -->

Our academia and industry collaboration can ensure the course series imparts the full-stack abilities that industry demands. Doing so requires content beyond the narrow, well-lit path of ML-model training, optimization, and inference. We therefore also focus on acquiring and cleansing data, deploying models in hardware, and managing continuous model updates on the basis of field results. Our hope is that learners will gain a whole new set of applied-ML skills and unlock new ideas.

<!-- chunk {"id": "body-0032", "role": "body", "section": "ML's Future Is Tiny and Bright", "weight": 1.0} -->

We employ Tiny Machine Learning (TinyML), a cutting-edge applied-ML field that brings the potential of ML to low-cost, low-performance, and power-constrained embedded systems and thereby enables hands-on learning. TinyML lets us impart ML-application design, development, deployment, and life-cycle-management skills.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Introduction to TinyML", "weight": 1.5} -->

TinyML refers to the deployment of ML resources on small, resource-constrained devices (Figure 2). It starkly contrasts with traditional ML, which increasingly focuses on large-scale implementations that are often confined to the cloud. TinyML is neither a specific technology nor a method per se, but it acts in many ways as a proto-engineering discipline that combines machine learning, embedded systems, and performance engineering. Similar to how chemical engineering evolved from chemistry and how electrical engineering evolved from electromagnetism, TinyML has evolved from machine learning in cloud and mobile computing systems.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Introduction to TinyML", "weight": 1.5} -->

The TinyML approach dispels the barriers of traditional ML, such as the high cost of suitable computing hardware and the availability of data. As Table 1 shows, TinyML systems are nearly two to three orders of magnitude cheaper and more power efficient than traditional ML systems. As such, this approach can serve in embedded devices at little to no cost and can handle tasks that go beyond traditional ML. The TinyML approach also makes it easy to emphasize the importance of responsible AI (Section 5).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Introduction to TinyML", "weight": 1.5} -->

Table 1. Cloud &amp; Mobile ML systems versus TinyML systems.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Introduction to TinyML", "weight": 1.5} -->

TinyML supports large-scale, distributed, and local ML tasks. Inference on low-cost embedded devices allows scalability, and their low power consumption enables distribution even to remote locations far from the electric grid. The number of tiny devices in the wild far exceeds the number of traditional cloud and mobile systems (icinsights, ). The ubiquity of tiny embedded devices makes TinyML a candidate for local ML tasks that were once prohibitively expensive, such as distributed sensor networks and predictive maintenance systems in industrial manufacturing settings.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Introduction to TinyML", "weight": 1.5} -->

TinyML applications are broad and continue to expand as the field gains traction. The approach's unique value stems primarily from bringing ML close to the sensor, right where the data stream originates. Therefore, TinyML permits a wide range of new applications that traditional ML cannot deliver because of bandwidth, latency, economics, reliability, and privacy (BLERP) limitations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Introduction to TinyML", "weight": 1.5} -->

Common TinyML applications include keyword spotting, visual wake words, and anomaly detection. Keyword spotting generally refers to identification of words that typically act as part of a cascade architecture to kick-start or control a system, such as a mobile phone responding to voice commands (ml-kws ml-kws-mobile, ). Visual wake words involve parsing image data to find an individual (human or animal) or object. This task can potentially serve in security systems (ml-security, ), intelligent lighting (ml-lighting, ), wildlife conservation (ml-wildlife ml-wildlife-2, ), and more. Anomaly detection looks for abnormalities in persistent activities (chandola2009anomaly, ). It has many applications in both consumer and commercial markets, such as checking for abnormal vibrations (ml-anamoly-vibration, ) or temperatures (ml-anamoly-temprature, ) to provide early warnings of potential failures and to enable preventive maintenance (ml-anamoly-earlywarning ml-anamoly-failure, ).

<!-- chunk {"id": "body-0039", "role": "body", "section": "TinyML for Applied ML", "weight": 1.0} -->

An applied-ML engineer should have this full-stack experience to appreciate the impact of the various ML-development stages on the end user. In prototypical ML, such as training large neural-network models in the cloud, learners are unable to participate locally in end-to-end ML development. For example, it is impossible to require them to collect millions of images (akin to ImageNet (deng2009imagenet, )) for large and complex tasks, such as general image classification. Even more difficult is asking all learners to buy the computational resources to train a complex ML model and then evaluate its performance in the real world.^22^2Just because a trained model performs well on a test data set does not automatically mean it will perform well in the real world.

<!-- chunk {"id": "body-0040", "role": "body", "section": "TinyML for Applied ML", "weight": 1.0} -->

By contrast, the small form factor and domain-specific tasks of TinyML enable the full ML workflow, starting from data collection and ending with model deployment on embedded devices. Students thereby gain a unique experience. For example, to implement keyword spotting in their native language, course participants learn to collect their own speech data (e.g., by saying "yá'át'ééh," which is Navajo for "hello"), train a model on that data, deploy it in an embedded device, and test the device in their community.

<!-- chunk {"id": "body-0041", "role": "body", "section": "TinyML for Applied ML", "weight": 1.0} -->

Such activities create an immersive learning experience, and they are feasible with TinyML because they only require about 30--40 samples of spoken keywords---easy to collect (only from people with their explicit consent) using a laptop with a web browser and microphone. Learners can then train the model using Google's free Colab environment (bisong2019google, ) and deploy it in a TinyML device using TensorFlow Lite for Microcontrollers (david2020tensorflow, ) or another open-source software technology. This approach allows small keyword-spotting models (about 16KB) to run efficiently on low-cost, highly constrained hardware (less than 256KB of RAM).

<!-- chunk {"id": "body-0042", "role": "body", "section": "TinyML for Expanding Access", "weight": 1.0} -->

The most difficult task in expanding applied-ML access is making low-cost hardware available anywhere. Cloud-ML technologies cost thousands of dollars, and their physical power, scale, and operational requirements limit their accessibility. Mobile-ML devices are more affordable and pervasive, but their availability is still limited because of network-infrastructure requirements and other factors.

<!-- chunk {"id": "body-0043", "role": "body", "section": "TinyML for Expanding Access", "weight": 1.0} -->

Research shows that although smartphones have become more affordable, their cost remains a barrier in many low- and middle-income countries (LMICs) (bahia2020state, ). Statista estimates only 59.5% of the world's population has Internet access, with large offline populations residing in both India and China (statista_2021, ). According to Pew Research, 76% of individuals in advanced economies have smartphones compared with 45% in emerging economies. Last in the latter group is India, where only 24% of the population has a smartphone (silver_2020, ). Students and teachers in many developing countries lack the resources necessary to learn and use traditional ML.

<!-- chunk {"id": "body-0044", "role": "body", "section": "TinyML for Expanding Access", "weight": 1.0} -->

In contrast, TinyML devices are low cost and pervasive. They are readily accessible, enabling hands-on learning anywhere in the world, and their portability eases demonstration of the complete applied-ML workflow in a realistic setting. Furthermore, TinyML applications are more numerous and easier to deploy than mobile-ML and cloud-ML applications. However, despite the wide availability of tiny devices, there is little material for teaching TinyML (see Figure 3). The number of general-ML courses far exceeds the number of TinyML courses (or, more generally, embedded-ML courses).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Applied-TinyML Specialization", "weight": 1.0} -->

We developed an applied-ML course specialization focusing on TinyML. Our specialization provides multiple on-ramps to enable a diverse learner population. Moreover, because TinyML is easy to deploy on hardware and test in the real world, it allows us to systematically explore applied ML's vast design space (algorithms, optimization techniques, etc.). It also lets us incorporate responsible AI in all four ML stages: design, development, deployment, and management at scale, which we discuss in greater depth in Section 5. We hope our description of this applied-ML specialization serves as a roadmap for anyone wishing to adopt the program.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Four-Course Spiral Design", "weight": 1.0} -->

The TinyML specialization comprises three foundational courses and one advanced course, which we consider optional. Participants would ideally start with the first course and work through the natural progression, but we allow them to go in any order they choose. Depending on their background, they can skip some courses and take the one most relevant to their knowledge and expertise.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Four-Course Spiral Design", "weight": 1.0} -->

Course 1: Fundamentals of TinyML 1.1. Course 1 Overview 1.2. The Future of ML Is Tiny and Bright 1.3. Tiny Machine Learning Challenges 1.4. Getting Started With ML 1.5. The ML Paradigm 1.6. The Elements of Deep Learning 1.7. Exploring ML Scenarios 1.8. Building a Computer-Vision Model 1.9. Responsible AI Design 1.10. Summary
Course 2: Applications of TinyML 2.1. Course 2 Overview 2.2. AI Life Cycle and ML Workflow 2.3. ML on Mobile and Edge Devices (Pt. 1) 2.4. ML on Mobile and Edge Devices (Pt. 2) 2.5. Keyword Spotting (KWS) 2.6. Data Engineering 2.7. Visual Wake Words (VWW) 2.8. Anomaly Detection 2.9. Responsible AI Development 2.10. Summary
Course 3: Deploying TinyML 3.1. Course 3 Overview 3.2. Getting Started 3.3. Embedded Hardware and Software 3.4. TensorFlow Lite Micro 3.5. Deploying Keyword Spotting 3.6. KWS Custom-Data-Set Engineering 3.7.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Four-Course Spiral Design", "weight": 1.0} -->

Deploying Visual Wake Words 3.8. Gesturing Magic Wand 3.9. Responsible AI Deployment 3.10. Summary

<!-- chunk {"id": "body-0049", "role": "body", "section": "Four-Course Spiral Design", "weight": 1.0} -->

Course 4: Scaling TinyML 4.1. Course 4 Overview 4.2. Profiling TinyML Systems 4.3. Benchmarking TinyML Systems 4.4. Micro NPUs &amp; Hardware Acceleration
4.5. Neural Architecture Search (NAS) 4.6. Machine Learning Operations (MLOps) 4.7. TinyML as a Service (TinyMLaaS) 4.8. Federated Learning for TinyML
4.9. Responsible AI Management 4.10. Summary

<!-- chunk {"id": "body-0050", "role": "body", "section": "Four-Course Spiral Design", "weight": 1.0} -->

Table 2. A breakdown of topics in the four TinyML courses. Each one has several activities, including videos, colabs, hands-on labs, quizzes, readings, assignments, tests, and discussion-forum participation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Four-Course Spiral Design", "weight": 1.0} -->

As we mentioned earlier, our application-focused spiral design covers the complete ML workflow, going outward from the middle. The curriculum begins with neural networks for TinyML in Course 1, expands to cover the details of TinyML applications in Course 2, deploys full TinyML applications in Course 3, and application management and scaled deployment in Course 4 (Figure 4). Our application focus increases learner engagement and enthusiasm (yang2017instructional, ), and our spiral design increases the technical depth over time while reinforcing the main concepts, providing multiple on-ramps and eventually enabling students to create their own TinyML application and deploy it on a physical microcontroller.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Four-Course Spiral Design", "weight": 1.0} -->

Table 2 shows a breakdown of the courses. Roughly, each one takes five or six weeks to complete. For a more detailed and up-to-date overview and links to all course materials, visit our courseware Github at

<!-- chunk {"id": "body-0053", "role": "body", "section": "Fundamentals of TinyML (Course 1)", "weight": 1.0} -->

Course 1 is titled Fundamentals of TinyML. Its objective is to ensure students understand the "language" of (tiny) ML so they can dive into future courses. TinyML differs from mainstream (e.g., cloud-based) ML in that it requires not only software expertise but also embedded-hardware expertise. It sits at the intersection of embedded-ML applications, algorithms, hardware, and software, so we cover each of these topics. As Figure 4 shows, the course focuses on a portion of the complete ML workflow. Moving to subsequent courses, we progressively expand participants' understanding of the rest of that workflow.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Fundamentals of TinyML (Course 1)", "weight": 1.0} -->

The course introduces students to basic concepts of embedded systems (e.g., latency, memory, embedded operating systems, and software libraries) and ML (e.g., gradient descent and convolution). The first portion emphasizes the relevance of embedded systems to TinyML. It describes embedded-system concepts through the lens of TinyML, exploring the memory, latency, and portability tradeoffs of deploying ML models in resource-constrained devices versus deploying them in cloud- and mobile-based systems.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Fundamentals of TinyML (Course 1)", "weight": 1.0} -->

The second portion goes deeper by focusing on the theory and practice of ML and deep learning, ensuring all students gain the requisite ML knowledge necessary for later courses. Through hands-on coding exercises, students explore central ML concepts, training their own ML models to perform classification using Python and the TensorFlow library in Google's Colaboratory programming environment.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Fundamentals of TinyML (Course 1)", "weight": 1.0} -->

We provide an overview of embedded systems and ML to ensure students recognize that the topics we cover in the specialization are relevant to their lives and careers, boosting motivation and retention (dyrberg2019motivational wladis2014investigation, ). For those with sufficient ML and embedded-systems experience, Course 1 is optional. By designing the series with these multiple on-ramps, we can meet participants wherever they are, regardless of their background and expertise.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Applications of TinyML (Course 2)", "weight": 1.0} -->

The objective of the second course is to give learners the opportunity to see practical (tiny) ML applications. Nearly all such applications differ from traditional ML because TinyML is all about real-time processing of time-series data that comes directly from sensors. As Figure 4 shows, we help students understand the complete end-to-end ML workflow by including additional stages, such as data preprocessing and model optimization. Moreover, when we revisit the same stages (e.g., model design and training), we employ spiral design to broach advanced concepts that build on Course 1.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Applications of TinyML (Course 2)", "weight": 1.0} -->

Course 2 examines ML applications in embedded devices. Participants study the code behind common TinyML use cases, such as keyword spotting (e.g., "OK Google"), in addition to how such front-end, user-facing, technologies integrate with more-complex smartphone functions, such as natural-language processing (NLP). They also examine other industry applications and full-stack topics, including visual wake words, anomaly detection, data-set engineering, and responsible AI.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Applications of TinyML (Course 2)", "weight": 1.0} -->

We take an application-driven approach to teaching the technical components. For example, we use the keyword-spotting (KWS) example to demonstrate the importance of preprocessing sensor inputs, showing the power of FFTs (fft, ) and MFCCs (mfcc, ) through coding exercises. We additionally explore the importance of holistic architecture by discussing the QoS metrics that evaluate KWS applications and the "cascade architecture" (i.e., ML models staged one after another for efficiency) for deploying them (gruenstein2017cascade, ). As another example, through the lens of the visual wake words (VWW) application, we introduce transfer learning (transfer-learning, ), teaching students to develop their neural-network models without voluminous training data and expensive hardware. Supplementing the theoretical concepts is a coding exercise that employs transfer learning on a pretrained MobileNet (mobilenet, ) model to detect whether an individual is wearing a mask---a real-world application that will resonate with learners in light of Covid-19.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Applications of TinyML (Course 2)", "weight": 1.0} -->

As a final example, we use anomaly detection (AD), in the context of predictive maintenance for manufacturing, to demonstrate the power (and limitations) of supervised learning and deep neural networks by exploring *k* nearest neighbors (knn, ), an unsupervised traditional-ML technique, and comparing it with autoencoders (baldi2012autoencoders, ), an unsupervised neural-network technique.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Applications of TinyML (Course 2)", "weight": 1.0} -->

The course not only teaches students about TinyML applications and their technical components, but also how to run and test these applications using TensorFlow Lite in Google's Colaboratory programming environment. This step completes the second learning spiral, providing a hands-on opportunity to explore full TinyML applications. The inclusion of TensorFlow Lite lets participants explore important TinyML topics (e.g., neural-network quantization), preparing them to add the next layer in Course 3: physical hardware. We intentionally avoided introducing microcontroller hardware until the third course so students could complete the first two entirely for free. They can then make an informed decision on whether to buy the low-cost hardware that Course 3 requires.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Deploying TinyML (Course 3)", "weight": 1.0} -->

Most instructional ML material focuses on models and algorithms, failing to provide hands-on experience in gathering input or training data, making decisions on the basis of a model's output, and testing models in the real world. Therefore, Course 3 explicitly focuses on demonstrating the complete ML workflow (Figure 4).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Deploying TinyML (Course 3)", "weight": 1.0} -->

We have found that learners are excited about using the knowledge they gain to solve real problems. But absent guidance in how to build an entire system, many become frustrated because they are unable to apply their knowledge. This issue arises in the form of questions that traditional courses leave out, such as "How can I find the training data for my problem?" and "What threshold should I use to decide whether a classification score is high enough for my application?" and "How do I go from an RGB-camera-image byte array to the float-tensor image my model needs?"

<!-- chunk {"id": "body-0064", "role": "body", "section": "Deploying TinyML (Course 3)", "weight": 1.0} -->

Providing universally applicable answers to all such questions is impossible. But alerting early learners to them and offering a set of comparable guided practical experiences reduces the frustration before these questions arise in their projects, hobbies, or careers. This is critical, as frustration squelches the desire to master the skills a field requires. Instead, we want to give students the support and confidence they need to overcome challenges and solve problems.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Deploying TinyML (Course 3)", "weight": 1.0} -->

"Deploying TinyML" mixes computer science and electrical engineering. It gives participants fundamental knowledge and hands-on experiences with ML training, inference, and deployment on embedded devices. Following the spiral pattern, it builds atop many of the techniques and applications from previous courses and adds new technical topics and extensions. Students develop and deploy full applications, such as KWS, person detection, audio/visual reaction, and gesture detection on their own microcontrollers.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Deploying TinyML (Course 3)", "weight": 1.0} -->

The course introduces TensorFlow Lite for Microcontrollers (david2020tensorflow, ), an embedded-ML software library that eases the task of efficiently running ML models on embedded hardware. Students learn how the library works, helping them appreciate the challenges that an embedded-ML-framework engineer faces in the real world. They also examine the library's APIs as they deploy applications such as KWS, VWW, and magic wand to their microcontrollers.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Deploying TinyML (Course 3)", "weight": 1.0} -->

Building on the concepts from the first two courses, we introduce new concepts such as multitenancy---that is, running more than one ML model at a time---when we revisit certain stages of the ML workflow (Figure 4). We present the tradeoffs between using multimodal learning that fuses sensor data versus using two separate models to make inferences. The former stresses the first half of the ML workflow (training), while the latter stresses the second half (deployment).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Deploying TinyML (Course 3)", "weight": 1.0} -->

A unique benefit of this course is the exercises that involve the entire ML process. Before they know it, students are implementing an entire TinyML application from beginning to end on a physical device they can hold in their hands. This approach gives our course the unique value of allowing participants to fully develop and use their own TinyML projects at home. This type of hands-on project-based learning is proven to enhance learning, motivation, and retention (krajcik2006project vesikivi2020impact, ). For instance, participants collect their own custom keyword data for training a KWS model, giving them first-hand experience with the challenges of getting ML models to work accurately. Some find that the tinyConv (tftinyconv, ) KWS model works well; others find that they must collect more data or adjust the preprocessing. A few individuals in this latter category are perplexed that even those improvements may fail to dramatically increase accuracy, finding that the 16 KB KWS model is too small. The point of the exercises is not necessarily to increase model accuracy, but to instead understand the challenges of applying ML models to the real world.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Deploying TinyML (Course 3)", "weight": 1.0} -->

The course uses the Tiny Machine Learning Kit, which we co-designed with Arduino for hands-, low-cost, accessible, project-based learning. This kit, shown in Figure 5 ‣ 4. Applied-TinyML Specialization ‣ TinyML on edX: Widening Access to Applied Machine Learning"), is globally accessible, and includes an Arduino board containing numerous sensors (microphone, temperature, humidity, pressure, vibration, orientation, color, brightness, proximity, gesture, etc.) that enable a wide range of TinyML applications. More importantly, it has a popular Arm Cortex-M-class microcontroller (martin2016designer, ) that binds the learning experience to reality. The kit provides everything a student needs to build TinyML applications for image recognition, audio processing, and gesture detection.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Deploying TinyML (Course 3)", "weight": 1.0} -->

After completing Courses 1, 2, and 3, students are eligible to receive the HarvardX/edX Tiny Machine Learning Certificate, testifying they are trained as full-stack TinyML engineers. We offer the certificate because many professional learners desire such awards to enhance their resumes and prove to potential employers that they have mastered particular skills. At this point in the series, participants have not only explored the technical and societal challenges that TinyML poses, but they have also gained hands-on experience with the complete TinyML-application pipeline: collecting data, developing and training models in the cloud using TensorFlow, testing them in the cloud using TensorFlow Lite, and deploying them in hardware with TensorFlow Lite for Microcontrollers.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Scaling TinyML (Course 4)", "weight": 1.0} -->

The first three courses bring learners up to speed on designing, developing, and deploying TinyML applications on a device. Course 4 builds on this foundation and considers scaled management of TinyML-application deployments. This advanced course covers two aspects of scaling. The first half focuses on "scaling up" the effectiveness of individual TinyML applications through performance benchmarking, model optimization, and hardware/software co-design. The second half focuses on "scaling out" TinyML applications from one device to thousands.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Scaling TinyML (Course 4)", "weight": 1.0} -->

In the scaling-up portion of the course, we start by introducing the concept of system-performance profiling through TinyMLPerf (banbury2020benchmarking, ) and other open-source, industry-standard benchmarks. Because embedded systems deal with sensor data in real time, the TinyML device must be able to keep up with the data rates. In safety-critical systems, such as automobiles, a slow response to new sensor inputs can be life threatening. Knowledge of benchmarking principles is therefore essential; it enables applied-ML engineers to compare ML systems in a fair and useful manner and to make informed decisions when selecting a device for a particular task.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Scaling TinyML (Course 4)", "weight": 1.0} -->

Next, given a suitable system, we discuss the art of picking a suitable model, emphasizing when and whether to be more code-centric (improve the model) or data-centric (improve the data set). The most accessible means of decreasing model latency is to change the neural-network architecture. Students can accelerate inference without changing any code by designing a new model that is sufficiently accurate yet requires fewer calculations. But designing ML-model architectures is difficult and time consuming because of the many decisions that affect model quality and latency: what type of neural network to choose, what size to make it, how many hidden layers and neurons to include, how to best initialize the network, and so forth. Fortunately, services have emerged to help design network architectures automatically. Cloud services such as AutoML (CloudAut6:online, ) and techniques such as neural-architecture search (NAS) (zoph2018learning, ) allow even developers with limited ML expertise to quickly train high-quality models that meet their needs. In TinyML, such services are essential because achieving efficiency means co-designing the MCU hardware, software, and models, a challenging task for humans.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Scaling TinyML (Course 4)", "weight": 1.0} -->

The course therefore introduces concepts such as AutoML and NAS, explaining the fundamentals so students can employ high-level automation tools with confidence.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Scaling TinyML (Course 4)", "weight": 1.0} -->

The second half of the course focuses on "scaling out" TinyML applications from one device to thousands. Applied-ML engineers must know how to manage such deployments as a production ecosystem may involve hundreds or thousands of devices. We thus offer a preview through the TinyML lens. We start by leveraging "ML operations" (MLOps) to develop, monitor, and improve a TinyML application. MLOps automates the complete workflow (Figure 4) as Figure 6 ‣ 4. Applied-TinyML Specialization ‣ TinyML on edX: Widening Access to Applied Machine Learning") shows. We discuss ways to automatically manage and process data, train ML models, version them, and evaluate, compare, and deploy them, all from the perspective of complete MLOps platforms. This approach introduces the advantages of an automatic ML workflow, which include managing the overwhelming complexity of ML deployments, reducing the burden of maintaining in-house ML knowledge, being more scientific, easing long-term maintenance, and ultimately improving the model's performance in the field.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Scaling TinyML (Course 4)", "weight": 1.0} -->

In addition, we also introduce TinyML as a service (TinyMLaaS), which allows production ecosystems to easily manage and integrate heterogeneous TinyML devices. Because embedded TinyML devices are specialized---from the ML compilers to the operating system and ML hardware---to achieve ultra-low-power energy efficiency, a highly fragmented ecosystem can result. Fragmentation limits a precompiled ML inference model's portability when the hardware changes. The model then requires recompilation for a particular device, leading to deployment complexity. To reap the efficiency benefits of hardware heterogeneity while coping with the fragmented ecosystem, we need a new "as-a-service" abstraction. To this end, we introduce learners to TinyMLaaS (doyu2021tinymlaas, ), a general method for tailoring an ML inference model to a specific device. It is a software abstraction layer that gathers information about the target device---such as the CPU type, RAM and ROM sizes, available peripherals, and underlying software---to generate the correct compiled inference model. The designated device then automatically downloads this generated inference model, and the process repeats for all other devices.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Scaling TinyML (Course 4)", "weight": 1.0} -->

Because TinyMLaaS enables firmware-over-the-air (FOTA) and software-over-the-air (SOTA) updates, it introduces privacy and security concerns for both the model and the data. Hence, we also cover how large device networks can train models while maintaining user privacy through federated learning (konevcny2016federated, ).

<!-- chunk {"id": "body-0078", "role": "body", "section": "Scaling TinyML (Course 4)", "weight": 1.0} -->

Participants who complete the four courses will have learned all the fundamentals of ML-model design, development, deployment, and management through the TinyML lens. This knowledge is invaluable for career advancement in this quickly emerging field.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Student Activities", "weight": 1.0} -->

People learn differently (pashler2008learning, ). To support many learning styles, we implemented proven strategies (lockman2020online, ) and a variety of methods (Figure 7). Our approach mixes video lectures, short readings, and coding exercises in Google's Colaboratory programming environment to teach and reinforce the course's main technical components. Thus, visual, auditory, and experiential participants all learn by their preferred method.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Student Activities", "weight": 1.0} -->

We keep the videos short (4--10 minutes). Research shows that people learn better from numerous short content modules than from a few long ones (guo2014video, ). Because some students will find that many of the coding components are new, we provide walk-throughs of major sections, numerous comments describing the code, and introductory text to explain the purpose of each code snippet.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Student Activities", "weight": 1.0} -->

In the first two courses, each section builds toward a coding assignment in Colaboratory to encourage project-based exploration and creativity. The assignments in Course 3 expand to full-on hardware deployment that lets students hold their own designed, trained, and deployed model in their hands and test it in the real world.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Student Activities", "weight": 1.0} -->

The activities grow in complexity and detail as students progress through the courses, following our spiral-design principle. Students thus gain confidence throughout, as complete application deployments can be challenging. Finally, we sought the input of industry veterans on our course staff to ensure the hands-on activities build relevant full-stack skills.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Student Activities", "weight": 1.0} -->

The courses also include formative multiple-choice quizzes throughout, focusing on the main concepts so students see their progress even if they do not understand every line of code. The quizzes also reinforce the importance of high-level tradeoffs and applied-ML concepts, which will be relevant to ML careers even if the technical stack changes. For those pursuing a paid certificate, we also included summary tests at the end of each section.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Student Activities", "weight": 1.0} -->

Finally, we provide many discussion forums that allow students to ask questions and get answers. Forums allow the course staff to support all participants regardless of their location. They also serve the dual function of building a community around the course. Our forums encourage students to ask any and all questions and to answer them for one another.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Student Activities", "weight": 1.0} -->

Each activity includes a strong ethics component, which we describe in detail later (Section 5). Briefly, however, we ask many open-ended questions to elicit student opinions on the opportunities and challenges of responsible TinyML-application design, development, and deployment. As the literature predicts (lockman2020online, ), many of these questions have led to conversations and debates between our online participants, despite their different geographic locations, ages, and technical backgrounds.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Accessible, Hands-on Learning", "weight": 1.0} -->

To enable hands-on learning anywhere in the world, we need a low-cost, self-contained yet extensible, approachable yet representative, flexibly abstracted, and globally accessible TinyML platform. Once again, microcontrollers are promising because they are inexpensive and widely available. So, to provide an easily accessible out-of-the-box experience, we custom designed the Tiny Machine Learning Kit (Figure 5 ‣ 4. Applied-TinyML Specialization ‣ TinyML on edX: Widening Access to Applied Machine Learning")) with Arduino. This section describes the kit and its development.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Accessible, Hands-on Learning", "weight": 1.0} -->

Systematic selection. The range of TinyML hardware and software options is wide, but we believe an ideal solution is fully self-contained yet extensible, approachable yet representative, and flexibly abstracted. As such, we searched for one that not only made it simple to integrate the sensors required for the course but also supported easy integration of additional sensors for future study.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Accessible, Hands-on Learning", "weight": 1.0} -->

Putting application-level software aside leaves two fundamental elements: hardware, from the microprocessor to peripherals and discrete circuitry, and software, from the application layer (our focus) to the silicon layer. An initial constraint on the field of potential microprocessors is the need to support TensorFlow Lite for Microcontrollers (david2020tensorflow, ), which is written in C++ and requires that the microcontroller support 32-bit computing.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Accessible, Hands-on Learning", "weight": 1.0} -->

We developed criteria for compatible microcontroller development boards, recognizing that an integrated off-the-shelf product would greatly increase accessibility. These criteria include a small form factor (it is *tiny* ML, after all), a low power budget (efficiency is critical to edge computing), a small system memory (some controllers have large memories, making them less accessible and limiting their range of application), sufficient clock speeds, wireless-communication capability (to enable periodic reporting and/or distributed systems), select sensor integration, and serial channels for extensibility. We defined similar criteria for the accompanying software, comprising the development environment, embedded framework, and logistics (fast, reliable distribution). Next, we added weights to the selection criteria and compiled the candidates in a Pugh matrix (pugh, ). We ranked a field of about two dozen hardware products, giving some preference to controllers that had undergone more-extensive testing---in particular, Arm's Cortex-M series (martin2016designer, ) and Espressif Systems' products (namely, the ) (esp32, ). Both of these embedded systems are widely popular.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Accessible, Hands-on Learning", "weight": 1.0} -->

The TinyML kit. Ultimately we selected the Arduino Nano 33 BLE Sense (arduino-nano, ) because it uniquely blends expert embedded-systems engineering and remarkable isolation of the application developer from many low-level hardware details (jamieson2011arduino, ). Furthermore, the Arduino framework and its software APIs ("cores") fit naturally with our spiral design. Arduino's many libraries and simple IDE are easy for inexperienced students to learn, yet it typically permits those interested in the "bare metal" to work their way down the embedded-software stack. Moreover, the Nordic nRF52840 Cortex-M4-based controller (nordic, ) on the Nano 33 BLE Sense development board, along with its Mbed real-time OS (mbed, ), represent industry-level hardware and software.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Accessible, Hands-on Learning", "weight": 1.0} -->

We also developed the Tiny Machine Learning Shield to enable plug-and-play integration of sensors that the Nano 33 BLE Sense lacks. In particular, it eliminates the need for users to make 18 individual connections between the microcontroller and the low-cost camera module we selected for the course---the OV7675 (ov7675, ), which typically sells for about US\$2. A series of Grove connectors (grove, ) line each side of the shield for connection to numerous additional sensors, which students can purchase for their own projects and integrate without soldering or low-level circuit design.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Accessible, Hands-on Learning", "weight": 1.0} -->

We bundled the Nano 33 BLE Sense with the shield, the OV7675 camera module, and a USB cable to form the Tiny Machine Learning Kit (Figure 5 ‣ 4. Applied-TinyML Specialization ‣ TinyML on edX: Widening Access to Applied Machine Learning")); learners can purchase a single item and be fully prepared for Course 3 for US\$49.99. To accommodate those few who prefer to purchase elements individually, we provide wiring diagrams and a custom Arduino software library so they can readily swap the OV7675 for the related OV7670 camera module.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Accessible, Hands-on Learning", "weight": 1.0} -->

Alternatives. In the months after we developed and announced our TinyML kit, similar boards emerged to provide alternative options. For example, the Pico4ML by ArduCam (pico4ml, ) is a notable single-board example that comes complete with a microphone, inertial measurement unit (IMU), and camera module, and is suitable for the course exercises. We are working to support some of these new and exciting hardware platforms to give students more flexibility with their projects.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Ethical & Responsible AI", "weight": 1.0} -->

Ethical and Responsible AI is about putting people, social benefit, and safety first. More specifically, ethical AI emphasizes the need for ML engineers to safeguard user privacy and security, mitigate algorithmic bias and discrimination, and ensure ML models perform reliably after deployment. It also extends to developing consumer trust. In this section, our goal is to shift learners from thinking about which ML technology is feasible to which is useful, with an understanding of how it will influence users and society.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Ethical Consideration of Ubiquitous ML", "weight": 1.0} -->

TinyML offers many helpful features, ranging from data privacy and security to low latency and high availability. Coupled with low-cost embedded hardware, these features make it a pervasive technology that can enable ML everywhere. TinyML sensors will monitor the environment in which they are deployed, be it mechanical or human, around the clock. With the prospect of ML everywhere comes a pressing need to address privacy, drift, bias, and other ethical issues.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Ethical Consideration of Ubiquitous ML", "weight": 1.0} -->

Fortunately, TinyML allows us to incorporate responsible AI into all four ML stages: design (Course 1), development (Course 2), deployment (Course 3), and scaling (Course 4). By embedding ethics into each TinyML course, we communicate the technology's ethical and social dimensions in a personal and practical manner.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Ethical Consideration of Ubiquitous ML", "weight": 1.0} -->

To achieve deep integration, we follow the Embedded EthiCS pedagogy at Harvard (EmbEth, ), where philosophers participate directly in computer-science courses to teach students how to think through the ethical and social implications of their work. We collaborated with a philosopher from this program to co-develop and include such material in our curriculum. Her commitment to learning the technical aspects of TinyML enabled us to customize the ethical content to meet the unique course needs of TinyML.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Ethical Consideration of Ubiquitous ML", "weight": 1.0} -->

By distributing responsible AI throughout the series, covering the entire ML workflow, students discover how ethical issues permeate all aspects of their work. Our aim is to introduce them to the conceptual tools for navigating these issues, in hopes they will view responsible AI as an active enterprise. Next, we describe our pedagogical goals for each responsible-AI unit, some examples we covered, and the exercises that reinforce the concepts.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Designing AI Responsibly (Course 1)", "weight": 1.0} -->

Access to, adoption of, and use of ML products is inequitably distributed. According to Pew Research, 64% of Americans believe technology companies create products and services that benefit people who are already advantaged, and 65% believe these companies fail to anticipate the societal impact of those offerings (techattitude, ).

<!-- chunk {"id": "body-0100", "role": "body", "section": "Designing AI Responsibly (Course 1)", "weight": 1.0} -->

To enable more-widespread, safer, and more-secure ML, we must raise awareness of its capabilities. Thanks to the low cost and accessibility of TinyML hardware, our students are diverse, and they will probably have to address different social and cultural factors when designing ML applications. To ensure they all can anticipate the effects of ML products and ensure equitable access, our approach to responsible AI focuses on forming a vision of both the problem to be solved and the people a solution will affect.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Designing AI Responsibly (Course 1)", "weight": 1.0} -->

We believe that by taking an active role in responsible ML design, students will be better able to address ethical challenges such as bias, fairness, and security. We therefore cover real-world examples, such as a Winterlight Labs auditory test for Alzheimer's disease. In this case, research revealed that nonnative English speakers are more likely to be mistakenly flagged as having Alzheimer's (Fraser2016LinguisticFI, ). In a discussion forum, students reflected on what the product designers could have done differently to avoid this failure. Such activities reinforce the importance of considering diverse user perspectives during the design phase, as doing so can inform data-collection decisions that mitigate ML bias.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Designing AI Responsibly (Course 1)", "weight": 1.0} -->

In a subsequent forum, learners practice ethical reasoning about the consequences of a KWS model's failure in terms of Type I (false positive) and Type II (false negative) errors. In this case, a false positive would result in audio being recorded, unbeknownst to the user, and sent to the cloud. A false negative means the device failed to activate when the user spoke the wake word. Students must justify their decision to optimize the model for high precision, thereby minimizing false positives, or to optimize for high recall, thereby minimizing false negatives.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Designing AI Responsibly (Course 1)", "weight": 1.0} -->

For the KWS activity, nearly all participants chose to optimize for high precision to minimize the risk of privacy violations. Interestingly, one provided a justification based on sustainability concerns related to unnecessary data transmission and storage in the cloud. Those who decided to optimize for high recall cited a variety of reasons. One noted that although people claim to value privacy, they tend to prioritize convenience. In contrast, another suggested enacting privacy measures elsewhere to offset the potential harm of optimizing for high recall. Lastly, yet another student prioritized model performance to meet user expectations. That student claimed the burden of preserving privacy should fall on the user, who has the ability to decide whether to purchase the product. There is no right or wrong answer. Our desire is to spur self-reflection and foster constructive discussion among learners from different backgrounds and cultures.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Developing AI Responsibly (Course 2)", "weight": 1.0} -->

Any developer employing ML must be aware of how data-collection bias and fairness affect application behavior. Our courses use public data sets, including Speech Commands (warden2018speech, ), Mozilla Common Voice (ardila2020common, ), ImageNet (deng2009imagenet, ), and Visual Wake Words (chowdhery2019visual, ), for nearly all of the programming assignments. Most data sets, however, have demographic-representation problems (pmlr-v81-buolamwini18a, ). For example, despite crowdsourcing efforts to increase diversity, the Common Voice data set lacks equal gender representation (only 24% of English-data-set contributors who revealed their gender are female) (lackoffemalevoicesincommonvoice, ).

<!-- chunk {"id": "body-0105", "role": "body", "section": "Developing AI Responsibly (Course 2)", "weight": 1.0} -->

Our goal is for students to see how data collection, bias, and fairness intertwine, as well as to equip them to mitigate the problems. because they are working with KWS models, we cover real-life biases relevant to this kind of ML application. For instance, research shows that voice-recognition tools struggle to identify African American Vernacular English, causing popular voice assistants to work less well for black individuals (Koenecke7684, ). Similarly, research shows that voice recognition struggles to identify nonnative English speakers and those with speech impairments (10.1145/3379503.3403563, ). To acquaint learners with recent work in mitigating bias, we discuss Project Euphonia, a initiative that launched in 2019 with the goal of collecting more data from individuals with speech impairments or heavy accents to fill the gaps in voice data sets (shor2019personalizing, ).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Developing AI Responsibly (Course 2)", "weight": 1.0} -->

We created a Colab activity that uses Google's What-If Tool (WIT) (google_2020_wit, ), based on its Responsible AI tool kit (google_2020, ). The WIT is one of the company's many open-source, interactive visualization tools for investigating trained-ML-model behavior with minimal coding. In this exercise, participants practiced ethical reasoning by exploring a real-life data set, identifying sources of bias, and evaluating threshold-optimization strategies for fairness. For the WIT activity, students noted how the visual representations fostered a deeper understanding of issues pertaining to fairness. One claimed that the focus on confusion matrices in particular was an effective way to clearly distinguish between the fairness metrics. In general, learners appreciated the opportunity to try out the WIT.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Deploying AI Responsibly (Course 3)", "weight": 1.0} -->

Even after designing and developing an ML model, deployment raises a new set of ethical challenges. For example, TinyML systems are often touted for preserving privacy. When an embedded system processes data locally (close to the sensor) rather than transmitting it to the cloud, we tend to believe it protects user privacy. But user interaction with the model raises new privacy and security concerns (prabhu2021privacypreserving, ). Moreover, ML interacting with a dynamic real-world environment using sensors raises concerns about model drift^33^3*Model drift* generally refers to prediction-accuracy degradation owing to environmental changes. over a product's lifetime.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Deploying AI Responsibly (Course 3)", "weight": 1.0} -->

To the extent that TinyML enables ML everywhere, the privacy, security, and even model-drift risks could be more widespread compared with traditional ML. To familiarize students with these risks, we cover real-life examples, such as doorbells that share data with law enforcement (doorbelldata, ) and fitness devices that leak user information (fitnessleak, ).

<!-- chunk {"id": "body-0109", "role": "body", "section": "Deploying AI Responsibly (Course 3)", "weight": 1.0} -->

Our goal is to equip students with strategies to mitigate these risks when deploying trained models in embedded devices. Importantly, the mitigation strategies available to traditional ML systems are sometimes unattractive or infeasible for TinyML. For instance, the resource constraints of an embedded device, such as low power and small memories, complicate implementation of robust security systems and model retraining. Therefore, we acquaint course participants with a wide array of strategies, such as minimizing the transmitted and stored data to preserve user privacy, minimizing hardware design to limit vulnerability to attackers, and running supervised experiments in the real world before releasing ML models.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Deploying AI Responsibly (Course 3)", "weight": 1.0} -->

Inspired by research showing we can use inaudible ultrasonic noise to trigger or eavesdrop on KWS models (zhang2017dolphinattack, ), we created an exercise that gives students hands-on experience attacking a KWS model. They trigger a false positive---"yes"---with seemingly innocent but adversarial static noise (Figure 8 ‣ 5. Ethical & Responsible AI ‣ TinyML on edX: Widening Access to Applied Machine Learning")), which in a real application would cause the system to constantly record and transmit the audio. This experience builds on our videos and readings and makes the security threat real---a crucial part of any major security-awareness program at large (reinheimer2020investigation, ). At the same time, it is also a cautionary tale of ML's limitations, a lesson all applied-AI engineers should learn.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Deploying AI Responsibly (Course 3)", "weight": 1.0} -->

To further reinforce this point, a subsequent discussion forum allows course participants to practice ethical reasoning to determine when malicious triggering of a false positive can cause serious harm. Some have noted that this vulnerability would be most likely to cause harm where security is a paramount value, such as using KWS to grant access to a secure space or to initiate a financial transaction. One student drew a connection to the practice of ethical hacking, or penetration testing, and the possibility of developing adversarial data for retraining the model to be more resilient. Interestingly, another noted that since users lack the ability to fix security issues, their only option is to stop using the device. But this choice ultimately depends on whether the company informs customers about the vulnerability. Lastly, one student claimed the adversarial example was more reliable than that student's own voice for triggering a "yes." The course staff then responded, prompting a discussion of data-set bias and the likelihood that American male accents are overrepresented in the data.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Scaling AI Responsibly (Course 4)", "weight": 1.0} -->

Many ethical implications require consideration when applying technology. Even minor biases, which can be difficult to detect in the proof of concept, can have a major impact when appearing in thousands or millions of devices.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Scaling AI Responsibly (Course 4)", "weight": 1.0} -->

This problem highlights the need to treat responsible ML as an iterative process. Rather than introduce entirely new ethical considerations, we revisit and expand on previous ones. For instance, to guide students in cleaning up a test data set before they conduct benchmarks, we revisit the ethical issues of data collection and bias. Similarly, we revisit privacy in depth once participants become acquainted with federated learning.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Scaling AI Responsibly (Course 4)", "weight": 1.0} -->

We are incorporating an active learning exercise using Google's Model Card Toolkit (MCT) (Mitchell_2019, ). Model cards are a reporting mechanism that can increase model transparency and facilitate the exchange of information between model creators, users, and others. This exercise requires that students practice using the model-card framework to document information relating to the model's development, performance, and ethical considerations.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Scaling AI Responsibly (Course 4)", "weight": 1.0} -->

We additionally discuss the environmental impact of large-scale TinyML networks, as the production and maintenance of billions of MCUs can have lead to substantial carbon emissions. Beyond the ethical pitfalls of scaling TinyML, we cover the potential positive social impact this technology can have in domains such as environmental sustainability, public health, and AI equity.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Access via MOOCs", "weight": 1.0} -->

In this section we describe how we leveraged technology to make the TinyML specialization broadly accessible and highlight important considerations made to ensure we supported our remote learners.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Massive Open Online Course", "weight": 1.0} -->

Our goal was to reach a global audience. We therefore chose to employ massive-open-online-course (MOOC) platforms. Examples such as edX and Coursera are ideal for making the content globally accessible; students need not travel to a different country to learn. These platforms host a wide variety of university-level courses and are generally cheaper than equivalent academic and professional training thanks to the economics of scale (belleflamme2014, ). We deployed the TinyML specialization on edX through HarvardX.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Massive Open Online Course", "weight": 1.0} -->

Participants can audit the course for free or pay to earn a professional certificate. Since they can "upgrade" to a professional certificate at any point during the course, both students and professionals can try before they buy, encouraging more to enroll. Although the professional certification includes summary tests that are absent from the audit version, we designed the curriculum so individuals who are just auditing learn the same crucial principles. Thus, all can attend the entire class, developing their skills for free. At the time of this writing, the number of auditors far outweighs the number of paying students by more than order of magnitude.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Massive Open Online Course", "weight": 1.0} -->

The course is asynchronous and self-paced rather than instructor led. Students progress through the material at whatever speed they find comfortable. But unlike in-person courses, interaction between students and staff is minimal, forcing staff to develop high-quality, self-explanatory, and self-sufficient materials that rely heavily on media (which we describe in greater detail in Section 6.2).

<!-- chunk {"id": "body-0120", "role": "body", "section": "Massive Open Online Course", "weight": 1.0} -->

Unlike most MOOCs, Course 3 employs the TinyML kit (Section 4.7) for hands-on learning. To maximize hardware accessibility, we worked with Arduino to make a custom all-in-one kit globally available for purchase through either that company's website (arduino, ) or one of its many distributors. We also provided a detailed bill of materials for students who wish to buy individual components instead. The main benefit of this approach is that it improves the efficiency for the host institutions (Harvard and Google) by reducing the burden on them for managing inventory and shipping logistics (taxes, international shipping rates, etc.).

<!-- chunk {"id": "body-0121", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

The typical development timeline for a series of online courses, such as the ones we described in Section 4, is about two years---far too long to keep up with changing ML technology. Applied ML, especially in the context of TinyML, remains a nascent yet quickly developing field. Therefore, media production for the online curriculum must be rapid to ensure the material is timely and relevant and to ensure broad access.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

We compressed the media-production time greatly, achieving an average development cadence of 6--8 weeks per course. To maintain this cadence, we created a custom remote-media-production workflow. We produced the TinyML course under the specter of Covid-19, but regardless of the safety limitations, a remote production strategy would still have been the only way to achieve these quick results. Remote production methods offer flexibility and allow an international crew to make contributions, meaning the process continues around the clock. Regardless, no matter when and how it is done, creating a flexible workflow requires a principled content-design approach, and advanced technology is necessary for rapid progress. The following breakdown can serve as a roadmap for others attempting to follow a similar approach.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

Production design. To expand access such that our effort meets the needs of a global audience (Section 2), we built our media-production strategy around five critical ingredients: compelling instructional narrative, best media practices for online learning, a diverse and skilled production team, prioritized use of production equipment, and willingness to innovate.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

A *compelling instructional narrative* that whets student interest is critical, as all great media experiences unite around a good story. TinyML offers a sound narrative because it provides an accessible, hands-on introduction to ML (Section 3). We aimed to communicate with a global audience and provide the practical knowledge for building complete, relevant TinyML applications and tools.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

Effectively communicating that narrative requires *best media practices for online learning*. Decisions made in postproduction often hold more weight than any others. For example, the decision of when to show the instructor, slides, or both in a picture-in-picture cut versus when to display graphics or other visual/auditory information can affect the viewer's cognitive load and overall learning (chen2015effects mayer2020five, ). When in doubt, Mayer's "12 principles of multimedia learning" (mayer2005cambridge, ) is an excellent place to discover such general practices for enhancing the student's experience.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

From the start, we determined the primary media types we would produce to hold students' attention and maintain their cognitive load balance (chen2015effects, ). We chose picture-in-picture and split-screen formats, allowing us to show the instructor or other imagery in full-screen mode to focus on the most important aspects of the presentation (Figures 9). We emphasized instructor screen time, however, to improve student learning (wang2020does, ).

<!-- chunk {"id": "body-0127", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

A *geographically distributed and responsive team* is necessary to quickly produce highly sophisticated content, especially for an emerging technical field. Our media team included a producer and director to establish a creative vision and ensure media delivery, a senior editor to assemble and craft the videos, a motion-graphics designer to provide custom graphical elements for our brand, and a production assistant to wrangle data, review content, and integrate the final videos into the platform. This team was relatively lean. One additional advantage was that contributors were scattered across 12 time zones (San Francisco to Boston to London to Mumbai), meaning at all times someone was awake and working on the project.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

A crucial ingredient to quickly producing content is *prioritized use of production equipment*. The remote nature of the production and the Covid-19 precautions only heightened this need. For example, webcams and audio supplies were sold out or on back order because people were setting up home offices so they could continue to work. Fortunately, we were able to make acceptable compromises and buy equipment in a way that ensured the greatest impact. We prioritized production-equipment purchases as follows: 1) audio, because it is more important to retaining viewer attention than video (AudioVideo2014, ); 2) lighting, as it can improve even a nonideal camera to draw the student's eye; and 3) video, which we mention last because it is the most expensive in a context where higher production value does not necessarily imply a better learning experience (guo2014video, ).

<!-- chunk {"id": "body-0129", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

The final ingredient was *willingness to innovate*. Course 3 (Deploying TinyML) involves hands-on learning. Typically, in-person teaching assistants (TAs) demonstrate labs to show students the goals and scope and to preemptively troubleshoot common errors. Doing the same online is extremely difficult. We developed a three-way split-screen medium (Figure 9(c)) that displays the device assembly, device testing, and TinyML lab exercises. We assembled a new film location to (remotely) support the teaching staff with the lab exercises, adding an overhead camera and additional lighting. Furthermore, we enhanced our visuals for the three-way split screen with a custom motion-graphics layer. This setup reached completion and underwent rapid testing without disturbing the production timeline. From start to finish, Course 3 took only eight weeks despite involving five hours of produced-video time, which includes short lectures, screencasts, and lab videos.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

Technology. Without globally accessible technology and services, remote media production at the level and pace we achieved would have been impossible. Cloud storage was the backbone of our strategy. It allowed contributors to ingest and manage footage globally. It was also the heart of our production workflow, giving us the ability to sync media project files instantly. Videotelephony services such as Zoom and Google Meet aided in assessing home-studio setups in addition to serving as a virtual rehearsal stage and writers' room. Amazon supplied 90% of our equipment. Frame.io streamlined our video-quality review and revision (frameio, ).

<!-- chunk {"id": "body-0131", "role": "body", "section": "Accelerated Remote Media Production", "weight": 1.0} -->

Copyright. Although on-camera presence was a major focus of remote production, video lectures are just one part of the students' activities. At the same time, a multidisciplinary team of content experts, graphic designers, and web developers at HarvardX rapidly designed and formatted readings and coding exercises. A major challenge in quickly producing course materials was ensuring each illustration, photo, and code library met strict licensing requirements to avoid copyright infringement. Given our project's more than two thousand graphics and tight timelines, we trained all content developers on proper sourcing for course materials. In-house custom graphics---necessary for a nascent field---predominated, and copyright specialists at HarvardX evaluated each piece as it arrived to cite all external creators.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Building Community", "weight": 1.0} -->

A common and well-known pitfall of MOOC platforms is the difficulty of developing community and fostering peer learning among a geographically distributed population. Students often struggle to discuss and collaborate after completing the course and even during the course. We therefore developed the TinyMLx community, which welcomes everyone beyond the edX platform.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Building Community", "weight": 1.0} -->

First, we created a Discourse forum ([discuss.TinyMLx.org](discuss.tinymlx.org)) to provide both a communication platform for students and a home for future initiatives. It has been successful, garnering over 3,500 user visits and over 58,500 page views in its first five months. We also conducted two live Q&A sessions for the TinyML community. For each session, between 100 and 200 learners joined live from around the world, and many more have since watched the recording. We received dozens of questions leading up to the events and dozens more during, with topics including how to best teach TinyML material, how to improve diversity in TinyML, and many others in between. Participants enjoyed the events, e.g., 90% of respondents to our first post-event poll said they would like to attend another. Finally, based on learner feedback we recently created a Discord chat to further enable easy collaboration, communication, and community building.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Building Community", "weight": 1.0} -->

To challenge our Course 3 students, who went on to deploy TinyML models on their microcontrollers, we developed an optional "capstone-project" competition. We believe this competition reinforces the value and usefulness of the technical skills that students are gaining. A prize will go to the individual (or individuals) whose project demonstrates technical mastery, is most creative in its implementation, and has the most potential to improve society. This initiative has already spawned collaborative-learning groups.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Building Community", "weight": 1.0} -->

To increase the impact of these projects and further reinforce the real-world applicability of the knowledge students gain through this course series, we are working with the Arribada Initiative (arribada, ) to create larger advised projects. This partnership will allow students to contribute their newly acquired TinyML skills to real-world conservation efforts, such as human/elephant conflict mitigation and sea-turtle monitoring, while receiving advice and support from both industry professionals and course staff. Finally, we are asking the community to continuously improve the course, since it is as much theirs as ours. As a result, we've seen many forum posts and GitHub pull requests offering typo corrections, bug fixes, and even content-improvement suggestions.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Our goal is to expand global access to applied ML through the lens of TinyML. In this section, we assess our work's initial impact by presenting data from edX Insights, a service that provides course statistics to instructors and staff. It is merely an initial impact assessment, as the first cohort of participants have just begun graduating from the core TinyML series (Courses 1-3), and Course 4 (optional) remains in development. As such, our early analysis considers enrollment in the first three courses by geography, background, age, and gender.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Course Enrollment", "weight": 1.0} -->

At the time of this writing, the total course enrollment stands at 43,000. Figure 10 shows the daily enrollment data, starting from the opening date. We announced Courses 1, 2, and 3 together in early October 2020 and launched them on October 27, 2020; December 16, 2020; and March 2, 2021, respectively. Students could enroll in any or all courses at the same time but could only start after each course's launch date.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Course Enrollment", "weight": 1.0} -->

TinyML is a young field, so the first useful metric is interest in the topic (i.e., acquiring applied-ML skills via TinyML). Figure 10 shows the strong and steady increase over time. On average, $\sim$`<!-- -->`{=html}1,000 new students enroll in at least one course each week. Interest in Courses 2 and 3 continues to grow---a phenomenon we attribute to participants promoting them through social media such as LinkedIn, Twitter, and Facebook as they earn their course-completion certificates. The sharp increases around the first week of October, third week of December, and third week of February align with course-announcement dates or major social-media activity. For instance, on January 24, Mashable handpicked "Fundamentals of TinyML" as one of the 10 best free Harvard courses to learn something new (turner_2021, ). TinyML ranked at the top of the STEM-courses listed.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Completion Rates", "weight": 1.0} -->

People take online courses for a wide variety of reasons. Some are curious about the topic and want to get their feet wet; they may audit a course but not complete it. Others would like to master the program and earning a certificate of completion, assuming they can afford it. Therefore, enrollment numbers alone are insufficient.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Completion Rates", "weight": 1.0} -->

We assessed how many verified enrollees complete the course. We have access only to the percentage who have earned a passing grade among those officially enrolled in the courses (i.e., the paid-certificate program). This number is constantly changing. At the time of writing, the completion rates are 59%, 55%, and 44% for Courses 1, 2, and 3, respectively. We believe Course 3's number is slightly lower because it is more challenging than Courses 1 and 2, which do not have a hands-on component. The average completion rate for most MOOCs is somewhere between 5% and 15% (hollands2019benefits, ), so the TinyML courses appear to be faring well. Although these results are preliminary (we need more data to make better quantitative comparisons), they shed a positive light on our design approach.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Learner Demographics", "weight": 1.0} -->

We conducted a demographic analysis of students' age, educational background, and gender. They volunteer this information to edX, so it covers only a fraction of the numbers in Figure 10. Nonetheless, the data is extensive enough that we can draw general conclusions. At the start of each course, a forum post asks students to introduce themselves and summarize what they hope to get out of the edX series. We derived additional qualitative analysis from these responses. So far we have a good distribution across age groups and educational backgrounds. Our gender diversity is lacking, however, but we are working to address it (Section 8).

<!-- chunk {"id": "body-0142", "role": "body", "section": "Learner Demographics", "weight": 1.0} -->

Age. Figure 12 shows the age distribution for all three courses combined. The median is 30. Some participants are high-school students as young as 15 and wish to pursue an ML career. Others are over 60 and wish to understand the latest technological innovations as well as their societal implications. This age diversity was one of our objectives (Section 2).

<!-- chunk {"id": "body-0143", "role": "body", "section": "Learner Demographics", "weight": 1.0} -->

Education. Figure 13 shows that nearly all our learners have either just a secondary (high-school) diploma or a bachelor's/master's degree. A few others have doctorate degrees. Judging from the forum discussions, we gather that individuals with a bachelor's or master's degree are trying to advance or shift their careers by adding an ML focus. Most participants with a doctorate want to apply (tiny) ML in their research. Many students expressed enthusiasm about enrolling in a career-advancing course backed by both Harvard and Google. This variety of educational backgrounds and career focuses also meets our expectations and objectives and further emphasizes the importance of our academia/industry partnership (Section 2).

<!-- chunk {"id": "body-0144", "role": "body", "section": "Learner Demographics", "weight": 1.0} -->

Gender. Figure 14 depicts the gender diversity across all three courses. It weighs heavily toward men; on average, across all three courses, 20% of our learners are women. We are working to change that ratio through our open education initiative (Section 8). More specifically, we are putting together a TinyML4Everyone working group to encourage more women to learn about TinyML.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Future Directions", "weight": 1.0} -->

TinyML can dramatically transform applied-ML education and development at many levels, far beyond what we achieved with the edX specialization. To this end, we launched the Tiny Machine Learning Open Education Initiative (TinyMLx) (tinymlxopen, ) to sponsor a wide variety of initiatives, such as TinyML4D (for applied-ML education via TinyML for developing countries), TinyML4STEM (for nurturing creative research in science, technology, engineering, and math), TinyML4Everyone (for building a shared identity and breaking stereotypes), and TinyML4x (for your favorite topic x).

<!-- chunk {"id": "body-0146", "role": "body", "section": "Future Directions", "weight": 1.0} -->

We are currently running the TinyML4D and TinyML4Everyone working groups that are looking for ways to broaden TinyML participation, access, and belonging. One way is to provide TinyML materials in a student's native language. For instance, we already have two projects for developing course content and instructional materials in Spanish and Portuguese (rovai21, ). Additionally, the makers of TinyML on edX, along with students and faculty of Navajo Technical University in New Mexico, plan to conduct a workshop in June 2021 that teaches Navajo students the basics of hardware programming and how to employ ML for their communities by creating voice-activated applications trained on the Navajo language.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Future Directions", "weight": 1.0} -->

TinyML can be instrumental for inspiring youth, as it offers a superb introduction to programming and ML for K--12 students. Deployment of TinyML applications on physical embedded devices intrigues students by allowing them to interact with actual technologies, not just on-screen representations. Our first step in this direction was to publicly release all course materials on our GitHub: We are working with STEM teachers worldwide to help us refine our tools for the classroom. Our aim is to develop ready-to-go project-based lessons and accompanying lesson plans to further increase ML access by reaching younger children. One possible project is to enable the use of visual programming abstractions (e.g., Microsoft MakeCode editor for the Arduino Nano BLE Sense 33) so people of all ages can apply ML without learning a programming language.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Future Directions", "weight": 1.0} -->

In addition, we are working with various organizations to assist teachers in learning applied ML. The 2021 Backyard Brains AI Fellowship (backyard_brains_2021, ), for example, is an early opportunity for teachers to help design TinyML projects for classrooms.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Limitations", "weight": 1.5} -->

We believe TinyML is an effective means to widen access to applied ML. Indeed, it is one way but not the only way. To provide a more balanced viewpoint, we describe some limitations of our approach and suggest alternative methods that may be more suitable.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Limitations", "weight": 1.5} -->

Hardware cost. TinyML requires the purchase of embedded hardware to acquire the full-stack ML-development experience. The TinyML kit we developed costs US\$49.99. In some developing countries, this exceeds the average income in a week, in some rare cases, even a month. Although this price is considered reasonable in some countries, it may still be too high in others. We have found that the cost of shipping to distant parts of the world depends heavily on the presence of nearby distribution centers that carry the device. If none exist, the kit's cost, including shipping, can sometimes double the original kit price.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Limitations", "weight": 1.5} -->

Ideally, TinyML would require no physical hardware, making the hardware cost zero. We are experimenting with open-source emulation platforms such as Renode.io from Antmicro (antmicro, ). Renode is an open-source framework that allows users to build and test embedded (ML) software without physical embedded hardware. It will enable developers to run their original code, which would have run on the hardware, unmodified in an emulated environment. Although this approach eliminates the hardware cost, students miss the opportunity and excitement of interacting with a device.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Limitations", "weight": 1.5} -->

Device accessibility. Globally, the number of embedded devices far exceeds the number of cloud and mobile devices (as Figure 3 shows). But individuals must procure the necessary embedded hardware, such as the TinyML kit that we have developed with Arduino, to learn. By comparison, devices such as laptop and desktop computers connected to the web benefit from easier access. Students can use a regular computer to gain access to the online course materials. Even if they lack immediate access to computers in their homes, they can access the online resources from Internet cafés that provide web access for a nominal fee. A crucial shortcoming of this approach, however, is that learners will have difficulty experiencing the complete ML workflow (Figure 4), since they will be unable to deploy in a device the models they train in the cloud.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Limitations", "weight": 1.5} -->

Smartphones may be a suitable compromise. They are highly accessible, even though they can be an order of magnitude more costly than the TinyML kit. Nevertheless, they enable students to experience the complete TinyML design, development, deployment, and management workflow. Also, an average smartphone has more than 10 sensors---many more than the Arduino Nano 33 BLE Sense we use in Course 3, enabling additional applications. Learners can hold the smartphone in their hands, much like the TinyML device. That said, conveying the significance of ML's future being tiny and bright (Section 3) is more challenging (though not impossible) because mobile devices have far more resources (compute power, memory, bandwidth, etc.) than TinyML devices (Table 1). Students may therefore miss the fundamental issue of embedded-resource constraints. But if the goal is ultimately to expand access to applied ML, mobile devices may be a fair compromise.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Limitations", "weight": 1.5} -->

Programming background. Building ML models for mobile devices (using TensorFlow Lite (tflite, )) or the web (using TensorFlow.js (smilkov2019ensorflowjs, )) is possible using high-level programming languages such as Python and JavaScript, respectively. These languages are easy to learn and far more accessible to beginners than C/C++, which is necessary to program embedded hardware (similar to Course 3). So although TinyML creates an opportunity to showcase the full-stack ML experience using embedded hardware, and we leverage the Arduino IDE and heavily scaffolded code with video walkthroughs to minimize the lift to C/C++, it may also narrow access in some regards. The additional necessary programming skills and associated education can be a roadblock.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Limitations", "weight": 1.5} -->

In the future, we believe that end-to-end developer platforms such as Edge Impulse (:online:online, ) that lower the entry barrier into TinyML will likely become mainstream and an essential part of the future developer ecosystem. Not every embedded ML engineer must know and understand all of the inner workings of TensorFlow Lite Micro or how an ML compiler works or how to extract the best performance from a highly customized ML hardware accelerator etc. Instead, learners need the right level of abstraction that allows them to focus on what matters most. Platforms such as Edge Impulse make it easy for learners, software developers, engineers and other domain experts to solve real-world problems using ML on the edge and TinyML devices without advanced degrees in ML or embedded systems. We therefore expose learners to the end-to-end MLOps platforms in Course 4, but note that more focus on such platforms in future courses could enable even more accessibility.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Limitations", "weight": 1.5} -->

In summary, there are many paths to broaden applied-ML access. The correct approach--or, better, the most suitable approach--depends on the situation. We, therefore, hope this discussion clarifies the pros and cons of approaching applied ML through TinyML.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Expanding access to high-quality educational content, especially for machine learning, is important to ensuring that expertise diffuses beyond just a few prominent organizations. But doing so in a way that is both accessible and affordable to many different people is a difficult task. The four-part TinyML edX series we present here aims to tackle these challenges by providing application-driven content that covers the entire ML life cycle, giving students hands-on experience guided by world experts and developing their ML skills regardless of their background. The forums, chats, optional project, and online discussions with the class creators promote community development and continued learning. The early impact of this approach is demonstrable: numerous participants from a variety of locations and demographics have signed up. We have also begun initiatives to further increase access by helping develop courses that target K--12 students and teachers, as well as courses in other languages.
