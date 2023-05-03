import streamlit as st
#import category_lookup as cl
import datetime
import pandas
import excel_write as ew
#import category_lookup

st.title("Family Expenses")
st.write("Keeping a record of expenses is <b>good</b> practice.",
         unsafe_allow_html=True)  #HTML enabled only for write function

def add_item():
    item_dict = {}
    dt = datetime.datetime.now()
    time_stamp = dt.strftime("%m-%d-%Y %I:%M%p")
    item_dict["Timestamp"] = time_stamp
    item_dict["description"] = st.session_state["description"]
    item_dict["date"] = st.session_state["date"]
    item_dict["amount"] = st.session_state["amount"]
    item_dict["payment_method"] = st.session_state["payment_method"]
    item_dict["online"] = st.session_state["online"]
    item_dict["main_category"] = st.session_state["main_category"]
    item_dict["category"] = st.session_state["sub_category"]

    # cw.add_item_row(dict_row)
    ew.add_item_to_excel(item_dict)
    st.write("**:tada: :blue[You have successfully submitted an item. Type in a new item]**")
    st.write(item_dict)
    #st.session_state["form_date"] = st.session_state["form_date"].today()
    #st.session_state["amount"] = ""
    #del st.session_state["amount"]

item_date = st.date_input(label="**:calendar: :blue[Enter date: ]**",
                          value=datetime.datetime.now(),
                          key="form_date")
st.session_state["date"] = item_date.strftime('%m/%d/%Y')

main_categories = ew.get_main_categories()
Category_selected = "Select a category"
main_categories.insert(0, "Select a category")
category_selected = st.selectbox(label="**:lower_left_ballpoint_pen: Select a category:**",
                                 options=main_categories, key="main_category")
#options (Sequence, numpy.ndarray, pandas.Series, pandas.DataFrame, or pandas.Index)

if (category_selected != "Select a category"):
    sub_categories = ew.get_sub_categories(category_selected)
    sub_categories.insert(0, "Select a subcategory")
    sub_category_selected = st.selectbox(label="**:lower_left_ballpoint_pen: Select a sub-category:**",
                                         options=sub_categories, key="sub_category")

st.text_input(label="**:page_facing_up: Description:**",
              placeholder="what, where, why...",
              key="description")

amount = st.number_input(label="**:heavy_dollar_sign: Enter Amount:**",
                value = 0, key="amount")

payment_methods = ew.get_payment_methods()
st.radio(label="**:credit_card: Select payment method:**",
         index=0, options = payment_methods, key="payment_method")

st.write("**:spider_web: Online payment?**")
st.checkbox(label="yes", value=False, key="online")

submit_button = st.button(label="-SUBMIT-", type="primary", key="submit")  # --need this? on_click=add_item

if submit_button:
    if category_selected == "Select a category":
        st.write(":broken_heart: :red[You must enter a category.]")
    elif sub_category_selected == "Select a subcategory":
        st.write(":broken_heart: :red[You must enter a subcategory.]")
    elif st.session_state["amount"] == 0:
        st.write(":broken_heart: :red[You must enter an amount.]")
    else:
        add_item()
        st.experimental_rerun()



