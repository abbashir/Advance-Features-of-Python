# Decorators: Modify base function by don't Touch base function. Base function: Like Library function.
# Base function
def get_name(name):
    return name


def get_name_Decorators(func):
    def wrapper(name):
        return name.upper()

    return wrapper


my_name = get_name_Decorators(get_name)
print(my_name("Abdul Bashir"))
