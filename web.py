import streamlit as st
import datetime
import excel_write as ew

main_categories = ew.get_main_categories()
main_categories.insert(0, "Select a category")

def add_item():
    dt = datetime.datetime.now()
    time_stamp = dt.strftime("%m-%d-%Y %I:%M%p")
    item_dict = {}

    for key, value in st.session_state.items():
        item_dict[key] = value

# ------ adding and cleaning up dictionary list ------ #
    item_dict["Timestamp"] = time_stamp
    del item_dict["form_date"]
    del item_dict["submit"]

#------------reset sesstion_state -----------------
    st.session_state["main_category"] = main_categories[0]
    st.session_state["amount"] = 0
    st.session_state["date"] = dt
    #st.session_state["payment_method"] = ew.get_payment_methods()[0]
    st.session_state["online"] = False

    ew.add_item_to_excel(item_dict)
    st.write(item_dict)

def on_click_function():
    if st.session_state["main_category"] == main_categories[0]:
        st.write(":broken_heart: :red[You must enter a category.]")
    elif st.session_state["sub_category"] == "Select a subcategory":
        st.write(":broken_heart: :red[You must enter a subcategory.]")
    elif st.session_state["amount"] == 0:
        st.write(":broken_heart: :red[You must enter an amount.]")
    else:
        add_item()
        st.write("**:tada: :blue[You have successfully submitted an item. Enter a new item.]**")

# *********************WIDGETS ************************
st.title("Family Expenses")
st.write("Keeping a record of expenses is <b>good</b> practice.",
         unsafe_allow_html=True)  #HTML enabled only for write function

col, empty_col = st.columns([1,4])
with col:
    item_date = st.date_input(label="**:calendar: :blue[Date: ]**", key="form_date")
    st.session_state["date"] = item_date.strftime('%m/%d/%Y')

st.text_input(label="**:page_facing_up: Description:**",
              placeholder="what, where, why...",
              key="description")

col1, col2, empty_col = st.columns([1.5, 1.5, 0.5])
with col1:
    category_selected = st.selectbox(label="**:lower_left_ballpoint_pen: Category:**",
                                     options=main_categories, key="main_category")

with col2:
    if (category_selected != main_categories[0]):
        sub_categories = ew.get_sub_categories(category_selected)
        sub_categories.insert(0, "Select a subcategory")
        sub_category_selected = st.selectbox(label="**:lower_left_ballpoint_pen: Sub-category:**",
                                             options=sub_categories, key="sub_category")

col3, col4, col5, empty_col = st.columns([3,3,3,1])

with col3:
    amount = st.number_input(label="**:heavy_dollar_sign: Amount:**",
                             key="amount", help="enter income as a negative value")
with col4:
    payment_methods = ew.get_payment_methods()
    st.selectbox(label="**:lower_left_ballpoint_pen: Payment method:**",
                 options=payment_methods, index=1, key="payment_method")

with col5:
   st.checkbox(label="Check here if online payment", value=False, key="online")

submit_button = st.button(label="-SUBMIT-", on_click=on_click_function,
                          type="primary", key="submit")





