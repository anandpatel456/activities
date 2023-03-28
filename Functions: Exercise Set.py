# Problem 1
#Suppose you are buying something online on amazon.com 

#On the website, you get
#a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

#Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result


def discount(amount, is_prime_member):
    if is_prime_member:
        total = amount * 0.85 
        total *= 0.92
    else:
        total = amount * 0.92 
    return total

amount = float(input("How much does the product cost? "))
prime_member = input("Are you a prime member? (y/n): ")

final_price = discount(amount, prime_member == "y")
print("Final price: ", final_price)



#Problem 2:Chit Chat Application - Function:

#(a)
#In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.

#Write a function that takes as input the,

#message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.


#If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.

def length(message):
    words = message.split()
    if len(words) <= 200:
        return message
    else:
        return ' '.join(words[:200])

message = input("Enter the message:\n")
message_length = length(message)
print(message_length)

#(b)
#How one can check if the restriction is on a number of words rather than letters?
#Write a function that allows a message with only 30 words.

def check_word(message):
    words =  len(message.split())
    if words > 30:
        return False
    else:
        return True

message = input("Enter the message:\n")

if check_word(message):
    print("message meets words limit.\n")
else:
    print("message exceed word limit.\n")
    