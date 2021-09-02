dict={'name':'zara' , 'age':'3','class':'first'}
print(dict)
print(dict['name'])
print("dict['name']:",dict['name'])

dict['age']=8      #update existing entry
print(dict)

dict['location']='kochi'  #new entry updation
print(dict)

dict.update({'name':'jitha'})  #another method
print(dict)


#empty dictionary
d={}
print(d)
print(type(d))

del dict['name']       #removing one key
dict.clear             #clearing all entries
del dict               #deleting entire dictionary
print (dict)

a={1:'hello', 2:{4:6,8:9}}  #nesting possible
print (a)