import random
rand_num: list = [random.randint(1, 100) for _ in range (50)]
print(rand_num)

#a#
print(" a ".center(30, "-"))
print()

print("More Than 50:",list(filter(lambda numbers: numbers> 50, rand_num)))

#b#
print(" b ".center(30, "-"))
print()

print("Numbers % 7 == x:",list(filter(lambda numbers: numbers % 7 == 0, rand_num)))

#c#
print(" c ".center(30, "-"))
print()

print("Has 2 Digits:",list(filter(lambda numbers: 100> numbers >10, rand_num)))

#d#
print(" d ".center(30, "-"))
print()

print("Has 2 Digits and same Unities and Dozens: ",list(filter(lambda numbers:  100> numbers >10 and numbers // 10 == numbers % 10, rand_num)))

#e#
print(" e ".center(30, "-"))
print()

print("Digits sum is 9:", list(filter(lambda numbers: 100 > numbers >9 and numbers// 10 + numbers % 10 == 9, rand_num)))

#f#
print(" f ".center(30, "-"))
print()

import statistics
print(f"The average in our list is: {statistics.mean(rand_num)}")
print("Numbers bigger than the average:", list(filter(lambda numbers: numbers > statistics.mean(rand_num), rand_num)))

#g#
print(" g ".center(30, "-"))
print()

print(f"The biggest number in our list is {max(rand_num)}, half of it is {max(rand_num)/2}, of course")
print("Bigger than half of the Biggest Number:", list(filter(lambda numbers: numbers > max(rand_num)/2, rand_num)))

#h#
print(" h ".center(30, "-"))
print()

import statistics
print(f"The median in our list is: {statistics.median(rand_num)}")
print("Numbers bigger than the median:", list(filter(lambda numbers: numbers > statistics.median(rand_num), rand_num)))

#i#
print(" i ".center(30, "-"))
print()

nums: list = []
for i in range (5):
    num: int = int(input ("Please enter a number"))
    if num not in rand_num:
        nums.append(num)
        rand_num.append(num)
print(f"The new list is: {rand_num}. \nThe new numbers in the list are: {nums}")

#j#
print(" j ".center(30, "-"))
print()

def is_prime (num: int = 2) -> bool:
    """Gets a number from the user and returns True for prime, False for non-prime"""

    num: int = int(input("Please enter a number"))
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

is_prime_lambda = lambda x: is_prime(x)

print("Number is Prime:", is_prime_lambda(5))
