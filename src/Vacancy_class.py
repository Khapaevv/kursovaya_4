class Vacancy:
    """
    Класс для работы с вакансиями по атрибутам
    """
    vac_title: str
    vac_url: str
    salary: int
    currency: str
    requirement: str


    def __init__(self, name, url, salary, requirement='Информация отсутствует', currency=None):
        """Зарплата проверяется по всем критериям,
        если есть и from и to, то выводится среднее значение зарплаты"""
        self.name = name
        self.url = url
        self.salary = salary
        if not isinstance(salary, int):
            if self.salary:
                if self.salary.get("from") and not self.salary.get("to"):
                    self.salary = self.salary.get("from")
                elif not self.salary.get("from") and self.salary.get("to"):
                    self.salary = self.salary.get("to")
                elif self.salary.get("from") and self.salary.get("to"):
                    self.salary = int((self.salary.get("from") + self.salary.get("to")) / 2)
                elif not self.salary.get("from") and not self.salary.get("to"):
                    self.salary = 0
            else:
                self.salary = 0
        self.requirement = requirement
        if salary is not None:
            if salary.get("currency"):
                self.currency = salary.get("currency")
            else:
                self.currency = "Валюта не указана"
        self.currency = currency
        self.__validate_salary(salary)
        self.__validate_requirement(requirement)


    def __validate_salary(self, salary):
        """Валидация зарплаты"""
        if salary is not None:
            if salary < 0:
                raise ValueError("Зарплата не может быть отрицательной")


    def __validate_requirement(self, requirement):
        """Валидация требований"""
        if not requirement:
            raise ValueError("Требования не указаны")


    def __repr__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Ссылка на вакансию: <{self.url}>\n'
                f'Зарплата: {self.salary}\n'
                f'Требования: {self.requirement}\n')


    def __gt__(self, other):
        """Метод сравнения зарплат"""
        return self.salary > other.salary


    def __lt__(self, other):
        """Метод сравнения зарплат"""
        return self.salary < other.salary


if __name__ == "__main__":
    klass = Vacancy("python", "https://hh.ru/vacancy/94354526",
                    {'from': 85000, 'to': 100000, 'currency': 'RUR', 'gross': False},
                    "уметь много программировать")

    klass2 = Vacancy("python", "https://hh.ru/vacancy/94354526",
                    {'from': 335000, 'to': 34100000, 'currency': 'RUR', 'gross': False},
                    "хоть что-то уметь")

    b = klass.__repr__()
    print(b)
    cc = klass2.__repr__()
    print(cc)
    dd = klass.__gt__(klass2)
    print(dd)
    ee = klass.__lt__(klass2)
    print(ee)