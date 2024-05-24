class Car:
    def __init__ ( self , manufacturer, model, hp): # __init__ function in class constructor,every class we use constructor,we also use some parameter,
        self .manufacturer = manufacturer #for example self function,in our langueage self function save all atributes: manufacturer, model, h!
        self .model = model
        self .hp = hp


class Car:
    def __init__ ( self , manufacturer, model, hp):
        self .manufacturer = manufacturer  #  we use again self function and self fucntion save all atributes
        self .model = model
        self .hp = hp
    def print_info(self): # we create one more fucntion and giving to argument self = (manufacturer, model, hp) and we print every arguments value with .format function
        print ( "Manufacturer: {}, Model: {}, HP; {}"
            .format( self .manufacturer,
                self .model, 
                self .hp)) 
        

class Car:
    amount_cars = 0

    def __init__ ( self , manufacturer, model, hp):# as you can see we use variable named amount_cars,it will be increace by 1 if we use one more car object
        self .manufacturer = manufacturer
        self .model = model
        self .hp = hp
        Car.amount_cars += 1
    def print_car_amount( self ):
        print ( "Amount: {}"
            .format(Car.amount_cars)) 

Car("Tesla","Model X", "1200") # like i told we use 2 car object and resulte was 2, because every cars object amount_cars increased by 1 so result is 2
Car("Tesla","Model X", "1200")
print(Car.amount_cars)
        

