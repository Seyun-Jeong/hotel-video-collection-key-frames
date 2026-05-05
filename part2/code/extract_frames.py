"""
Extract frames for the five videos used in Part 2.

This script:
1. Reads data/metadata.jsonl.
2. Keeps only the selected Part 2 video IDs.
3. Finds each downloaded video file in part2/videos/.
4. Extracts one frame per second from each video's interior_intervals.
5. Saves extracted frames under part2/frames/{video_id}/.
6. Writes frame metadata to part2/results/extracted_frames.jsonl.

FFmpeg is used for frame extraction.
"""

import json 
import subprocess
from pathlib import Path


TARGET_IDS = {"video_11", "video_09", "video_12", "video_21","video_29"}


results_path = Path("part2/results/extracted_frames.jsonl")
results_path.parent.mkdir(parents=True, exist_ok=True)

with results_path.open("w") as out:
    with open('data/metadata.jsonl', 'r') as f:
        for line in f:
            record = json.loads(line)
            if record['video_id'] not in TARGET_IDS:
                continue
                    
            input_video = next(Path("part2/videos").glob(f'{record["video_id"]}.*'), None)
            if input_video is None:
                raise FileNotFoundError(
                    f'No video file for {record["video_id"]} in part2/videos/'
                )
                    
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