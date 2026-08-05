<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Towards a Mathematical Theory of Super-Resolution

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper develops a mathematical theory of super-resolution. Broadly speaking, super-resolution is the problem of recovering the fine details of an object - the high end of its spectrum - from coarse scale information only - from samples at the low end of the spectrum. Suppose we have many point sources at unknown locations in and with unknown complex-valued amplitudes. We only observe Fourier samples of this object up until a frequency cut-off f_c. We show that one can super-resolve these point sources with infinite precision - i.e. recover the exact locations and amplitudes - by solving a simple convex optimization problem, which can essentially be reformulated as a semidefinite program. This holds provided that the distance between sources is at least 2/f_c. This result extends to higher dimensions and other models. In one dimension for instance, it is possible to recover a piecewise smooth function by resolving the discontinuity points with infinite precision as well. We also show that the theory and methods are robust to noise. In particular, in the discrete setting we develop some theoretical results explaining how the accuracy of the super-resolved signal is expected to degrade when both the noise level and the super-resolution factor vary.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Super-resolution", "weight": 1.0} -->

Super-resolution is a word used in different contexts mainly to design techniques for enhancing the resolution of a sensing system. Interest in such techniques comes from the fact that there usually is a physical limit on the highest possible resolution a sensing system can achieve. To be concrete, the spatial resolution of an imaging device may be measured by how closely lines can be resolved. For an optical system, it is well known that resolution is fundamentally limited by diffraction. In microscopy, this is called the Abbe diffraction limit and is a fundamental obstacle to observing sub-wavelength structures. This is the reason why resolving sub-wavelength features is a crucial challenge in fields such as astronomy, medical imaging, and microscopy. In electronic imaging, limitations stem from the lens and the size of the sensors, e. g. pixel size. Here, there is an inflexible limit to the effective resolution of a whole system due to photon shot noise which degrades image quality when pixels are made smaller. Some other fields where it is desirable to extrapolate fine scale details from low-resolution data---or resolve sub-pixel details---include spectroscopy, radar, non-optical medical imaging and geophysics.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Super-resolution", "weight": 1.0} -->

For a survey of super-resolution techniques in imaging, see and the references therein.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Super-resolution", "weight": 1.0} -->

This paper is about super-resolution, which loosely speaking is the process whereby the fine scale structure of an object is retrieved from coarse scale information only.^11^1We discuss here computational super-resolution methods as opposed to instrumental techniques such as interferometry. A useful mathematical model may be of the following form: start with an object $x{(t_{1},t_{2})}$ of interest, a function of two spatial variables, and the point-spread function $h{(t_{1},t_{2})}$ of an optical instrument. This instrument acts as a filter in the sense that we may observe samples from the convolution product In the frequency domain, this equation becomes where $\hat{x}$ is the Fourier transform of $x$, and $\hat{h}$ is the modulation transfer function or simply transfer function of the instrument.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Super-resolution", "weight": 1.0} -->

Now, common optical instruments act as low-pass filters in the sense that their transfer function $\hat{h}$ vanishes for all values of $\omega$ obeying ${|\omega|} \geq \Omega$ in which $\Omega$ is a frequency cut-off; that is, In microscopy with coherent illumination, the bandwidth $\Omega$ is given by $\Omega = {{2\pi\text{NA}}/\lambda}$ where NA is the numerical aperture and $\lambda$ is the wavelength of the illumination light. For reference, the transfer function in this case is simply the indicator function of a disk and the point-spread function has spherical symmetry and a radial profile proportional to the ratio between the Bessel function of the first order and the radius. In microscopy with incoherent light, the transfer function is the Airy function and is proportional to the square of the coherent point-spread function. Regardless, the frequency cut-off induces a physical resolution limit which is roughly inversely proportional to $\Omega$ (in microscopy, the Rayleigh resolution distance is defined to be ${{0.61 \times 2}\pi}/\Omega$).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Super-resolution", "weight": 1.0} -->

The daunting and ill-posed super-resolution problem then consists in recovering the fine-scale or, equivalently, the high-frequency features of $x$ even though they have been killed by the measurement process. This is schematically represented in Figure 1, which shows a highly resolved signal together with a low-resolution of the same signal obtained by convolution with a point-spread function. Super-resolution aims at recovering the fine scale structure on the left from coarse scale features on the right. Viewed in the frequency domain, super-resolution is of course the problem of extrapolating the high-end and missing part of the spectrum from the low-end part, as seen in Figure 2. For reference, this is very different from a typical compressed sensing problem in which we wish to interpolate---and not extrapolate---the spectrum.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Super-resolution", "weight": 1.0} -->

