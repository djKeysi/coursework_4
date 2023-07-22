import json
def print_welcome_user():
    print("\n1. headhunter.ru\n2. superjob.ru\n"
          "\n0. Выход\n")
def print_operations():
    print("Введите поисковый запрос;"
          "\n1. Получить все вакансии по профессии"
          "\n2. Получить вакансии по желаемой зарплате"
          "\n3. Выход\n"
          )

def prof():
    print("Введите желаемую профессию\n")
def salary():
    print("Введите желаемую зарплату\n")

def delete_vacancy(user_del):
    """Метод удаления вакансии по id """
    try:
        with open("data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            minimal = 0
            for txt in data['items']:
                if txt['id'] == user_del:
                    data['items'].pop(minimal)

                #else:
                    #print("Нет такого id")
                minimal += minimal

        with open("data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print("УДАЛЕНО")
    except KeyError:
        with open("data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            minimal = 0
            for txt in data['objects']:
                if txt['id'] == user_del:
                    data['objects'].pop(minimal)

                #else:
                    #print("Нет такого id")
                minimal += minimal
        with open("data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print("УДАЛЕНО")

