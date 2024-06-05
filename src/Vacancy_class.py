class Vacancy:
    """
    Класс для работы с вакансиями по атрибутам
    """
    vac_title: str
    vac_url: str
    salary: int
    currency: str
    requirement: str

    def __init__(self, name, url, salary, requirement, currency):
        """Зарплата проверяется полностью, а вот для валюты такие проверки еще не сделал"""
        self.name = name
        self.url = url
        self.salary = salary
        if type(self.salary) != int:
            if self.salary != None:
                if self.salary.get("from") and not self.salary.get("to"):
                    self.salary = self.salary.get("from")
                elif not self.salary.get("from") and self.salary.get("to"):
                    self.salary = self.salary["to"]
                elif self.salary.get("from") and self.salary.get("to"):
                    self.salary = self.salary.get("from")
                elif not self.salary.get("from") and not self.salary.get("to"):
                    self.salary = 0
            else:
                self.salary = 0
        self.requirement = requirement
        self.currency = currency

    def __repr__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Ссылка на вакансию: <{self.url}>\n'
                f'Зарплата: {self.salary}: {self.currency}\n'
                f'Требования: {self.requirement}\n'
                f'Валюта: {self.currency}\n')



if __name__ == "__main__":
    klass = Vacancy("python", "https://hh.ru/vacancy/94354526",
                    {'from': 85000, 'to': 100000, 'currency': 'RUR', 'gross': False},
                    "kjhflakhflahf;jh'fK", "RUR")

    b = klass.__repr__()
    print(b)


