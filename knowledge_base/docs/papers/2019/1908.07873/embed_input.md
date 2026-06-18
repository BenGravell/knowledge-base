Federated Learning: Challenges, Methods, and Future Directions

Topics include Federated learning, Privacy, Distributed systems, Optimization, Learning.

Federated learning involves training statistical models over remote devices or siloed data centers, such as mobile phones or hospitals, while keeping data localized. Training in heterogeneous and potentially massive networks introduces novel challenges that require a fundamental departure from standard approaches for large-scale machine learning, distributed optimization, and privacy-preserving data analysis. In this article, we discuss the unique characteristics and challenges of federated learning, provide a broad overview of current approaches, and outline several directions of future work that are relevant to a wide range of research communities.

## Introduction

Mobile phones, wearable devices, and autonomous vehicles are just a few of the modern distributed networks generating a wealth of data each day. Due to the growing computational power of these devices---coupled with concerns over transmitting private information---it is increasingly attractive to store data *locally* and push network computation to the edge.

The concept of edge computing is not a new one. Indeed, computing simple queries across distributed, low-powered devices is a decades-long area of research that has been explored under the purview of query processing in sensor networks, computing at the edge, and fog computing. Recent works have also considered training machine learning models centrally but serving and storing them locally; for example, this is a common approach in mobile user modeling and personalization.

However, as the storage and computational capabilities of the devices within distributed networks grow, it is possible to leverage enhanced local resources on each device. This has led to a growing interest in *federated learning*, which explores *training* statistical models directly on remote devices^11^1We use the term 'device' throughout the article to describe entities in the network, such as nodes, clients, sensors, or organizations..

Federated learning methods have been deployed by major service providers, and play a critical role in supporting privacy-sensitive applications where the training data are distributed at the edge \e.g.,. Examples of potential applications include: learning sentiment, semantic location, or activities of mobile phone users; adapting to pedestrian behavior in autonomous vehicles; and predicting health events like heart attack risk from wearable devices.

## Conclusion

In this article, we have provided an overview of federated learning, a learning paradigm where statistical models are trained at the edge in distributed networks. We have discussed the unique properties and associated challenges of federated learning compared with traditional distributed data center computing and classical privacy-preserving learning. We provided an extensive survey on classical results as well as more recent work specifically focused on federated settings. Finally, we have outlined out a handful of open problems worth future research effort.
