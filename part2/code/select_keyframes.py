'''
Read extracted_frames.jsonl.
Group records by video_id.
Print the frame counts.
Sort each video’s records by timestamp_seconds.
'''
import json
import shutil
from pathlib import Path

METHOD_NAME = "uniform_temporal_sampling"

KEYFRAMES_DIR = Path("part2/keyframes")
OUTPUT_PATH = Path("part2/results/selected_keyframes.jsonl")

video_ids = ["video_09", "video_11", "video_12", "video_21", "video_29"]
#read extracted_frames.jsonl
video_frames = {}

for video_id in video_ids:
    video_frames[video_id] = []

with open('part2/results/extracted_frames.jsonl', 'r') as f:
    #group records by video_id
    for line in f:
        record = json.loads(line)
        video_id = record['video_id']

        if video_id in video_ids:
            video_frames[video_id].append(record)
        #print the frame counts
for video_id in video_ids:
    print(f'Video {video_id}: {len(video_frames[video_id])} frames')

#sort each video's records by timestamp_seconds
for video_id in video_ids:
    video_frames[video_id].sort(key=lambda x: x['timestamp_seconds'])

    first_timestamp = video_frames[video_id][0]["timestamp_seconds"]
    last_timestamp = video_frames[video_id][-1]["timestamp_seconds"]

    # reset output folder so old keyframes do not mix with new ones
    if KEYFRAMES_DIR.exists():
        shutil.rmtree(KEYFRAMES_DIR)

    KEYFRAMES_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print(f"{video_id}: first={first_timestamp}, last={last_timestamp}")

def evenly_spaced_indices(num_frames, k):
    if num_frames < k:
        raise ValueError(f"Cannot select {k} frames from only {num_frames} frames.")

    if k == 1:
        return [0]

    indices = []
    for i in range(k):
        index = round(i * (num_frames - 1) / (k - 1))
        indices.append(index)

    return indices

K = 10

total_selected = 0

with OUTPUT_PATH.open("w", encoding="utf-8") as out:
    for video_id in video_ids:
        records = video_frames[video_id]
        indices = evenly_spaced_indices(len(records), K)

        video_output_dir = KEYFRAMES_DIR / video_id
        video_output_dir.mkdir(parents=True, exist_ok=True)

        selected_timestamps = []

        for keyframe_number, index in enumerate(indices, start=1):
            record = records[index]

            timestamp = record["timestamp_seconds"]
            source_frame_path = Path(record["frame_path"])

            if not source_frame_path.exists():
                raise FileNotFoundError(source_frame_path)

            selected_frame_path = (
                video_output_dir
                / f"keyframe_{keyframe_number:02d}_t{timestamp:06d}.jpg"
            )

            shutil.copy2(source_frame_path, selected_frame_path)

            selected_record = {
                "video_id": video_id,
                "timestamp_seconds": timestamp,
                "source_frame_path": str(source_frame_path),
                "selected_frame_path": str(selected_frame_path),
                "method": METHOD_NAME,
                "k": K,
                "source_frame_index": index,
                "keyframe_number": keyframe_number,
            }

            out.write(json.dumps(selected_record) + "\n")
            selected_timestamps.append(timestamp)
            total_selected += 1

        print(video_id, selected_timestamps)

print(f"Total selected keyframes: {total_selected}")
print(f"Wrote selected keyframe metadata to: {OUTPUT_PATH}")