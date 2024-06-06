from abc import ABC, abstractmethod
from src.Vacancy_class import Vacancy
import json

class ForJsonClass(ABC):
    pass



    @abstractmethod
    def add_vacancy_like_atr(self, *args):
        pass


    @abstractmethod
    def get_data(self, *args):
        pass


class AddClass(ForJsonClass):
    pass

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



    def get_data(self, *args):
        pass

    def delete_vacancy(self):
        pass

if __name__ == "__main__":
    proba = AddClass()
    print(proba.add_vacancy_like_atr())
    # print(list_vacancies)
