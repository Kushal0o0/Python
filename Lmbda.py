def cube(y):
    return y * y * y


print(cube(5))

cubel = lambda y: y * y * y
print(cubel(5))


###################################################################################################################

def square(x):
    if x > 0:
        return x * x


print(square(5))

square = lambda x: x * x if x > 0 else "none"
print(square(5))
