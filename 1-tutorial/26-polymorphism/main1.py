class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # polymorphism
    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # polymorphism
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")  # create a Car class
boat1 = Boat("Ibiza", "Touring 20")  # create a Boat class
plane1 = Plane("Boeing", "747")  # create a Plane class

for x in (car1, boat1, plane1):
    x.move()
