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

########### 2 ################

def find_min(mass):
   elem_min = mass[0]
   for elem in mass:
       if elem < elem_min:
           elem_min = elem
   return elem_min
mass = [int(s) for s in input().split()]
print(find_min(mass))

################# 3 #################

def count_primes(lst):
    def is_prime(n):
    if n < 2:
return False
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
    return False
return True

############ 4 ############

def delete_number(list, number):
   count = 0
   for i in list:
       if i == number:
           list.remove(i)
           count += 1
   return count

############# 5 #############

def combine_lists(list1, list2):
    combined = list1 + list2
    return combined
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = combine_lists(list1, list2)
print(combined_list)

############## 6 ############

def power_list(lst, power):
 result = []
 for x in lst:
   result.append(x**power)
 return result
nums = [1, 2, 3, 4]
powered = power_list(nums, 3)
print(powered)

###