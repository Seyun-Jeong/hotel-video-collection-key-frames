"""
1. Read data/metadata.jsonl
2. Keep only selected video IDs
3. For now, test only video_11
4. Read video_11's interior_intervals
5. Create part2/frames/video_11/
6. For each second inside the interval:
      call FFmpeg
      save frame_tXXXXXX.jpg
      record timestamp + frame path
7. Save a mapping file:
      part2/results/extracted_frames.jsonl

pesudo code:
TARGET_IDS = {"video_11"}   # test only one video first

load records from data/metadata.jsonl

for each record:
    if video_id is not in TARGET_IDS:
        skip

    input_video = part2/videos/{video_id}.mp4
    output_folder = part2/frames/{video_id}/

    for each [start, end] in interior_intervals:
        for timestamp in range(start, end):
            output_path = part2/frames/{video_id}/frame_t{timestamp}.jpg

            run:
            ffmpeg -y -ss timestamp -i input_video -frames:v 1 output_path

            write mapping line to extracted_frames.jsonl
"""

import json 
import subprocess
from pathlib import Path


TARGET_IDS = {"video_11", "video_09", "video_12", "video_21","video_29"}   # test only one video first


results_path = Path("part2/results/extracted_frames.jsonl")
results_path.parent.mkdir(parents=True, exist_ok=True)

with results_path.open("w") as out:
    with open('data/metadata.jsonl', 'r') as f:
        for line in f:
            record = json.loads(line)
            if record['video_id'] not in TARGET_IDS:
                continue
                    
            input_video = Path("part2/videos") / f'{record["video_id"]}.mp4'
            if not input_video.exists():
                raise FileNotFoundError(input_video)
                    
            output_folder = Path("part2/frames") / record["video_id"]
            output_folder.mkdir(parents=True, exist_ok=True)

            for start, end in record["interior_intervals"]:
                for timestamp in range(start, end):
                    output_path = output_folder / f"frame_t{timestamp:06d}.jpg"
                    subprocess.run([
                        "ffmpeg",
                        "-hide_banner",
                        "-loglevel", "error",
                        "-y",
                        "-ss", str(timestamp),
                        "-i", str(input_video),
                        "-frames:v", "1",
                        "-update", "1",
                        str(output_path),
                    ], check=True)

                    mapping = {
                        "video_id": record["video_id"],
                        "timestamp_seconds": timestamp,
                        "frame_path": str(output_path),
                    }
                            

                    out.write(json.dumps(mapping) + "\n")