
import json

import pandas as pd


with open("029_data.json", "r") as my_file:
    data = json.load(my_file)


    data = pd.json_normalize(data)

    data.to_excel("031_data.xlsx", index=False)

    print("Excel file created: successfully: 031_data.xlsx")
