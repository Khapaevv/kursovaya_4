from src.HH_class import HHRussia
from src.Vacancy_class import Vacancy
from src.Methods_by_json import ClassForChange


def user_interface():
    """Функция для работы с пользователем"""
    while True:

        vac_name = input("Введите ключевое слово для общего запроса вакансий из hh.ru: \n")
        hh = HHRussia(vac_name)
        vacancies = hh.load_vacancies()

        check_class = ClassForChange()


        try:
            len_top = int(input("Введите количество Топа зарплат из полученного списка: \n"))
            if len_top is not int and len_top <= 0:
                raise ValueError
        except ValueError:
            print('Получено некорректное значение. Нужно ввести цифру. Давай по новой!')
            break
        top = check_class.top_by_salary(len_top)

        key_word_name = input('Введите ключевое слово в названии вакансии \n(если не нужно - нажмите enter): \n')
        for_name = check_class.get_data_from_name(key_word_name, top)
        quantity_for_name = len(for_name)
        print(f'Найдено {quantity_for_name} вакансий')

        key_word_requirement = input('Введите ключевое слово в описании вакансии \n(если не нужно - нажмите enter): \n')
        for_requirement = check_class.get_data_from_requirement(key_word_requirement, for_name)
        quantity_for_requirement = len(for_requirement)
        print(f'Найдено {quantity_for_requirement} вакансий, вот ссылки на них:')

        for item in for_requirement:
            item['url']
            print(item['url'])
        break





if __name__ == "__main__":
    user_interface()
    # print(user_interface())


