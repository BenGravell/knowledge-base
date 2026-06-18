Live Music Models

We introduce a new class of generative models for music called live music models that produce a continuous stream of music in real-time with synchronized user control. We release Magenta RealTime, an open-weights live music model that can be steered using text or audio prompts to control acoustic style. On automatic metrics of music quality, Magenta RealTime outperforms other open-weights music generation models, despite using fewer parameters and offering first-of-its-kind live generation capabilities. We also release Lyria RealTime, an API-based model with extended controls, offering access to our most powerful model with wide prompt coverage. These models demonstrate a new paradigm for AI-assisted music creation that emphasizes human-in-the-loop interaction for live music performance.

## Introduction

Music exists in two complementary forms: as static recorded pieces ("music as a noun"), and as live performances collectively experienced in real time ("music as a verb"). This second form of *live* music is particularly tied to the fundamental human experiences of creative flow, embodied expression, and social connection. Despite this, modern generative AI systems for musical audio have had an overwhelming emphasis on offline, turn-based generation.

Live music represents a new frontier for generative AI, one with numerous opportunities and technical challenges. In the conventional offline setting, users input control information, wait $L$ seconds (offline *latency*), and receive $T$ seconds of audio. In our proposed live setting, users continuously input control information, receiving $T$ seconds of an uninterrupted audio stream from $T$ seconds of interaction, with $D$ seconds of *delay* between their control inputs and their influence on the audio stream.

To allow users to navigate these tradeoffs based on their application goals, we introduce a pair of systems that span both paradigms: Magenta RT (open-weights, on-device) and Lyria RT (API, cloud-based). Both use the same core methodological framework, which centers around codec language modeling (Figure 1). Specifically, we train a language model (LM) to generate audio tokens from SpectroStream, using a method similar to to achieve live streaming.

## Conclusion

In this work, we introduced live music models, a new class of generative systems designed for real-time, continuous music creation with synchronized user control. We presented two such systems: Magenta RealTime, a fully open-weights model, and Lyria RealTime, an API-based model with extended controls. These models facilitate a novel paradigm for AI-assisted music, emphasizing interactive, human-in-the-loop performance that prioritizes the creative process over just the end product. With future work, we aim to further decrease the control latency to unlock new interactive possibilities.
