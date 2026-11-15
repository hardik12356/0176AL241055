salary = int(input("Enter monthly salary: "))
credit_score = int(input("Enter credit score: "))
age = int(input("Enter age: "))

if salary >= 30000 and credit_score >= 700 and 21 <= age <= 60:
    print("Loan Approved")
elif salary >= 25000 and credit_score >= 650 and 21 <= age <= 60:
    print("Conditionally Approved")
else:
    print("Loan Rejected")