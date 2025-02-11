def change_birthday(func):
    def wrapper(*args):
        print("before func I'm a summber baby!")
        result = func (*args)
        return result
    return wrapper


@change_birthday
def introduce(month):
    print("Hi I'm a " +month+ " baby!")

introduce("Winter")