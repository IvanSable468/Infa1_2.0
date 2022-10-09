a = input()
b = input()
c = []
for i in a:
    for j in b:
        if i == "" or j == "":
            continue
        if i == j:
            c.append(i)
print(c)