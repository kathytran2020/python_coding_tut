favorite_animals = ["pomeranian", "rabbit", "cat", "shiba inu"]
favorite_animals.append("turtles")
favorite_animals.insert(1, "turtles+pompoms")
# for animal in favorite_animals:
#     #print(f"I love {animal}")
#     print(animal)
person = {"name": "Kat", "age": 23, "school": "UCSB"}
print(person["name"])
person["favorite_animals"] = favorite_animals
for key, value in person.items():
    if key == "favorite_animals":
        for animal in value:
            print(f"I love {animal}")
    else: 
        print(f"{key} is {value}")