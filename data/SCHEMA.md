# Dataset Schema

This file documents every field in `metadata.jsonl`. The file contains one
JSON object per line, one record per video.

## Identity fields

**`schema_version`** — string identifying which version of this schema the
record follows. Current value: `"v1"`. Bump when required fields change
shape, are added, or removed.

**`video_id`** — unique identifier, format `video_XX` where XX is zero-padded
(e.g. `video_01`, `video_3`). Assigned in the order videos are added.

**`hotel_name`** — full official hotel name as it appears on the hotel's
website or major booking platforms. Prefer the English version when a hotel
has multiple language names.

**`hotel_chain`** — parent chain name (e.g. `"IHG"`, `"Marriott International"`,
`"Hilton"`). Use `"Independent"` for unaffiliated hotels. Use the top-level
parent group, not the sub-brand — `"IHG"` not `"Holiday Inn Express"`.

**`city`** — city where the hotel is located. Common English name.

**`country`** — country where the hotel is located. Common English name.

**`identity_confidence`** — how confident I am that the hotel identity is
correct. One of:
- `high`: 
- `medium`: 
- `low`: 

**`identity_evidence`** — short free-text note describing the specific
evidence used to identify the hotel. When `identity_confidence` is `low`,
this field must be `"none — hotel unidentified"`.

## Provenance fields

**`source_url`** — direct URL to the source video.

**`channel`** — name of the YouTube channel that uploaded the video. Used to
prevent leakage when splitting the dataset into train/test — videos from the
same channel should not be split across sides.

**`duration_seconds`** — total video length in seconds (integer), as reported
by YouTube or yt-dlp. This is the full video length, not the usable interior
portion.

**`download_date`** — ISO 8601 date (`YYYY-MM-DD`) when the video was
confirmed accessible and added to the dataset.

## Temporal structure

**`interior_intervals`** — list of `[start_second, end_second]` pairs (integer
seconds, inclusive on both ends) marking which portions of the video show
the hotel room interior. Example: `[[8, 92], [110, 184]]` means interior is
shown from 0:08–1:32 and 1:50–3:04.

**`distinct_rooms_shown`** — integer count of how many different rooms
within the same hotel are shown in the video. Minimum value: 1.

## Video style

**`video_style`** — categorizes the video along the same axis the Hotels-50K
dataset uses to separate its two image sources. One of:
- `hotel_promo`: 
- `travel_blogger`: 
- `guest_vlog`: 
- `room_review`: 

## Object-centric content

**`visible_objects`** — list of objects from the fixed vocabulary below that
appear somewhere in the video. Free-text drift is not allowed — every entry
must match the vocabulary exactly.

**Fixed vocabulary:**
`bed`, `headboard`, `lamp`, `desk`, `chair`, `couch`, `art`, `sink`,
`toilet`, `tv`, `curtain`, `carpet`, `mirror`, `window`, `nightstand`,
`dresser`, `other`.

When `other` is used, explain what the object was in `caveats`.

**`discriminative_elements`** — list of objects in the video that are
visually distinctive enough to serve as identifying features for this
specific hotel or chain. One entry per distinctive view — the same object
shot from a different angle or distance gets its own entry.

Each entry is a dict with four keys:
- `object`: string, must be from the fixed vocabulary above
- `description`: short free-text describing what makes this instance
  distinctive (e.g. `"brushed-nickel gooseneck lamp, head-on"`)
- `timestamp_range`: `[start_second, end_second]` integer seconds, inclusive,
  marking the window where the object is clearly visible
- `unoccluded`: boolean, `true` if the object is fully visible in this window,
  `false` if partially blocked

## Realism and retrieval value

**`person_in_frame_seconds`** — total seconds (integer) where a person
(narrator, family member, other guest) appears in frame and occludes part
of the room. `0` is a valid value meaning no people appear.

**`retrieval_utility`** — overall judgment of how useful this video is as a
source of training or retrieval data. One of:
- `high`: 
- `medium`: 
- `low`: 

## Graph structure

**`same_chain_video_ids`** — list of other `video_id` strings in this dataset
from the same `hotel_chain`. Excludes the record's own `video_id`.
Auto-generated from `hotel_chain` rather than labeled by hand.

## Free-text notes

**`caveats`** — optional free-text field for one-off observations that don't
fit any other field. Examples: `"narrator reads room number aloud at 0:52"`,
`"near-duplicate bed pans at 0:30 and 1:40"`. Leave empty (`""`) if there
is nothing to note.

## Changes

- 2026-04-20: initial schema.