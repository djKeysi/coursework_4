import json


class JSONSaver:
    def add_vacancy(self):
        with open('data.json','w',encoding='utf-8') as file:
            json.dumps(file)

    def get_vacancies(self):
        pass

    def delete_vacancy(self):
        pass