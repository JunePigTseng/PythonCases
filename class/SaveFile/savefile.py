import random
import csv

def GetNames(num:int)->list[str]:
    with open("SaveFile/names.txt",encoding="utf-8") as file:
        names = []
        for name in file:
            names.append(name.rstrip())
    return random.choices(names,k=num)
def GenerateStudent():
    return [random.randint(0,100) for i in range(5)]
def SaveCsvFile(file:str,data:list)->bool:
    try:
        with open(file,"w",newline="",encoding="utf-8") as infile:
            csvfile = csv.writer(infile)
            csvfile.writerow(["姓名","國文","英文","數學","自然","社會"])
            csvfile.writerows(students)
    except:
        return False
    else:
        return True

num = int(input())
names = GetNames(num)
students = []
for i in range(num):
    score = GenerateStudent()
    score.insert(0,names[i])
    students.append(score)

if SaveCsvFile("SaveFile/stuscore.csv",students):
    print("成功")
else:
    print("失敗")