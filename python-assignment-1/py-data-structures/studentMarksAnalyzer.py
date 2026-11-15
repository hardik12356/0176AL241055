students = {
    "Rahul": 85,
    "Aman": 45,
    "Priya": 92,
    "Rohit": 28,
    "Neha": 76
}

topper = max(students, key=students.get)
average = sum(students.values()) / len(students)

print("Topper:", topper)
print("Highest Marks:", students[topper])
print("Average Marks:", average)

print("Failed Students:")
for name, marks in students.items():
    if marks < 33:
        print(name)