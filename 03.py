import streamlit as st

# Set the title of the app
st.title("this is the app title")

# Add markdown text (bold and larger than normal)
st.markdown("<h2><b>this is the markdown</b></h2>", unsafe_allow_html=True)

# Add a caption (instead of a header)
st.caption("this is the header")

# Add a subheader
st.subheader("this is the subheader")

# Add a caption
st.caption("this is the caption")

# Add code block with the value of x
x = 2021
st.code(f"x = {x}", language="python")
