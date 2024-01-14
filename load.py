import json
def load_items(filePath):
    try:
        with open(filePath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}