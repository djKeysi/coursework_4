from abc import ABC,abstractmethod
import requests
from files_json.json_vacancy import JSONSaverHeadHunter,JSONSaverSuperJob

class HH_SuperJob_API(ABC):
    @abstractmethod
    def get_vacancies(self,professions, per_page):
        pass

class HeadHunterAPI(HH_SuperJob_API) :
    """
    класс для работы с сайтом HeadHunter
            text - Поисковый запрос
            per_page - Количество вакансий на странице
            """
    def get_vacancies(self,professions, per_page) -> None:
        params = {
        'text': f"NAME:{professions}",
        'per_page': per_page,
        #'page':page
        }
        req = requests.get('https://api.hh.ru/vacancies',params=params).json()
        #item = [req for item in req['items'] if item.get("salary").get("from") is not None]
        JSONSaverHeadHunter.add_vacancy(req)
        #return req
        #if req.status_code != 200:
            #print("Ошибка при выполнении запроса:")
        #d = req.content.decode()

class SuperJobAPI(HH_SuperJob_API):
    """
        класс для работы с сайтом SuperJob
                text - Поисковый запрос
                per_page - Количество вакансий на странице
                """
    def get_vacancies(self,professions, per_page):
        headers = {
            'X-Api-App-Id': 'v3.r.137688907.fc31712eeb1c5efb24178a284f5506d8ce9f73eb.1957629336f15fea6dc585930924e4d453edc1ee'
        }

        #catalogue_id = 48  # id каталога "Разработка, программирование"
        #town_id = 4  # id города Москва
        #vacancies_count = per_page  # api запрещает запрашивать больше 100 вакансий
        #keyword = 'python'
        #params = {'town': town_id, 'catalogues': catalogue_id, 'count': vacancies_count, 'keyword': keyword}
        params = {'count': per_page, 'keyword': professions }
        data = requests.get('https://api.superjob.ru/2.0/vacancies', params=params, headers=headers).json()
        JSONSaverSuperJob.add_vacancy(data)
        #return data


