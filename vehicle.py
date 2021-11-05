## Program Assessement

# Class Vehicle


class Vehicle:
    def __init__(self, fare):
        self.fare = fare

# Part A create two instances of Vehicle,
 
class bus(Vehicle):
    def __init__(self, fare, number_of_passengers):
        self.fare = fare
        self.number_of_passengers = number_of_passengers
        
class car(Vehicle):
    def __init__(self, fare, number_of_passengers):
        self.fare = fare
        self.number_of_passengers = number_of_passengers
class total:
    def __add__(car, bus):
        return car.fare + bus.fare
class greaterthan:
    def __gt__(self, bus, car):
        return bus.fare > car.fare

class lowerthan:
    def __lt__(self, bus, car):
        return bus.fare < car.fare  

    


# Input fares

if __name__ == '__main__':
    def main():
        
        supermetro = Vehicle(1)
        nissan = Vehicle(1)
        
        fare  = float(input("Enter the fare: "))
        number_of_passengers = int(input("Enter the number of passengers: "))
        supermetro = bus(fare, number_of_passengers)
        
        print("The fare is: ", supermetro.fare)
        print("The number of passengers is: ", supermetro.number_of_passengers) 
        print("The total fare is: ", total(nissan, supermetro))



       
    
    