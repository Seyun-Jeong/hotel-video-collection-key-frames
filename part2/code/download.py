# download.py — fetches the 5 selected videos for Part 2 keyframe extraction.
# References:
#   yt-dlp project: https://github.com/yt-dlp/yt-dlp
#   Embedding yt-dlp in Python: https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp

import yt_dlp
import json

target_ids = {"video_09","video_11","video_12","video_21","video_29"}

with open("data/metadata.jsonl") as f:
    records = [json.loads(line) for line in f]

target_videos = [(r["video_id"], r["source_url"]) for r in records if r["video_id"] in target_ids]

# Track successes and failures
succeeded = []
failed = []
for video_id, url in target_videos:
    ydl_opts = {
        'format': 'best[height<=720]',
        'outtmpl': f'part2/videos/{video_id}.%(ext)s',
    }
    print(f"Downloading {video_id}...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        succeeded.append(video_id)
    except Exception as e:
        print(f"  Failed: {e}")
        failed.append(video_id)

print(f"\nDone. {len(succeeded)} succeeded, {len(failed)} failed.")
if failed:
    print(f"Failed videos: {failed}")