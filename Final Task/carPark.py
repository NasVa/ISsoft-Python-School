class Car:
    ''' '''
    def __repr__(self):
        return f'Type : {self.__class__.__name__}, Passability coefficient : {self.passability_coefficient}, Fuel consumption : {self.fuel_consumption}'

class CarFactory:
    ''' Cars factory. Create car of requested type.'''

    car_types = {}

    def get_car_types():
        str = ""
        for i in CarFactory.car_types:
            str += i + ", "
        str = str[:-2]
        return str


    def add_car_type(name, passability_coefficient, fuel_consumption):
        ''' Add a new type of car'''
        CarFactory.car_types[name] = type(name, (Car,), dict(passability_coefficient = passability_coefficient, fuel_consumption =  fuel_consumption))

    def create_car(car_type):
        return CarFactory.car_types[car_type]()

'''
CarFactory.add_car_type("MiddleCar", 2, 6)
CarFactory.add_car_type("BigCar", 4, 9)
CarFactory.add_car_type("SmallCar", 1, 3)
CarFactory.add_car_type("Bus", 5, 12)

audi = CarFactory.create_car("MiddleCar")
mers = CarFactory.create_car("MiddleCar")
'''