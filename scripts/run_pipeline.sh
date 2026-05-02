#!/bin/bash
set -e

python part2/code/download.py
python part2/code/extract_frames.py
python part2/code/select_keyframes.py
python part2/code/evaluate.py
