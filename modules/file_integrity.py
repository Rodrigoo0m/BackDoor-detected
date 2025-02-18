import hashlib
import os

def check_integrity(file_path):
    """Check if the file's hash matches a known hash."""
    known_hashes = {
        "/etc/passwd": "known_hash_value",
        "/etc/shadow": "known_hash_value",
    }

    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
            if file_hash != known_hashes.get(file_path):
                return f"Suspicious file modification detected: {file_path}"
    return None
