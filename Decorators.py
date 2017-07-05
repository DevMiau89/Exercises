def people(func):
    def wrapper(names):
        for name in names:
            print(func(name))
    return wrapper

@people
def greetings(name):
    return "Hello {}".format(name)

print greetings(["Mary", "John", "DevBear85"])
