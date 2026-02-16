# Assignment 12: Salary Credit Check
# Use Case: Payroll system
# Input:
# credited_salary = 30000
# expected_salary = 30000
# Output:
# True

credited_salary= int(input("\nEnter your credited salary: "))
expected_salary= int(input("Enter ecpected salary: "))

if credited_salary==expected_salary:
    print("True\n")
else:
    print("False\n")