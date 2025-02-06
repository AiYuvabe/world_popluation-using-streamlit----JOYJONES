import streamlit as st
import requests

st.set_page_config(
    page_title="tab title",
    page_icon="❤️"
)
st.title('Hello streamlit')
st.subheader('This is a streamlit app')
st.write('This is a simple example of a streamlit app')
st.text_input('Enter your name',value='',placeholder='enter your name',)

data = requests.get('https://share.streamlit.io/user/hamagistral')
json = data.json()

immersiver_product = json['immersiver_product']

for product in immersiver_product:
    with st.container(
        border = true
    ):
        st.subheader(product['title'])
        st.write('⭐'*round(product['rating']))