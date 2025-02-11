# Simple decorator
def my_decorator(func):

    def  wrapper():
        print('Перед выполнением функции')
        func()
        print('После выполнения функции')

    return wrapper

@my_decorator
def hello():
    print('Привет мир!!')

hello()


# Decorator with argument
def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper
    return decorator

@repeat(3)
def greet():
    print('HI')

greet()

# Class decorator

def class_decorator(cls):

    class NewClass(cls):

        def new_method(self):
            return print("New method")

    return NewClass

@class_decorator
class MyClass:

    def old_method(self):
        return print ("Old method")

example = MyClass()

example.old_method()
example.new_method()