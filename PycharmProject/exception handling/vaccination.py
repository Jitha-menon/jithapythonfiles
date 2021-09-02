print('Vaccination slots available')
age=int(input('age: '))
if age>80:
    raise Exception('age above 80 is not applicable')
else:
    print('you are applicable for next step')
