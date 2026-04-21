import json

record = {
    # identity fields
    "schema_version": "v1",
    "video_id": "video_01",
    "hotel_name": "",
    "hotel_chain": "",
    "city": "",
    "country": "",
    "identity_confidence": "",
    "identity_evidence": "",

    # provenance fields
    "source_url": "",
    "channel": "",
    "duration_seconds": 0,
    "download_date": "",

    # temporal structure fields
    "interior_intervals": [],
    "distinct_rooms_shown": 0,

    # video style field
    "video_style": "",

    # object-centric content fields
    "visible_objects": [],
    "discriminative_elements": [],

    # realism & overall value fields
    "person_in_frame_seconds": 0,
    "retrieval_utility": "",

    # graph structure fields
    "same_chain_video_ids": [],

    # free-text fields
    "caveats": "",
}

with open("data/metadata.jsonl", "a") as f:
    f.write(json.dumps(record, ensure_ascii=False) + "\n")