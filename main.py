#делаем два класса которые работают с апи достают данные
# класс который работает с файликом добавить удалить получает
# класс вакансии который обрабатывает данные и создает экземпляры классов
#1 достать данные с сумерджоба
#2 достать с хх
#3 достать с двух сайтов
#отфильстровать все по ключевому слову, зарплате , имени вакансии
# введите топ вакансий сколько вывести
#уже в записанном файле вызывается сортировка по зарплате
# проверка что есть доступ к апи


class Vacancy:
    def __init__(self, title,url,salary,description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description
