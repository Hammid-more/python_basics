import json

a = input("Enter id:")

b = input("Enter first_name")

c = input("Enter last_name")

d = input("Enter email")

e = input("Enter password")

user = {

        "id": a,

        "first_name": b,

        "last_name": c,

        "email": d,

        "password": e

        }


with open("015_register.json", "w")as json_file:
    json.dump(user, json_file)

    print(user)



