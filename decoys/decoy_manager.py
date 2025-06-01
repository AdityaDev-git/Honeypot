import os
import random

DECOY_FILES = [
    "passwords.txt",
    "admin_creds.xlsx",
    "backup.zip",
    "db_dump.sql",
    "private_keys.pem"
]

def create_decoy_files(folder="decoys"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for filename in DECOY_FILES:
        filepath = os.path.join(folder, filename)
        with open(filepath, "w") as f:
            f.write(generate_fake_content(filename))
    print(f"[+] Created {len(DECOY_FILES)} decoy files in {folder}")

def generate_fake_content(filename):
    fake_data = {
        "passwords.txt": "admin:admin123\nuser:userpass\n",
        "admin_creds.xlsx": "Fake Excel binary content (placeholder)",
        "backup.zip": "Fake zip archive content (placeholder)",
        "db_dump.sql": "CREATE TABLE users (id INT, username TEXT, password TEXT);\n",
        "private_keys.pem": "-----BEGIN PRIVATE KEY-----\nFAKEKEYDATA\n-----END PRIVATE KEY-----"
    }
    return fake_data.get(filename, "Placeholder file content.")
