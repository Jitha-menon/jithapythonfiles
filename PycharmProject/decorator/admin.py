def admin_req(func):
    def wrapper(a,b):
        if a!='admin':
            raise Exception('not allowed')
        else:
            return func(a,b)
    return wrapper

@admin_req
def change_pin(user,pin):
    mypin=pin
    return mypin

@admin_req
def delete_ac(user,acno):
    return str(acno)+'delete'

print(delete_ac('admin',1000))
