<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Optimum Method for Two-Level Rendition of Continuous-Tone Pictures

Topics include Ordered dithering, Digital halftoning, Dither matrices, Image processing, Computer graphics, Bilevel rendering.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Bayer introduces the ordered dithering construction now associated with Bayer matrices, giving a deterministic way to render continuous-tone images on bilevel devices. The work became a foundational reference for digital halftoning because it turns tone reproduction into a spatial threshold-pattern design problem rather than a purely local quantization rule.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A rule is established for designing optimum dither patterns for two-level rendition of continuous-tone pictures. In such a rendition, apparent brightness is controlled by the presence or absence of fixed-sized dots on a regular picture lattice. The dither pattern specifies the order in which these dots are added to the lattice as brightness is varied, and therefore dictates picture quality. The visibility of unwanted artificial texture can be measured usefully in terms of a Fourier analysis of the dot patterns at different brightness levels. When the dot pattern for a uniform patch has components at several different wavelengths, that component or components with the longest finite wavelength should usually be the most visible. If this longest wavelength is used as a measure of quality, a necessary and sufficient rule can be derived for the optimum order of adding dots to the lattice. The rule applies to the construction of dither patterns having a basic subcell of either 2^n by 2^n or 3^n by 2^n lattice points. The 4 by 4 square, ordered-dither pattern described by Limb and also by Lippel and Kurland satisfies this rule. Use of the rule ensures that picture detail will be rendered well.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Pictures are included whereby the optimum arrangement can be compared visually with a random arrangement and with a simulated halftone print.
