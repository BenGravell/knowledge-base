Song from PI: A Musically Plausible Network for Pop Music Generation

We present a novel framework for generating pop music. Our model is a hierarchical Recurrent Neural Network, where the layers and the structure of the hierarchy encode our prior knowledge about how pop music is composed. In particular, the bottom layers generate the melody, while the higher levels produce the drums and chords. We conduct several human studies that show strong preference of our generated music over that produced by the recent method by Google. We additionally show two applications of our framework: neural dancing and karaoke, as well as neural story singing.

## Introduction

Neural networks have revolutionized many fields. They have not only proven to be powerful in performing perception tasks such as image classification and language understanding, but have also shown to be surprisingly good "artists". In Gatys et al., photos were turned into paintings by exploiting particular drawing styles such as Van Gogh's, Kiros et al. produced stories about images biased by writing style (e.g., romance books), Karpathy et al. wrote Shakespeare inspired novels, and Simo-Serra et al. gave fashion advice.

Music composition is another artistic domain where neural based approaches have been proposed. Early approaches exploiting Recurrent Neural Networks (Bharucha & Todd; Mozer; Chen & Miikkulainen; Eck & Schmidhuber ) date back to the 80's. The main variations between the different models is the representation of the notes and the outputs they produced, which typically encode melody and chord. Most of these approaches were single track, in that they produced only one note per time step. The exception is Boulanger-lewandowski et al. which generated polyphonic music, i.e., simultaneous independent melodies.

## Conclusion and Future Work

We have presented a hierarchical approach to pop song generation which exploits music theory in the model design. In contrast to past work, our approach is able to generate multi-track music. Our human studies shows the strength of our framework compared to an existing strong baseline. We additionally proposed two new applications: neural dancing & karaoke, and neural story singing. We next discuss the limitations and avenues for future work. As most existing approaches our method's objective is to learn to produce music at the note level....

The keys alone are not sufficient to describe how the melody is performed. Additionally we also need to know the duration that each key needs to be pressed for. Towards this goal, conditioned on the melody, we generate the duration of each key with a two-layer LSTM with a 512-dimensional hidden state. We represent the duration of pressing as a forward counting sequence that is conditioned on the generated melody. The press outputs 1 when a new key is pressed, and sequentially outputs 2, 3, 4 and so on as the key is held on. When the current key is released, the press counter is reset to 1....