This paper develops a mathematical theory of super-resolution, which is not developed at all despite the abundance of empirical work in this area, see Section 1.8 for some references. Our theory takes multiple forms but a simple and appealing incarnation is as follows. Suppose we wish to super-resolve a spike-train signal as in Figure 1, namely, a superposition of pointwise events. Our main result is that we can recover such a signal exactly from low-frequency samples by tractable convex optimization in which one simply minimizes the continuous analog to the $\ell_{1}$ norm for discrete signals subject to data constraints. This holds as long as the spacing between the spikes is on the order of the resolution limit. Furthermore, the theory shows that this procedure is robust in the sense that it degrades smoothly when the measurements are contaminated with noise. In fact, we shall quantify quite precisely the error one can expect as a function of the size of the input noise and of the resolution one wishes to achieve.\

<!-- chunk {"id": "body-0009", "role": "body", "section": "Models and methods", "weight": 1.0} -->

For concreteness, consider a continuous-time model in which the signal of interest is a weighted superposition of spikes where $\{ t_{j}\}$ are locations in $\lbrack 0,1\rbrack$ and $\delta_{\tau}$ is a Dirac measure at $\tau$. The amplitudes $a_{j}$ may be complex valued. Expressed differently, the signal $x$ is an atomic measure on the unit interval putting complex mass at time points $t_{1}$, $t_{2}$, $t_{3}$ and so.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Models and methods", "weight": 1.0} -->

The information we have available about $x$ is a sample of the lower end of its spectrum in the form of the lowest ${2f_{c}} + 1$ Fourier series coefficients ($f_{c}$ is an integer): For simplicity, we shall use matrix notations to relate the data $y$ and the object $x$ and will write (1.3) as $y = {\mathcal{F}_{n}x}$ where $\mathcal{F}_{n}$ is the linear map collecting the lowest $n = {{2f_{c}} + 1}$ frequency coefficients. It is important to bear in mind that we have chosen this model mainly for ease of exposition. Our techniques can be adapted to settings where the measurements are modeled differently, e. g. by sampling the convolution of the signal with different low-pass kernels. The important element is that just as before, the frequency cut-off induces a resolution limit inversely proportional to $f_{c}$; below we set $\lambda_{c} = {1/f_{c}}$ for convenience.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Models and methods", "weight": 1.0} -->

To recover $x$ from low-pass data we shall find, among all measures fitting the observations, that with lowest total variation. The total variation of a complex measure (see Section A in the Appendix for a rigorous definition) can be interpreted as being the continuous analog to the $\ell_{1}$ norm for discrete signals. In fact, with $x$ as in (1.2), ${\| x\|}_{\text{TV}}$ is equal to the $\ell_{1}$ norm of the amplitudes ${\| a\|}_{1} = {\sum_{j}{|a_{j}|}}$. Hence, we propose solving the convex program where the minimization is carried out over the set of all finite complex measures $\overset{\sim}{x}$ supported on $\lbrack 0,1\rbrack$. Our first result shows that if the spikes or atoms are sufficiently separated, at least $2\lambda_{c}$ apart, the solution to this convex program is exact.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Super-resolution in higher dimensions", "weight": 1.0} -->

Our results extend to higher dimensions and reveal the same dependence between the minimum separation and the measurement resolution as in one dimension. For concreteness, we discuss the $2$-dimensional setting and emphasize that the situation in $d$ dimensions is similar. Here, we have a measure as before but in which the $t_{j} \in {\lbrack 0,1\rbrack}^{2}$. We are given information about $x$ in the form of low-frequency samples of the form This again introduces a physical resolution of about $\lambda_{c} = {1/f_{c}}$. In this context, we may think of our problem as imaging point sources in the 2D plane---such as idealized stars in the sky---with an optical device with resolution about $\lambda_{c}$---such as a diffraction limited telescope. Our next result states that it is possible to locate the point sources without any error whatsoever if they are separated by a distance of $2.38\lambda_{c}$ simply by minimizing the total variation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Discrete super-resolution", "weight": 1.0} -->

Our continuous theory immediately implies analogous results for finite signals. Suppose we wish to recover a discrete signal $x \in {\mathbb{C}}^{N}$ from low-frequency data. Just as before, we could imagine collecting low-frequency samples of the form the connection with the previous sections is obvious since $x$ might be interpreted as samples of a discrete signal on a grid $\{{t/N}\}$ with $t = {0,1,\ldots,{N - 1}}$. In fact, the continuous-time setting is the limit of infinite resolution in which $N$ tends to infinity while the number of samples remains constant ($f_{c}$ fixed). Instead, we can choose to study the regime in which the ratio between the actual resolution of the signal $1/N$ and the resolution of the data defined as $1/f_{c}$ is constant. This gives the corollary below.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The super-resolution factor", "weight": 1.0} -->

