import json
import os

class JsonReader:

    @staticmethod
    def read_all(env):
        base_path = os.path.join("test-data", env)

        if not os.path.isdir(base_path):
            raise FileNotFoundError(f"Environment folder not found: {base_path}")

        data = {}

        for file in os.listdir(base_path):
            if file.endswith(".json"):
                file_path = os.path.join(base_path, file)

                with open(file_path, "r") as f:
                    # key = filename without .json
                    data[file.replace(".json", "")] = json.load(f)
        return data
    
    @staticmethod
    def read_json(path, key): 
        with open(path) as f: 
            data = json.load(f) 
        return data[key] 
