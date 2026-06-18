Federated Learning: Challenges, Methods, and Future Directions

Topics include Federated learning, Privacy, Distributed systems, Optimization, Learning.

Federated learning involves training statistical models over remote devices or siloed data centers, such as mobile phones or hospitals, while keeping data localized. Training in heterogeneous and potentially massive networks introduces novel challenges that require a fundamental departure from standard approaches for large-scale machine learning, distributed optimization, and privacy-preserving data analysis. In this article, we discuss the unique characteristics and challenges of federated learning, provide a broad overview of current approaches, and outline several directions of future work that are relevant to a wide range of research communities.

## Introduction

Mobile phones, wearable devices, and autonomous vehicles are just a few of the modern distributed networks generating a wealth of data each day. Due to the growing computational power of these devices---coupled with concerns over transmitting private information---it is increasingly attractive to store data *locally* and push network computation to the edge.

The concept of edge computing is not a new one. Indeed, computing simple queries across distributed, low-powered devices is a decades-long area of research that has been explored under the purview of query processing in sensor networks, computing at the edge, and fog computing. Recent works have also considered training machine learning models centrally but serving and storing them locally; for example, this is a common approach in mobile user modeling and personalization.

## Conclusion

In this article, we have provided an overview of federated learning, a learning paradigm where statistical models are trained at the edge in distributed networks. We have discussed the unique properties and associated challenges of federated learning compared with traditional distributed data center computing and classical privacy-preserving learning. We provided an extensive survey on classical results as well as more recent work specifically focused on federated settings. Finally, we have outlined out a handful of open problems worth future research effort....

### Fault Tolerance

In federated settings, optimization methods that allow for flexible local updating and low client participation have become the de facto solvers. The most commonly used method for federated learning is Federated Averaging (FedAvg), a method based on averaging local stochastic gradient descent (SGD) updates for the primal problem. FedAvg has been shown to work well empirically, particularly for non-convex problems, but comes without convergence guarantees and can diverge in practical settings when data are heterogeneous. We discuss methods to handle such statistical heterogeneity in more detail in Section 2.3.2.

Statistical heterogeneity also presents novel challenges in terms of analyzing the convergence behavior in federated settings---even when learning a single global model....
