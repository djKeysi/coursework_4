from utils import print_welcome_user, print_operations,prof,salary
from vacancy import Vacancy
from json_vacancy import JSONSaverHeadHunter
from  API_Vacancy import HH_SuperJob_API,HeadHunterAPI


def user_interaction():
    #platforms = ["HeadHunter", "SuperJob"]
    print_welcome_user()


    search_query = input("Введите цифру платформы:\n")
    hhapi = HeadHunterAPI()
    jsaver = JSONSaverHeadHunter()
    if search_query == "1":
         print("Вы выбрали HeadHunter")
         operations = input(print_operations())
    if  operations == "1":
        profession = input(prof())

        hhapi.get_vacancies(profession,100)
        #vacancy = Vacancy(jsaver.get_title("data_sort_salary.json"),jsaver.url("data_sort_salary.json"),jsaver.get_salary_not_sort("data_sort_salary.json"),jsaver.requirement("data_sort_salary.json"))
        vacancy = Vacancy(jsaver.get_title("data.json"),jsaver.url("data.json"),jsaver.get_salary_not_sort("data.json"),jsaver.requirement("data.json"))

        print(vacancy)
    elif operations == "2":
        profession = input(prof())

        hhapi.get_vacancies(profession, 100)
        salary_ = input(salary())
        jsaver.sorty_by_salary(int(salary_))

        vacancy = Vacancy(jsaver.get_title("data_sort_salary.json"),jsaver.url("data_sort_salary.json"),jsaver.get_salary_not_sort("data_sort_salary.json"),jsaver.requirement("data_sort_salary.json"))
        print(vacancy)

    #elif search_query == 0 :
       # break


if __name__ == "__main__":
    user_interaction()



