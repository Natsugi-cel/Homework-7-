print("Hello world")

######### 1 #########
# v1
def bigmult(*numbers):
    n = 1
    for i in numbers:
        n *= i
    return n

print(bigmult(1, 2, 3))

# v2
def multiply_elements(lst):
    result = 1
for element in lst:
    result *= element
    return result

############ 2 ################

