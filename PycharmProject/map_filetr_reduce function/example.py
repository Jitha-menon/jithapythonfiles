lst=[2,3,4,5,6]

squares=list(map(lambda num:num**2,lst))
print(squares)

cubes=list(map(lambda num:num**3,lst))
print(cubes)

#filter

even=list(filter(lambda num:num%2==0,lst))
print(even)

odd=list(filter(lambda num:num%2!=0,lst))
print(odd)
