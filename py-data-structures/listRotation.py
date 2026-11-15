lst = [1, 2, 3, 4, 5]
k = int(input("Enter rotation positions: "))

k = k % len(lst)

left = lst[k:] + lst[:k]
right = lst[-k:] + lst[:-k]

print("Left Rotation:", left)
print("Right Rotation:", right)