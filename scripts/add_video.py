"""
Helper script for appending one video record to data/metadata.jsonl.
"""

import json
from pathlib import Path


METADATA_PATH = Path("data/metadata.jsonl")


record = {
    "schema_version": "v1",
    "video_id": "video_XX",
    "hotel_name": "",
    "hotel_chain": "",
    "city": "",
    "country": "",
    "identity_evidence": "",
    "source_url": "",
    "channel": "",
    "duration_seconds": 0,
    "interior_intervals": [],
    "video_style": "",
    "visible_objects": [],
    "discriminative_elements": [
        {
            "object": "",
            "description": "",
            "timestamp_range": [0, 0],
            "unoccluded": True,
        }
    ],
    "person_in_frame_seconds": 0,
    "caveats": "",
}


def load_existing_video_ids(path):
    video_ids = set()

    if not path.exists():
        return video_ids

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            existing_record = json.loads(line)
            video_ids.add(existing_record["video_id"])

    return video_ids


def validate_record(record):
    required_fields = [
        "schema_version",
        "video_id",
        "hotel_name",
        "hotel_chain",
        "city",
        "country",
        "identity_evidence",
        "source_url",
        "channel",
        "duration_seconds",
        "interior_intervals",
        "video_style",
        "visible_objects",
        "discriminative_elements",
        "person_in_frame_seconds",
        "caveats",
    ]

    missing_fields = [field for field in required_fields if field not in record]

    if missing_fields:
        raise ValueError(f"Missing required fields: {missing_fields}")

    if record["video_id"] == "video_XX":
        raise ValueError("Update video_id before running this script.")

    required_non_empty_strings = [
        "hotel_name",
        "hotel_chain",
        "city",
        "country",
        "identity_evidence",
        "source_url",
        "channel",
        "video_style",
    ]
    for field in required_non_empty_strings:
        if not record[field]:
            raise ValueError(f"{field} cannot be empty.")
    if not record["visible_objects"]:
        raise ValueError("visible_objects cannot be empty.")

    if not record["interior_intervals"]:
        raise ValueError("interior_intervals cannot be empty.")

    if not record["discriminative_elements"]:
        raise ValueError("discriminative_elements cannot be empty.")


def append_record(record, path):
    existing_video_ids = load_existing_video_ids(path)

    if record["video_id"] in existing_video_ids:
        raise ValueError(f"{record['video_id']} already exists in {path}")

    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Added {record['video_id']} to {path}")


if __name__ == "__main__":
    validate_record(record)
    append_record(record, METADATA_PATH)
