
def change_major(func):
    def wrapper(*args):
        print("before func I'm a nursing student!")
        result = func (*args)
        return result
    return wrapper


@change_major
def introduce(major):
    print("Hi I'm a " +major+ " student!")

introduce("Comp Sci")