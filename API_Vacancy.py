from abc import ABC,abstractmethod
import requests
from json_vacancy import JSONSaverHeadHunter

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
        #if req.status_code != 200:
            #print("Ошибка при выполнении запроса:")
        #d = req.content.decode()

class SuperJobAPI(HH_SuperJob_API):
    def get_vacancies(self,professions, per_page):
        headers = {
            'X-Api-App-Id': 'v3.r.137688907.fc31712eeb1c5efb24178a284f5506d8ce9f73eb.1957629336f15fea6dc585930924e4d453edc1ee'
        }

        catalogue_id = 48  # id каталога "Разработка, программирование"
        town_id = 4  # id города Москва
        vacancies_count = 100  # api запрещает запрашивать больше 100 вакансий
        keyword = 'python'
        params = {'town': town_id, 'catalogues': catalogue_id, 'count': vacancies_count, 'keyword': keyword}
        data = requests.get('https://api.superjob.ru/2.0/vacancies', params=params, headers=headers).json()
        return data





#if choice == "1":
 #   search_query = input("Введите поисковый запрос: ")
  #  res = platform().get_search_vacancies(search_query)
   # print(print_result_search(platform, res))
    #vacancies = []
    #for vac in print_result_search(platform, res):
     #   vacancy = Vacancy(vac[0], vac[1], vac[2], vac[3], vac[4], vac[5], vac[6])
      #  vacancies.append(vacancy)
    #input("Нажмите ENTER, чтобы продолжить!")
    #break

import json



#2 достать с хх обработать через обработчик вакансий и записать все в файл
#далее выбираю меню отсортировать по з.п функция или отфильтровать по ключевому слову например джуниор и напечатал пользователю
#hhapi = HeadHunterAPI()
#superjobapi = SuperJobAPI()
#print(superjobapi.get_vacansies())
#print(hhapi.get_vacancies('python',100))

#vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#print(vacancy)
#jsonsave = JSONSaver()
#jsonsave.add_vacancy(hhapi.get_vacansies('python'))




