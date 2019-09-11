#!/usr/bin/env python3

class Animal(object):
    
    __slots__ = ('name', 'age')

class Cat(Animal):

    __slots__ = ('address')


dog = Animal()

print(callable(Animal))
print(callable(dog))

dog.name = 'wangcai'

dog.age = 2

cat = Cat()

cat.name = 'Kitty'

print(cat.name)

#dog.gender = 'male'

#cat.gender 'male'


