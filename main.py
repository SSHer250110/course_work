from settings import OPERATIONS_PATH
from src.utils import load_data, get_instances_class, get_executed_operations, sort_operations_by_date


def main():
    operations = load_data(OPERATIONS_PATH)
    instances = get_instances_class(operations)
    executed_operations = get_executed_operations(instances)
    sorted_operations = sort_operations_by_date(executed_operations)
    print(1)


if __name__ == '__main__':
    main()
