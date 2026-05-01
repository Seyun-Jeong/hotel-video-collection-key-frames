## Quantitative results

For each of the five videos, I selected 10 keyframes from the extracted interior frames.

- video_09: 137 extracted frames -> 10 selected frames. Covered 4 of 5 discriminative elements.
- video_11: 170 extracted frames -> 10 selected frames. Covered 2 of 5 discriminative elements.
- video_12: 126 extracted frames -> 10 selected frames. Covered 2 of 5 discriminative elements.
- video_21: 139 extracted frames -> 10 selected frames. Covered 0 of 5 discriminative elements.
- video_29: 146 extracted frames -> 10 selected frames. Covered 2 of 5 discriminative elements.

Overall, the method reduced 718 extracted frames to 50 selected keyframes. This keeps about 7% of the frames and removes about 93%. Across all videos, 10 of 25 annotated discriminative elements were covered.

This result shows that uniform temporal sampling is useful as a simple baseline. It reduced the number of frames a lot, from 718 extracted frames to 50 keyframes. However, it only covered 10 of the 25 discriminative elements. This means the method is efficient, but it can miss important room details because it selects frames by time instead of by visual content.

The clearest failure case is video_21. It had 139 extracted frames and 10 selected keyframes, but none of the selected timestamps overlapped with the annotated discriminative element ranges.