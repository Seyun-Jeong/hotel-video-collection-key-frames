# Dataset Schema

This file documents every field in `metadata.jsonl`. The file contains one
JSON object per line, one record per video.

## Identity fields
**`schema_version`**

**`video_id`** — 

**`hotel_name`** — 

**`hotel_chain`** — 

**`city`** — 

**`country`** — 

**`identity_confidence`** — one of:
- `high`: 
- `medium`: 
- `low`: 

**`identity_evidence`** — 

## Provenance fields

**`source_url`** — 

**`channel`** — 

**`duration_seconds`** — 

**`download_date`** — 

## Temporal structure

**`interior_intervals`** — 

**`distinct_rooms_shown`** — 

## Video style

**`video_style`** — one of:
- `hotel_promo`: 
- `travel_blogger`: 
- `guest_vlog`: 
- `room_review`: 

## Object-centric content

**`visible_objects`** — 

**`discriminative_elements`** — list of dicts with keys:
- `object`: 
- `description`: 
- `timestamp_range`: 
- `unoccluded`: 

## Realism and retrieval value

**`person_in_frame_seconds`** — 

**`retrieval_utility`** — one of:
- `high`: 
- `medium`: 
- `low`: 

## Graph structure

**`same_chain_video_ids`** — 

## Free-text notes

**`caveats`** — 

## Changes

- 2026-04-20: initial schema.