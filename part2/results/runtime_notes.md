# Runtime Notes

The keyframe selection step is fast because it reads timestamp metadata, sorts frames by timestamp, computes evenly spaced indices, and copies 50 selected images.

The evaluation step is also fast because it only reads JSONL metadata and compares selected timestamps against annotated timestamp ranges.

The slower part of the pipeline is frame extraction, because it uses FFmpeg to decode frames from video files.

Approximate timing can be measured with:

```bash
/usr/bin/time -p python part2/code/select_keyframes.py
/usr/bin/time -p python part2/code/evaluate.py
```

Scalability note: uniform temporal sampling should scale well after frame extraction because it does not require image feature extraction, clustering, or neural-network inference. The main bottleneck is video decoding and frame extraction.

## Measured runtime
- Keyframe selection: real 0.05 seconds
- Evaluation: real 0.02 seconds