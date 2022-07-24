class Car:
    def __init__(self, **kwargs):
        self.window = 4
        self.color = kwargs.get("color", "balck")


class Open_car(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.door = kwargs.get("door", "0")


my_car = Open_car(door="2")

print(my_car.door)
