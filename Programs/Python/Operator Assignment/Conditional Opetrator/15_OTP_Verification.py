# Assignment 15: OTP Verification
# Use Case: Secure login
# Input:
# otp_entered = 5678
# otp_sent = 5678
# Output:
# True

import random
otp_sent= random.randint(1000,9999)
print("\nYour OTP is:", otp_sent,"Enter it correctly.")

otp_entered= int(input("Enter your OTP: "))

if otp_entered==otp_sent:
    print("True\n")
else:
    print("False\n")