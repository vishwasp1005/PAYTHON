from functools import reduce

#Walrus

if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

#type defination

n: int = 5

def greet(name: str) -> str:
    return f"Hi {name}"

print(greet("Het"))

#lambda

mult = lambda x,y: x*y

print(mult(2,4))

#enumarator

l = [1,3,6,2,4,9]

# index = 0
# for item in l:
#     print(f"{item} at index {index}")
#     index+=1

for index,item in enumerate(l):
    print(f"{item} at index {index}")


# join Method

l = ["het","bhai","ho"]

final = '-'.join(l)
print(final)

#map

l = [1,2,3,4,5,6]

squre = lambda x: x*x
sqlist = map(squre, l)
print(list(sqlist))

#filter

def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

#reduce

l = [1, 2, 3, 4, 5, 6]
sum = lambda x, y: x + y
print(reduce(sum, l))