

s_l = ()
dict_ = {}
l=[]
for i in range(2):
    list_ = input("enter number:")

    s_l =tuple(list_.split(':'))

#s_l = dict([list_.split(',')])
    print(s_l)

    l.append(s_l)

    print (l)

dict_ = dict(l)

print(dict_)