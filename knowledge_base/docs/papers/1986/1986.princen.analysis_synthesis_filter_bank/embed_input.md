<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Analysis/Synthesis Filter Bank Design Based on Time Domain Aliasing Cancellation

Topics include Audio compression, Signal processing, Filtering, Transforms, Information theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Establishes the time-domain aliasing cancellation principle behind lapped, critically sampled analysis/synthesis filter banks. The result is central to practical transform audio coding because it enables efficient overlapping blocks with perfect reconstruction, a path that later codecs exploit through MDCT-style filter banks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A single-sideband analysis/synthesis system is proposed which provides perfect reconstruction of a signal from a set of critically sampled analysis signals. The technique is developed in terms of a weighted overlap-add method of analysis/synthesis and allows overlap between adjacent time windows. This implies that time domain aliasing is introduced in the analysis; however, this aliasing is cancelled in the synthesis process, and the system can provide perfect reconstruction. Achieving perfect reconstruction places constraints on the time domain window shape which are equivalent to those placed on the frequency domain shape of analysis/synthesis channels used in recently proposed critically sampled systems based on frequency domain aliasing cancellation. In fact, a duality exists between the new technique and the frequency domain techniques. The proposed technique is more efficient than frequency domain designs for a given number of analysis/synthesis channels, and can provide reasonably band-limited channel responses. The technique could be particularly useful in applications where critically sampled analysis/synthesis is desirable, e.g., coding.
