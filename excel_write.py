#from csv import DictWriter
from openpyxl import Workbook, load_workbook
from pandas import read_excel
import os

FILEPATH = "family_finance_master.xlsx"

#ref_sheet = work_book['Ref_Categories']

#work_book = load_workbook(FILEPATH)
#main_sheet = work_book['ITEMS']
ref_cat = read_excel(FILEPATH, index_col=0, sheet_name="Ref_Categories")
ref_pay = read_excel(FILEPATH, header=0, sheet_name="Payment Methods")


def add_item_to_excel(dict_list):
    pass
"""
if not os.path.exists(FILEPATH):
    with open(FILEPATH,"w", newline="") as file:
        file = DictWriter(file, fieldnames = HEADERS)  #create a new file
        file.writeheader()          #write headers on that file

def add_item_row(item_dict):
    with open(FILEPATH, "a", newline="") as file:
        dict_file = DictWriter(file, fieldnames = HEADERS)
        print("dict_file: ")
        print(dict_file)
        dict_file.writerow(item_dict)
"""

""" To retrieve data from the excel file (using pandas)"""
def get_sub_categories(category):
    return ref_cat[ref_cat["Category"] == category].index.tolist()

def get_main_categories():
    return ref_cat['Category'].drop_duplicates().values.tolist()

def get_payment_methods():
    return ref_pay['payment_methods'].tolist()