In the discrete framework, we wish to resolve a signal on a fine grid with spacing $1/N$. However, we only observe the lowest $n = {{2f_{c}} + 1}$ Fourier coefficients so that in principle, one can only hope to recover the signal on a coarser grid with spacing only $1/n$ as shown in Figure 4. Hence, the factor $N/n$, or equivalently, the ratio between the spacings in the coarse and fine grids, can be interpreted as a super-resolution factor (SRF). Below, we set when the SRF is equal to 5 as in the figure, we are looking for a signal at a resolution 5 times higher than what is stricto senso permissible. One can then recast Corollary 1.4 as follows: if the nonzero components of ${\{ x_{t}\}}_{t = 0}^{N - 1}$ are separated by at least $4 \times \text{SRF}$, perfect super-resolution via $\ell_{1}$ minimization occurs.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The super-resolution factor", "weight": 1.0} -->

The reason for introducing the SRF is that with inexact data, we obviously cannot hope for infinite resolution. Indeed, noise will ultimately limit the resolution one can ever hope to achieve and, therefore, the question of interest is to study the accuracy one might expect from a practical super-resolution procedure as a function of both the noise level and the SRF.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Stability", "weight": 1.0} -->

To discuss the robustness of super-resolution methods vis a vis noise, we examine in this paper the discrete setting of Section 1.4. In this setup, we could certainly imagine studying a variety of deterministic and stochastic noise models, and a variety of metrics in which to measure the size of the error. For simplicity, we study a deterministic scenario in which the projection of the noise onto the signal space has bounded $\ell_{1}$ norm but is otherwise arbitrary and can be adversarial. The observations are consequently of the form for some $\delta \geq 0$, where $F_{n}$ is as before.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Stability", "weight": 1.0} -->

Letting $P_{n}$ be the orthogonal projection of a signal onto the first $n$ Fourier modes, $P_{n} = {\frac{1}{N}F_{n}^{\ast}F_{n}}$, we can view (1.13) as an input noise model since with $w = {F_{n}z}$, we have Another way to write this model with arbitrary input noise $z \in {\mathbb{C}}^{N}$ is since the high-frequency part of $z$ is filtered out by the measurement process. Finally, with $s = {N^{- 1}F_{n}^{\ast}y}$, (1.13) is equivalent to In words, we observe a low-pass version of the signal corrupted with an additive low-pass error whose $\ell_{1}$ norm is at most $\delta$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stability", "weight": 1.0} -->

In the case where $n = N$, $P_{n} = I$, and our model becomes In this case, one cannot hope for a reconstruction $\hat{x}$ with an error in the $\ell_{1}$ norm less than the noise level $\delta$. We now wish to understand how quickly the recovery error deteriorates as the super-resolution factor increases.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stability", "weight": 1.0} -->

We propose studying the relaxed version of the noiseless problem (1.11) We show that this recovers $x$ with a precision inversely proportional to $\delta$ and to the square of the super-resolution factor.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sparsity and stability", "weight": 1.0} -->

Researchers in the field know that super-resolution under sparsity constraints alone is hopelessly ill posed. In fact, without a minimum distance condition, the support of sparse signals can be very clustered, and clustered signals can be nearly completely annihilated by the low-pass sensing mechanism. The extreme ill-posedness can be understood by means of the seminal work of Slepian on discrete prolate spheroidal sequences. This is surveyed in Section 3.2 but we give here a concrete example to drive this point home.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sparsity and stability", "weight": 1.0} -->

To keep things simple, we consider the 'analog version' of (1.14) in which we observe $\mathcal{P}_{W}{(x)}$ is computed by taking the discrete-time Fourier transform ${y{(\omega)}} = {\sum_{t \in {\mathbb{Z}}}{x_{t}e^{- {i2\pi\omegat}}}}$, ${\omega \in {\lbrack{- {1/2}},{1/2}\rbrack}},$ and discarding all 'analog' frequencies outside of the band $\lbrack{- W},W\rbrack$. If we set we essentially have $\mathcal{P}_{W} = P_{n}$ where the equality is true in the limit where $N\rightarrow\infty$ (technically, $\mathcal{P}_{W}$ is the convolution with the sinc kernel while $P_{n}$ uses the Dirichlet kernel).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sparsity and stability", "weight": 1.0} -->

Set a mild level of super-resolution to fix ideas, Now the work of Slepian shows that there is a $k$-sparse signal supported on $\lbrack 0,\ldots,{k - 1}\rbrack$ obeying Even knowing the support ahead of time, how are we going to recover such signals from noisy measurements? Even for a very mild super-resolution factor of just $\text{SRF} = 1.05$ (we only seek to extend the spectrum by 5%), (1.17) becomes which implies that there exists a unit-norm signal with at most $256$ consecutive nonzero entries such that ${\|{\mathcal{P}_{W}x}\|}_{2} \leq {1.2 \times 10^{- 15}}$. Of course, as the super-resolution factor increases, the ill-posedness gets worse. For large values of SRF, there is $x$ obeying (1.17) with It is important to emphasize that this is not a worst case analysis.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sparsity and stability", "weight": 1.0} -->

