from abc import ABC, abstractmethod
import requests
import json


class Parser(ABC):
    """Класс Parser является абсрактным классом
    для всех поисковых платформ"""

    def __init__(self, vac_name):
        self.vac_name = vac_name

    @abstractmethod
    def load_vacancies(self, url):
        pass

class HHRussia(Parser):
    """Класс для работы с API HeadHunter России"""

    def __init__(self, vac_name):
        super().__init__(vac_name)


    def load_vacancies(self, url=None):
        """Метод вытаскивает вакансии по ключевому
        слову (только по России) и складывает в json"""
        url = 'https://api.hh.ru/vacancies?area=113'
        params = {
            'page': 0,
            'per_page': 100
        }
        response = requests.get(f'{url}&text={self.vac_name}', params)
        data = response.json()
        with open("../data/vacancies.json", "w") as file:
            json.dump(data, file, sort_keys=True, indent=4, ensure_ascii=False)
        return data


if __name__ == "__main__":
    vacancy = HHRussia("python")
    a = vacancy.load_vacancies()
    # print(vacancy.load_vacancies())
    print(a["items"][8]["name"])
    print(a["items"][8]["salary"])
    print(a["items"][8]["salary"]['from'])
    print(a["items"][8]["salary"]['to'])
    print(a["items"][8]["salary"]['currency'])
    print(a["items"][8]["alternate_url"])


