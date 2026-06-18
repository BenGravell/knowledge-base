GPT-4 Technical Report

We report the development of GPT-4, a large-scale, multimodal model which can accept image and text inputs and produce text outputs. While less capable than humans in many real-world scenarios, GPT-4 exhibits human-level performance on various professional and academic benchmarks, including passing a simulated bar exam with a score around the top 10% of test takers. GPT-4 is a Transformer-based model pre-trained to predict the next token in a document. The post-training alignment process results in improved performance on measures of factuality and adherence to desired behavior. A core component of this project was developing infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed us to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4.

## Introduction

This technical report presents GPT-4, a large multimodal model capable of processing image and text inputs and producing text outputs. Such models are an important area of study as they have the potential to be used in a wide range of applications, such as dialogue systems, text summarization, and machine translation. As such, they have been the subject of substantial interest and progress in recent years.

One of the main goals of developing such models is to improve their ability to understand and generate natural language text, particularly in more complex and nuanced scenarios. To test its capabilities in such scenarios, GPT-4 was evaluated on a variety of exams originally designed for humans. In these evaluations it performs quite well and often outscores the vast majority of human test takers. For example, on a simulated bar exam, GPT-4 achieves a score that falls in the top 10% of test takers. This contrasts with GPT-3.5, which scores in the bottom 10%.

Core contributors^1010^10All author lists sorted alphabetically.\
Christopher Berner Supercomputing lead\
Greg Brockman Infrastructure lead\
Trevor Cai Throughput lead\
David Farhi Manager of optimization team\
Chris Hesse Infrastructure usability co-lead\
Shantanu Jain Infrastructure usability co-lead\
Kyle Kosic Uptime and stability lead\
Jakub Pachocki Overall lead, optimization lead\
Alex Paino Architecture & data vice lead\
Mikhail Pavlov Software correctness lead\
Michael Petrov Hardware correctness lead\
Nick Ryder Architecture & data lead\
Szymon Sidor Optimization vice lead\
Nikolas Tezak Execution lead\
Phil Tillet Triton...

We also acknowledge and thank every OpenAI team member not explicitly mentioned above, including the amazing people on the executive assistant, finance, go to market, human resources, legal, operations and recruiting teams. From hiring everyone in the company, to making sure we have an amazing office space, to building the administrative, HR, legal, and financial structures that allow us to do our best work, everyone at OpenAI has contributed to GPT-4.\
We thank Microsoft for their partnership, especially Microsoft Azure for supporting model training with infrastructure design and management, and the Microsoft Bing team and Microsoft's...

The image shows a package for a "Lightning Cable" adapter with three panels.
