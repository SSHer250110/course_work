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
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to=operation["to"]
            ))
    return operation_instances


def get_executed_operations(operations: list[Operation]) -> list[Operation]:
    executed_operations = []
    for operation in operations:
        if operation.state == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def sort_operations_by_date(operations: list[Operation]) -> list[Operation]:
    return sorted(operations, key=lambda operation: operation.date, reverse=True)