In fact, with $k = 48$ and $\text{SRF} = 4$, Slepian shows that there is a large dimensional subspace of signals supported on ${\mathbb{C}}^{k}$ spanned by orthonormal eigenvectors with eigenvalues of magnitudes nearly as small as (1.18).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Comparison with related work", "weight": 1.0} -->

The use of $\ell_{1}$ minimization for the recovery of sparse spike trains from noisy bandlimited measurements has a long history and was proposed in the 1980s by researchers in seismic prospecting. For finite signals and under the rather restrictive assumption that the signal is real valued and nonnegative, and prove that $k$ spikes can be recovered from ${2k} + 1$ Fourier coefficients by this method. The work extends this result to the continuous setting by using total-variation minimization. In contrast, our results require a minimum distance between spikes but allow for arbitrary complex amplitudes, which is crucial in applications. The only theoretical guarantee we are aware of concerning the recovery of spike trains with general amplitudes is very recent and due to Kahane. Kahane offers variations on compressive sensing results in and studies the reconstruction of a function with lacunary Fourier series coefficients from its values in a small contiguous interval, a setting that is equivalent to that of Corollary 1.4 when the size $N$ of the fine grid tends to infinity.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Comparison with related work", "weight": 1.0} -->

With our notation, whereas we require a minimum distance equal to $4 \times \text{SRF}$, this work shows that a minimum distance of ${10 \times \text{SRF}}\sqrt{\log\text{SRF}}$ is sufficient for exact recovery. Although the log factor might seem unimportant at first glance, it in fact precludes extending Kahane's result to the continuous setting of Theorem 1.2. Indeed, by letting the resolution factor tend to infinity so as to approach the continuous setting, the spacing between consecutive spikes would need to tend to infinity as well.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Comparison with related work", "weight": 1.0} -->

As to results regarding the robustness of super-resolution in the presence of noise, Donoho studies the modulus of continuity of the recovery of a signed measure on a discrete lattice from its spectrum on the interval $\left\lbrack {- f_{c}},f_{c} \right\rbrack$, a setting which is also equivalent to that of Corollary 1.4 when the size $N$ of the fine grid tends to infinity. More precisely, if the support of the measure is constrained to contain at most $\ell$ elements in any interval of length $2/{({\ellf_{c}})}$, then the modulus of continuity is of order $O\left( \text{SRF}^{{2\ell} + 1} \right)$ as SRF grows to infinity (note that for $\ell = 1$ the constraint reduces to a minimum distance condition between spikes, which is comparable to the separation condition (1.6)).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Comparison with related work", "weight": 1.0} -->

This means that if the $\ell_{2}$ norm of the difference between the measurements generated by two signals satisfying the support constraints is known to be at most $\delta$, then the $\ell_{2}$ norm of the difference between the signals may be of order $O\left( {\text{SRF}^{{2\ell} + 1}\delta} \right)$. This result suggests that, in principle, the super-resolution of spread-out signals is not hopelessly ill-conditioned. Having said this, it does not propose any practical recovery algorithm (a brute-force search for sparse measures obeying the low-frequency constraints would be computationally intractable).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Comparison with related work", "weight": 1.0} -->

Finally, we would like to mention an alternative approach to the super-resolution of pointwise events from coarse scale data. Leveraging ideas related to error correction codes and spectral estimation, shows that it is possible to recover trains of Dirac distributions from low-pass measurements at their rate of innovation (in essence, the density of spikes per unit of time). This problem, however, is extraordinarily ill posed without a minimum separation assumption as explained in Sections 1.7 and 3.2. Moreover, the proposed reconstruction algorithm in needs to know the number of events ahead of time, and relies on polynomial root finding. As a result, it is highly unstable in the presence of noise as discussed, and in the presence of approximate sparsity. Algebraic techniques have also been applied to the location of singularities in the reconstruction of piecewise polynomial functions from a finite number of Fourier coefficients (see and references therein). The theoretical analysis of these methods proves their accuracy up to a certain limit related to the number of measurements. Corollary 1.6 takes a different approach, guaranteeing perfect localization if there is a minimum separation between the singularities.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Connections to sparse recovery literature", "weight": 1.0} -->

