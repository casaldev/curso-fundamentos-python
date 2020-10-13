class Engine:
    def start(self):
        pass

    def stop(self):
        pass

class ElectricEngine(Engine):               # É um motor
    pass


class V8Engine(Engine):                     # É um motor
    pass


class Car:
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()     # Tem um motor

    def start(self):
        print(
            f'Starting engine {self.engine.__class__.__name__} for car {self.__class__.__name__}...')
        self.engine.start()

    def stop(self):
        self.engine.stop()

        
class RaceCar(Car):                         # É um carro de corrida
    engine_cls = V8Engine

    
class CityCar(Car):                         # É um carro
    engine_cls = ElectricEngine

    
class F1Car(RaceCar):                       # É um carro de corrida e também é um carro
    pass                                    # engine_cls a mesma coisa que a mãe


car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()
