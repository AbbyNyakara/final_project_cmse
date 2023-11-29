import streamlit as st

def intro():
    st.header("Welcome to Boston in the 1970's")
    st.image("https://1.bp.blogspot.com/-s9H7MShR5IM/UECRt6888wI/AAAAAAAAE7E/UDt8d2HDf4Y/s1600/Boston+1970.JPG")
    st.markdown(
      '''
        As a former architect, I worked on lots of construction project(Guess I still am).
        My goal in this one is slightly different. 
        I would like to estimate the cost of a project before it starts.

        To do so, I will build a model that can provide a price estimate based on a home's characteristics like:
        - The number of rooms
        - The distance to employment centres
        - How rich or poor the area is
        - How many students there are per teacher in local schools etc
      '''
    )