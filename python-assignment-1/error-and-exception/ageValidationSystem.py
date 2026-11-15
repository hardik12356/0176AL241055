age = int(input("Enter your age: "))

try:
    if age < 18:
        raise Exception("Age must be 18 or above")
    print("Eligible")
except Exception as e:
    print("Error:", e)