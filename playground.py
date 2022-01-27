#Code used to Demo the power of Unlimited Positional Arguments. Can be used to enter any number of
#arguments for a function and they will be used.

#Code below is used to iterate through the args given by the user and then done upon


def add(*args):
    for _ in args:
        total = sum(args)
    print(total)


add(2, 6, 18, 400)


#Demo kwargs

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


#can also be used in Methods

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Saab", model="9-3", color="Blue")
print(my_car.make, my_car.model, my_car.color)