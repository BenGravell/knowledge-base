<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Features of Music from Scratch

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper introduces a new large-scale music dataset, MusicNet, to serve as a source of supervision and evaluation of machine learning methods for music research. MusicNet consists of hundreds of freely-licensed classical music recordings by 10 composers, written for 11 instruments, together with instrument/note annotations resulting in over 1 million temporal labels on 34 hours of chamber music performances under various studio and microphone conditions. The paper defines a multi-label classification task to predict notes in musical recordings, along with an evaluation protocol, and benchmarks several machine learning architectures for this task: i) learning from spectrogram features; ii) end-to-end learning with a neural net; iii) end-to-end learning with a convolutional neural net. These experiments show that end-to-end models trained for note prediction learn frequency selective filters as a low-level representation of audio.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Music research has benefited recently from the effectiveness of machine learning methods on a wide range of problems from music recommendation to music generation; see also the recent demos of the Google Magenta project^11^1 As of today, there is no large publicly available labeled dataset for the simple yet challenging task of note prediction for classical music. The MIREX MultiF0 Development Set and the dataset together contain less than 7 minutes of labeled music. These datasets were designed for method evaluation, not for training supervised learning methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This situation stands in contrast to other application domains of machine learning. For instance, in computer vision large labeled datasets such as ImageNet are fruitfully used to train end-to-end learning architectures. Learned feature representations have outperformed traditional hand-crafted low-level visual features and lead to tremendous progress for image classification. In, Humphrey, Bello, and LeCun issued a call to action: "Deep architectures often require a large amount of labeled data for supervised training, a luxury music informatics has never really enjoyed. Given the proven success of supervised methods, MIR would likely benefit a good deal from a concentrated effort in the curation of sharable data in a sustainable manner."

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper introduces a new large labeled dataset, MusicNet, which is publicly available^22^2 as a resource for learning feature representations of music. MusicNet is a corpus of aligned labels on freely-licensed classical music recordings, made possible by licensing initiatives of the European Archive, the Isabella Stewart Gardner Museum, Musopen, and various individual artists. The dataset consists of 34 hours of human-verified aligned recordings, containing a total of $1,299,329$ individual labels on segments of these recordings. Table 1 summarizes statistics of MusicNet.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The focus of this paper's experiments is to learn low-level features of music from raw audio data. In Sect. 4, we will construct a multi-label classification task to predict notes in musical recordings, along with an evaluation protocol. We will consider a variety of machine learning architectures for this task: i) learning from spectrogram features; ii) end-to-end learning with a neural net; iii) end-to-end learning with a convolutional neural net. Each of the proposed end-to-end models learns a set of frequency selective filters as low-level features of musical audio, which are similar in spirit to a spectrogram. The learned low-level features are visualized in Figure 1. The learned features modestly outperform spectrogram features; we will explore possible reasons for this in Sect. 5.

<!-- chunk {"id": "body-0007", "role": "body", "section": "MusicNet", "weight": 1.0} -->

Related Works. The experiments in this paper suggest that large amounts of data are necessary to recovering useful features from music; see Sect. 4.5 for details. The Lakh dataset, released this summer based on the work of Raffel & Ellis, offers note-level annotations for many 30-second clips of pop music in the Million Song Dataset. The syncRWC dataset is a subset of the RWC dataset consisting of 61 recordings aligned to scores using the protocol described in Ewert et al.. The MAPS dataset is a mixture of acoustic and synthesized data, which expressive models could overfit. The Mazurka project^33^3 consists of commercial music. Access to the RWC and Mazurka datasets comes at both a cost and inconvenience. Both the MAPS and Mazurka datasets are comprised entirely of piano music.

<!-- chunk {"id": "body-0008", "role": "body", "section": "MusicNet", "weight": 1.0} -->

The MusicNet Dataset. MusicNet is a public collection of labels (exemplified in Table 2) for 330 freely-licensed classical music recordings of a variety of instruments arranged in small chamber ensembles under various studio and microphone conditions. The recordings average 6 minutes in length. The shortest recording in the dataset is 55 seconds and the longest is almost 18 minutes. Table 1 summarizes the statistics of MusicNet with breakdowns into various types of labels. Table 2 demonstrates examples of labels from the MusicNet dataset.

<!-- chunk {"id": "body-0009", "role": "body", "section": "MusicNet", "weight": 1.0} -->

MusicNet labels come from 513 label classes using the most naive definition of a class: distinct instrument/note combinations. The breakdowns reported in Table 1 indicate the number of distinct notes that appear for each instrument in our dataset. For example, while a piano has 88 keys only 83 of them are performed in MusicNet. For many tasks a note's value will be a part of its label, in which case the number of classes will expand by approximately an order of magnitude after taking the cartesian product of the set of classes with the set of values: quarter-note, eighth-note, triplet, etc. Labels regularly overlap in the time series, creating polyphonic multi-labels.

