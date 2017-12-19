#lOUIS
#Dec 12th 2017
import math


def cheese():
    '''Makes a screen full of I LIKE CHEESE'''
    print("I LIKE CHEESE!" * 100)

def temp_C(temp_F):
    '''convert a temperture in Fahrenhiet to Celsius'''
    answer = (temp_F - 32) * (5/9)
    return answer

def volume_sphere(radius):
    """Calculate volume of sphere radius is an interger or float"""
    volume = (3/4)*math.pi *r**3
    print ("calculating")
    return volume

def top_hat(your_height_cm):
    '''Calculate height with top hats'''
    hat_height = 20 # in cm
    height = input("What is your height in centimeters")
    height = top_hat + your_height
    return height
cheese()

x = input("Please enter a temperature in Fahrenheit: ")
x = float(x)
t_in_C = temp_C(x)
print("That temperture is in Celsius is",t_in_C)


r = input ("Please enter a radius of a sphere: ")
r = float (r)
v_sphere = volume_sphere(r)
print("The volume of the sphere is", v_sphere)


print ("This is your hieght in top hats",height)




