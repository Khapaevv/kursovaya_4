import data
from src.HH_class import HHRussia
from src.for_json_class import ClassForChange
import os
from abc import ABC, abstractmethod
import requests
import json

vac_name = input("Введите поисковый запрос для запроса вакансий из hh.ru: \n")
hh = HHRussia(vac_name)
vacancies = hh.load_vacancies()



fv = ClassForChange()
# key_word = input('Введите ключевое слово в названии вакансии: \n')
# for_name = fv.get_data_from_name(key_word)
#
# key_word = input('Введите ключевое слово в описании вакансии: \n')
# for_requirement = fv.get_data_from_requirement(key_word)

#
#     fv1 = fv.get_data_from_name(vacancies)
if __name__ == "__main__":
    proba = ClassForChange()
    # print(proba.add_vacancy_like_atr())
    proba.get_data_from_name("разработчик")
