import json

def print_welcome_user():
    return "1. headhunter.ru\n2. superjob.ru \
          \n3. Выход\n"

def print_operations():
    return "Введите поисковый запрос; \
          \n1. Получить все вакансии \
          \n2. Получить вакансии по желаемой зарплате \
          \n3. Назад \
          \n4. Выход\n"


def prof():
    return "Введите желаемую профессию\n"

def count_vacansies():
    return "Введите количество вакансий для вывода от 1 до 100\n"

def salary():
    return "Введите желаемую зарплату\n"

def header():
    return "|id вакансии| Наименование вакансии           | Зарплата       |       Ссылка на вакансию |                       Описание вакансии\n"

def delete_vacancy(user_del):
    """Метод удаления вакансии по id """
    try:
        with open("../data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            minimal = 0
            for txt in data['items']:
                if txt['id'] == user_del:
                    data['items'].pop(minimal)

                #else:
                    #print("Нет такого id")
                minimal += minimal

        with open("../data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print("УДАЛЕНО")
    except KeyError:
        with open("../data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            minimal = 0
            for txt in data['objects']:
                if txt['id'] == user_del:
                    data['objects'].pop(minimal)

                #else:
                    #print("Нет такого id")
                minimal += minimal
        with open("../data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print("УДАЛЕНО")

