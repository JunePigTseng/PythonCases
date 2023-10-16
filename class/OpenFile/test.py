import csv

ch_max = ["name",0]
ma_max = ["name",0]
en_max = ["name",0]
si_max = ["name",0]
so_max = ["name",0]

with open("OpenFile/stuscore.csv",newline="",encoding="utf-8") as file:
    csvfile = csv.DictReader(file)
    students = list(csvfile)
    '''
    for i in csvfile:
        print(i)
        if int(i[1]) > ch_max[1]:
            ch_max[0] = i[0]
            ch_max[1] = int(i[1])
        if int(i[2]) > ma_max[1]:
            ma_max[0] = i[0]
            ma_max[1] = int(i[2])
        if int(i[3]) > en_max[1]:
            en_max[0] = i[0]
            en_max[1] = int(i[3])
        if int(i[4]) > si_max[1]:
            si_max[0] = i[0]
            si_max[1] = int(i[4])
        if int(i[5]) > so_max[1]:
            so_max[0] = i[0]
            so_max[1] = int(i[5])
    print(ch_max)
    print(ma_max)
    print(en_max)
    print(si_max)
    print(so_max)
    '''
    
    for stu in students:
        stu['國文'] = int(stu['國文'])
        stu['英文'] = int(stu['英文'])
        stu['數學'] = int(stu['數學'])
        stu['自然'] = int(stu['自然'])
        stu['社會'] = int(stu['社會'])
        stu['sum'] = stu['國文'] + stu['英文'] + stu['數學'] + stu['自然'] + stu['社會']
        print(stu)