<!-- chunk {"id": "body-0010", "role": "body", "section": "MusicNet", "weight": 1.0} -->

MusicNet is skewed towards Beethoven, thanks to the composer's popularity among performing ensembles. The dataset is also skewed towards Solo Piano due to an abundance of digital scores available for piano works. For training purposes, researchers may want to augment this dataset to increase coverage of instruments such as Flute and Oboe that are under-represented in MusicNet. Commercial recordings could be used for this purpose and labeled using the alignment protocol described in Sect. 3.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Dataset Construction", "weight": 1.0} -->

MusicNet recordings are freely-licensed classical music collected from the European Archive, the Isabella Stewart Gardner Museum, Musopen, and various artists' collections. The MusicNet labels are retrieved from digital MIDI scores, collected from various archives including the Classical Archives (classicalarchives.com) Suzuchan's Classic MIDI (suzumidi.com) and HarfeSoft (harfesoft.de). The methods in this section produce an alignment between a digital score and a corresponding freely-licensed recording. A recording is labeled with events in the score, associated to times in the performance via the alignment. Scores containing $6,550,760$ additional labels are available on request to researchers who wish to augment MusicNet with commercial recordings.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Dataset Construction", "weight": 1.0} -->

Music-to-score alignment is a long-standing problem in the music research and signal processing communities. Dynamic time warping (DTW) is a classical approach to this problem. An early use of DTW for music alignment is Orio & Schwarz where a recording is aligned to a crude synthesis of its score, designed to capture some of the structure of an overtone series. The method described in this paper aligns recordings to synthesized performances of scores, using side information from a commercial synthesizer. To the best of our knowledge, commercial synthesis was first used for the purpose of alignment in Turetsky & Ellis.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Dataset Construction", "weight": 1.0} -->

The majority of previous work on alignment focuses on pop music. This is more challenging than aligning classical music because commercial synthesizers do a poor job reproducing the wide variety of vocal and instrumental timbers that appear in modern pop. Furthermore, pop features inharmonic instruments such as drums for which natural metrics on frequency representations--including $\ell^{2}$--are not meaningful. For classical music to score alignment, a variant of the techniques described in Turetsky & Ellis works robustly. This method is described below; we discuss the evaluation of this procedure and its error rate on MusicNet in the appendix.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Dataset Construction", "weight": 1.0} -->

In order to align the performance with a score, we need to define a metric that compares short segments of the score with segments of a performance. Musical scores can be expressed as binary vectors in $E \times K$ where $E = {\{ 1,\ldots,n\}}$ and $K$ is a dictionary of notes. Performances reside in ${\mathbb{R}}^{T \times p}$, where $T \in {\{ 1,\ldots,m\}}$ is a sequence of time steps and $p$ is the dimensionality of the spectrogram at time $T$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Dataset Construction", "weight": 1.0} -->

Given some local cost function $C:{{({\mathbb{R}}^{p},K)}\rightarrow{\mathbb{R}}}$, a score $\mathbf{Y} \in {E \times K}$, and a performance $\mathbf{X} \in {\mathbb{R}}^{T \times p}$, the alignment problem is to Dynamic time warping gives an exact solution to the problem in $\mathcal{O}{({mn})}$ time and space.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dataset Construction", "weight": 1.0} -->

The success of dynamic time warping depends on the metric used to compare the score and the performance. Previous works can be broadly categorized into three groups that define an alignment cost $C$ between segments of music x and score y by injecting them into a common normed space via maps $\Psi$ and $\Phi$: The most popular approach--and the one adopted by this paper--maps the score into the space of the performance. An alternative approach maps both the score and performance into some third space, commonly a chromogram space. Finally, some recent methods consider alignment in score space, taking $\Phi = {Id}$ and learning $\Psi$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dataset Construction", "weight": 1.0} -->

With reference to the general cost, we must specify the maps $\Psi,\Phi$, and the norm $\parallel \cdot \parallel$. We compute the cost in the performance feature space ${\mathbb{R}}^{p}$, hence we take $\Psi = {Id}$. For the features, we use the log-spectrogram with a window size of 2048 samples. We use a stride of 512 samples between features. Hence adjacent feature frames are computed with 75% overlap. For audio sampled at 44.1kHz, this results in a feature representation with ${44,{100/512}} \approx 86$ frames per second. A discussion of these parameter choices can be found in the appendix. The map $\Phi$ is computed by a synthetizer: we used Plogue's Sforzando sampler together with Garritan's Personal Orchestra 4 sample library.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dataset Construction", "weight": 1.0} -->

