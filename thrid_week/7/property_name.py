#!/usr/bin/env python3

class UserData(object):
    def __init__(self, ID, Name):
        self._id = ID
        self._name = Name

class NewUser(UserData):

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, value):
        if len(value) > 3 :
            self._name = value
        else:
            print('Error')







if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.name = 'Luo'
    user1.name = 'Jackie'
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)




