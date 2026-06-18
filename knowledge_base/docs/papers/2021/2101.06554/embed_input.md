Diverse Complexity Measures for Dataset Curation in Self-driving

Modern self-driving autonomy systems heavily rely on deep learning. As a consequence, their performance is influenced significantly by the quality and richness of the training data. Data collecting platforms can generate many hours of raw data in a daily basis, however, it is not feasible to label everything. It is thus of key importance to have a mechanism to identify "what to label". Active learning approaches identify examples to label, but their interestingness is tied to a fixed model performing a particular task. These assumptions are not valid in self-driving, where we have to solve a diverse set of tasks (i.e., perception, and motion forecasting) and our models evolve over time frequently. In this paper we introduce a novel approach and propose a new data selection method that exploits a diverse set of criteria that quantize interestingness of traffic scenes. Our experiments on a wide range of tasks and models show that the proposed curation pipeline is able to select datasets that lead to better generalization and higher performance.

## Introduction

Self-driving has recently benefited from deep learning breakthroughs, which have enhanced the performance of autonomy systems significantly. The performance achieved by these systems is tightly coupled to the quality, size and richness of training datasets. Furthermore, as self-driving is a safety critical application it is very important to have a diverse set of testing scenarios that are representative of driving.

Collecting data is a fairly easy process -- a single vehicle can generate several Tb of data a day. However, it is not feasible to label everything that has been collected. For instance, it could cost around \$150K^11^1scale.com to simply annotate the bounding-box of objects in one hour of camera data, assuming average density of 50 objects per image. Hence, it is of key importance to have a mechanism to identify "what to label" such that we can get the most relevant labeled dataset to achieve the highest autonomy performance given a labeling budget.

## Conclusion

In this paper we presented a dataset curation pipeline for self-driving to select unlabeled data for labeling. We described a set of intuitive complexity measures to characterize the traffic scene of the collected data wrt various aspects including the topology of the map, diversity and complexity of surrounding actors and their behaviors, and the executed maneuver of the SDV. We also presented a method to select interesting and challenging sections of the collected logs using the described measures together with adding diverse examples to the final selected set of scenarios....

### Bike-lanes and crosswalks

Limiting the data selection to only challenging scenarios will not necessarily lead to a diverse dataset, or to a complete set of scenarios that we might encounter in the real world. The goal of this additional selection step is to identify a set of snippets that ensures completeness and diversity. We quantize the dissimilarity between snippets as a function of their difference in the complexity measures, where in order to get geo-diversity we expand the complexity vectors with the latitude and longitude coordinates of the frames....

where $\omega_{i}$ is a discreet speeds computed for the $i^{\text{th}}$ actor and $\Omega$ is the set of average speeds for all the actors.
