from datetime import datetime


class Operation:
    def __init__(
            self,
            pk: int,
            date: str,
            state: str,
            operation_amount: dict,
            description: str,
            from_: str,
            to: str
    ):
        self.pk = pk
        self.date = self.convert_date(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to

    def convert_date(self, date: str):
        format_data = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return format_data.strftime("%d.%m.%Y")
        # iso_date = datetime.fromisoformat(date)
        # return iso_date.strftime("%d.%m.%Y")
