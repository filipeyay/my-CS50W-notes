# Object-oriented programming -> is a programming paradigm based on the concept of "objects", which can contain data in the form of fields, also known as attributes, and codes, in the form of procedures, also known as methods

# To apply this with Python we can use Classes

# __init__ -> "magic method"


class Point:
    # all functions that operate on objects themselves receive the first argument 'self'
    def __init__(self, input1, input2):  # <- when i create the class that should happen

        # the values (input1, input 2) are been stored in the Class itself, inside the property
        self.x = input1
        self.y = input2


r = Point(2, 5)

# now it's possible to access the values x and y in a easy way thanks to the Class
print(r.x)
print(r.y)

# EXERCISE: An airline is making a passenger list and cannot allow more passengers than the plane can hold.


class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passagers = []

    def add_passagers(self, name):
        if not self.seats_avaible():
            return False
        self.passagers.append(name)
        return True

    def seats_avaible(self):
        return self.capacity - len(self.passagers)


flight = Flight(3)

people = ["Sam", "Frodo", "Bilbo", "Gollum"]

for person in people:
    if flight.add_passagers(person):
        print(f"Added {person} in the flight.")
    else:
        print(f"No seats avaible for {person}.")
