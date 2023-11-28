from datetime import datetime


class Operation:
    """
    Класс одной операции
    """
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
        self.from_ = self.convert_info_payment(from_)
        self.to = self.convert_info_payment(to)

    def convert_date(self, date: str) -> datetime.date:
        """
        Метод преобразования даты в нужный вид
        """
        iso_date = datetime.fromisoformat(date)
        return datetime.strftime(iso_date, "%d.%m.%Y")

    def convert_info_payment(self, info_payment: str) -> str:
        """
        Метод вывода информации о платеже в нужном виде
        """
        if info_payment:
            info_list = info_payment.split()
            if info_payment.startswith("Счет"):
                num_payment = info_list.pop()
                num_payment = f"**{num_payment[-4:]}"
                info_list.append(num_payment)
            else:
                num_payment = info_list.pop()
                num_payment = f"{num_payment[:4]} {num_payment[5:7]}** **** {num_payment[-4:]}"
                info_list.append(num_payment)
            return " ".join(info_list)
        return "Данные отправителя отсутствуют"

    def __str__(self):
        """
        Метод вывода информации о платежах:
        <дата перевода> <описание перевода>
        <откуда> -> <куда>
        <сумма перевода> <валюта>
        """
        return (f"{self.date} {self.description}\n"
                f"{self.from_} -> {self.to}\n"
                f"{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}\n")
