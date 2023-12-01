import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
import numpy as np
boston = pd.read_csv("boston.csv")


def river_homes():
    st.subheader( "1. 1970's Home Avalilability based on proximity to Charles river")

    option  = st.selectbox(
        "Are you looking for a home near Charles river?",
        ("All","Yes", "No")
        )
    
    st.write("Here are the Options available: ")

    if option == "All":
        data = boston
    elif option == "Yes":
        data = boston[boston['CHAS']==1.00]
    else:
        data = boston[boston['CHAS']==0.00]

    fig = px.histogram(data, x='PRICE', nbins=50, marginal='rug', color_discrete_sequence=['#AC182F'])
    
    # Updating figure layout
    fig.update_layout(
        title="1.1970s Home Availability based on proximity to Charle's River",
        xaxis_title='Price in 000s',
        yaxis_title='Nr. of Homes Available',
        bargap=0.1,
        showlegend=False
    )
    st.plotly_chart(fig)
    st.write("It is very clear that there are very few homes close to the river.")


def available_budget():
    st.subheader("2. How old/new is the house?")
    st.write("Varying the age of the home reveals how many homes are available at that price and their respective prices.")

    boston['AGE'] = boston['AGE'].round(0)

    available_ages = [int(age) for age in boston['AGE']]
    new_ages  = list(set(available_ages))

    option  = st.selectbox(
        label = 'Select the age of the house',
        options = new_ages
    )
    sliced_df = boston[boston['AGE'] == option]

    fig = px.histogram(sliced_df, x='PRICE', nbins=50, marginal='rug', color_discrete_sequence=['#6D527B'])

    fig.update_layout(
        title="1.1970s Home Availability based on the age of the home",
        xaxis_title='Price in 000s',
        yaxis_title='Nr. of Homes Available',
        bargap=0.1,
        showlegend=False
    )
    st.plotly_chart(fig)
    st.write("- You might have noticed that there are more older houses than newer ones")
    st.write("- This could also imply that not many new houses are being built")

    
