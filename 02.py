import streamlit as st

st.header('st.button')

if st.button('Say Hello'):
    st.write('Why Hello there')
else:
    st.write('Goodbye')