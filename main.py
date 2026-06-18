import hashlib, os
import time
import logging

from flask import json

def get_file_hash(path):
    sha256 = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    print("Initial hash calculated.")
    return sha256.hexdigest()

def build_baseline(paths):
    baseline = {}
    for path in paths:
        for root,_,files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    baseline[file_path] = get_file_hash(file_path)
                except PermissionError:
                    continue
    with open('baseline.json', "w") as f:
        json.dump(baseline, f, indent=4)
    print("Baseline built and saved to baseline.json.")




if __name__ == "__main__":
    build_baseline(paths=[r"C:\Users\wishi\Documents\File Checker"])