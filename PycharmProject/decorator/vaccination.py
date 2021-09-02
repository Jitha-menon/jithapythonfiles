def vaccination(func):
    def wrapper(a):
        if a>18:
            raise Exception('not allowed')
        else:
            return func(a)
    return wrapper

@vaccination
def age_limit(age):
    return ('eligible')

print(age_limit(9))