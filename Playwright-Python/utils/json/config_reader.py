import json
import os

class ConfigReader:

    @staticmethod
    def get_config(env):
        file_path = os.path.join("test-data", env, "config.json")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Config file not found for env: {env}")

        with open(file_path, "r") as file:
            return json.load(file)
