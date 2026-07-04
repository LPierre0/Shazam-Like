# Data 
Data came from the FMA (Free Music Access) database, here i will use only the fma_small dataset. 


# Download

```bash
python src/scripts/download_fma.py

unzip -d data/raw/ data/raw/fma_small.zip
```

# Roadmap


 1. [ ] Signal pipeline — Audio loading (mono, 11 kHz resampling), STFT spectrogram from scratch (numpy)
 2. [ ] Peak detection — Extract the spectral peak "constellation" (local maxima, adaptive threshold, target peak density), constellation overlay visualization validated on synthetic chirp
 3. [ ] Fingerprint hashing — 32-bit hash encoding/decoding (f1 | f2 | Δt bit-packing) with round-trip tests, combinatorial pair generation (anchor + target zone, fan-out tuning)
 4. [ ] Indexing — index CLI command: fingerprint a folder of tracks (FMA dataset) into the SQLite inverted index; report track count, hash count, and indexing time
 5. [ ] Recognition — recognize CLI command: match a query clip via time-coherence voting (offset delta histogram), confidence score, "unknown track" threshold
 6. [ ] Evaluation & benchmarks — Systematic degradation test bench (noise levels, clip duration, mic re-recording), recognition rate curves, false positive rate on out-of-database clips, lookup latency vs database size, hyperparameter tuning (FFT size, peak density, fan-out, hash entropy trade-off)
 7. [ ] Live demo — Real-time microphone capture (listen command) and a small interactive web app to demo recognition (Web app created by claude code)