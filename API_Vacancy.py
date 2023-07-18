import requests
#params = {
    #'text': 'python',
    #'per_page': 100,
    #'page':page
#}
#data = requests.get('https://api.hh.ru/vacancies',params=params).json()

headers = {
    'X-Api-App-Id':'v3.r.137688907.fc31712eeb1c5efb24178a284f5506d8ce9f73eb.1957629336f15fea6dc585930924e4d453edc1ee'
}

catalogue_id = 48  # id каталога "Разработка, программирование"
town_id = 4  # id города Москва
vacancies_count = 100  # api запрещает запрашивать больше 100 вакансий
keyword = 'python'
params = {'town': town_id, 'catalogues': catalogue_id, 'count': vacancies_count, 'keyword': keyword}
data = requests.get('https://api.superjob.ru/2.0/vacancies',params=params,headers=headers).json()


#https://api.hh.ru/vacancies/?text=python
print(data)


