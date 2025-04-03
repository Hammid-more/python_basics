import json

student = {
        
        "id":   "001",

        "name": "Hammid",

        "gender":   "male",

        "department":   "Accounting",

        "school":   "Lasu"
        }


import json

with open("013_data.json", "w") as my_file:
    json.dump(student, my_file)

    print(student)
