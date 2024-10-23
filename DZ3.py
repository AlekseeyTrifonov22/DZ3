x1 = int(input("Введите секунды: "))
f = int(input("1 - секунды\n2 - минуты\n3 - часы\n"))
if f == 1:
    print(86400 - x1)
elif f == 2:
    print((86400 - x1) / 60)
elif f == 3:
    print((86400 - x1) / 3600)