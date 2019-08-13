x = 0
while x < 100:
    x += 1
    if x % 7==0 :
        continue
    elif x % 10 == 7:
        continue
    elif x // 10 == 7:
        continue
    else:
        print(x)
