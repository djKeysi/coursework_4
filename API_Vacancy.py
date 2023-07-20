from abc import ABC,abstractmethod
import requests

class HH_SuperJob_API(ABC):
    @abstractmethod
    def get_vacansies(self):
        pass

class HeadHunterAPI(HH_SuperJob_API):
    def get_vacansies(self,professions):
        params = {
        'text': f"NAME:{professions}",
        'per_page': 10,
        #'page':page
        }
        req = requests.get('https://api.hh.ru/vacancies',params=params).json()
        #d = req.content.decode()
        return req
class SuperJobAPI(HH_SuperJob_API):
    def get_vacansies(self):
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
class Vacancy:
    def __init__(self, title,url,salary,description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

def print_welcome_user_2():
    print("\n1. headhunter.ru\n2. superjob.ru\n3. trudvsem.ru"
          "\n0. Выход\n")
def print_operations():
    print("1. Ввести поисковый запрос;"
          "\n2. Получить топ N вакансий по зарплате;"
          "\n3. Получить вакансии выбранного региона;"
          "\n4. Получить вакансии, по ключевому слову в описании.\n"
          "\n0. Назад.\n")


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
class JSONSaver:
    def add_vacancy(self,data):
        """Выводит словарь в json-подобном удобном формате с отступами (Для разработки)"""
        with open('data.json','w',encoding='utf-8') as file:
            json.dump(data,file,indent=2,ensure_ascii=False)

    def get_vacancies(self):
        pass

    def delete_vacancy(self):
        pass



#2 достать с хх обработать через обработчик вакансий и записать все в файл
#далее выбираю меню отсортировать по з.п функция или отфильтровать по ключевому слову например джуниор и напечатал пользователю
hhapi = HeadHunterAPI()
superjobapi = SuperJobAPI()
#print(superjobapi.get_vacansies())
print(hhapi.get_vacansies('python'))

vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
jsonsave = JSONSaver()
jsonsave.add_vacancy(hhapi.get_vacansies('python'))




