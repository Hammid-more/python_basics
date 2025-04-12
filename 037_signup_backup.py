import json

import pandas as pd

with open("035_signup_data.json", "r") as my_file:
    data = json.load(my_file)

    df = pd.json_normalize(data)

    df.to_excel("038_first_exam_result.xlsx", index=False)


    print("Signup backup created succesfully,")
