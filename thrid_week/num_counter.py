#!/usr/bin/env python3


class Counter(object):
    def __init__(self, func ):
        self.func = func 

        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, *kwargs)


@Counter

def num_counter():
    pass

for i in range(20):
    num_counter()

print(num_counter.count)

