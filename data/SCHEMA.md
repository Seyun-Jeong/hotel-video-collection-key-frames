# Dataset Schema

This file documents every field in `metadata.jsonl`. The file contains one
JSON object per line, one record per video.

## Identity fields

**`schema_version`** — string identifying which version of this schema the
record follows. Current value: `"v1"`. Bump when required fields change
shape, are added, or removed.

**`video_id`** — unique identifier, format `video_XX` where XX is
zero-padded (e.g. `video_01`). Assigned in the order videos are added.

**`hotel_name`** — full official hotel name as it appears on the hotel's
website or major booking platforms. Prefer the English version when the
hotel has multiple language names.

**`hotel_chain`** — the specific sub-brand, not the parent group. Use
`"Holiday Inn Express"` not `"IHG"`, `"Conrad"` not `"Hilton"`, `"Moxy"`
not `"Marriott"`. Use `"Independent"` for unaffiliated hotels and for
soft brands (Ascend Collection, Curio, etc.) where each property has its
own visual identity.

**`city`** — city where the hotel is located. Common English name.

**`country`** — country where the hotel is located. Common English name.

**`identity_evidence`** — short free-text note describing the specific
evidence used to confirm the hotel identity. Examples: on-screen text
overlay, branded signage, narrator naming the property, YouTube Featured
Places tag, window view matching the known property, room key.
Title-only evidence is not sufficient; include at least one independent
signal.

## Provenance fields

**`source_url`** — direct URL to the source video.

**`channel`** — name of the YouTube channel that uploaded the video. Used
to prevent leakage when splitting the dataset into train/test — videos
from the same channel should not be split across sides.

**`duration_seconds`** — total video length in seconds (integer), as
reported by YouTube or yt-dlp. This is the full video length, not the
usable interior portion.

## Temporal structure

**`interior_intervals`** — list of `[start_second, end_second]` pairs
(integer seconds, inclusive on both ends) marking which portions of the
video show the guest-room interior. Example: `[[8, 92], [110, 184]]`
means interior is shown from 0:08–1:32 and 1:50–3:04. Lobbies,
corridors, and public spaces do not count.

## Video style

**`video_style`** — categorizes the video by how it was produced. One of:
- `hotel_promo`: produced by or on behalf of the property. Professional
  lighting, staged rooms, polished edit.
- `travel_blogger`: produced by a travel-content creator as an
  independent review. Handheld or gimbal camera, evaluative narration.
- `guest_vlog`: produced by a traveler documenting a personal trip. Room
  is lived-in, narration is casual, the hotel is one element of a
  broader vlog.
- `room_review`: produced by a creator who systematically tours hotel
  rooms as their primary content. Structured walkthrough with feature
  callouts.

## Object-centric content

**`visible_objects`** — list of objects from the fixed vocabulary below
that appear somewhere in the guest-room interior. Free-text drift is not
allowed — every entry must match the vocabulary exactly. All-lowercase,
singular. Brand names never appear here — put those in
`discriminative_elements` or `caveats`.

**Fixed vocabulary:**
`bed`, `headboard`, `lamp`, `desk`, `chair`, `couch`, `art`, `sink`,
`toilet`, `tv`, `curtain`, `carpet`, `mirror`, `window`, `nightstand`,
`dresser`, `other`.

When `other` is used, explain what the object was in `caveats`.

**`discriminative_elements`** — list of objects in the video that are
visually distinctive enough to serve as identifying features for this
specific hotel or chain. One entry per distinctive view — the same
object shot from a different angle or distance gets its own entry.

Each entry is a dict with four keys:
- `object`: string, must be from the fixed vocabulary above, or a short
  descriptive noun for unique items that don't fit (e.g.
  `"gachapon_machine"`, `"painting_headboard"`).
- `description`: short free-text describing what makes this instance
  distinctive. May include brand names, patterns, materials.
- `timestamp_range`: `[start_second, end_second]` integer seconds,
  inclusive, marking the window where the object is clearly visible.
- `unoccluded`: boolean, `true` if the object is fully visible in this
  window, `false` if partially blocked.

## Realism

**`person_in_frame_seconds`** — total seconds (integer) where a person
(narrator, family member, other guest) appears in frame and occludes
part of the room. `0` is a valid value meaning no people appear.

## Free-text notes

**`caveats`** — optional free-text field for one-off observations that
don't fit any other field. Examples: `"narrator reads room number aloud
at 0:52"`, `"night footage from 3:20–4:10 is low-light"`, `"multi-room
compilation, this record covers only the first room"`. Leave empty
(`""`) if there is nothing to note.

## Changes

- 2026-04-20: initial schema.
- 2026-04-21: added the details.
- 2026-04-23: trimmed unused fields; clarified `hotel_chain` as
  sub-brand; filled in `video_style` rubrics.