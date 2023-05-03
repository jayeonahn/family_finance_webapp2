#from csv import DictWriter
import os

"""
item_dict = {'date': '4/3/2023', 'category': 'eating out', 'description': 'dinner at Uno'}
"""

FILEPATH = "family_expenses.xlsx"



HEADERS = ["date", "category", "description", "amount", "payment_method", "online", "main_category"]
print("cvs.headers", HEADERS)
    #["date", "category", "main_category", "description", "description", "amount", "payment_method", "online", "notes"]

if not os.path.exists(FILEPATH):
    with open(FILEPATH,"w", newline="") as file:
        file = DictWriter(file, fieldnames = HEADERS)
        file.writeheader()

def add_item_row(item_dict):
    with open(FILEPATH, "a", newline="") as file:
        dict_file = DictWriter(file, fieldnames = HEADERS)
        print("dict_file: ")
        print(dict_file)
        dict_file.writerow(item_dict)