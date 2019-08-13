#!/usr/bin/env python3
import sys
age = int(sys.argv[1])
if age>=0 and age<10 :
    print("you beloge to kids")
elif age>=10 and age<18 :
    print("you beloge to teenager")
elif age>=18 and age<30 :
    print("you beloge to adult")
elif age>=30 and age<60 :
    print("you beloge to older")
else :
    print("you beloge to oldest")
