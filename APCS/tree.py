class nood():
    mom = None
    son = []
    def __init__(self,d = None):
        date = d


nood_num = int(input())
nood_list = [nood(i) for i in range(nood_num)]

for i in range(nood_num):
    inp = input().split()
    for j in range(1,len(inp)):
        nood_list[i].son.append(inp[j]) #子節點設定
        nood_list[j].mom = i
