GPT-4o System Card

GPT-4o is an autoregressive omni model that accepts as input any combination of text, audio, image, and video, and generates any combination of text, audio, and image outputs. It's trained end-to-end across text, vision, and audio, meaning all inputs and outputs are processed by the same neural network. GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time in conversation. It matches GPT-4 Turbo performance on text in English and code, with significant improvement on text in non-English languages, while also being much faster and 50\% cheaper in the API. GPT-4o is especially better at vision and audio understanding compared to existing models. In line with our commitment to building AI safely and consistent with our voluntary commitments to the White House, we are sharing the GPT-4o System Card, which includes our Preparedness Framework evaluations.

## Introduction

GPT-4o is an autoregressive omni model, which accepts as input any combination of text, audio, image, and video and generates any combination of text, audio, and image outputs. It's trained end-to-end across text, vision, and audio, meaning that all inputs and outputs are processed by the same neural network.

GPT-4o can respond to audio inputs in as little as 232 milliseconds, with an average of 320 milliseconds, which is similar to human response time in a conversation. It matches GPT-4 Turbo performance on text in English and code, with significant improvement on text in non-English languages, while also being much faster and 50% cheaper in the API. GPT-4o is especially better at vision and audio understanding compared to existing models.

## Model data and training

GPT-4o's

## Limitations of the evaluation methodology

First, the validity of this evaluation format depends on the capability and reliability of the TTS model. Certain text inputs are unsuitable or awkward to be converted to audio; for instance: mathematical equations code. Additionally, we expect TTS to be lossy for certain text inputs, such as text that makes heavy use of white-space or symbols for visual formatting. Since we expect that such inputs are also unlikely to be provided by the user over Advanced Voice Mode, we either avoid evaluating the speech-to-speech model on such tasks, or alternatively pre-process examples with such inputs.

A second concern may be whether the TTS inputs are representative of the distribution of audio inputs that users are likely to provide in actual usage. We evaluate the robustness of GPT-4o on audio inputs across a range of regional accents in Section 3.3.3. However, there remain many other dimensions that may not be captured in a TTS-based evaluation, such as different voice intonations and valence, background noise, or cross-talk, that could lead to different model behavior in practical usage.