Theorem 1.2 and Corollary 1.4 can be interpreted in the framework of sparse signal recovery. For instance, by swapping time and frequency, Corollary 1.4 asserts that one can recover a sparse superposition of tones with arbitrary frequencies from $n$ time samples of the form where the frequencies are of the form $\omega_{j} = {j/N}$. Since the spacing between consecutive frequencies is not $1/n$ but $1/N$, we may have a massively oversampled discrete Fourier transform, where the oversampling ratio is equal to the super-resolution factor. In this context, a sufficient condition for perfectly super-resolving these tones is a minimum separation of $4/n$. In addition, Theorem 1.2 extends this to continuum dictionaries where tones $\omega_{j}$ can take on arbitrary real values.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Connections to sparse recovery literature", "weight": 1.0} -->

In the literature, there are several conditions that guarantee perfect signal recovery by $\ell_{1}$ minimization. The results obtained from their application to our problem are, however, very weak.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Connections to sparse recovery literature", "weight": 1.0} -->

The matrix with normalized columns $f_{j} = {\{{e^{- {i2\pit\omega_{j}}}/\sqrt{n}}\}}_{t = 0}^{n - 1}$ does not obey the restricted isometry property since a submatrix composed of a very small number of contiguous columns is already very close to singular, see and Section 3.2 for related claims. For example, with $N = 512$ and a modest SRF equal to 4, the smallest singular value of submatrices formed by eight consecutive columns is $3.32\;10^{- 5}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Connections to sparse recovery literature", "weight": 1.0} -->

Applying the discrete uncertainty principle proved, we obtain that recovery by $\ell_{1}$ minimization succeeds as long as If $n < {N/2}$, i.e. $\text{SRF} > 2$, this says that $|T|$ must be zero. In other words, to recover one spike, we would need at least half of the Fourier samples.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Connections to sparse recovery literature", "weight": 1.0} -->

Other guarantees based on the coherence of the dictionary yield similar results. A popular condition requires that where $M$ is the coherence of the system defined as $\max_{i \neq j}{|{\langle f_{i},f_{j}\rangle}|}$. When $N = 1024$ and $\text{SRF} = 4$, $M \approx 0.9003$ so that this becomes ${|T|} \leq 1.055$, and we can only hope to recover one spike.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Connections to sparse recovery literature", "weight": 1.0} -->

There are slightly improved versions of (1.21). In, Dossal studies the deconvolution of spikes by $\ell_{1}$ minimization. This work introduces the weak exact recovery condition (WERC) defined as The condition ${\text{WERC}(T)} < 1$ guarantees exact recovery. Considering three spikes and using Taylor expansions to bound the sine function, the minimum distance needed to ensure that ${\text{WERC}(T)} < 1$ may be lower bounded by ${{24\text{SRF}^{3}}/\pi^{3}} - {2\text{SRF}}$. This is achieved by considering three spikes at $\omega \in {\{ 0,{\pm \Delta}\}}$, where $\Delta = {{({k + {1/2}})}/n}$ for some integer $k$; we omit the details.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Connections to sparse recovery literature", "weight": 1.0} -->

If $N = {20,000}$ and the number of measurements is $1,000$, this allows for the recovery of at most $3$ spikes, whereas Corollary 1.4 implies that it is possible to reconstruct at least ${n/4} = 250$. Furthermore, the cubic dependence on the super-resolution factor means that if we fix the number of measurements and let $N\rightarrow\infty$, which is equivalent to the continuous setting of Theorem 1.2, the separation needed becomes infinite and we cannot guarantee the recovery of even two spikes.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Connections to sparse recovery literature", "weight": 1.0} -->

Finally, we would also like to mention some very recent work on sparse recovery in highly coherent frames by modified greedy compressed sensing algorithms. Interestingly, these approaches explicitly enforce conditions on the recovered signals that are similar in spirit to our minimum distance condition. As opposed to $\ell_{1}$-norm minimization, such greedy techniques may be severely affected by large dynamic ranges (see ) because of the phenomenon illustrated in Figure 3. Understanding under what conditions their performance may be comparable to that of convex programming methods is an interesting research direction.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Extensions", "weight": 1.0} -->

Our results and techniques can be extended to super-resolve many other types of signals. We just outline such a possible extension. Suppose $x:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{C}}}$ is a periodic piecewise smooth function with period 1, defined by on each time interval $(t_{j - 1},t_{j})$, $x$ is polynomial of degree $\ell$. For $\ell = 0$, we have a piecewise constant function, for $\ell = 1$, a piecewise linear function and so. Also suppose $x$ is globally $\ell - 1$ times continuously differentiable (as for splines).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Extensions", "weight": 1.0} -->

