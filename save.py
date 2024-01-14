import json
def save_data(filePath, data):
    with open(filePath, "w") as f:
        json.dump(data, f)