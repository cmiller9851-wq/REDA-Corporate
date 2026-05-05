import hashlib
import json

def get_canonical_hash(data):
    """Enforces Miller Standard: UTF-8, sorted keys, no whitespace."""
    canonical_bytes = json.dumps(
        data, 
        sort_keys=True, 
        separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(canonical_bytes).hexdigest()

def verify_signature(payload, signature):
    return get_canonical_hash(payload) == signature