We observe The $({\ell + 1})$th derivative of $x$ (in the sense of distributions) denoted by $x^{({\ell + 1})}$ is an atomic measure supported on $T$ and equal to Hence, we can imagine recovering $x^{({\ell + 1})}$ by solving Standard Fourier analysis gives that the $k$th Fourier coefficient of this measure is given by Hence, we observe the Fourier coefficients of $x^{({\ell + 1})}$ except that corresponding to $k = 0$, which must vanish since the periodicity implies ${\int_{0}^{1}{x^{({\ell + 1})}{({\text{d}t})}}} = 0 = {\int_{0}^{1}{x^{(j)}{(t)}\text{d}t}}$, $1 \leq j \leq \ell$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Extensions", "weight": 1.0} -->

Hence, it follows from Theorem 1.2 that (1.22) recovers $x^{({\ell + 1})}$ exactly as long as the discontinuity points are at least $2\lambda_{c}$ apart. Because $x$ is $\ell - 1$ times continuously differentiable and periodic, $x^{({\ell + 1})}$ determines $x$ up to a shift in function value, equal to its mean. However, we can read the mean value of $x$ off $y_{0} = {\int_{0}^{1}{x{(t)}\text{d}t}}$ and, therefore, (1.22) achieves perfect recovery.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Organization of the paper", "weight": 1.0} -->

The remainder of the paper is organized as follows. We prove our main noiseless result in Section 2. There, we introduce our techniques which involve the construction of an interpolating low-frequency polynomial. Section 3 proves our stability result and argues that sparsity constraints cannot be sufficient to guarantee stable super-resolution. Section 4 shows that (1.4) can be cast as a finite semidefinite program. Numerical simulations providing a lower bound for the minimum distance that guarantees exact recovery are presented in Section 5. We conclude the paper with a short discussion in Section 6.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Noiseless Recovery", "weight": 1.0} -->

This section proves the noiseless recovery result, namely, Theorem 1.2. Here and below, we write $\Delta = {\Delta{(T)}} \geq \Delta_{\text{min}} = {2\lambda_{c}}$. Also, we identify the interval $\lbrack 0,1)$ with the circle $\mathbb{T}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Dual polynomials", "weight": 1.0} -->

In the discrete setting, the compressed sensing literature has made clear that the existence of a certain dual certificate guarantees that the $\ell_{1}$ solution is exact. In the continuous setting, a sufficient condition for the success of the total-variation solution is this: for any $v \in {\mathbb{C}}^{|T|}$ with ${|v_{j}|} = 1$, there exists a low-frequency trigonometric polynomial obeying the following properties This result follows from elementary measure theory and is included in Section A of the Appendix for completeness. Constructing a bounded low-frequency polynomial interpolating the sign pattern of certain signals becomes increasingly difficult if the minimum distance separating the spikes is too small. This is illustrated in Figure 5, where we show that if spikes are very near, it would become in general impossible to find an interpolating low-frequency polynomial obeying (2.2).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Proofs of Lemmas", "weight": 1.0} -->

The proofs of the three lemmas above make repeated use of the fact that the interpolation kernel and its derivatives decay rapidly away from the origin. The intermediate result below proved in Section B of the Appendix quantifies this.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Improvement for real-valued signals", "weight": 1.0} -->

The proof for real-valued signals is almost the same as the one we have discussed for complex-valued signals---only simpler. The only modification to Lemmas 2.2 and 2.4 is that the minimum distance is reduced to $1.87\lambda_{c}$, and that the bound in Lemma 2.4 is shown to hold starting at $0.17\lambda_{c}$ instead of $0.1649\lambda_{c}$. For reference, we provide upper bounds on $F_{\ell}{({1.87\lambda_{c}},t)}$ at $t \in {\{ 0,{0.17\lambda_{c}}\}}$ in Table 4. As to Lemma 2.3, the only difference is that to bound $|q|$ between the origin and $0.17\lambda_{c}$, it is sufficient to show that the second derivative of $q$ is negative and make sure that $q > {- 1}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Stability", "weight": 1.0} -->

This section proves Theorem 1.5 and we begin by establishing a strong form of the null-space property. In the remainder of the paper $P_{T}$ is the orthogonal projector onto the linear space of vectors supported on $T$, namely, ${({P_{T}x})}_{i} = x_{i}$ if $i \in T$ and is zero otherwise.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Sparsity is not enough", "weight": 1.0} -->

Consider the vector space ${\mathbb{C}}^{48}$ of sparse signals of length $N = 4096$ supported on a certain interval of length 48. Figure 7 shows the eigenvalues of the low-pass filter $P_{n} = {\frac{1}{N}F_{n}F_{n}^{\ast}}$ acting on ${\mathbb{C}}^{48}$ for different values of the super-resolution factor. For $\text{SRF} = 4$, there exists a subspace of dimension 24 such that any unit-normed signal (${\| x\|}_{2} = 1$) belonging to it obeys For $\text{SRF} = 16$ this is true of a subspace of dimension 36, two thirds of the total dimension. Such signals can be completely canceled out by perturbations of norm $5.02\;10^{- 8}$, so that even at signal-to-noise ratios (SNR) of more than 145 dB, recovery is impossible by any method whatsoever.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Sparsity is not enough", "weight": 1.0} -->

