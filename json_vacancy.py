import json
from vacancy import Vacancy


class JSONSaverHeadHunter:
    @staticmethod
    def add_vacancy(data):
        """Выводит словарь в json-подобном удобном формате с отступами (Для разработки)"""
        with open("data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)


    def get_vacancies(self):
        pass

    def delete_vacancy(self):
        pass


    def read_to_file(self,file_json):
        with open(file_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_title(self,file_json):
        item_list = []
        if file_json == "data.json":
            for i in self.read_to_file(file_json)["items"]:
                item_list.append(i["name"])
                name = [i for i in item_list]
        else:
            for i in self.read_to_file(file_json):
                item_list.append(i["name"])
                name = [i for i in item_list]
        return  "\n".join(name)
        #return item_list
    def get_salary_not_sort(self,file_json):
        item_list = []
        if file_json == "data.json":
            for i in self.read_to_file("data.json")['items']:
                if i.get("salary", "") is not None:
                    if i.get("salary", {}).get("to") is None:
                        item_list.append(str(i.get("salary", {}).get("from", "")))
                    else:
                        item_list.append(str(i.get("salary", {}).get("to", "")))
                else:
                    item_list.append("Зарплата не указана")
        else:
            for i in self.read_to_file("data_sort_salary.json"):
                if i.get("salary", "") is not None:
                    if i.get("salary", {}).get("to") is None:
                        item_list.append(str(i.get("salary", {}).get("from", "")))
                    else:
                        item_list.append(str(i.get("salary", {}).get("to", "")))

                        #item_list.append(0)
        return "\n".join(item_list)
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
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for sort_salary in data['items']:
                if sort_salary['salary'] is not None:
                    if sort_salary['salary']['from'] is not None:
                        if sort_salary['salary']['from'] >=salary:
                            list_salary.append(sort_salary)
                with open('data_sort_salary.json', 'w+', encoding='utf-8') as file:
                    json.dump(list_salary, file, indent=2, ensure_ascii=False)
            return list_salary

    def url(self,file_json):
        item_list = []
        if file_json == "data.json":
            for i in self.read_to_file(file_json)["items"]:
                item_list.append(i["url"])
                url = [i for i in item_list]
        else:
            for i in self.read_to_file(file_json):
                item_list.append(i["url"])
                url = [i for i in item_list]
        return "\n".join(url)

    def requirement(self, file_json):
        item_list = []
        if file_json == "data.json":
            for i in self.read_to_file(file_json)["items"]:
                item_list.append(i['snippet']["requirement"])
                req = [i for i in item_list]
        elif file_json == "data_sort_salary.json":
            for i in self.read_to_file(file_json):
                item_list.append(i['snippet']["requirement"])
                req = [i for i in item_list]
        return "\n".join(req)



                        #print(item)
            #for i in data["items"]:

                #if i.get("salary", {}).get("from") is not None:
               # r= sorted(data["items"], key=lambda x: x['salary']['from'],reverse=True)

                #else:
                    #print("111")
        #return item



        #print(json_file)
        #print(sorted_obj)




jsaver = JSONSaverHeadHunter()
#print(jsaver.sorty_by_salary())
#print(jsaver.sorty_by_salary(100000))
#print(jsaver.get_salary('data_sorty_json.json'))

#print(jsaver.requirement("data_sort_salary.json"))
#print(jsaver.get_salary_not_sort())

vacancy = Vacancy(jsaver.get_title("data_sort_salary.json"),jsaver.url("data_sort_salary.json"),jsaver.get_salary_not_sort("data_sort_salary.json"),jsaver.requirement("data_sort_salary.json"))
print(vacancy)
#print(jsaver.sorty_by_salary('data.json'))

#print(jsaver.read_to_file())
#    {'items': [{'id': '83761018',



#item_list_name = []

#for l in item_list:
   #data = jsaver.get_name().pop(l)
   #item_list_name.append(data)

#for l in jsaver.sort_salary():
 #   data = jsaver.get_salary().pop(l)
  #  item_list_salary.append(data)


#print(data)
   #data2 = jsaver.get_salary()

   #item_list_salary.append(data2)

#print(item_list_name)


#vacancy = Vacancy(jsaver.get_salary())
#print(jsaver.get_name())
#print(vacancy)



