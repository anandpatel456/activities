# Problem Statement- I
# Design and write a program to calculate Net Run Rate scored by the two teams use controls to validate a condition such that the team with the higher run rate will top the points table and also think for the tie-breaker condition.

# Steps to Follow: 
# Understand how net run rate getting calculated (Cite the reference in submission comment)
# Follow the computational thinking process.
# Understand inputs required to calculate various parameters (Give Appropriate Comments to the code)
# Design Controls -  Compound Statements and Suites
# Provide Feedback to the User (Console level Feedback)
# Test (Paper Calculation)
# Validate (Paper Calculation = Code  Result)

T1_scored_r = int(input("Enter the total runs scored by T1: "))
T1_faced_o = int(input("Enter the total overs faced by T1: "))
T1_conceded_r = int(input("Enter the total runs conceded by T1: "))
T1_bowled_r = int(input("Enter the total overs bowled by T1: "))

T2_scored_r = int(input("Enter the total runs scored by Team 2: "))
T2_faced_o = int(input("Enter the total overs faced by Team 2: "))
T2_conceded_r = int(input("Enter the total runs conceded by Team 2: "))
T2_bowled_r = int(input("Enter the total overs bowled by Team 2: "))

T1_Nrr = (T1_scored_r / T1_faced_o) - (T1_conceded_r / T1_bowled_r)
print("T1 Net Run Rate =", round(T1_Nrr, 2))
T2_Nrr = (T2_scored_r / T2_faced_o) - (T2_conceded_r / T1_bowled_r)
print("T2 Net Run Rate =", round(T2_Nrr, 2))

if T1_Nrr > T2_Nrr:
    print("T1 has a higher Net Run Rate and tops the points table.")
elif T2_Nrr > T1_Nrr:
    print("T2 has a higher Net Run Rate and tops the points table.")
else:
    T1_wc = int(input("Enter number of wickets taken by T1: "))
    T2_wc = int(input("Enter number of wickets taken by T2: "))
    
    if T1_wc > T2_wc:
        print("T1 has a higher Net Run Rate and more wickets and tops the points table.")
    elif T2_wc > T1_wc:
        print("T2 has a higher Net Run Rate and more wickets and tops the points table.")
    else:
        print("Both teams have the same Net run rate and wickets taken and are tied on points.")


# Problem Statement- II
# We have three categories to check. If the sum of divisors is greater than a number, the number is
# abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
# be perfect design control structure for this problem statement

#Nint=28 # Number to be validated 
#Div=1    #Divisor
#while Div<Nint:
#   if Nint % Div==0:
#        print(Div) # Suit1
#Div=Div+1  # Suit 2


Nint = 28  
Div = 1    
Sum_of_divisors = 0    

while Div < Nint:
    if Nint % Div == 0:
        Sum_of_divisors += Div  
    
    Div += 1  

if Sum_of_divisors > Nint:
    print("The number", Nint, "is abundant")
elif Sum_of_divisors < Nint:
    print("The number", Nint, "is deficient")
else:
    print("The number", Nint, "is perfect")
