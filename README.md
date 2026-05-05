# Hotel Room Interior Video Collection and Keyframe Selection

A dataset of 50 hotel room interior videos, with structured metadata for each. A uniform temporal sampling pipeline that selects 10 keyframes from each of 5 videos.

## What this is

TraffickCam helps investigators identify hotel locations from images as evidence in trafficking cases. This repository aims to extend TraffickCam from images to video. This assignment covers video dataset and keyframe selection.

## Repository structure

```
.
├── data/
│   ├── metadata.jsonl       # 50 video records
│   └── SCHEMA.md            # field definitions for metadata.jsonl
├── part2/
│   ├── code/                # pipeline scripts (download, extract, select, evaluate)
│   ├── videos/              # 5 downloaded source videos (gitignored)
│   ├── frames/              # extracted frames at 1 fps (gitignored)
│   ├── keyframes/           # 50 selected keyframes (5 videos × 10)
│   └── results/             # metrics.json and analysis summaries
├── report/                  # final report
├── scripts/
│   ├── add_video.py         # helper for appending metadata records
│   └── run_pipeline.sh      # runs the full Part 2 pipeline
├── .gitignore
├── README.md                # this file
└── requirements.txt         # python dependencies (yt-dlp)
```

## Setup

Requires Python 3.9+ and FFmpeg installed on the system.

Install FFmpeg:

```bash
# macOS
brew install ffmpeg

# Ubuntu or Debian
sudo apt install ffmpeg

# Windows
winget install ffmpeg
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## How to reproduce Part 2

Run the full pipeline from the repo root:

```bash
bash scripts/run_pipeline.sh
```

The pipeline runs four stages in order:

1. `download.py`: downloads 5 source videos via yt-dlp.
2. `extract_frames.py`: extracts frames at 1 fps from interior intervals.
3. `select_keyframes.py`: selects 10 keyframes per video by uniform temporal sampling.
4. `evaluate.py`: computes compression ratio and discriminative-element coverage.

Frame extraction is the slow step (takes a few minutes). The other three stages finish in under a second each.

Outputs:

- `part2/keyframes/`: 50 selected keyframes (5 videos x 10).
- `part2/results/metrics.json`: quantitative metrics.
- `part2/results/*.md`: analysis summaries.

## Results and analysis

- `part2/results/metrics.json`: quantitative metrics.
- `part2/results/evaluation_summary.md`: discussion of results and failure case.
- `report/`: final report with full analysis.


## Limitations

**Dataset:**
- I searched videos across multiple channels and filtered by recent uploads to avoid the most popular and recommended videos, diversifying both video styles and filming skills. Still, the resulting style distribution is heavily skewed toward room reviews(22), guest vlogs(17), and travel vlogs(10), with only one hotel promo.

- Initially I tried to annotate each video manually but found the labels became shallow yes/no judgments and were time-consuming. I switched to drafting metadata with Google Gemini's YouTube video analysis, then manually validating each draft. This produced richer schema fields than fully manual work, but the final labels still reflect a single reviewer's judgment, and visual inspection during Part 2 surfaced minor timestamp errors in some discriminative_elements ranges (e.g., video_12, video_29).

**Method and metric:**
- uniform temporal sampling has no content awareness - it picks evenly spaced frames by time, not by what is visible. 
- The range metric achieved 10 out of 25 elements covered. Visual check found 17 out of 25, which is a 28 percentage-point gap. The metric calculates timestamp overlap, not whether the feature is visible in the keyframe; thus, it understates real coverage.