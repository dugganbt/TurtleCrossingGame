from car import Car

MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = 0.1

    def move_all_cars(self):
        for car in self.cars:
            car.move_car(MOVE_INCREMENT)

    def new_car(self):
        self.cars.append(Car())

    def increase_car_speed(self):
        self.car_speed *= 10
        print(self.car_speed)

