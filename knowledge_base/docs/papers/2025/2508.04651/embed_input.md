Live Music Models

We introduce a new class of generative models for music called live music models that produce a continuous stream of music in real-time with synchronized user control. We release Magenta RealTime, an open-weights live music model that can be steered using text or audio prompts to control acoustic style. On automatic metrics of music quality, Magenta RealTime outperforms other open-weights music generation models, despite using fewer parameters and offering first-of-its-kind live generation capabilities. We also release Lyria RealTime, an API-based model with extended controls, offering access to our most powerful model with wide prompt coverage. These models demonstrate a new paradigm for AI-assisted music creation that emphasizes human-in-the-loop interaction for live music performance.

## Introduction

Music exists in two complementary forms: as static recorded pieces ("music as a noun"), and as live performances collectively experienced in real time ("music as a verb") \[\]. This second form of *live* music is particularly tied to the fundamental human experiences of creative flow, embodied expression \[\], and social connection \[\]. Despite this, modern generative AI systems for musical audio have had an overwhelming emphasis on offline, turn-based generation.

Live music represents a new frontier for generative AI, one with numerous opportunities and technical challenges. In the conventional offline setting, users input control information, wait $L$ seconds (offline *latency*), and receive $T$ seconds of audio. In our proposed live setting, users continuously input control information, receiving $T$ seconds of an uninterrupted audio stream from $T$ seconds of interaction, with $D$ seconds of *delay* between their control inputs and their influence on the audio stream....

### Program Management

### Executive Sponsors

We complement this subjective measure with more constrained experiments to examine the effects of our controls and provide comparisons to existing models where possible. We focus these experiments on assessing core capabilities that are common to both live and offline music audio generation models, such as audio quality and adherence to text conditioning (Section 3.2.1), alongside others that are unique to our live music models, such as the ability to generate musical transitions following changes in the conditioning signal (Section 3.2.2)....

We instead propose *chunk-based autoregression*, where we operate on chunks of length $C = 2$ seconds, and, under a Markov assumption, predict each chunk based on a limited context of $H = 5$ previous chunks ($10$ seconds of history). This has several advantages: it reduces error accumulation and allows for stateless inference, eliminating the need to maintain a generation cache and simplifying model deployment. It also introduces flexibility during sampling, since conditioning is updated between calls without preserving information about controls beyond the context window.

### Generating musical transitions

Open-weights models are particularly well-suited for live generative music because they can run locally on users' devices....
