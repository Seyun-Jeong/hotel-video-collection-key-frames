# Runtime Notes

The keyframe selection step is fast because it reads timestamp metadata, sorts frames by timestamp, computes evenly spaced indices, and copies 50 selected images.

The evaluation step is also fast because it only reads JSONL metadata and compares selected timestamps against annotated timestamp ranges.

The slowest measured local step was frame extraction, because it uses FFmpeg to decode frames from video files.

Approximate timing can be measured with:

```bash
/usr/bin/time -p python part2/code/download.py
/usr/bin/time -p python part2/code/extract_frames.py
/usr/bin/time -p python part2/code/select_keyframes.py
/usr/bin/time -p python part2/code/evaluate.py
```

Scalability note: uniform temporal sampling should scale well after frame extraction because it does not require image feature extraction, clustering, or neural-network inference. The main bottleneck is video decoding and frame extraction.

## Measured runtime
- Download step: real 6.27 seconds, but this was with videos already downloaded locally.
- Frame extraction: real 46.67 seconds.
- Keyframe selection: real 0.05 seconds.
- Evaluation: real 0.02 seconds.