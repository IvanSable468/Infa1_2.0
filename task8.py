int_list = []
for element in input().split():
    int_list.append(int(element))

for x in int_list:
    if x == 237:
        break
    elif x % 2 == 0:
        print(x)