Interestingly, the sharp transition shown in Figure 7 between the first singular values almost equal to one and the others, which rapidly decay to zero, can be characterized asymptotically by using the work of Slepian on prolate spheroidal sequences. Introduce the operator $\mathcal{T}_{k}$, which sets the value of an infinite sequence to zero on the complement of an interval $T$ of length $k$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Sparsity is not enough", "weight": 1.0} -->

With the notation of Section 1.7, the eigenvectors of the operator $\mathcal{P}_{W}\mathcal{T}_{k}$ are the discrete prolate spheroidal sequences ${\{ s_{j}\}}_{j = 1}^{k}$ introduced, Set $v_{j} = {{\mathcal{T}_{k}s_{j}}/\sqrt{\lambda_{j}}}$, then by (3.4), it is not hard to see that In fact, the $v_{j}$'s are also orthogonal to each other, and so they form an orthonormal basis of ${\mathbb{C}}^{k}$ (which can represent any sparse vector supported on $T$).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Sparsity is not enough", "weight": 1.0} -->

For values of $j$ near $k$, the value of $\lambda_{j}$ is about Therefore, for a fixed value of $\text{SRF} = {{1/2}W}$, and $k \geq 20$, the small eigenvalues are equal to zero for all practical purposes. In particular, for $\text{SRF} = 4$ and $\text{SRF} = 1.05$ we obtain (1.17) and (1.19) in Section 1.7 respectively. Additionally, a Taylor series expansion of $\gamma$ for large values of SRF yields (1.20).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Sparsity is not enough", "weight": 1.0} -->

Since ${\|{\mathcal{P}_{W}v_{j}}\|}_{L_{2}} = \sqrt{\lambda_{j}}$, the bound on $\lambda_{j}$ for $j$ near $k$ directly implies that some sparse signals are essentially zeroed out, even for small super-resolution factors. However, Figure 7 suggests an even stronger statement: as the super-resolution factor increases not only some, but most signals supported on $T$ seem to be almost completely suppressed by the low pass filtering. Slepian provides an asymptotic characterization for this phenomenon. Indeed, just about the first $2kW$ eigenvalues of $\mathcal{P}_{W}\mathcal{T}_{k}$ cluster near one, whereas the rest decay abruptly towards zero.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Sparsity is not enough", "weight": 1.0} -->

To be concrete, for any $\epsilon > 0$ and $j \geq {2kW\left({1 + \epsilon} \right)}$, there exist positive constants $C_{0}$, and $\gamma_{0}$ (depending on $\epsilon$ and $W$) such that This holds for all $k \geq k_{0}$, where $k_{0}$ is some fixed integer. This implies that for any interval $T$ of length $k$, there exists a subspace of signals supported on $T$ with dimension asymptotically equal to $\left({1 - {1/\text{SRF}}} \right)k$, which is obliterated by the measurement process. This has two interesting consequences. First, even if the super-resolution factor is just barely above one, asymptotically there will always exist an irretrievable vector supported on $T$. Second, if the super-resolution factor is two or more, most of the information encoded in clustered sparse signals is lost.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Sparsity is not enough", "weight": 1.0} -->

Consider for instance a random sparse vector $x$ supported on $T$ with i.i.d. entries. Its projection onto a fixed subspace of dimension about $\left({1 - {1/\text{SRF}}} \right)k$ (corresponding to the negligible eigenvalues) contains most of the energy of the signal with high probability. However, this component is practically destroyed by low-pass filtering. Hence, super-resolving almost any tightly clustered sparse signal in the presence of noise is hopeless. This justifies the need for a minimum separation between nonzero components.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Minimization via semidefinite programming", "weight": 1.0} -->

At first sight, finding the solution to the total-variation norm problem (1.4) might seem quite challenging, as it requires solving an optimization problem over an infinite dimensional space. It is of course possible to approximate the solution by discretizing the support of the signal, but this could lead to an increase in complexity if the discretization step is reduced to improve precision. Another possibility is to try approximating the solution by estimating the support of the signal in an iterative fashion. Here, we take a different route and show that (1.4) can be cast as a semidefinite program with just $\left( {n + 1} \right)^{2}/2$ variables, and that highly accurate solutions can be found rather easily. This formulation is similar to that in which concerns a related infinite dimensional convex program. Our exposition is less formal here than in the rest of the paper.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Minimization via semidefinite programming", "weight": 1.0} -->

