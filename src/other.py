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
        """Не доделал валюту нормально, как хотел"""
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

        if self.currency:
            self.currency = currency
        elif type(self.salary) != int:
            self.currency = "dddd"
            # if self.salary == None:
            #     self.currency = "Валюта не указана"
            # else:
            #     self.currency = self.salary.get("currency")
        else:
            self.currency = "Валюта указанаf в аргументах"


""" рабочие методы зарплаты и валюты не нашел им применения"""

def salary_check(self):
    """Метод проверки зарплаты"""
    if type(self.salary) != int:
        if self.salary != None:
            if self.salary.get("from") and not self.salary.get("to"):
                return self.salary.get("from")
            elif not self.salary.get("from") and self.salary.get("to"):
                return self.salary["to"]
            elif self.salary.get("from") and self.salary.get("to"):
                return self.salary.get("from")
            elif not self.salary.get("from") and not self.salary.get("to"):
                return 0
        else:
            return 0
    else:
        return self.salary


def currency_check(self):
    """Метод проверки валюты"""
    if self.currency:
        return self.currency
    elif type(self.salary) != int:
        if self.salary == None:
            return "Валюта не указана"
        else:
            return self.salary.get('currency')
    else:
        return "Валюта не указана"

    def __repr__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Ссылка на вакансию: <{self.url}>\n'
                f'Зарплата: {self.salary}: {self.currency}\n'
                f'Требования: {self.requirement}\n'
                f'Валюта: {self.currency}\n')

if __name__ == "__main__":
    klass = Vacancy("python", "https://hh.ru/vacancy/94354526",
                    {'from': 85000, 'to': 100000, 'currency': 'RUR', 'gross': False},
                    "kjhflakhflahf;jh'fK")

    b = klass.__repr__()
    print(b)
    # c = self.salary.get("currency")





    # def salary_check(self):
    #     """Метод проверки зарплаты"""
    #     if type(self.salary) != int:
    #         if self.salary != None:
    #             if self.salary.get("from") and not self.salary.get("to"):
    #                 return self.salary.get("from")
    #             elif not self.salary.get("from") and self.salary.get("to"):
    #                 return self.salary["to"]
    #             elif self.salary.get("from") and self.salary.get("to"):
    #                 return self.salary.get("from")
    #             elif not self.salary.get("from") and not self.salary.get("to"):
    #                 return 0
    #         else:
    #             return 0
    #     else:
    #         return self.salary
    #
    # def currency_check(self):
    #     """Метод проверки валюты"""
    #     if self.currency:
    #         return self.currency
    #     elif type(self.salary) != int:
    #         if self.salary == None:
    #             return "Валюта не указана"
    #         else:
    #             return self.salary.get('currency')
    #     else:
    #         return "Валюта не указана"








# class Vacance:
#     """
#     Калсс для работы с вакансиями по атрибутам
#     """
#     vac_title: str
#     vac_url: str
#     salary: dict
#     currency: str
#     requirement: str
#
#     def __init__(self, vac_title, vac_url, salary_from, salary_to, requirement, currency):
#         self.vac_title = vac_title
#         self.vac_url = vac_url
#         self.salary_from = salary_from
#         self.salary_to = salary_to
#         self.requirement = requirement
#         self.currency = currency
#
#     def __repr__(self):
#         return (f'Название вакансии: {self.vac_title}\n'
#                 f'Ссылка на вакансию: <{self.vac_url}>\n'
#                 f'Зарплата: {self.salary}\n'
#                 f'Требования: {self.requirement}\n'
#                 f'Валюта: {self.currency}\n')
#
#     def salary_check(self):
#         if self.salary["from"] and not self.salary["to"]:
#             return self.salary["from"]
#         elif not self.salary["from"] and self.salary["to"]:
#             return self.salary["to"]
#         elif self.salary["from"] and self.salary["to"]:
#             return self.salary["from"]
#         elif not self.salary["from"] and not self.salary["to"]:
#             return 0
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     klass = Vacance("python", "https://hh.ru/vacancy/94354526",
#                     {'from': None, 'to': 56000, 'currency': 'RUR', 'gross': False}, "kjhflakhflahf;jh'fKH", )
#     b = klass.__repr__()
#     print(b)
#     c = klass.salary_check()
#     print(c)
#
#
# class Vacance:
#     """
#     Калсс для работы с вакансиями по атрибутам
#     """
#     vac_title: str
#     vac_url: str
#     salary: dict
#     currency: str
#     requirement: str
#
#     def __init__(self, vac_title, vac_url, salary, requirement):
#         self.vac_title = vac_title
#         self.vac_url = vac_url
#         self.salary = salary
#         self.requirement = requirement
#         self.currency = self.salary["currency"]
#
#     def __repr__(self):
#         return (f'Название вакансии: {self.vac_title}\n'
#                 f'Ссылка на вакансию: <{self.vac_url}>\n'
#                 f'Зарплата: {self.salary}\n'
#                 f'Требования: {self.requirement}\n'
#                 f'Валюта: {self.currency}\n')
#
#     # def __str__(self):
#     #     return (f'Название вакансии: {self.vac_title}\n'
#     #             f'Ссылка на вакансию: <{self.vac_url}>\n'
#     #             f'Зарплата: salary_check()\n'
#     #             f'Требования: {self.requirement}\n'
#     #             f'Валюта: {self.currency}\n')
#     # @classmethod
#     # def salary_check(cls):
#     #     if cls.salary["from"] and not cls.salary["to"]:
#     #         return cls.salary["from"]
#     #     elif not cls.salary["from"] and cls.salary["to"]:
#     #         return cls.salary["to"]
#     #     elif cls.salary["from"] and cls.salary["to"]:
#     #         return cls.salary["from"]
#     #     elif not cls.salary["from"] and not cls.salary["to"]:
#     #         return 0
#
#     def salary_check(self):
#         if self.salary["from"] and not self.salary["to"]:
#             return self.salary["from"]
#         elif not self.salary["from"] and self.salary["to"]:
#             return self.salary["to"]
#         elif self.salary["from"] and self.salary["to"]:
#             return self.salary["from"]
#         elif not self.salary["from"] and not self.salary["to"]:
#             return 0
#
#
# if __name__ == "__main__":
#     klass = Vacance("python", "https://hh.ru/vacancy/94354526",
#                     {'from': None, 'to': 56000, 'currency': 'RUR', 'gross': False}, "kjhflakhflahf;jh'fKH", )
#     b = klass.__repr__()
#     print(b)
#     c = klass.salary_check()
#     print(c)
#
