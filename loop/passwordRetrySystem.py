password = "hariOm"
attempts = 0

while attempts < 3:
    entered = input("Enter password: ")

    if entered == password:
        print("Login Successful")
        break
    else:
        attempts += 1
        print("Incorrect Password")

if attempts == 3:
    print("Account Blocked")