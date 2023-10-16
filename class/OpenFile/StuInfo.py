import csv

class stu():
    def __init__(self,stuinfo:dict):
        stu.name = stuinfo['姓名']
        stu.國文 = int(stuinfo['國文'])
        stu.英文 = int(stuinfo['英文'])
        stu.數學 = int(stuinfo['數學'])
        stu.自然 = int(stuinfo['自然'])
        stu.社會 = int(stuinfo['社會'])
        stu.總和 = stu.國文 + stu.英文 + stu.數學 + stu.自然 + stu.社會
        stu.平均 = stu.總和 / 5
    def __repr__(self) -> str:
        print(f"{i.name}的資料")
    def show_info(self):
        print(f"姓名 : {i.name}")
        print(f"國文 : {i.國文}")
        print(f"英文 : {i.英文}")
        print(f"數學 : {i.數學}")
        print(f"自然 : {i.自然}")
        print(f"社會 : {i.社會}")
        print(f"總和 : {i.總和}")
        print(f"平均 : {i.平均}")

with open("OpenFile/stuscore.csv",newline="",encoding="utf-8") as import_file:
    students = list(csv.DictReader(import_file))
    stu_list = []
    for i in range(len(students)):
        stu_list.append(stu(students[i]))
    for i in stu_list:
        print("=============")
        i.show_info()