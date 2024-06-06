class Vacancy:
    """
    Класс для работы с вакансиями по атрибутам
    """
    vac_title: str
    vac_url: str
    salary: str
    currency: str
    requirement: str

    def __init__(self, name, url, salary, requirement):
        """Зарплата проверяется полностью, а вот для валюты такие проверки еще не сделал"""
        self.name = name
        self.url = url
        self.salary = salary
        if type(self.salary) != int:
            if self.salary:
                if self.salary.get("from") and not self.salary.get("to"):
                    self.salary = self.salary.get("from")
                elif not self.salary.get("from") and self.salary.get("to"):
                    self.salary = self.salary["to"]
                elif self.salary.get("from") and self.salary.get("to"):
                    self.salary = (self.salary.get("from") + self.salary.get("to"))/2
                elif not self.salary.get("from") and not self.salary.get("to"):
                    self.salary = 0
            else:
                self.salary = 0
        self.requirement = requirement
        if salary.get("currency"):
            self.currency = salary.get('currency')
        else:
            self.currency = "Валюта не указана"


    def __repr__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Ссылка на вакансию: <{self.url}>\n'
                f'Зарплата: {self.salary}: {self.currency}\n'
                f'Требования: {self.requirement}\n')


    def __gt__(self, other):
        """Метод сравнения зарплат"""
        if self.salary > other.salary:
            return True
        else:
            return False


    def __lt__(self, other):
        """Метод сравнения зарплат"""
        if self.salary < other.salary:
            return True
        else:
            return False


if __name__ == "__main__":
    klass = Vacancy("python", "https://hh.ru/vacancy/94354526",
                    {'from': 85000, 'to': 100000, 'currency': 'RUR', 'gross': False},
                    "уметь много программировать")

    klass2 = Vacancy("python", "https://hh.ru/vacancy/94354526",
                    {'from': 335000, 'to': 34100000, 'currency': 'RUR', 'gross': False},
                    "хоть что-то уметь")

    b = klass.__repr__()
    print(b)
    # cc = klass2.__repr__()
    # print(cc)
    # dd = klass.__gt__(klass2)
    # print(dd)
    # ee = klass.__lt__((klass2))
    # print(ee)


