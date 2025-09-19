# What's happening here?

dog = {
    "dogName": "Spot",
    "dogBreed": "Jack Russell",
    "dogAge": 4,
    "coatColour": ["Brown", "White"],
    "barkType": "Yap",
    "dogBark": lambda: f"{dog['barkType']} {dog['barkType']} !" 
}

print(dog["dogBark"]())
