rivers = {'nile': 'egypt', 'sepik river': 'papua', 'volga': 'russia'}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())

print("\n")

for river in rivers.keys():
    print(river.title())

print("\n")

for country in rivers.values():
    print(country.title())

    
