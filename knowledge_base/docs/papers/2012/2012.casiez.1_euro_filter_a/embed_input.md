<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

1 Euro Filter: A Simple Speed-Based Low-Pass Filter for Noisy Input in Interactive Systems

Topics include Signal filtering, Low-pass filtering, Adaptive filters, Interactive systems, Input devices, Jitter reduction, Latency reduction, Human-computer interaction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a practical adaptive first-order low-pass filter for noisy real-time input signals, especially human-motion and pointing data. The key idea is to raise the cutoff frequency with estimated signal speed, trading more smoothing at rest for less lag during fast motion, which makes the method compact, cheap to run, and easier to tune than model-heavy alternatives.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The 1 Euro filter ("one Euro filter") is a simple algorithm to filter noisy signals for high precision and responsiveness. It uses a first order low-pass filter with an adaptive cutoff frequency: at low speeds, a low cutoff stabilizes the signal by reducing jitter, but as speed increases, the cutoff is increased to reduce lag. The algorithm is easy to implement, uses very few resources, and with two easily understood parameters, it is easy to tune. In a comparison with other filters, the 1 Euro filter has less lag using a reference amount of jitter reduction.
