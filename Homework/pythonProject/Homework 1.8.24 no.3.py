import random
ran_num: list = [(random.randint (-50,50)) for _ in range (20)]

#a#
print(" a ".center(30, "-"))
print()

print(f"The original list was: {ran_num}")
print("Power 3 numbers:", list (map(lambda numbers: numbers ** 3, ran_num)))

#b#
print(" b ".center(30, "-"))
print()

print(f"The original list was:{ran_num}")
print("Only Unities:", list (map(lambda numbers: numbers % 10, ran_num)))

#c#
print(" c ".center(30, "-"))
print()

print(f"The original list was: {ran_num}")
print("Converted to Fahrenheit:", list(map(lambda numbers: round(numbers * 9/5 + 32, 2), ran_num )))

#d#
print(" d ".center(30, "-"))
print()

print(f"The original list was: {ran_num}")
print("'Positive' for positive, Negative for negative:", list(map(lambda numbers: "Positive" if numbers > 0 else "Negative" if numbers<0 else "Zero!", ran_num)))

#e#
print(" e ".center(30, "-"))
print()

max_val = max(ran_num)
min_val = min(ran_num)
print(f"The original list was: {ran_num}")
print("Replace the biggest with 'Max' and the smallest with 'Min':", list(map(lambda numbers: "Max" if numbers == max_val else "Min" if numbers == min_val else numbers, ran_num)))

#f#
print(" f ".center(30, "-"))
print()


print(f"The original list was: {ran_num}")
print("Switching the order of digits", list(map(lambda numbers: str(numbers)[::-1], ran_num)))

#g#
print(" g ".center(30, "-"))
print()

print(f"The original list was: {ran_num}")
print("Every number as absolute:", list(map(lambda numbers: abs(numbers), ran_num)))

#h#
print(" h ".center(30, "-"))
print()

income_expanses: list = [
                        [10000, 7000],
                        [300, 5000],
                        [2000, 8000],
                        [11000, 12500],
                        [14320, 9850]
                        ]

print("Balance for monthly expenses:", list(map(lambda balance: balance[0]-balance[1],income_expanses)))

