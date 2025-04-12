import json
with open("035_signup_data.json", "r") as file:

    my_list_dict = json.load(file)

    a = input("id:")

    b = input("first_name:")

    c = input("last_name:")

    d = input("email:")

    e = input("password:")


    data_dict = {
            
            "id": a,

            "first_name": b,

            "last_name": c,

            "email": d,

            "password": e

            }

    my_list_dict.append(data_dict)

    with open("035_signup_data.json",  "w") as file:
        json.dump(my_list_dict, file)

    print(my_list_dict)



