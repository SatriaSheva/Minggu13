import streamlit as st
from datetime import date


number = st.number_input("Pick a number", min_value=1, step=1, value=1)


email = st.text_input("Email address")

travel_date = st.date_input("Travelling date", value=date(2022, 6, 17))

time_options = ["08:00", "09:00", "10:00", "11:00"]
school_time = st.selectbox("School time", time_options)

description = st.text_area("Description:")

uploaded_file = st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "xlsx"])

color = st.color_picker("Choose your favourite color", "#800080")  # Default purple color

# Display the data
if st.button("Submit"):
    st.write("Form Data:")
    st.write(f"Number: {number}")
    st.write(f"Email: {email}")
    st.write(f"Travelling Date: {travel_date}")
    st.write(f"School Time: {school_time}")
    st.write(f"Description: {description}")
    if uploaded_file:
        st.write("Uploaded file name:", uploaded_file.name)
    st.write(f"Favourite Color: {color}")
