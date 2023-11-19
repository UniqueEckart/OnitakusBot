import os

def debugLog(text):
    if os.environ.get("DEBUG"):
        print(f"[DEBUG] {text}")