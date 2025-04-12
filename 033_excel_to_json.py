import pandas as pd

file = pd.read_excel("032_book.xlsx")

file.to_json("034_data.json", orient="records", index=2)
