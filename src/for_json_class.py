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
    def get_data_from_name(cls, key_word):
        cls.add_vacancy_like_atr()
        filtered_from_name = []
        """Метод для фильтрации вакансий по ключевому слову в названии, выводит список"""
        with open('./data/add_vacancies_like_atr.json', 'r', encoding='utf-8') as file:
            file = json.load(file)
            for object in file:
                if key_word in object['name']:
                    filtered_from_name.append(object)
        return filtered_from_name

    @classmethod
    def get_data_from_requirement(cls, key_word):
        cls.add_vacancy_like_atr()
        filtered_from_requirement = []
        """Метод для фильтрации вакансий по ключевому слову в описании, выводит список"""
        with open('./data/add_vacancies_like_atr.json', 'r', encoding='utf-8') as file:
            file = json.load(file)
            for object in file:
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



if __name__ == "__main__":
    proba = ClassForChange()
    # proba.add_vacancy_like_atr()
    proba.get_data_from_name("разработчик")
    print(len(proba.get_data_from_name("разработчик")))
    print(proba.get_data_from_name("разработчик"))
    proba.get_data_from_requirement("разработчик")
    print(proba.get_data_from_requirement("разработчик"))
    # proba.delete_vacancy_if_not_key_word("Junior")
    # print(proba.delete_vacancy_if_not_key_word("Junior"))


    # print(proba.filtered_from_name)
    # proba.delete_vacancy_if_not_key_word("разработчик")
    # print(proba.delete_vacancy_if_not_key_word("разработчик"))
