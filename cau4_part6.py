class Vehicle:
    def __init__(self, brand, model, year):
        
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
      
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
       
        Vehicle.__init__(self, brand, model, year)
        
        self.num_doors = num_doors

    def display_info(self):

        Vehicle.display_info(self) 
        print("Number of doors:", self.num_doors)

class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
       
        Vehicle.__init__(self, brand, model, year)
        
        self.bike_type = bike_type

    def display_info(self):
        
        Vehicle.display_info(self) 
        print("Type:", self.bike_type)


car = Car("Toyota", "Camry", 2022, 4)
bike = Bike("Giant", "Defy", 2021, "Road")


print("Car info:")
car.display_info()
print("\nBike info:")
bike.display_info()