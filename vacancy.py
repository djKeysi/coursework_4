

def str_to_digit(input_str):
    return int(input_str.split(" ")[0])


class Vacancy:
    """
       Класс для работы с вакансиями.
       Атрибуты:
           - ид вакансии
           - название вакансии;
           - ссылка на вакансию;
           - зарплата;
           - краткое описание;


       """
    def __init__(self, title,url,salary,requirement,id):
        self.id = id
        self.title = title
        self.url = url
        self.salary = salary
        self.requirement = requirement

    #def __str__(self):
        #return f"{self.title} {self.salary} {self.description} {self.url}"

    def __str__(self):
        r=""
        for i in zip(self.id,self.title,self.url,self.salary,self.requirement):
            return " ".join(i)
        #return print("{:<100} | {:<100} | {:<100} | {:>30}".format(self.title,self.url,self.salary,self.requirement))
        #return print(print(" {:<25} | {:<25} | {:>11} | {:>11}".format(self.title, self.url, self.salary, self.requirement)))
        #return f"{self.title}                             {self.url}                                      {self.salary}                                  {self.requirement} "


    def __eq__(self, other):
        return str_to_digit(self.salary) == str_to_digit(other.salary)

    def __lt__(self, other):
        return str_to_digit(self.salary) < str_to_digit(other.salary)

    def __gt__(self, other):
        return str_to_digit(self.salary) > str_to_digit(other.salary)