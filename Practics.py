class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


my_house = House(14)
print(my_house.numberOfFloors)
my_house.setNewNumberOfFloors(5)
print(my_house.numberOfFloors)
