from utils import print_welcome_user, print_operations,prof,salary,delete_vacancy,count_vacansies,header
from vacancy import Vacancy
from files_json.json_vacancy import JSONSaverHeadHunter, JSONSaverSuperJob
from  API_Vacancy import HeadHunterAPI, SuperJobAPI

DATA_JSON = "../data.json"
DATA_JSON_SORT_SALARY = "../data_sort_salary.json"

def user_interaction():

    """Пользовательский метод запуска программы"""
    #platforms = ["HeadHunter", "SuperJob"]
    flag = True

    hhapi = HeadHunterAPI()
    sjapi = SuperJobAPI()
    jsonsaverHH = JSONSaverHeadHunter()
    jsaverSJ = JSONSaverSuperJob()
    while flag:
        print(print_welcome_user())

        search_query = input("Введите цифру платформы:\n")
        if search_query == "1":
            print("Вы выбрали HeadHunter")
            operations = input(print_operations())

            if  operations == "1":

                profession = input(prof())


                hhapi.get_vacancies(profession,100)
                count_vacancies = input(count_vacansies())
                #vacancy = Vacancy(jsaver.get_id("data.json"),jsaver.get_title("data.json"),jsaver.url("data.json"),jsaver.get_salary_not_sort("data.json"),jsaver.requirement("data.json"))
                vacancy = Vacancy(jsonsaverHH.get_title(DATA_JSON), jsonsaverHH.url(DATA_JSON),
                                  jsonsaverHH.get_id(DATA_JSON), jsonsaverHH.get_salary_not_sort(DATA_JSON),
                                  jsonsaverHH.requirement(DATA_JSON))
                print(header())
                for i in range(int(count_vacancies)):
                     print("".join(vacancy.salary[i]) +",     "+"".join(vacancy.title[i]) +",  "+   "".join(vacancy.requirement[i]) +" руб."  + ",  " + "".join(vacancy.url[i]) + ",  " + "".join(vacancy.id[i])    )



            # print(vacancy)
            elif operations == "2":
                profession = input(prof())


                hhapi.get_vacancies(profession, 100)
                salary_ = input(salary())
                jsonsaverHH.sorty_by_salary(int(salary_))
                count_vacancies = input(count_vacansies())
                vacancy = Vacancy(jsonsaverHH.get_title(DATA_JSON_SORT_SALARY), jsonsaverHH.url(DATA_JSON_SORT_SALARY),
                                  jsonsaverHH.get_id(DATA_JSON_SORT_SALARY), jsonsaverHH.get_salary_not_sort(DATA_JSON_SORT_SALARY),
                                  jsonsaverHH.requirement(DATA_JSON_SORT_SALARY))
                print(header())
                for i in range(int(count_vacancies)):
                    print("".join(vacancy.salary[i]) + ",     " + "".join(vacancy.title[i]) + ",  " + "".join(
                        vacancy.requirement[i]) + " руб." + ",  " + "".join(vacancy.url[i]) + ",  " + "".join(
                        vacancy.id[i]))
            elif operations == "3":
                flag = True
            elif operations == "4":
                print("Выход")
                flag = False

        if search_query =="2":
             print("Вы выбрали SuperJob")
             operations = input(print_operations())
             if  operations == "1":
                 profession = input(prof())
                 #jsaverSJ.add_vacancy(sjapi.get_vacancies(profession,100))
                 sjapi.get_vacancies(profession, 100)
                 count_vacancies = input(count_vacansies())
                 vacancy = Vacancy(jsaverSJ.get_title(DATA_JSON), jsaverSJ.url(DATA_JSON),
                                   jsaverSJ.get_id(DATA_JSON),
                                   jsaverSJ.get_salary_not_sort(DATA_JSON),
                                   jsaverSJ.requirement(DATA_JSON))
                 print(header())
                 for i in range(int(count_vacancies)):
                     print("".join(vacancy.salary[i]) + ",     " + "".join(vacancy.title[i]) + ",  " + "".join(
                         vacancy.requirement[i]) + " руб." + ",  " + "".join(vacancy.url[i]) + ",  " + "".join(
                         vacancy.id[i]))
                     print("________________________________________________\n\n")

             elif operations == "2":
                 profession = input(prof())
                 sjapi.get_vacancies(profession,100)
                 salary_ = input(salary())
                 jsaverSJ.sorty_by_salary(int(salary_))
                 count_vacancies = input(count_vacansies())
                 vacancy = Vacancy(jsaverSJ.get_title(DATA_JSON_SORT_SALARY), jsaverSJ.url(DATA_JSON_SORT_SALARY),
                                   jsaverSJ.get_id(DATA_JSON_SORT_SALARY),
                                   jsaverSJ.get_salary_not_sort(DATA_JSON_SORT_SALARY),
                                   jsaverSJ.requirement(DATA_JSON_SORT_SALARY))
                 print(header())
                 for i in range(int(count_vacancies)):
                     print("".join(vacancy.salary[i]) + ",     " + "".join(vacancy.title[i]) + ",  " + "".join(
                         vacancy.requirement[i]) + " руб." + ",  " + "".join(vacancy.url[i]) + ",  " + "".join(
                         vacancy.id[i]))
                     print("________________________________________________\n\n")

             elif operations == "3":
                flag = True
             elif operations == "4":
                 print("Выход")
                 flag = False
        if search_query == "3":
            flag = False



    # Блок управления вакансиями в файле
    while True:
        user_choice = input("1 - Посмотреть вакансии \n"
                            "2 - Удалить вакансию по id\n"
                            "0 - Выход\n"
                            )

        if user_choice == "1":
            try:
                vacancy = Vacancy(jsonsaverHH.get_title(DATA_JSON), jsonsaverHH.url(DATA_JSON),
                                  jsonsaverHH.get_id(DATA_JSON), jsonsaverHH.get_salary_not_sort(DATA_JSON),
                                  jsonsaverHH.requirement(DATA_JSON))
                count_vacancies = input("Введите количество вакансий для просмотра от 1 до 99\n")
                print(header())
                for i in range(int(count_vacancies)):
                    print("".join(vacancy.salary[i]) + ",     " + "".join(vacancy.title[i]) + ",  " + "".join(
                        vacancy.requirement[i]) + " руб." + ",  " + "".join(vacancy.url[i]) + ",  " + "".join(
                        vacancy.id[i]))

            except KeyError:
                vacancy = Vacancy(jsaverSJ.get_title(DATA_JSON), jsaverSJ.url(DATA_JSON),
                                  jsaverSJ.get_id(DATA_JSON),
                                  jsaverSJ.get_salary_not_sort(DATA_JSON),
                                  jsaverSJ.requirement(DATA_JSON))
                count_vacancies = input("Введите количество вакансий для просмотра от 1 до 99\n")
                print(header())
                for i in range(int(count_vacancies)):
                    print("".join(vacancy.salary[i]) + ",     " + "".join(vacancy.title[i]) + ",  " + "".join(
                        vacancy.requirement[i]) + " руб." + ",  " + "".join(vacancy.url[i]) + ",  " + "".join(
                        vacancy.id[i]))
                    print("________________________________________________\n\n")
        elif user_choice == "2":
            user_del = input("id вакансии: ")
            delete_vacancy(user_del)


        elif user_choice == "0":
            print("Выход")
            break



if __name__ == "__main__":
    user_interaction()


