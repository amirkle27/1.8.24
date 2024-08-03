games: list = ["V Auto Theft Grand","Fortnite",
"The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]

#a#
print(" a ".center(30, "-"))
print()

print("Bigger than 8 letters:",list(filter(lambda name: len(name) > 8, games)))

#b#
print(" b ".center(30, "-"))
print()

print("Name starts with 'F':", list(filter(lambda games: games [0] == "F", games)))

#c#
print(" c ".center(30, "-"))
print()

print("Games with only two words in their name:", list (filter(lambda games: games.count(" ") == 1, games)))

#d#
print(" d ".center(30, "-"))
print()

print("Name starts with 'V':", list (filter(lambda games: games.startswith ("V"), games)))

#e#
print(" e ".center(30, "-"))
print()

print("Has special character:", list(filter(lambda game: any(char in "!%&$:" for char in game), games)))

#f#
print(" f ".center(30, "-"))
print()


games_with_years = [
    ["Fortnite", 2017],
    ["Grand Theft Auto V", 2013],
    ["The Elder Scrolls V: Skyrim", 2011],
    ["Dark Souls", 2011],
    ["Overwatch", 2016]
]


print("Games made after 2014:", list(filter(lambda game: game[1] > 2014, games_with_years)))
