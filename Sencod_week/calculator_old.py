#!/usr/bin.python3

#print user rate_pay

import sys

try:
    pay = int(sys.argv[1])


except ValueError:
    print("Parameter Error")


rate_pay = pay -5000
if rate_pay < 3000:
    rate_pay = rate_pay * 0.03 - 0
    print('{:.2f}'.format(rate_pay))
elif rate_pay >= 3000 and rate_pay < 12000 :
    rate_pay = rate_pay * 0.10 - 210
    print('{:.2f}'.format(rate_pay))
elif rate_pay >= 12000 and rate_pay < 25000 :
    rate_pay = rate_pay * 0.20 - 1410
    print('{:.2f}'.format(rate_pay))
elif rate_pay >= 25000 and rate_pay < 35000 :
    rate_pay = rate_pay * 0.25 - 2660
    print('{:.2f}'.format(rate_pay))
elif rate_pay >= 35000 and rate_pay < 55000 :
     rate_pay = rate_pay * 0.30 - 4410
     print('{:.2f}'.format(rate_pay))
elif rate_pay >= 55000 and rate_pay < 88000 :
    rate_pay = rate_pay * 0.35 - 7160
    print('{:.2f}'.format(rate_pay))
else:
    rate_pay = rate_pay * 0.45 - 15160
    print({".2f"}.format(rate_pay))