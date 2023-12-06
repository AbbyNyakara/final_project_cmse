import streamlit as st

def intro():
    st.header("Welcome to Boston in the 1970's-Real Estate Analysis 🏠")
    st.image("https://1.bp.blogspot.com/-s9H7MShR5IM/UECRt6888wI/AAAAAAAAE7E/UDt8d2HDf4Y/s1600/Boston+1970.JPG")
    st.markdown(
      '''
        **As a former architect, I worked on lots of construction projects, drew construction plans and attended
        an ungodly number of meetings**
        
        **With this model, a real estate investor can estimate the price of a home before construction even begins.**

        *To do so, I will build a model that can provide a price estimate based on a home's characteristics such as:*

        *1. The number of rooms*

        *2.The distance to employment/town centres*

        *3.How rich or poor the area is*

        *4.How many students there are per teacher in local schools.. etc*
      '''
    )