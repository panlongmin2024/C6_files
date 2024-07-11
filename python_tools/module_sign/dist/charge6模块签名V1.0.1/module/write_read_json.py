import json
from typing import Any


class RWJson(object):

    @staticmethod
    def read_json(address):
        try:
            with open(address, encoding="utf-8") as f:
                data = json.load(f)
            return data
        except Exception as exc:
            print(str(exc))
            data: dict = {}
            return data

    @staticmethod
    def write_json(address: str, json_data: dict) -> None:
        with open(address, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, sort_keys=True, ensure_ascii=False)
            f.close()
