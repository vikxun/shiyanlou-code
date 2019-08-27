#!/usr/bin/env python3

class UserData(object):

    def __init__(self, ID, Name):
        self._ID = ID
        self._name = Name

    def __repr__(self):
        pass

class NewUser(UserData):

    group = 'shiyanlou-louplus' 

    @classmethod

    def get_group(cls):
        return cls.group

    @staticmethod

    def format_userdata(ID, Name):
        Id = ID
        name = Name

        str_ = "{}'s id is {}".format(Name, Id)
        return str_


if __name__ == '__main__' :
    
    print(NewUser.get_group())

    print(NewUser.format_userdata(109, 'Lucy'))
