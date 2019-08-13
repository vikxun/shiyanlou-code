list_  = list_1 = list_2 = []
dict_ = {}
tuple_ = ()

def check(a,b):
    num1 = int(a)
    num2 = float(b)

    return num1,num2

for i in range(2):
    l = input("Enter: ")
    list_ = l.split(':')
    print(list_)
    a= list_[0]
    b =list_[1]
    print(check(a,b))
    tuple_ = check(a,b)
    list_2.append(tuple_)
    print(list_2)

dict_ = dict(list_2)
print(dict_)
for key,value in dict_.items():
    print("{} {}".format(key,value))