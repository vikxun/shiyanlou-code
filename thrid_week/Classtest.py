#!/usr/bin/env python3

class UserData(object):
    def __init__(self, ID, Name):
        self._ID = ID
        self._name = Name

class NewUser(UserData):

    def __call__(self):
        print("{}'s id is {}".format(self._name, self._ID))


    @property
    def name(self):
        return self._name()

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value
        else:
            print('Error')




if __name__ == '__main__' :

    user = NewUser(101, 'Jack')
    user.name = 'Holland'
    user()
