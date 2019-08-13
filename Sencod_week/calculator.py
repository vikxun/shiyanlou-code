#!/usr/bin/env python3

import sys

salary = ()
list_salary = []
list_ = []
dict_ = {}


def calculator_salary(id_, pay):

    if pay <= 5000:
        in_hand_salary =  pay - pay * 0.165
   
    else:
        should_pay = float(pay  - pay * 0.165 - 5000)

        if should_pay > 0 and should_pay <= 3000:
            should_pay = should_pay * 0.03
        elif should_pay > 3000 and should_pay <= 12000 :
            should_pay = should_pay * 0.10 - 210
        elif should_pay > 12000 and should_pay <=25000 :
            should_pay = should_pay * 0.20 - 1410
        elif should_pay > 25000 and should_pay <= 35000 :
            should_pay = should_pay * 0.25 - 2660
        elif should_pay > 35000 and should_pay <= 55000 :
            should_pay = should_pay * 0.30 - 4410
        elif should_pay > 55000 and should_pay <= 80000 :
            should_pay = should_pay * 0.35 - 7160 
        else:
            should_pay = should_pay * 0.45 - 15160
        
        in_hand_salary = (pay - pay * 0.165 - should_pay)

    return id_, in_hand_salary



for argv in sys.argv[1:] :
    list_ = argv.split(':')
    try:
        pay = int(list_[1])
               
    except ValueError:

        print("Parameter Error")


    fact_salary = calculator_salary(list_[0], pay)
    # income_dict[list_[0]]= pay

    list_salary.append(fact_salary)
 


dict_ = dict(list_salary)


for key,value in dict_.items():
    
    print('{}:{:.2f}'.format(key,value))
        
