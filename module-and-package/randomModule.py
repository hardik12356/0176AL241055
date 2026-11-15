import random
import string

# Generate OTP
otp = random.randint(100000, 999999)
print("OTP:", otp)

# Generate Random Password
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print("Random Password:", password)

# Generate Random List
lst = [random.randint(1, 100) for i in range(5)]
print("Random List:", lst)