# Frame Extraction Summary

I manually reviewed and corrected the `interior_intervals` for the five selected Part 2 videos before rerunning frame extraction.

The intervals were corrected to include only visible hotel-room interior footage. Bathroom and shower areas were included as room interior. Outside-only window views, balcony/outside shots, static/animation-only segments, and end-screen/static construction images were excluded.

The extraction script uses `range(start, end)`, so interval end values are excluded.

## Corrected intervals and extracted frames

video_09: [[169, 209], [217, 314]] = 137 frames  
video_11: [[10, 119], [124, 158], [163, 190]] = 170 frames  
video_12: [[90, 111], [129, 234]] = 126 frames  
video_21: [[25, 118], [137, 183]] = 139 frames  
video_29: [[1, 119], [222, 250]] = 146 frames  

Total extracted frames: 718  
Total mapping records: 718  

Result: frame files and `extracted_frames.jsonl` records match.