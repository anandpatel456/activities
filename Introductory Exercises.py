
# Complete the Following Exercises.
# You are free to use any IDE.

# Steps Involved:
# 1. Understand a Problem (Make it clear through Instructor)

# 2. Understand Inputs

# 3. Understand Output 

# 4.Understand the Constraints

# 5.Code 

# 6. Validate  

 

# Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
# Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
# Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
# Factor:  Calculate temperature that a person feels because of the wind (Python3)
# Note: Naming Convention Files: Crate files based on the purpose of the exercise eg: If calculating factor then use factor.py  


#problem 1
x=input("Which Arithetic operation you want to get? ")
y=int(input("Enter no. 1 "))
z=int(input("Enter no. 2 "))
if x=="add" or x=="Add" or x=="ADD" or x=="plus" or x=="Plus" :
    print(y+z)
elif x=="subtract" or x=="Subtract" or x=="SUBTRACT" or x=="minus" or x=="Minus":
    print(y-z)   
elif x=="multiply" or x=="Multiply" or x=="MULTIPLY" or x=="Multiplication" or x=="multiplication":
    print(y*z)
elif x=="divide" or x=="Divide" or x=="DIVIDE" or x=="Division" or x=="division":
    print(y/z)
elif x=="power" or x=="Power" or x=="POWER":
    print(y**z)
elif x=="floor division" or x=="Floor Division" or x=="Floor division" or x=="FLOOR DIVISION":
    print(y//z)
elif x=="remainder" or x=="Remainder" or x=="REMAINDER":
    print(y%z)
else:
    print("Invalid Operation")


#Problem 2
A=float(input("Enter distance in Kilometers: "))
B=A/1.069
print(B,"miles")
C=A*1000
print(C,"meters")
D=float(input("Enter the weight of oil in Kilograms: "))
E=D*1000
print(E,"grams")
F=D*1.1364
print(F,"litres")

#Problem 3

#Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
erth= float(input("Enter magnitude of Earthquake: "))

if erth<2:
    print("Micro Earthquake")
elif 2<=erth<3:
    print("Very Minor Earthquake")
elif 3<=erth<4:
    print("Minor Earthquake")
elif 4<=erth<5:
    print("Light Earthquake")
elif 5<=erth<6:
    print("Moderate Earthquake")
elif 6<=erth<7:
    print("Strong Earthquake")
elif 7<=erth<8:
    print("Major Earthquake")
else:
    print("Great Earthquake")


 #Problem 4
 
T = float(input("Enter temperature in °C: "))
w = float(input("Enter wind speed in km/h: "))

output = 13.12 + 0.6215 * T - 11.37 * (w**0.16) + 0.3965 * T * (w**0.16)
print("wind chill temperature is:", round(output, 2), "°C")

