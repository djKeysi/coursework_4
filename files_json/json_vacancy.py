import json


class JSONSaverHeadHunter:
    """Класс сохранения в фойл для НН"""
    @staticmethod
    def add_vacancy(data):
        """Выводит словарь в json-подобном удобном формате с отступами (Для разработки)"""
        with open("../data.json", 'w', encoding='utf-8') as file:
           vac= json.dump(data, file, indent=2, ensure_ascii=False)
        return vac


    def read_to_file(self,file_json):
        with open(file_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    def get_id(self,file_json):
        """Метод выводит информацию о название вакансии"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file(file_json)["items"]:
                item_list.append(str(i["id"]))
                id = [i for i in item_list]
        else:
            for i in self.read_to_file(file_json):
                item_list.append(str(i["id"]))
                id = [i for i in item_list]
        #return "\n".join(id)
        return id

    def get_title(self,file_json):
        """Метод выводит информацию о название вакансии"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file(file_json)["items"]:
                item_list.append(i["name"])
                name = [i for i in item_list]
        else:
            for i in self.read_to_file(file_json):
                item_list.append(i["name"])
                name = [i for i in item_list]
        #return  "\n".join(name)
        return item_list

    def get_salary_not_sort(self,file_json):
        """Метод выводит информацию о зарплате"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file("../data.json")['items']:
                if i.get("salary", "") is not None:
                    if i.get("salary", {}).get("to") is None:
                        item_list.append(str(i.get("salary", {}).get("from", "")))
                    else:
                        item_list.append(str(i.get("salary", {}).get("to", "")))
                else:
                    item_list.append("Зарплата не указана")
        else:
            for i in self.read_to_file("../data_sort_salary.json"):
                if i.get("salary", "") is not None:
                    if i.get("salary", {}).get("to") is None:
                        item_list.append(str(i.get("salary", {}).get("from", "")))
                    else:
                        item_list.append(str(i.get("salary", {}).get("to", "")))

                        #item_list.append(0)
        #return "\n".join(item_list)
        return item_list
            #pass
            #k+=i
        #return print(i)
        #return "\n".join(salary)
    #def sort_salary(self):
        #item_list44 = []
        #k = 0
        #for i in jsaver.get_salary():
            # if i == 0:
           # k += 1
            #print(f"{i} {k - 1}")
            #if i == "0":
              #  item_list44.append(k - 1)  # вытащили нулевые значения
        #return item_list44

    def sorty_by_salary(self,salary):
        """
         метод сортировки по зарплате вызвать если пользователь запросил сортировку
         """
        list_salary=[]
        #    {'items': [{'id': '83761018',
        #list_salary.insert(0,"items")
        with open('../data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for sort_salary in data['items']:
                if sort_salary['salary'] is not None:
                    if sort_salary['salary']['from'] is not None:
                        if sort_salary['salary']['from'] >=salary:
                            list_salary.append(sort_salary)
                with open('../data_sort_salary.json', 'w+', encoding='utf-8') as file:
                    json.dump(list_salary, file, indent=2, ensure_ascii=False)
            return list_salary

    def url(self,file_json):
        """Метод выводит информацию о название вакансии"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file(file_json)["items"]:
                item_list.append(i["url"])
                url = [i for i in item_list]
        else:
            for i in self.read_to_file(file_json):
                item_list.append(i["url"])
                url = [i for i in item_list]
        #return "\n".join(url)
        return url


    def requirement(self, file_json):
        """Метод выводит информацию о требовниии к вакансии"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file(file_json)["items"]:
                item_list.append(i['snippet']["requirement"])
                req = [i for i in item_list]
        elif file_json == "../data_sort_salary.json":
            for i in self.read_to_file(file_json):
                item_list.append(i['snippet']["requirement"])
                req = [i for i in item_list]
        #return "\n".join(req)
        return req


class JSONSaverSuperJob:
    @staticmethod
    def add_vacancy(data):
        """Выводит словарь в json-подобном удобном формате с отступами (Для разработки)"""
        with open("../data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def read_to_file(self,file_json):
        with open(file_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_id(self,file_json):
        """Метод выводит информацию о название вакансии"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file(file_json)["objects"]:
                item_list.append(str(i["id"]))
                id = [i for i in item_list]
        else:
            for i in self.read_to_file(file_json):
                item_list.append(str(i["id"]))
                id = [i for i in item_list]
        #return "\n".join(id)
        #return item_list
        #return "\n".join(id)
        return id
    def get_title(self,file_json):
        """Метод выводит информацию о название вакансии"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file(file_json)["objects"]:
                item_list.append(i["profession"])
                name = [i for i in item_list]
        else:
            for i in self.read_to_file(file_json):
                item_list.append(i["profession"])
                name = [i for i in item_list]
        #return  "\n".join(name)
        return name

    def get_salary_not_sort(self, file_json):
        """Метод выводит информацию о зарплате"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file("../data.json")['objects']:
                if i.get("payment_to") is None:
                    item_list.append(str(i.get("payment_from", "")))
                else:
                    item_list.append(str(i.get("payment_to", "")))
                #else:
                    #item_list.append("Зарплата не указана")
        else:
            for i in self.read_to_file("../data_sort_salary.json"):
                if i.get("payment_to") is None:
                    item_list.append(str(i.get("payment_from", "")))
                else:
                    item_list.append(str(i.get("payment_to", "")))

                        # item_list.append(0)
        #return "\n".join(item_list)
        return item_list
    def sorty_by_salary(self,salary):
        """
         метод сортировки по зарплате вызвать если пользователь запросил сортировку
         """
        list_salary=[]
        #    {'items': [{'id': '83761018',
        #list_salary.insert(0,"items")
        with open('../data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for sort_salary in data['objects']:
               if sort_salary['payment_from'] is not None and sort_salary['payment_to'] !=0:
                   if sort_salary['payment_from'] >=salary :
                       list_salary.append(sort_salary)
               with open('../data_sort_salary.json', 'w+', encoding='utf-8') as file:
                    json.dump(list_salary, file, indent=2, ensure_ascii=False)
            return list_salary

    def url(self, file_json):
        """Метод выводит информацию о название вакансии"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file(file_json)["objects"]:
                item_list.append(i["link"])
                url = [i for i in item_list]
        else:
            for i in self.read_to_file(file_json):
                item_list.append(i["link"])
                url = [i for i in item_list]
        #return "\n".join(url)
        return url

    def requirement(self, file_json):
        """Метод выводит информацию о требовниии к вакансии"""
        item_list = []
        if file_json == "../data.json":
            for i in self.read_to_file(file_json)["objects"]:
                #item_list.append(i["client"]["description"])
                item_list.append(i["candidat"])
                req = [i for i in item_list]
        elif file_json == "../data_sort_salary.json":
            for i in self.read_to_file(file_json):
                item_list.append(i["candidat"])
                req = [i for i in item_list]
        #return "\n".join(req)
        return req



