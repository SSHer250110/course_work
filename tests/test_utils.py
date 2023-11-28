from datetime import datetime, time

from src.operation import Operation
from src.utils import get_instances_class, get_executed_operations, sort_operations_by_date


def test_get_instances_class(operation_dict):
    operations = get_instances_class(operation_dict)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert len(operations) == 2
    assert operations[1].pk == 407169720
    assert operations[1].operation_amount["amount"] == "67011.26"


def test_get_executed_operations(operation_instance):
    executed_operation = get_executed_operations(operation_instance)
    assert len(executed_operation) == 1
    assert isinstance(executed_operation, list)
    assert isinstance(executed_operation[0], Operation)
    assert executed_operation[0].to == "Счет **8358"
    assert executed_operation[0].state == "EXECUTED"


def test_sort_operations_by_date(operation_instance):
    sort_date = sort_operations_by_date(operation_instance)
    assert len(sort_date) == 2
    assert isinstance(sort_date, list)
    assert isinstance(sort_date[0], Operation)
    assert datetime.strptime(sort_date[0].date, "%d.%m.%Y") > datetime.strptime(sort_date[1].date, "%d.%m.%Y")