The convex program dual to (1.4) is the constraint says that the trigonometric polynomial ${{({\mathcal{F}_{n}^{\ast}c})}{(t)}} = {\sum_{{|k|} \leq f_{c}}{c_{k}e^{i2\pikt}}}$ has a modulus uniformly bounded by $1$ over the interval $\lbrack 0,1\rbrack$. The interior of the feasible set contains the origin and is consequently non empty, so that strong duality holds by a generalized Slater condition. The cost function involves a finite vector of dimension $n$, but the problem is still infinite dimensional due to the constraints. A corollary to Theorem 4.24 in allows to express this constraint as the intersection between the cone of positive semidefinite matrices $\{ X:{X \succeq 0}\}$ and an affine hyperplane.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

To evaluate the minimum distance needed to guarantee exact recovery by $\ell_{1}$ minimization of any signal in ${\mathbb{C}}^{N}$, for a fixed $N$, we propose the following heuristic scheme: For a super-resolution factor $\text{SRF} = {N/n}$, we work with a partial DFT matrix $F_{n}$ with frequencies up to $f_{c} = {\lfloor{n/2}\rfloor}$. Fix a candidate minimum distance $\Delta$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Using a greedy algorithm, construct an adversarial support with elements separated by at least $\Delta$ by sequentially adding elements to the support. Each new element is chosen to minimize the condition number formed by the columns corresponding to the selected elements.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Take the signal $x$ to be the singular vector corresponding to the smallest singular value of $F_{n}$ restricted to $T$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Solve the $\ell_{1}$-minimization problem (1.11) and declare that exact recovery occurs if the normalized error is below a threshold (in our case $10^{- 4}$).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

This construction of an adversarial signal was found to be better adapted to the structure of our measurement matrix than other methods proposed in the literature such as. We used this scheme and a simple binary search to determine a lower bound for the minimum distance that guarantees exact recovery for $N = 4096$, super-resolution factors of 8, 16, 32 and 64 and support sizes equal to 2, 5, 10, 20 and 50. The simulations were carried out in Matlab, using CVX to solve the optimization problem. Figure 12 shows the results, which suggest that on the discrete grid we need at least a minimum distance equal to twice the super-resolution factor in order to guarantee reconstruction of the signal (red curve). Translated to the continuous setting, in which the signal would be supported on a grid with spacing $1/N$, this implies that $\Delta \gtrsim \lambda_{c}$ is a necessary condition for exact recovery.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we have developed the beginning of a mathematical theory of super-resolution. In particular, we have shown that we can super-resolve 'events' such as spikes, discontinuity points, and so on with infinite precision from just a few low-frequency samples by solving convenient convex programs. This holds in any dimension provided that the distance between events is proportional to ${1/f_{c}} = \lambda_{c}$, where $f_{c}$ is the highest observed frequency; for instance, in one dimension, a sufficient condition is that the distance between events is at least $2\lambda_{c}$. Furthermore, we have proved that when such condition holds, stable recovery is possible whereas super-resolution---by any method whatsoever---is in general completely hopeless whenever events are at a distance smaller than about $\lambda_{c}/2$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Improvement", "weight": 1.0} -->

In one dimension, Theorem 1.2 shows that a sufficient condition for perfect super-resolution is ${\Delta{(T)}} \geq {2\lambda_{c}}$. Furthermore, the authors of this paper have a proof showing that ${\Delta{(T)}} \geq {1.85\lambda_{c}}$ is sufficient. This proof, however, is longer and more technical and, therefore, not presented here. In fact, we expect that arguments more sophisticated than those presented here would allow to lower this value even further. On the other hand, our numerical experiments show that we need at least ${\Delta{(T)}} \geq \lambda_{c}$ as one can otherwise find sparse signals which cannot be recovered by $\ell_{1}$ minimization. Hence, the minimum separation needed for success is somewhere between $\lambda_{c}$ and $1.85\lambda_{c}$. It would be interesting to know where this critical value might be.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Extensions", "weight": 1.0} -->

We have focused in this paper on the super-resolution of point sources, and by extension of discontinuity points in the function value, or in the derivative and so. Clearly, there are many other models one could consider as well. For instance, we can imagine collecting low-frequency Fourier coefficients of a function where $\{{\varphi_{j}{(t)}}\}$ are basis functions. Again, $f$ may have lots of high-frequency content but we are only able to observe the low-end of the spectrum. An interesting research question is this: suppose the coefficient sequence $x$ is sparse, then under what conditions is it possible to super-resolve $f$ and extrapolate its spectrum accurately? In a different direction, it would be interesting to extend our stability results to other noise models and error metrics. We leave this to further research.
