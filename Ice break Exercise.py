# <!-- Problem -I 
# The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
# spectrum is continuous, it is often divided into 6 colors as shown below:

# Violet 380 to less than 450
# Blue 450 to less than 495
# Green 495 to less than 570
# Yellow 570 to less than 590
# Orange 590 to less than 620
# Red 620 to 750

# Write a program that reads a wavelength from the user and reports its color. Display
# an appropriate error message if the wavelength entered by the user is outside of the
# visible spectrum.

 

# Problem -II
# Electromagnetic radiation can be classified into one of 7 categories according to its
# frequency, as shown in the table below:

# Radio Waves Less than 3 × 10^9
# Microwaves 3 × 10^9 to less than 3 × 10^12
# Infrared Light 3 × 10^12 to less than 4.3 × 10^14
# Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
# Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
# X-Rays 3 × 10^17 to less than 3 × 10^19
# Gamma Rays 3 × 10^19 or more

# Write a program that reads the frequency of some radiation from the user and
# displays name of the radiation as part of an appropriate message. -->

# Problem 1

x=float(input("Enter wavelength (in nm): "))

if  x< 380 or x> 750:
    print("Error: wavelength is outside of visible spectrum")
elif x < 450:
    print("Violet")
elif x < 495:
    print(" Blue")
elif x < 570:
    print("Green")
elif x < 590:
    print("Yellow")
elif x < 620:
    print("Orange")
else:
    print(" Red")



#problem 2

#Problem 2

x= float(input("Enter frequency : "))

if x< (3*(10**9)):
    print(" Radio Waves")
elif x < 3*10**12:
    print("Microwaves")
elif x < 4.3*10**14:
    print(" Infrared Light")
elif x < 7.5*10**14:
    print(" Visible Light")
elif x < 3*10**17:
    print("Ultraviolet Light")
elif x <  3*10**19:
    print(" X-Rays")
else:
    print("Gamma Rays")