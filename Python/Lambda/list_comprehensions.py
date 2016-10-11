#!/usr/local/bin/python3

f = lambda x: x*x
print([f(x) for x in range(10)])
print([lambda x: x*x for x in range(10)])
print([lambda x: (x*x for x in range(10))])
print([(lambda x: x*x) (x) for x in range(10)])
