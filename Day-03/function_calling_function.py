def hello ():
    print("Hello")
def world():
    hello()
    print("World")

world()    

#Bill calculation
def calculation_total(price, quantity):
    return price * quantity
def print_bill():
    print("Total_Bill : " ,  calculation_total(100 , 5))
print_bill()
