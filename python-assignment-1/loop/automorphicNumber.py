num = int(input("Enter a number: "))

square = num * num
digits = len(str(num))

if square % (10 ** digits) == num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")