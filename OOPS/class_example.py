#Class is like a blueprint for different shirts consisting of methods and attributes
class Shirt:
    #self is like a dictionary which holds all your attributes and their values
    #Using self,you can access those attributes through out the class.
    
    #method
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    #method
    def change_price(self, new_price):
    
        self.price = new_price

    #method    
    def discount(self, discount):

        return self.price * (1 - discount)


#insantiating a shirt object
shirt_one=Shirt('red','S','long_sleeve',25)

#printing the price 
print(shirt_one.price)


#Change the price of shirt to 10
shirt_one.change_price(10)

print(shirt_one.price)

#discount method to print the price of the shirt with a 12% discount
print(shirt_one.discount(.12))

#instantiate another object:
shirt_two=Shirt('orange','L','short_sleeve',10)

#calculate the total cost of shirt_one and shirt_two
total=shirt_one.price + shirt_two.price


#use the shirt discount method to calculate the total cost if
# shirt_one has a discount of 14% and shirt_two has a discount
# of 6%

total_discount=shirt_one.discount(0.14) + shirt_two.discount(0.06)

