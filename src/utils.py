import json

from src.operation import Operation


def load_data(path: str) -> list[dict]:
    # Чтение данных из файла
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_instances_class(operations: list[dict]) -> list[Operation]:
    operation_instances = []
    for operation in operations:
        if operation:
            operation_instances.append(Operation(
                pk=operation["id"],
                state=operation["state"],
                date=operation["date"],
                operation_amount=operation["operation_amount"],
                description=operation["description"],
                from_=operation["from"],
                to=operation["to"]
            ))
    return operation_instances
