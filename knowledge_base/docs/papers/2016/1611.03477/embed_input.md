Song from PI: A Musically Plausible Network for Pop Music Generation

We present a novel framework for generating pop music. Our model is a hierarchical Recurrent Neural Network, where the layers and the structure of the hierarchy encode our prior knowledge about how pop music is composed. In particular, the bottom layers generate the melody, while the higher levels produce the drums and chords. We conduct several human studies that show strong preference of our generated music over that produced by the recent method by Google. We additionally show two applications of our framework: neural dancing and karaoke, as well as neural story singing.

## Introduction

Neural networks have revolutionized many fields. They have not only proven to be powerful in performing perception tasks such as image classification and language understanding, but have also shown to be surprisingly good "artists". In Gatys et al., photos were turned into paintings by exploiting particular drawing styles such as Van Gogh's, Kiros et al. produced stories about images biased by writing style (e.g., romance books), Karpathy et al. wrote Shakespeare inspired novels, and Simo-Serra et al. gave fashion advice.

In this paper, we aim to generate pop music, where the melody but also chords and other instruments make up what is typically called a song. We draw inspiration from the Song from $\pi$ by Macdonald ^11^1 a piano video on Youtube, where the pleasing music is created from a sequence of digits of $\pi$. This video shows both the randomness and the regularity of music. On one hand, since any possible digit sequence is a subset of the $\pi$ digit sequence, this implies that pleasing music can be created even from a totally random base signal.

Following the ideas of Songs from $\pi$, we aim to generate both the melody as well as accompanying effects such as chords and drums. Arguably, these turn even a not particularly pleasing melody into a well sounding song. We propose a hierarchical approach, where each level is a Recurrent Neural Network producing a key aspect of the song. The bottom layers generate the melody, while the higher levels produce drums and chords. This enables the drum and chord layers to compensate for the melody in order to produce appleasing music.

## Conclusion and Future Work

We have presented a hierarchical approach to pop song generation which exploits music theory in the model design. In contrast to past work, our approach is able to generate multi-track music. Our human studies shows the strength of our framework compared to an existing strong baseline. We additionally proposed two new applications: neural dancing & karaoke, and neural story singing. We next discuss the limitations and avenues for future work. As most existing approaches our method's objective is to learn to produce music at the note level.
