from abc import ABC, abstractmethod

# Абстрактний базовий клас
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

# Клас для авто
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

# Клас для мото
class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

# Абстрактна фабрика для створення транспортних засобів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass
    
    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} (US Spec)", model)

# Фабрика для ЄС
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} (EU Spec)", model)

# Використання фабрик для створення транспортних засобів

# Створення фабрик
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Створення транспортних засобів для США
vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

# Створення транспортних засобів для ЄС
vehicle3 = eu_factory.create_car("Volkswagen", "Golf")
vehicle3.start_engine()

vehicle4 = eu_factory.create_motorcycle("BMW", "Ducatti")
vehicle4.start_engine()