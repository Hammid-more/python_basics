age = int(input("Enter your age:"))

nationality = input("Enter your nationality:")

if age >= 18 and nationality == "Nigeria":
    print("You are eligible to vote in Nigeria.")

if age <18 and nationality == "Nigeria":
    print("You are not eligible to vote.")

else:
    print("You must be a Nigerian citizen to vote here.")
