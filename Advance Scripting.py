# Problem:-
#names = # get and process input for a list of names
#Admission_ID = # get and process input for a list of the number of admission ID
 #CAP_Rank = # get and process input rank of the student in CAP # Information to be sent to be used for each student
# HINT: use .format() with this string in your for loop
#message = "Hi {},\n\n Congratulations...!  {} You got selected for next round of recruitment process \ submit your academic credential including primary and secondary certificates. Your admission ID is {} and will be eligible \ for the next round of interview with a CAP rank of {} If you submit all the documents on time and process university might offer you a scholarship. \n\n" # write a for loop that iterates through each set of names, Admission_ID, and CAP ranks to print each student's message.


Names=(input("Enter your name :"))
Admission_ID=(input("Enter your Admission ID : "))
CAP_Rank=(input("Enter your CAP Rank :"))
print(f"Hi {Names}, Congratulations...!  \n You got selected for next round of recruitment process . Submit your academic credential including primary and secondary certificates.\n Your admission ID is {Admission_ID} and will be eligible for the next round of interview with a CAP rank of {CAP_Rank} If you submit all the documents on time and process university might offer you a scholarship.")