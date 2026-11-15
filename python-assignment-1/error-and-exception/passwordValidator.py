class ShortPassword(Exception):
    pass

class NoUppercase(Exception):
    pass

class NoNumber(Exception):
    pass

password = input("Enter password: ")

try:
    if len(password) < 8:
        raise ShortPassword("Password must contain at least 8 characters")

    elif not any(ch.isupper() for ch in password):
        raise NoUppercase("Password must contain an uppercase letter")

    elif not any(ch.isdigit() for ch in password):
        raise NoNumber("Password must contain a number")

    else:
        print("Password is valid")

except ShortPassword as e:
    print("Error:", e)

except NoUppercase as e:
    print("Error:", e)

except NoNumber as e:
    print("Error:", e)