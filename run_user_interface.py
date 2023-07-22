from utils import print_welcome_user, print_operations,prof,salary,delete_vacancy
from vacancy import Vacancy
from json_vacancy import JSONSaverHeadHunter, JSONSaverSuperJob
from  API_Vacancy import HeadHunterAPI, SuperJobAPI


def user_interaction():
    """Пользовательский метод запуска программы"""
    #platforms = ["HeadHunter", "SuperJob"]
    print_welcome_user()


    search_query = input("Введите цифру платформы:\n")
    hhapi = HeadHunterAPI()
    sjapi = SuperJobAPI()
    jsaver = JSONSaverHeadHunter()
    jsaverSJ = JSONSaverSuperJob()
    while True:
        if search_query == "1":
            print("Вы выбрали HeadHunter")
            operations = input(print_operations())
            if  operations == "1":
                profession = input(prof())

                hhapi.get_vacancies(profession,100)
                vacancy = Vacancy(jsaver.get_id("data.json"),jsaver.get_title("data.json"),jsaver.url("data.json"),jsaver.get_salary_not_sort("data.json"),jsaver.requirement("data.json"))

                print(vacancy)
            elif operations == "2":
                profession = input(prof())

                hhapi.get_vacancies(profession, 100)
                salary_ = input(salary())
                jsaver.sorty_by_salary(int(salary_))

                vacancy = Vacancy(jsaver.get_id("data_sort_salary.json"),jsaver.get_title("data_sort_salary.json"),jsaver.url("data_sort_salary.json"),jsaver.get_salary_not_sort("data_sort_salary.json"),jsaver.requirement("data_sort_salary.json"))
                print(vacancy)
        if search_query =="2":
            print("Вы выбрали SuperJob")
            operations = input(print_operations())
            if  operations == "1":
                profession = input(prof())
                jsaverSJ.add_vacancy(sjapi.get_vacancies(profession,100))
                vacancy = Vacancy(jsaverSJ.get_id("data.json"),jsaverSJ.get_title("data.json"),jsaverSJ.url("data.json"),jsaverSJ.get_salary_not_sort("data.json"),jsaverSJ.requirement("data.json"))
                print(vacancy)
            elif operations == "2":
                profession = input(prof())
                sjapi.get_vacancies(profession,100)
                salary_ = input(salary())
                jsaverSJ.sorty_by_salary(int(salary_))
                vacancy = Vacancy(jsaverSJ.get_id("data_sort_salary.json"),jsaverSJ.get_title("data_sort_salary.json"),jsaverSJ.url("data_sort_salary.json"),jsaverSJ.get_salary_not_sort("data_sort_salary.json"),jsaverSJ.requirement("data_sort_salary.json"))
                print(vacancy)
        elif search_query == "0" or operations == "3":
            print("Выход")
            break


    # Блок управления вакансиями в файле
    while True:
        user_choice = input("1 - Посмотреть вакансии \n"
                            "2 - Удалить вакансию по id\n"
                            "0 - Выход\n"
                            )

        if user_choice == "1":
            try:
                vacancy = Vacancy(jsaver.get_id("data.json"), jsaver.get_title("data.json"),
                                  jsaver.url("data.json"), jsaver.get_salary_not_sort("data.json"),
                                  jsaver.requirement("data.json"))
                print(vacancy)
            except KeyError:
                vacancy = Vacancy(jsaverSJ.get_id("data_sort_salary.json"), jsaverSJ.get_title("data_sort_salary.json"),
                                  jsaverSJ.url("data_sort_salary.json"),
                                  jsaverSJ.get_salary_not_sort("data_sort_salary.json"),
                                  jsaverSJ.requirement("data_sort_salary.json"))
                print(vacancy)
        elif user_choice == "2":
            user_del = input("id вакансии: ")
            delete_vacancy(user_del)


        elif user_choice == "0":
            break



            #jsaverSJ.get_salary_not_sort("data_sort_salary.json")



    #elif search_query == 0 :
       # break


if __name__ == "__main__":
    user_interaction()



