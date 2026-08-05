"""
# scenario 1

shirt = 800
shoes = 1200
total_bill = shirt + shoes
print("Total bill for shirt and shoes is:", total_bill)

# scenario 2

account_balance = 10000
withdraw_amount = 2500
new_balance = account_balance - withdraw_amount
print("New account balance after withdrawal is:", new_balance)

# scenario 3

movie_ticket_price = 250
number_of_tickets = 4
total_amount = movie_ticket_price * number_of_tickets
print("Total amount for", number_of_tickets, "movie tickets is:", total_amount)

# scenario 4

restaurant_bill = 1500
number_of_people = 4
per_person_share = restaurant_bill / number_of_people
print("Each person need to pay:",per_person_share)

# scenario 5

total_chocolates = 53
number_of_chocolates_per_box = 10
number_of_boxes = total_chocolates // number_of_chocolates_per_box
remaining_chocolates = total_chocolates % number_of_chocolates_per_box
print("Number of boxes:", number_of_boxes)
print("Remaining chocolates:", remaining_chocolates)

# scenario 6

minutes = 145
hours = minutes // 60
remaining_minutes = minutes % 60
print("Total time is:",hours,"hours and",remaining_minutes,"minutes")

# scenario 7

student_roll_number = 12
if (student_roll_number % 2 == 0):
    print("The student roll number is even.")
else:
    print("The student roll number is odd.")

# scenario 8

side_of_square = 5
area_of_square = side_of_square ** 2
print("Area of square with side",side_of_square,"is:",area_of_square)

# scenario 9

wallet_balance=500
added_amount=200
wallet_balance+=added_amount
print("New wallet balance after adding amount is:",wallet_balance)

# scenario 10

player_points=100
gained_points=50
player_points+=gained_points
losed_points=20
player_points-=losed_points
print("The player's final score is:",player_points)

# scenario 11

student_score= 65
if student_score >= 40:
    print("The student has passed the exam.")
else:
    print("The student has failed the exam.")

# scenario 12

stored_password = "abhi123"
user_input = input("Enter your password:")
if user_input == stored_password:
    print("Access granted.")
else:
    print("Access denied.")

# scenario 13

stock =75
if stock != 0:
    print("The item is in stock.")
else:
    print("The item is out of stock.")

# scenario 14

Age = int(input("Enter your age: "))
passed_test = input("Have you passed the driving test? (yes/no): ")
if Age >= 18 and passed_test == "yes":
    print("you are eligible to drive.")
else:
    print("you are not eligible to drive.")


# scenario 15

weekend = input("Enter the day of the week: ")
if weekend == "saturday" or weekend == "sunday":
    print("It's a weekend!")
else:
    print("It's a weekday.")


# scenario 16

order_amount =(int(input("Enter the order amount: ")))
premium_member = input("Are you a premium member? (yes/no): ")
if order_amount >= 1000 or premium_member == "yes":
    print("You are eligible for free shipping.")
else:
    print("You are not eligible for free shipping.")

# scenario 18

age =24
graduation=(input("Have you graduated? (yes/no): "))
banned=(input("Are you banned from the platform? (yes/no): "))
if age >= 21 and graduation == "yes" and banned == "no":
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")


# scenario 19

customer_search = "Laptop"
products = ["Laptop", "Mobile", "Tablet", "Headphones"]
if customer_search in products:
    print("The item is available.")
else:
    print("The item is not available.")
    

# scenario 20

username = input("Enter your username: ")
blocked_names = ["admin", "root", "system"]
if username not in blocked_names:
    print("Welcome,", username)
else:
    print("Access denied. The username is blocked.")
    
"""