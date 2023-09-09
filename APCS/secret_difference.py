#秘密差
inp = input()

a, b = 0, 0
for i in range(len(inp)):
    if i%2 == 0:
        a += int(inp[i])
    else:
        b += int(inp[i])

if a > b:
    print(a-b)
else:
    print(b-a)