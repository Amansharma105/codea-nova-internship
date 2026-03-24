import random
import string

print("Password Generator")

try:
    length = int(input("Enter password length: "))
    
    if length <= 0:
        print("Length should be greater than 0")
        exit()

    print("Select password type:")
    print("1. Only Letters")
    print("2. Letters and Numbers")
    print("3. Strong Password (Letters, Numbers, Symbols)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        characters = string.ascii_letters
    elif choice == "2":
        characters = string.ascii_letters + string.digits
    elif choice == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice")
        exit()

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number")
    with open("passwords.txt","a") as file:
        file.write(password+"\n")