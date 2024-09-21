from abc import ABC , abstractmethod


class Carbase(ABC) :
    @abstractmethod
    def detail (self):
        pass

    @abstractmethod
    def price (self):
        pass

class Detailbase(ABC) :
    @abstractmethod
    def show (self):
        pass


class Car_detail (Detailbase) :
    def __init__(self , car):
        self.car = car

    def show (self):
        return f"Car name : {self.car.name} \t Car model : {self.car.model}"
    

class Car_price(Detailbase) :
    def __init__(self , car):
        self.car = car
    
    def show(self):
        return f"car price : {self.car._price}"


class Car (Carbase) :
    def __init__(self , name , model , price):
        self.name = name
        self.model = model
        self._price = price

    @property
    def detail (self):
        return Car_detail(self)
    
    @property
    def price (self):
        return Car_price(self)
    
    def show (self):
        pass


if __name__ == "__main__" :
    car1 = Car("benz" , 2014 , 12000000)
    car2 = Car("bmw" , 2014 , 12000000)
    car3 = Car("bmw coupe" , 2014 , 12000000)
    car4 = Car("benz cls" , 2014 , 12000000)

    products = [car1 , car2 , car3 , car4]

    for product in products :
        print(product.detail.show())
        print(product.price.show())
