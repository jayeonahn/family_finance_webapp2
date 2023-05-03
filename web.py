import streamlit as st
#import category_lookup as cl
import datetime
#import csv_write as cw
#import category_lookup

st.title("Family Expenses")
st.subheader("Enter an item.")
st.write("Keeping record of expenses is good practice.")

def add_item():
    dict_row = {}
    dict_row["description"] = st.session_state["description"]
    dict_row["date"] = st.session_state["date"]
    dict_row["amount"] = st.session_state["amount"]
    dict_row["payment_method"] = st.session_state["payment_method"]
    dict_row["online"] = st.session_state["online"]
    dict_row["main_category"] = st.session_state["main_category"]
    dict_row["category"] = st.session_state["category"]

    print(dict_row)
    #cw.add_item_row(dict_row)

    st.write("**:tada: :blue[You have successfully submitted an item. Type in a new item]**")
    #st.session_state["form_date"] = st.session_state["form_date"].today()
    #st.session_state["amount"] = ""
    #del st.session_state["amount"]

item_date = st.date_input(label="**:calendar: :blue[Enter date: ]**",
                          value=datetime.datetime.now(),
                          key="form_date")
st.session_state["date"] = item_date.strftime('%m/%d/%Y')

#categories_list = cl.get_main_categories()
main_categories = ["thing one", "thing two", "thing three"]
category_selected = st.selectbox(label="**:white_check_mark: Select a category:**",
                                 options=main_categories, key="main_category")

#subcategories = cl.look_up_subcategory(category_selected)
subcategories = ["sub1", "sub3", "sub3"]
st.selectbox(label="**:calendar: Select a sub-category:**",
             options=subcategories, key="category")

#categories_list = cl.get_subcategories()
#category_selected = st.selectbox(label=":white_check_mark: Select a category:",
#                           options=categories_list, key="category")

st.text_input(label="**:page_facing_up: Enter Description:**",
              placeholder="what, where, why...",
              key="description")

st.number_input(label="**:heavy_dollar_sign: Enter Amount:**",
                value = 0, key="amount")

#payment_methods = cl.get_payment_methods()
payment_methods = ["AmEx", "CapitalOne", "Cash"]
st.radio(label="**:credit_card: Select payment method:**",
         index=0, options = payment_methods, key="payment_method")

st.write("**:spider_web: Online payment?**")
st.checkbox(label="yes", value=False, key="online")

submit_button = st.button(label="-SUBMIT-")  # --need this? on_click=add_item

if submit_button:
    add_item()
    st.experimental_rerun()

st.write(submit_button)


