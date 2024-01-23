print("Hello world")

######### 1 #########
# # v1
# def bigmult(*numbers):
#     n = 1
#     for i in numbers:
#         n *= i
#     return n
#
# print(bigmult(1, 2, 3))
#
# # v2
# def multiply_elements(lst):
#     result = 1
# for element in lst:
#     result *= element
#     return result

############ 2 ################

def find_min(mass):
   elem_min = mass[0]
   for elem in mass:
       if elem < elem_min:
           elem_min = elem
   return elem_min
mass = [int(s) for s in input().split()]
print(find_min(mass))
