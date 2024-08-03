cities: list = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

#a#
print(" a ".center(30, "-"))
print()

print("Cities sorted by length", sorted(cities,key= lambda city: len(city)))

#b#
print(" b ".center(30, "-"))
print()

print("City's last letter", sorted(cities, key= lambda city: city[-1]))

#c#
print(" c ".center(30, "-"))
print()

print(f"Cities after switching order of letters:", list(map(lambda city: city [::-1], cities)))
print("Sorting after letters switch", sorted(cities, key= lambda city: city [::-1]))

#d#
print(" d ".center(30, "-"))
print()

more_details: list = [
                     ["Tokyo", 5760, "Asia"],
                     ["New York", 5690, "North America"],
                     ["Paris", 2050,"Europe"],
                     ["London", 2240, "Europe"],
                     ["Sydney", 8780, "Australia"],
                     ["Dubai", 1300, "Asia"],
                     ["Shanghai", 4920, "Asia"]
                     ]

#d.a#

print("Sorted by distance from Israel:", sorted(more_details, key= lambda city: city[1]))

#d.b#

print("Sorted by distance Big to Small:", sorted(more_details, key=lambda city: city[1])[::-1])

#d.c#

print("Sorted by Continent:", sorted(more_details, key= lambda city: city[2] ))

#d.d#

print("Sorted by Continent and Distance", sorted(more_details, key= lambda city: (city[2],city[1])))




