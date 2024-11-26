import streamlit as st

# Checkbox
st.checkbox("yes")

# Button
st.button("Click")

# Radio buttons
st.write("Pick your gender")
gender = st.radio("", ["Male", "Female"], index=0)

# Dropdown menu
st.write("Pick your gender")
gender_dropdown = st.selectbox(" ", ["Male", "Female"])

# Another dropdown menu
st.write("choose a planet")
planet = st.selectbox("Choose an option", ["Mercury", "Venus", "Earth", "Mars", "Jupiter"])

# Slider with custom labels (Bad, Good, Excellent)
st.write("Pick a mark")
mark = st.select_slider(
    "Pick a mark:",
    options=["Bad", "Good", "Excellent"],
    value="Good"  # Default value
)


# Another slider
st.write("Pick a number")
number = st.slider("Pick a number:", 0, 50, 9)
