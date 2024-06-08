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
    def get_data_from_name(cls, key_word, list):
        pass

    @abstractmethod
    def get_data_from_requirement(cls, key_word, list):
        pass

    @abstractmethod
    def delete_vacancy_if_not_key_word(cls, key_word):
        pass


class ClassForChange(AbstractClass):
    """класс для добавления объектов класса Vacancy в файл и других методов"""


    @staticmethod
    def add_vacancy_like_atr():
        """Метод добавляет объекты класса Vacancy в файл add_vacancies.json из файла
         (в котором находятся вся информация по ключевому слову ваканcии)"""
        list_vacancies = []
        with open("./data/vacancies.json", "r", encoding='utf-8') as file:
            items = json.load(file)['items']
            for item in items:
                if item.get("salary") is not None:
                    vacancy = Vacancy(item.get("name"), item.get("alternate_url"), item.get("salary"),
                                      item["snippet"].get("requirement"))
                else:
                    vacancy = Vacancy(item.get("name"), item.get("alternate_url"), None,
                                      item["snippet"].get("requirement"))
                list_vacancies.append(vacancy.__dict__)
            with open('./data/add_vacancies_like_atr.json', 'w', encoding='utf-8') as file:
                json.dump(list_vacancies, file, sort_keys=True, indent=4, ensure_ascii=False)

    @classmethod
    def sort_objects_by_salary(cls):
        """Метод сортировки вакансий по зарплате в порядке возрастания"""
        cls.add_vacancy_like_atr()
        sorted_salary = []
        with open('./data/add_vacancies_like_atr.json', 'r', encoding='utf-8') as file:
            file = json.load(file)
            sorted_salary = sorted(file, key=lambda object: object['salary'], reverse=True)
        return sorted_salary


    @classmethod
    def top_by_salary(cls, len_top):
        top = []
        top = cls.sort_objects_by_salary()[:len_top]
        return top

    @classmethod
    def get_data_from_name(cls, key_word, list):
        """Метод для фильтрации вакансий по ключевому слову в названии, выводит список"""
        filtered_from_name = []
        for object in list:
            if key_word in object['name']:
                filtered_from_name.append(object)
        return filtered_from_name

    @classmethod
    def get_data_from_requirement(cls, key_word, list):
        filtered_from_requirement = []
        """Метод для фильтрации вакансий по ключевому слову в описании,
         из списка, полученного после get_data_from_name выводит новыый список"""
        for object in list:
            if object['requirement'] is not None:
                if key_word in object['requirement']:
                    filtered_from_requirement.append(object)
        return filtered_from_requirement


    @classmethod
    def delete_vacancy_if_not_key_word(cls, key_word):
        cls.add_vacancy_like_atr()
        list_with_key_word = []
        """Метод удаления объектов класса Vacancy, если в них нет ключевого слова"""
        with open('./data/add_vacancies_like_atr.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for object in data:
                # print(object)
                #НЕ ЗНАЮ ЧТО С КОДОМ,
                #Почему пустой список на выходе????????
                if key_word in object:
                    list_with_key_word.append(object)
            print(list_with_key_word)
            # return list_with_key_word
            # with open('../data/delete_vacancy_if_not_key_word.json', 'w', encoding='utf-8') as file:
            #     json.dump(list_with_key_word, file, sort_keys=True, indent=4, ensure_ascii=False)

