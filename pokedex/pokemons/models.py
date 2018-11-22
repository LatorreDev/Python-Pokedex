import uuid

class Pokemon:
    def __init__(self,name, species, typeA, typeB, weight, height, abilities, description, uid=None):
        self.name = name
        self.species = species
        self.typeA = typeA
        self.typeB = typeB
        self.weight = weight
        self.height = height
        self.abilities = abilities
        self.description = description
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['name', 'species', 'typeA', 'typeB', 'weight', 'height', 'abilities', 'description', 'uid']
