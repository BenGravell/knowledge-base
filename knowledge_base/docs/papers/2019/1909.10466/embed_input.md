Dynamic Mode Decomposition: Theory and Data Reconstruction

Topics include Dynamic mode decomposition, Data-driven, Data reconstruction.

Tutorial and survey that presents theoretical analysis of DMD with a focus on data reconstruction from DMD modes, addressing the relationship between DMD approximations and the underlying dynamics of the system.

Dynamic Mode Decomposition (DMD) is a data-driven decomposition technique extracting spatio-temporal patterns of time-dependent phenomena. In this paper, we perform a comprehensive theoretical analysis of various variants of DMD. We provide a systematic advancement of these and examine the interrelations. In addition, several results of each variant are proven. Our main result is the exact reconstruction property. To this end, a new modification of scaling factors is presented and a new concept of an error scaling is introduced to guarantee an error-free reconstruction of the data.

## Introduction

The analysis of time-dependent phenomena is at the heart of investigation in a broad range of scientific research. Within these studies, the integration of data in the form of time-series has increased considerably. Therefore, the application of innovative algorithms is necessary to gain deep insights into the characteristics of data. In this paper, we address time-series analysis by Dynamic Mode Decomposition (DMD), which was first introduced by Schmid and Sesterhenn in 2008.

DMD is a data-driven and model-free algorithm extracting spatio-temporal patterns in the form of so-called DMD modes and DMD eigenvalues. As an efficient tool in fluid mechanics, DMD has gained much attention. DMD has been investigated on both practical and theoretical grounds. Nonetheless, the focus of these analyses was mainly a practical one. For example, various types of flow were considered, such as airflow around an airfoil, fuel flow in a combustion chamber, or heat conduction in various cases. Completely different fields of application comprise financial trading, video processing, epidemiology, neuroscience, and control theory.

In contrast, we focus on theoretical investigations. The paper is thus structured as follows: After discussing related work, we introduce the theoretical framework of DMD dealing with the background mechanisms. In this process, we define the so-called system matrix, which is pioneering for DMD and prove the following results: a characterization for the exactness and diagonalizability of the system matrix as well as the resulting reconstruction of data with its spectral components.

## Conclusion

A comprehensive theoretical analysis of Dynamic Mode Decomposition has been developed that clarify the connection between different variants of DMD (CDMD, SDMD, and EXDMD) and demonstrates several features of them. One of these features is the reconstruction property, which was proven for all variants and the system matrix as well. To this end, different scaling factors were used and new ones introduced to ensure this property.
