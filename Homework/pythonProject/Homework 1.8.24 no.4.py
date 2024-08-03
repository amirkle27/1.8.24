fruits: list = ["Mango","Orange","Banana","Apple","Strawberry","Pineapple","Grapes","Watermelon"]

#a#
print(" a ".center(30, "-"))
print()

print("Switching the order of letters:", list(map(lambda fruit: fruit [::-1], fruits)))

#b#
print(" b ".center(30, "-"))
print()

print("Fruit's first letter:", list(map(lambda fruit: fruit [0], fruits)))

#c#
print(" c ".center(30, "-"))
print()

print("In capital letters:", list(map(lambda fruit: fruit.upper(), fruits)))

#d#
print(" d ".center(30, "-"))
print()

print("Length of fruit words:", list(map(lambda fruit: len(fruit), fruits)))

#e#
print(" e ".center(30, "-"))
print()

print("Adding '!' for fruits that end with 's':", list(map(lambda fruit: fruit+"!" if fruit [-1] == "s" else fruit, fruits)))

#f#
print(" f ".center(30, "-"))
print()

fruits_with_cal: list = [
                        ["Apple", 52],
                        ["Banana", 89],
                        ["Orange", 47],
                        ["Mango", 60],
                        ["Strawberry", 32],
                        ["Pineapple", 50],
                        ["Grapes", 69],
                        ["Watermelon", 30]
                        ]
#f.a#

print("Only the calories:", list(map(lambda calories: calories[1], fruits_with_cal)))

#f.b#

print("fruits and calories combined:", list(map(lambda F_and_C: (F_and_C [0] + str(F_and_C[1])), fruits_with_cal)))

#f.c#

print("Adding '!' above 50 calories:", list(map(lambda fruits: fruits[0]+"!" if fruits[1]>50 else fruits, fruits_with_cal)))


