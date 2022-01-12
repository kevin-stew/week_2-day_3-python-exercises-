from math import pi

def house_area():
    length = int(input("Enter the length of the house: "))
    width = int(input("Enter the width of the house: "))
    area = length * width 
    print("The area of your house is: " + str(area)) 

# print(house_area())

def circumference():
    radius = int(input("What is the radius of your circle? "))
    print("The circumference of your circle is: " + str(2*pi*radius))

# circumference()