For a (pseudo)-metric on ${\mathbb{R}}^{p}$, we take the $\ell^{2}$ norm $\parallel \cdot \parallel_{2}$ on the low $50$ dimensions of ${\mathbb{R}}^{p}$. Recall that ${\mathbb{R}}^{p}$ represents Fourier components, so we can roughly interpret the $k$'th coordinate of ${\mathbb{R}}^{p}$ as the energy associated with the frequency ${k \times \left( 22,{050/1024} \right)} \approx {k \times 22.5}$Hz, where $22,050$Hz is the Nyquist frequency of a signal sampled at $44.1$kHz. The 50 dimension cutoff is chosen empirically: we observe that the resulting alignments are more accurate using a small number of low-frequency bins rather than the full space ${\mathbb{R}}^{p}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Dataset Construction", "weight": 1.0} -->

Synthesizers do not accurately reproduce the high-frequency features of a musical instrument; by ignoring the high frequencies, we align on a part of the spectrum where the synthesis is most accurate. The proposed choice of cutoff is aggressive compared to usual settings; for instance, Turetsky & Ellis propose cutoffs in the $2.5$kHz range. The fundamental frequencies of many notes in MusicNet are higher than the ${{50 \times 22.5}\text{Hz}} \approx 1$kHz cutoff. Nevertheless, we find that all notes align well using only the low-frequency information.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Methods", "weight": 1.0} -->

We consider identification of notes in a segment of audio $\mathbf{x} \in \mathcal{X}$ as a multi-label classification problem, modeled as follows. Assign each audio segment a binary label vector $\mathbf{y} \in {\{ 0,1\}}^{128}$. The 128 dimensions correspond to frequency codes for notes, and $\mathbf{y}_{n} = 1$ if note $n$ is present at the midpoint of $\mathbf{x}$. Let $f:{\mathcal{X}\rightarrow\mathcal{H}}$ indicate a feature map. We train a multivariate linear regression to predict $\hat{\mathbf{y}}$ given $f{(\mathbf{x})}$, which we optimize for square loss.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Methods", "weight": 1.0} -->

The vector $\hat{\mathbf{y}}$ can be interpreted as a multi-label estimate of notes in $\mathbf{x}$ by choosing a threshold $c$ and predicting label $n$ iff ${\hat{\mathbf{y}}}_{n} > c$. We search for the value $c$ that maximizes $F_{1}$-score on a sampled subset of MusicNet.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Multi-layer perceptrons", "weight": 1.0} -->

We build a two-layer network with features ${f_{i}{(\mathbf{x})}} = {\log\left( {1 + {\max{(0,{\text{w}_{i}^{T}\mathbf{x}})}}} \right)}$. We find that compression introduced by a logarithm improves performance versus a standard ReLU network (see Table 3). Figure 1 illustrates a selection of weights $w_{i}$ learned by the bottom layer of this network. The weights learned by the network are modulated sinusoids. This explains the effectiveness of spectrograms as a low-level representation of musical audio. The weights decay at the boundaries, analogous to Gabor filters in vision. This behavior is explained by the labeling methodology: the audio segments used here are approximately $1/3$ of a second long, and a segment is given a note label if that note is on in the center of the segment. Therefore information at the boundaries of the segment is less useful for prediction than information nearer to the center.

<!-- chunk {"id": "body-0023", "role": "body", "section": "(log-)Spectrograms", "weight": 1.0} -->

Spectrograms are an engineered feature representation for musical audio signals, available in popular software packages such as librosa. Spectrograms (resp. log-spectrograms) are closely related to a two-layer ReLU network (resp. the log-ReLU network described above). If $\mathbf{x} = {(x_{1},\ldots,x_{t})}$ denotes a segment of an audio signal of length $t$ then we can define These features are not precisely learnable by a two-layer ReLU network.

<!-- chunk {"id": "body-0024", "role": "body", "section": "(log-)Spectrograms", "weight": 1.0} -->

But recall that ${|x|} = {{\max{(0,x)}} + {\max{(0,{- x})}}}$ and if we take weight vectors ${\mathbf{u},\mathbf{v}} \in {\mathbb{R}}^{T}$ with $u_{s} = {\cos{({{2\piks}/t})}}$ and $v_{s} = {\sin{({{2\piks}/t})}}$ then the ReLU network can learn We call this family of features a ReLUgram and observe that it has a similar form to the spectrogram; we merely replace the $x\mapsto x^{2}$ non-linearity of the spectrogram with $x\mapsto{|x|}$. These features achieve similar performance to spectrograms on the classification task (see Table 3).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Window Size", "weight": 1.0} -->

