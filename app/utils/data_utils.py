import hashlib
import json

def mask_pii(data):
    if "user_id" not in data.keys() or "device_type" not in data.keys() or "ip" not in data.keys():
        print("Data is Invalid")
        return
    for key in data.keys():
        if "id" in key or "ip" in key:
            data[key] = hashlib.md5(data[key].encode()).hexdigest()
    return data

def convert_to_json(data):
    return mask_pii(json.loads(data["Body"]))