from abc import ABC, abstractmethod
import requests
import json


class Parser(ABC):
    """
    Класс Parser является абсрактным классом для всех поисковых платформ
    """

    def __init__(self, vac_name):
        self.vac_name = vac_name

    @abstractmethod
    def load_vacancies(self, url):
        pass

class HHRussia(Parser):
    """
    Класс для работы с API HeadHunter России
    """

    def __init__(self, vac_name):
        super().__init__(vac_name)

    def load_vacancies(self, url=None):
        url = 'https://api.hh.ru/vacancies?area=113'
        response = requests.get(f'{url}&text={self.vac_name}')
        data = response.json()
        with open("../data/vacancies.json", "w") as file:
            json.dump(data, file, ensure_ascii=False)
        return data


if __name__ == "__main__":
    vacancy = HHRussia("python")
    a = vacancy.load_vacancies()
    # print(vacancy.load_vacancies())
    print(a["items"][2]["name"])
    print(a["items"][2]["salary"])
    print(a["items"][2]["salary"]['from'])
    print(a["items"][2]["salary"]['to'])
    print(a["items"][2]["salary"]['currency'])
    print(a["items"][2]["alternate_url"])


