library = {
    "Python": 5,
    "C++": 3,
    "Java": 4,
    "DBMS": 2
}

book = input("Enter book name: ")

if book in library:
    print("Available copies:", library[book])
else:
    print("Book not found")

# Add a new book
new_book = input("Enter new book name: ")
quantity = int(input("Enter quantity: "))

library[new_book] = quantity

print("Library Records:")
print(library)