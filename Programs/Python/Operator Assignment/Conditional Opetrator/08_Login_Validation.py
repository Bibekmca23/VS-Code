# Assignment 8: Login Validation
# Use Case: Authentication system
# Input:
# entered_password = "admin"
# stored_password = "admin123"
# Condition:
# Entered password == Stored password
# Output:
# False

e_user= input("\nEnter username: ")
e_pass= input("Enter password: ")

stored_username= "admin"
stored_password= "admin123"

if e_user == stored_username and e_pass == stored_password:
    print("True\n")
else:
    print("False\n")