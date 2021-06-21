num = 0

while True:
    num+=1
    div = num
    c = 0
    while (div > 0):
        if ((num % div) == 0):
            c+=1
        div-=1
    if (c == 2):
        print(str((num*num)%24) + "\t\t\t\t" + str(num))
