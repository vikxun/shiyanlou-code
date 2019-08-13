#!/usr/bin/env python3


end = 100
i = 1
result = 3

def compute():
    #global result, i, end
    result = 0
    i = 1
    while i <= end:
        result += i
        i += 1
        print(result)

if __name__ == '__main__':

    compute()
