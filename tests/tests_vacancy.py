import pytest
from src.Vacancy_class import Vacancy


@pytest.fixture
def klass():
    return Vacancy("python", "https://hh.ru/vacancy/94354526",
                    {'from': 85000, 'to': 100000, 'currency': 'RUR', 'gross': False},
                    "уметь много программировать")


@pytest.fixture
def klass2():
    return Vacancy("CC", "https://hh.ru/vacancy/94354590",
                    {'from': 335000, 'to': 34100000, 'currency': 'RUR', 'gross': False},
                    "хоть что-то уметь")


def test_vacancy_init(klass, klass2):
    assert klass.name == "python"
    assert klass.salary == 92500
    assert klass.url == "https://hh.ru/vacancy/94354526"
    assert klass.requirement == "уметь много программировать"

    assert klass2.name == "CC"
    assert klass2.salary == 17217500
    assert klass2.url == "https://hh.ru/vacancy/94354590"
    assert klass2.requirement == "хоть что-то уметь"


def test_vacancy_repr(klass, klass2):
    assert repr(klass) == f'Название вакансии: python\n' \
                          f'Ссылка на вакансию: <https://hh.ru/vacancy/94354526>\n' \
                          f'Зарплата: 92500\n' \
                          f'Требования: уметь много программировать\n'

    assert repr(klass2) == f'Название вакансии: CC\n' \
                           f'Ссылка на вакансию: <https://hh.ru/vacancy/94354590>\n' \
                           f'Зарплата: 17217500\n' \
                           f'Требования: хоть что-то уметь\n'


def test_vacancy_gt(klass, klass2):
    assert klass.__gt__(klass2) is False


def test_vacancy_lt(klass, klass2):
    assert klass.__lt__(klass2) is True