An Overview of Diffusion Models: Applications, Guided Generation, Statistical Rates and Optimization

Topics include Diffusion models, Generative artificial intelligence, Score-based generative modeling, Stochastic processes, Controlled generation, Conditional sampling, High-dimensional optimization, Machine learning theory, Survey.

This review surveys diffusion models as generative samplers, guided generators, and tools for structured optimization, emphasizing statistical rates, sampling guarantees, and the transition from unconditional diffusion to conditional and controlled generation.

Diffusion models, a powerful and universal generative AI technology, have achieved tremendous success in computer vision, audio, reinforcement learning, and computational biology. In these applications, diffusion models provide flexible high-dimensional data modeling, and act as a sampler for generating new samples under active guidance towards task-desired properties. Despite the significant empirical success, theory of diffusion models is very limited, potentially slowing down principled methodological innovations for further harnessing and improving diffusion models. In this paper, we review emerging applications of diffusion models, understanding their sample generation under various controls. Next, we overview the existing theories of diffusion models, covering their statistical properties and sampling capabilities. We adopt a progressive routine, beginning with unconditional diffusion models and connecting to conditional counterparts. Further, we review a new avenue in high-dimensional structured optimization through conditional diffusion models, where searching for solutions is reformulated as a conditional sampling problem and solved by diffusion models.

## Introduction

The field of artificial intelligence (AI) has been revolutionized by generative models, particularly large language models and diffusion models. Recognized as foundation models, they are trained on massive corpora of data and have opened up vibrant possibilities in machine learning research and applications. While large language models focus on generating coherent text based on context, diffusion models excel at modeling complex data distributions and generating diverse samples, both of which find widespread use across various domains.

Diffusion models, inspired by thermodynamics modeling, have emerged in recent years with ground-breaking performance, surpassing the previous state-of-the-art, such as Generative Adversarial Networks (GANs) and Variational AutoEncoders (VAEs). Diffusion models are widely adopted in computer vision and audio generation tasks, and further utilized in text generation, sequential data modeling, reinforcement learning and control, as well as life-science. For a more comprehensive exposition of applications, we refer readers to survey papers.

The celebrated performance of diffusion models is indispensable to numerous methodological innovations that significantly expand the scope and boost the functionality of diffusion models, enabling high-fidelity generation, efficient sampling, and flexible control of the sample generation. For example, extend diffusion models to discrete data generation, while the vanilla diffusion models target at continuous data. Meanwhile, there is an active line of research aiming to expedite the sample generation speed of diffusion models.

This paper serves as a contemporary exposure to diffusion models for stimulating sophisticated and forward-looking study on them.

## Conclusion

In this paper, we have surveyed how diffusion models generate samples, their wide applications, and existing theoretical underpinnings of them. We have adopted a continuous-time description of the forward and backward processes in diffusion models and discussed their training procedure, especially when there exists guidance to steer the sample generation. We have started with an exposure to theories of unconditional diffusion models, covering its score approximation, statistical estimation, and sampling theories.
