'''
Evaluate keyframe selection counts, compression, and discriminative element coverage.
'''

import json
from collections import Counter

video_ids = ["video_09", "video_11", "video_12", "video_21", "video_29"]

extracted_frames_count = Counter()
selected_frames_count = Counter()

with open('part2/results/extracted_frames.jsonl', 'r') as f:
    for line in f:
        record = json.loads(line)
        extracted_frames_count[record['video_id']] += 1
with open('part2/results/selected_keyframes.jsonl', 'r') as f:
    for line in f:
        record = json.loads(line)
        selected_frames_count[record['video_id']] += 1

for video_id in video_ids:
    print(
        f'{video_id}: extracted {extracted_frames_count[video_id]}, selected {selected_frames_count[video_id]}'
    )

#compression_ratio = selected_keyframes / extracted_frames
compression_ratio = {}
for video_id in video_ids:
    compression_ratio[video_id] = selected_frames_count[video_id] / extracted_frames_count[video_id]
for video_id in video_ids:
    print(f'{video_id}: compression ratio {compression_ratio[video_id]}')

#reduction_percent = 100 * (1 - selected/extracted)
reduction_percent = {}
for video_id in video_ids:
    reduction_percent[video_id] = 100 * (1 - selected_frames_count[video_id] / extracted_frames_count[video_id])
for video_id in video_ids:
    print(f'{video_id}: reduction percent {reduction_percent[video_id]}')


'''
Evaluate whether selected keyframe timestamps overlap annotated
discriminative element timestamp ranges.
'''
coverage_results = {}

selected_timestamps = {}

for video_id in video_ids:
    selected_timestamps[video_id] = []

with open('part2/results/selected_keyframes.jsonl', 'r') as f:
    for line in f:
        record = json.loads(line)
        video_id = record['video_id']

        if video_id in video_ids:
            selected_timestamps[video_id].append(record['timestamp_seconds'])

for video_id in video_ids:
    selected_timestamps[video_id].sort()

metadata_by_video = {}

with open('data/metadata.jsonl', 'r') as f:
    for line in f:
        record = json.loads(line)
        video_id = record['video_id']

        if video_id in video_ids:
            metadata_by_video[video_id] = record

def element_is_covered(element, timestamps):
    start, end = element['timestamp_range']

    for timestamp in timestamps:
        if start <= timestamp <= end:
            return True

    return False

for video_id in video_ids:
    timestamps = selected_timestamps[video_id]
    elements = metadata_by_video[video_id]['discriminative_elements']

    covered_elements = 0

    for element in elements:
        if element_is_covered(element, timestamps):
            covered_elements += 1

    total_elements = len(elements)
    if total_elements == 0:
        coverage_percent = 0
    else:
        coverage_percent = round((covered_elements / total_elements) * 100, 2)

    coverage_results[video_id] = {
        'discriminative_elements_total': total_elements,
        'discriminative_elements_covered': covered_elements,
        'coverage_percent': coverage_percent,
    }

    print(f'{video_id}: covered {covered_elements}/{total_elements}, coverage={coverage_percent}%')

metrics = {
    "method": "uniform_temporal_sampling",
    "k": 10,
    "coverage_metric_note": (
        "Coverage is a proxy metric. It measures whether selected keyframe "
        "timestamps overlap manually annotated discriminative_elements. "
        "It does not prove real hotel retrieval performance."
    ),
    "extracted_frames_count": dict(extracted_frames_count),
    "selected_frames_count": dict(selected_frames_count),
    "compression_ratio": {
        video_id: round(compression_ratio[video_id], 4)
        for video_id in video_ids
    },
    "reduction_percent": {
        video_id: round(reduction_percent[video_id], 2)
        for video_id in video_ids
    },
    "discriminative_elements_coverage": coverage_results,
}


#save metrics to part2/results/metrics.json.
with open('part2/results/metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)