import json
from random import randint
def addPetPayload(petName,status):
    pet={}
    petID = randint(100, 999)
    category = {
            "id": 1,
            "name": "Dogs"
        }
    tags = [
        {
            "id": 0,
            "name": "string"
        }
    ]
    pet = {
        "id": petID,
        "name": petName,
        "category": category,
        "tags" : tags,
        "status": status
    }
    return pet, petID