import json
with open("016_data.json", "r") as my_file:
    my_list = json.load(my_file)

    
    i = input("id:")

    ii = input("first_name:")

    iii = input("last_name:")

    iv = input("email:")

    v = input("password:")

    data_dict = {

            "id": i,

            "first_name": ii,

            "last_name":  iii,

            "email":  iv,

            "password":  v
            }

    my_list.append(data_dict)

    print(my_list)

    with open("016_data.json", "w") as my_file:
        json.dump(my_list, my_file)