When we parameterize a network, we must choose the width of the set of weights in the bottom layer. This width is called the receptive field in the vision community; in the music community it is called the window size. Traditional frequency analyses, including spectrograms, are highly sensitive to the window size. Windows must be long enough to capture relevant information, but not so long that they lose temporal resolution; this is the classical time-frequency tradeoff. Furthermore, windowed frequency analysis is subject to boundary effects, known as spectral leakage. Classical signal processing attempts to dampen these effects with predefined window functions, which apply a mask that attenuates the signal at the boundaries.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Window Size", "weight": 1.0} -->

The proposed end-to-end models learn window functions. If we parameterize these models with a large window size then the model will learn that distant information is irrelevant to local prediction, so the magnitude of the learned weights will attenuate at the boundaries. We therefore focus on two window sizes: 2048 samples, which captures the local content of the signal, and 16,384 samples, which is sufficient to capture almost all relevant context (again see Figure 1).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Regularization", "weight": 1.0} -->

The size of MusicNet is essential to achieving the results in Figure 1. In Figure 3 (Left) we optimize a two-layer ReLU network on a small subset of MusicNet consisting of $65,000$ monophonic data points. While these features do exhibit dominant frequencies, the signal is quite noisy. Comparable noisy frequency selective features were recovered by Dieleman & Schrauwen; see their Figure 3. We can recover clean features on a small dataset using heavy regularization, but this destroys classification performance; regularizing with dropout poses a similar tradeoff. By contrast, Figure 3 (Right) shows weights learned by an unregularized two-layer network trained on the full MusicNet dataset. The models described in this paper do not overfit to MusicNet and optimal performance (reported in Table 3) is achieved without regularization.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Convolutional networks", "weight": 1.0} -->

Previously, we estimated $\hat{\mathbf{y}}$ by regressing against $f{(\mathbf{x})}$. We now consider a convolutional model that regresses against features of a collection of shifted segments $\mathbf{x}_{\ell}$ near to the original segment $\mathbf{x}$. The learned features of this network are visually comparable to those learned by the fully connected network (Figure 1). The parameters of this network are the receptive field, stride, and pooling regions. The results reported in Table 3 are achieved with 500 hidden units using a receptive field of $2,048$ samples with an 8-sample stride across a window of $16,384$ samples. These features are grouped into average pools of width 16, with a stride of 8 features between pools. A max-pooling operation yields similar results. The learned features are consistent across different parameterizations. In all cases the learned features are comparable to those of a fully connected network.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Results", "weight": 1.0} -->

We hold out a test set of 3 recordings for all the results reported in this section: Bach's Prelude in D major for Solo Piano. WTK Book 1, No 5. Performed by Kimiko Ishizaka. MusicNet recording id 2303.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results", "weight": 1.0} -->

Mozart's Serenade in E-flat major. K375, Movement 4 - Menuetto. Performed by the Soni Ventorum Wind Quintet. MusicNet recording id 1819.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

Beethoven's String Quartet No. 13 in B-flat major. Opus 130, Movement 2 - Presto. Released by the European Archive. MusicNet recording id 2382.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

The test set is a representative sampling of MusicNet: it covers most of the instruments in the dataset in small, medium, and large ensembles. The test data points are evenly spaced segments separated by 512 samples, between the 1st and 91st seconds of each recording. For the wider features, there is substantial overlap between adjacent segments. Each segment is labeled with the notes that are on in the middle of the segment.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate our models on three scores: precision, recall, and average precision. The precision score is the count of correct predictions by the model (across all data points) divided by the total number of predictions by the model. The recall score is the count of correct predictions by the model divided by the total number of (ground truth) labels in the test set. Precision and recall are parameterized by the note prediction threshold $c$ (see Sect. 4). By varying $c$, we construct precision-recall curves (see Figure 4). The average precision score is the area under the precision-recall curve.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

A spectrogram of length $n$ is computed from $2n$ samples, so the linear 1024-point spectrogram model is directly comparable to the MLP runs with 2048 raw samples. Learned features^44^4A demonstration using learned MLP features to synthesize a musical performance is available on the dataset webpage: modestly outperform spectrograms for comparable window sizes. The discussion of windowing in Sect. 4.4 partially explains this. Figure 5 suggests a second reason. Recall (Sect. 4.3Spectrograms ‣ 4 Methods ‣ Learning Features of Music from Scratch")) that the spectrogram features can be interpreted as the magnitude of the signal's inner product with sine waves of linearly spaced frequencies. In contrast, the proposed networks learn weights with frequencies distributed similarly to the distribution of notes in MusicNet (Figure 5). This gives the network higher resolution in the most critical frequency regions.
