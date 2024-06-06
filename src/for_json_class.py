from abc import ABC, abstractmethod
from src.Vacancy_class import Vacancy
import json

class AbstractClass(ABC):
    pass

    @staticmethod
    @abstractmethod
    def add_vacancy_like_atr():
        pass


    @abstractmethod
    def get_data_from_name(cls, key_word):
        pass

    @abstractmethod
    def get_data_from_requirement(cls, key_word):
        pass

    @abstractmethod
    def delete_vacancy_if_not_key_word(cls, key_word):
        pass


class ClassForChange(AbstractClass):
    """класс для добавления объектов класса Vacancy в файл"""

    filtered_from_name = []
    filtered_from_requirement = []

    @staticmethod
    def add_vacancy_like_atr():
        """Метод добавляет вакансии в файл add_vacancies.json из файла
        vacancies.json (в котором находятся вся информация по ключевому слову ваканcии)"""
        list_vacancies = []
        with open("../data/vacancies.json", "r", encoding='utf-8') as file:
            items = json.load(file)['items']
            for item in items:
                if item.get("salary") is not None:
                    vacancy = Vacancy(item.get("name"), item.get("alternate_url"), item.get("salary"),
                                      item["snippet"].get("requirement"))
                else:
                    vacancy = Vacancy(item.get("name"), item.get("alternate_url"), None,
                                      item["snippet"].get("requirement"))
                list_vacancies.append(vacancy.__dict__)
            with open('../data/add_vacancies_like_atr.json', 'w', encoding='utf-8') as file:
                json.dump(list_vacancies, file, sort_keys=True, indent=4, ensure_ascii=False)


    @classmethod
    def get_data_from_name(cls, key_word):
            """Метод для фильтрации вакансий по ключевому слову в названии"""
            with open('../data/add_vacancies_like_atr.json', 'r', encoding='utf-8') as file:
                file = json.load(file)
                for key_name in file:
                    if key_word in key_name['name'].lower():
                        cls.filtered_from_name.append(key_name)

    @classmethod
    def get_data_from_requirement(cls, key_word):
            """Метод для фильтрации вакансий по ключевому слову в описании"""
            with open('../data/add_vacancies_like_atr.json', 'r', encoding='utf-8') as file:
                file = json.load(file)
                for key_name in file:
                    if key_word in key_name['name'].lower():
                        cls.filtered_from_requirement.append(key_name)
    @classmethod
    def delete_vacancy_if_not_key_word(cls, key_word):
        """Метод удаления объектов класса Vacancy, если в них нет ключевого слова"""
        with open('../data/add_vacancies_like_atr.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            if key_word in data:
                with open('../data/delete_vacancy_if_not_key_word.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file, sort_keys=True, indent=4, ensure_ascii=False)
            else:
                pass


if __name__ == "__main__":
    proba = ClassForChange()
    # print(proba.add_vacancy_like_atr())
    proba.get_data_from_name("разработчик")

    # print(proba.filtered_from_name)
    proba.delete_vacancy_if_not_key_word("разработчик")
    print(proba.delete_vacancy_if_not_key_word("разработчик"))
