import json


def load_data(path: str) -> list[dict]:
    # Чтение данных из файла
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
