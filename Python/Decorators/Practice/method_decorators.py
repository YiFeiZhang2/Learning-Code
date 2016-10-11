# * and ** is the important syntax. args and kwargs by convention
# * is for unknown number of arguments  ex def func(*args) -> func(1, 2, 3...)
# ** is for previously undefined arguments ex def func(x = "hi", y = "ho")
# * and ** can be used with values too, but arguments before *, * before **
# can also use * and ** when calling a function

def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print my_person.get_fullname()