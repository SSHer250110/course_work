from settings import OPERATIONS_PATH
from src.utils import load_data, get_instances_class, get_executed_operations


def main():
    operations = load_data(OPERATIONS_PATH)
    instances = get_instances_class(operations)
    executed_operations = get_executed_operations(instances)

if __name__ == '__main__':
    main()
