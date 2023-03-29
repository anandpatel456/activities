# Complete the Exercises - Representing Abstraction Through Code 
# In programming, we deal with two kinds of elements: functions and data. 

# Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. 

# By the concept of abstraction create functions representing abstracting principles through function 

# Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function.
# Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
# Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
# Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
# Factor:  Calculate temperature that a person feels because of the wind (Python3)


#Problem 1
# Problem 1
a=int(input())
b=int(input())
def add(a,b):
    c=a+b
    return c
print("Addition:",add(a,b))
def subtract(a,b):
    c=a-b
    return c
print("Subtraction:",subtract(a,b))
def multiply(a,b):
    c=a*b
    return c
print("Multiplication:",multiply(a,b))
def divide(a,b):
    c=a/b
    return c
print("Division:",divide(a,b))
def power(a,b):
    c=a**b
    return c
print("Power:",power(a,b))
def remainder(a,b):
    c=a%b
    return c
print("Remainder:",remainder(a,b))
def floor_division(a,b):
    c=a+b
    return c
print("Floor division:",floor_division(a,b))

#Problem 2
# Problem 2
#Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
magnitude = float(input("Enter magnitude of Earthquake: "))
def Earthquake_Impact(magnitude):
    if magnitude<2:
        return "Micro Earthquake"
    elif 2<=magnitude<3:
        return "Very Minor Earthquake"
    elif 3<=magnitude<4:
        return "Minor Earthquake"
    elif 4<=magnitude<5:
        return "Light Earthquake"
    elif 5<=magnitude<6:
        return "Moderate Earthquake"
    elif 6<=magnitude<7:
        return "Strong Earthquake"
    elif 7<=magnitude<8:
        return "Major Earthquake"
    else:
        return "Great Earthquake"
print(Earthquake_Impact(magnitude))

#Problem 3

#Problem 3
#Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3)
a=float(input("Enter distance in Kilometers: "))
def km_miles(a):
    conversion=a/1.069
    return conversion
print(km_miles(a),"miles")
def km_meter(a):
    conversion=a*1000
    return conversion
print(km_meter(a),"meters")
b=float(input("Enter the weight of oil in Kilograms: "))
def kg_gram(b):
    conversion=b*1000
    return conversion
print(kg_gram(b),"grams")
def kg_litre(b):
    conversion=b*1.1364
    return conversion
print(kg_litre(b),"litres")

#Problem 4

T = float(input("Enter temperature in °C: "))
w = float(input("Enter wind speed in Km/h: "))

def P_F_T(T, w):
    output = 13.12 + 0.6215*T - 11.37*(w*0.16) + 0.3965*T*(w**0.16) 
    return round(output, 2)

print(P_F_T(T, w), "°C")
