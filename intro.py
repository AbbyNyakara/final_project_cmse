import streamlit as st

def intro():
    st.header("Welcome to Boston in the 1970's-Real Estate Analysis 🏠")
    st.image("https://1.bp.blogspot.com/-s9H7MShR5IM/UECRt6888wI/AAAAAAAAE7E/UDt8d2HDf4Y/s1600/Boston+1970.JPG")
    st.markdown(
    '''
    - As a former architect deeply involved in numerous construction projects, I dedicated considerable time to creating construction plans and participating in countless meetings. Drawing upon this experience, I recognize the pivotal role real estate investors play in estimating home prices even before the commencement of construction.

    - In this endeavor, I aim to develop a robust multivariable linear regression model. 
    
    - This model will serve as a valuable tool for predicting home prices based on a range of key characteristics, including:

     **1.  the number of rooms**

     **2.proximity to employment and town centers**

     **3. socioeconomic status of the area**
     
     **4. student-to-teacher ratios in local schools, and more.**
     
     **Through the amalgamation of these variables, the model will offer insightful price estimates, empowering investors with informed decision-making capabilities.**
    '''
    )