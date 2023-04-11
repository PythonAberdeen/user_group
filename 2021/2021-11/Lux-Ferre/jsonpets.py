# Cats and Dogs

import sys
import json
from dataclasses import dataclass

@dataclass
class Animal:
    pass

@dataclass
class Pet(Animal):
    name: str

@dataclass
class Dog(Pet):
    breed: str
    leash_color: str

@dataclass
class Cat(Pet):
    pattern: str
    favorite_toy: str

@dataclass
class Hedgehog(Pet):
    breed: str
    favorite_food: str


def get_pets(raw: object) -> list[Cat | Dog | Hedgehog]:
    match raw:
        case [*raw_pets]:  # List of pets
            return [get_pet(raw_pet) for raw_pet in raw_pets]
        case {**raw_pet}:  # Maybe a single pet
            return [get_pet(raw_pet)]
        case _:
            raise TypeError(f"Neither a pet nor a list of pets: {raw}")


def get_pet(raw_pet: object) -> Cat | Dog | Hedgehog:
    match raw_pet:
        case {"type": "cat", "name": str(name), "pattern": str(pattern), "favorite_toy": str(toy)}:
            return Cat(name, pattern, toy)
        case {"type": "dog", "name": str(name), "breed": str(breed), "leash_color": str(leash)}:
            return Dog(name, breed, leash)
        case {"type": "hedgehog", "name": str(name), "breed": str(breed), "favorite_food": str(food)}:
            return Hedgehog(name, breed, food)
        case {"type": "cat" | "dog" | "hedgehog"}:
            raise TypeError(f"Malformed pet: {raw_pet}")
        case _:
            raise TypeError(f"Not a pet: {raw_pet}")


def main() -> None:
    raw = json.load(sys.stdin)
    for pet in get_pets(raw):
        print(pet)


if __name__ == "__main__":
    main()

# Example input:
#
# {"type": "dog", "name": "Sorry", "breed": "mutt", "leash_color": "black"},
# {"type": "cat", "name": "Catelyn", "pattern": "tuxedo", "favorite_toy": "laser pointer"},
# {"type": "hedgehog", "name": "Alfie", "breed": "African Pygmy", "favorite_food": "meal worms"},
# {"type": "dog", "name": "Benji", "breed": "wheaten terrier"},
# {"type": "horse", "name": "Lass", "breed": "clydesdale", "favorite_food": "sugar cubes"},
# ]
#
# Output:
#
# Dog(name='Sorry', breed='mutt', leash_color='black')
# Cat(name='Catelyn', pattern='tuxedo', favorite_toy='laser pointer')
# Hedgehog(name='Alfie', breed='African Pygmy', favorite_food='meal worms')
# TypeError: Malformed pet: {'type': 'dog', 'name': 'Benji', 'breed': 'wheaten terrier'}
# TypeError: Not a pet: {'type': 'horse', 'name': 'Lass', 'breed': 'clydesdale', 'favorite_food': 'sugar cubes'}
