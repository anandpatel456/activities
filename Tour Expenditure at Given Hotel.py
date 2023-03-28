#Tour Expenditure at Given Hotel 

#The family has spent the vacation in Goa and now they are returning home to do so they will have to check out from the hotel.

#Tariff on Room: Delux Room- 7500 
#Non AC Room- 4500 INR 

#You  as a developer has to create a program for a hotel owner which has the following requirements,

#The program should begin with taking input from the checkout counter 

#Type of room booked 
#Total number of days 
#Total Amount on Food (Amount is expected )
#There are the following cases to be considered while generating a bill.

#The tax on food amount is dependent on the type of room booked.

#Tax on food for the deluxe room will be billed  18% of the total food amount.

#Tax on food for the Non AC room will be billed  5% of the total food amount.

#You are supposed to include a tip of 10% on the food amount.

#The output from your program should include;

#The  Room Tariff on the number of days spend, GST on a meal(Breakdown of GST is necessary based on CGST and SGST and same has to get reflected on console ) 

#The tip amount, and the grand total for the meal including both the tax and the tip.

#Format the output so that all of the values are displayed using two decimal places.


a = "Delux room"
b = "Non Ac room"

Type_of_room_booked = input("Which type of room did you book?\n  1. Delux Room\n  2. Non AC Room\n")

Total_number_of_days = int(input("Enter the total number of days:\n"))
Total_amount_on_food = float(input("Enter the total amount of food:\n"))

if Type_of_room_booked == "1":
    Total_number_of_days = Total_number_of_days * 7500
    Total_amount_on_food = Total_amount_on_food * 1.18
    Tip_amount = Total_amount_on_food * 0.1
    Total = Total_amount_on_food + Tip_amount
    GST_amount = Total * 0.18
    final_amount = Total + Total_number_of_days + GST_amount
    
    print(f"You stayed in Delux Room for {Total_number_of_days//7500} days.")
    print("18% GST added on your food amount.")
    print("Extra 10% tip amount added to your bill.")
    print("The total amount payable for a Delux Room is:", final_amount)
    print("Thank you, have a nice day!")
    
elif Type_of_room_booked == "2":
    Total_number_of_days = Total_number_of_days * 4500
    Total_amount_on_food = Total_amount_on_food * 1.05
    Tip_food_price = Total_amount_on_food * 0.1
    final = Total_amount_on_food + Tip_food_price
    GST_amount = final * 0.05
    final_amount = Total_number_of_days + final + GST_amount
    
    print(f"You stayed in Non AC Room for {Total_number_of_days//4500} days.")
    print("5% GST added on your food amount.")
    print("Extra 10% tip amount added to your bill.")
    print("The total amount payable for a Non AC Room is:", final_amount)
    print("Thank you, have a nice day!")
    
else:
    print("Invalid room type selected!")
