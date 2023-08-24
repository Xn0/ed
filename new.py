import re
import functools

def validate_names(func):
    """
    Validates that names doesn't contain any off those symbols:
    @#$%^&*();:"§[]{}~_+=\\/?!><±0123456789
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = args[2]
        names_attrs = ['first_name', 'last_name']
        forbidden_chars = '@#$%^&*();:"§[]{}~_+=\\/?!><±0123456789'
        pattern = r'[' + re.escape(forbidden_chars) + r']'
        if args[1] in names_attrs and re.search(pattern, value):
            value = ''
        return func(args[0], args[1], value, **kwargs)
    return wrapper

class Names:
    @validate_names
    def __setattr__(self, key, value):
        self.__dict__[key] = value


if __name__ == '__main__':
    names = Names()
    names.first_name = 'John'
    names.last_name = 'Doe'
    names.data = 'data'
    print(names.first_name, names.last_name, names.data)
    names.first_name = 'John1'
    names.last_name = 'Doe1'
    names.data = 'data1'
    print(names.first_name, names.last_name, names.data)
    names = Names()
    names.first_name = 'John'
    names.last_name = 'Doe'
    names.data = 'data'
    print(names.first_name, names.last_name, names.data)
    names.first_name = 'John1'
    names.last_name = 'Doe1'
    names.data = 'data1'
    print(names.first_name, names.last_name, names.data)