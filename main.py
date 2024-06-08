from src.HH_class import HHRussia
from src.Vacancy_class import Vacancy
from src.for_json_class import ClassForChange


def user_interface():
    """Функция для работы с пользователем"""
    for_name = ''
    vac_name = input("Введите ключевое слово для запроса вакансий из hh.ru: \n")
    hh = HHRussia(vac_name)
    vacancies = hh.load_vacancies()

    check_class = ClassForChange()
    key_word_name = input('Введите ключевое слово в названии вакансии: \n')
    for_name = check_class.get_data_from_name(key_word_name)
    # return for_name
    #
    #
    key_word_requirement = input('Введите ключевое слово в описании вакансии: \n')
    for_requirement = check_class.get_data_from_requirement(key_word_requirement, for_name)
    return for_requirement
#
#     fv1 = fv.get_data_from_name(vacancies)
# if __name__ == "__main__":
#     proba = ClassForChange()
#     # print(proba.add_vacancy_like_atr())
#     proba.get_data_from_name("разработчик")
#     print(for_requirement)
if __name__ == "__main__":
    # user_interface()
    print(user_interface())
#     vacancy1 = HHRussia("python")
#     a = vacancy1.load_vacancies()

# if __name__ == "__main__":
#     user_interface()
#     print(for_name)
#     print(for_requirement)

    # proba = ClassForChange()
    # proba.add_vacancy_like_atr()
    # proba.get_data_from_name("разработчик")
    # print(len(proba.get_data_from_name("разработчик")))
    # print(proba.get_data_from_name("инженер"))
    # proba.get_data_from_requirement("Junior")
    # print(proba.get_data_from_requirement("проект"))
    # proba.delete_vacancy_if_not_key_word("Junior")
    # print(proba.delete_vacancy_if_not_key_word("Junior"))