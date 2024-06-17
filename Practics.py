class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


b1 = Building(15, 'Многоэтажный дом')
b2 = Building(2, 'Частный дом')
b3 = Building(2, 'Частный дом')

print(b1 == b2)
print(b2 == b3)
