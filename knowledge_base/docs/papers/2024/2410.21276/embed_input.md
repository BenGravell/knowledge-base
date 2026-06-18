GPT-4o System Card

GPT-4o is an autoregressive omni model that accepts as input any combination of text, audio, image, and video, and generates any combination of text, audio, and image outputs. It's trained end-to-end across text, vision, and audio, meaning all inputs and outputs are processed by the same neural network. GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time in conversation. It matches GPT-4 Turbo performance on text in English and code, with significant improvement on text in non-English languages, while also being much faster and 50\% cheaper in the API. GPT-4o is especially better at vision and audio understanding compared to existing models. In line with our commitment to building AI safely and consistent with our voluntary commitments to the White House, we are sharing the GPT-4o System Card, which includes our Preparedness Framework evaluations....

## Introduction

GPT-4o is an autoregressive omni model, which accepts as input any combination of text, audio, image, and video and generates any combination of text, audio, and image outputs. It's trained end-to-end across text, vision, and audio, meaning that all inputs and outputs are processed by the same neural network.

GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time in a conversation. It matches GPT-4 Turbo performance on text in English and code, with significant improvement on text in non-English languages, while also being much faster and 50% cheaper in the API. GPT-4o is especially better at vision and audio understanding compared to existing models.

Red Teaming Organizations:\
METR, Apollo Research, Virtue AI

Choice Mpanza, David Adelani, Edward Bayes, Igneciah Pocia Thete, Imaan Khadir, Israel A. Azime, Jesujoba Oluwadara Alabi, Jonas Kgomo, Naome A. Etori, Shamsuddeen Hassan Muhammad

Although some technical mitigations are still in development, our Usage Policies disallow intentionally deceiving or misleading others, and circumventing safeguards or safety mitigations. In addition to technical mitigations, we enforce our Usage Policies through monitoring and take action on violative behavior in both ChatGPT and the API.

Risk Mitigation: We post-trained GPT-4o with a diverse set of input voices to have model performance and behavior be invariant across different user voices.

Our evaluation tested the ability to execute chained actions and reliably execute coding tasks. GPT-4o was unable to robustly take autonomous actions. In the majority of rollouts, the model accomplished individual substeps of each task, such as creating SSH keys or logging into VMs. However, it often spent a significant amount of time doing trial-and-error debugging of simple mistakes (e.g., hallucinations, misuses of APIs) for each step....

In line with our commitment to building AI safely and consistent with our voluntary commitments to the White House, we are sharing the GPT-4o System Card, which includes our Preparedness Framework evaluations. In this System Card, we provide a detailed look at GPT-4o's capabilities, limitations, and safety evaluations across multiple categories, with a focus on speech-to-speech (voice)^11^1Some evaluations, in particular, the...
