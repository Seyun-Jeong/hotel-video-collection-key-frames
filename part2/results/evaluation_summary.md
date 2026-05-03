## Quantitative results (timestamp-overlap coverage)

For each of the five videos, I selected 10 keyframes from the extracted interior frames.

- video_09: 137 extracted frames -> 10 selected frames. Covered 4 of 5 discriminative elements.
- video_11: 170 extracted frames -> 10 selected frames. Covered 2 of 5 discriminative elements.
- video_12: 126 extracted frames -> 10 selected frames. Covered 2 of 5 discriminative elements.
- video_21: 139 extracted frames -> 10 selected frames. Covered 0 of 5 discriminative elements.
- video_29: 146 extracted frames -> 10 selected frames. Covered 2 of 5 discriminative elements.

Overall, the method reduced 718 extracted frames to 50 selected keyframes. This keeps about 7% of the frames and removes about 93%. Across all videos, 10 of 25 annotated discriminative elements were covered.

This result shows that uniform temporal sampling is useful as a simple baseline. It reduced the number of frames a lot, from 718 extracted frames to 50 keyframes. However, it only covered 10 of the 25 discriminative elements. This means the method is efficient, but it can miss important room details because it selects frames by time instead of by visual content.


## Visual inspection

I visually inspected all 50 keyframes against the annotated discriminative elements. Across all five videos, 17 of 25 elements were visible in at least one keyframe, compared to 10 of 25 by the timestamp-overlap metric. The per-video numbers and observations are below.



video_09: metric 4/5., visual 5/5 notes: chair[194-200}Chair wasn’t the main focus also bed also was visible, "mirror"[286, 305]partially visible also other mirror standing mirror also visible
"other"[200, 204]Was shown in keyframe_03_t000199.jpg

video_11: metric 2/5, visual 4/5 notes: sink[66-77]barely visible because of bathroom door was opening image."toilet"[73, 77]:keyframe_05_t000085.jpg also is shown this toilet."tv"[139, 144]partially visible along with chairs(chairs more focused on the image) tv is upright side barely visible.

video_12: metric 2/5, visual 2/5, notes: Although numbers are matching but one of actual dicriminative elements is not matching "other"[160, 165] there is time flame for 164 but black rag and black trash bin wasn’t shown so the timeframe should have been 160-162.  "headboard"[96, 100]so barely visible of headboard on keyframe_04_t000150.jpg."couch"[105, 110] keyframe_02_t000104.jpg shows the couch on the left side but it wasn’t focused of couch more of chairs and desk."other"[191, 195] this wasn’t shown correctly.

video_21: metric 0/5, visual 1/5, notes: "sink"[26, 28]keyframe_01_t00025.jpg is shown the sink however can’t see American Standard logo due to partially visible of sink on the bottom of image."sink"[26, 28]  keyframe_10_t000182.jpg shows the sink explicitly in the bathroom so sink is outside of bathroom at the kitchen and also inside of bathroom.

video_29: metric 2/5, visual 5/5, notes:"tv"[101, 106] TV is visible on keyframe_10_t000249."window"[118, 130]this is also shown at keyframe_08_t000114.jpg."other"[25, 30]keyframe_03_t000033.jpg,shaky image barely visible of the washing machine(time frame should be changed to 31-33). "bed"[93, 98]although keyframe_07_t000098.jpg is shown but bed is largely not visible only its edge is shown,also bed is partially visible on keframe_09_t000233.jpg."other"[78, 85]so keyframe_06_t000082.jpg is there however that is more showing inside of refrigerator so it’s not part of interior(what do you think?).


## What this means 

The metric is useful as a proxy yet understates actual coverage by about 28%.
Some annotation timestamp ranges were imprecise, which compounds the strictness of the metric. 
Future work could either: tighten sampling near annotated ranges, use content-aware selection (e.g., embedding-based), or score by visual similarity rather than timestamp overlap. The fact that visual inspection contradicted the metric is a methodological lesson on its own, proxy metrics need to be validated against what they actually claim to measure.
