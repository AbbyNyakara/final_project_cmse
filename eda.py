import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import numpy as np

data = pd.read_csv("boston.csv")

def rooms():
    st.subheader("2. Number of homes")
    sns.displot(data.RM, 
            aspect=2,
            kde=True, 
            color='#00796b')

    plt.title(f'Distribution of Rooms in Boston. Average: {data.RM.mean():.2}')
    plt.xlabel('Average Number of Rooms')
    plt.ylabel('Nr. of Homes')

    plt.show()
    st.write("On average, each house has about 6 rooms")

def home_price():
    st.subheader("1. Home price distribution")
    
    # Creating a Plotly figure
    fig = px.histogram(data, x='PRICE', nbins=50, marginal='rug', color_discrete_sequence=['#203F8B'])
    
    # Updating figure layout
    fig.update_layout(
        title=f'1970s Home Values in Boston. Average: ${(1000 * data["PRICE"].mean()):.6}',
        xaxis_title='Price in 000s',
        yaxis_title='Nr. of Homes',
        bargap=0.1,
        showlegend=False
    )

    st.plotly_chart(fig)

    st.write("Note there is a spike in the number of homes at the very right tail at the $50,000 mark. 🤔")


def employment_dist():
    st.subheader("3. Number of homes in relation to employment centers")

    fig = px.histogram(data, x='DIS', nbins=50, marginal='rug', color_discrete_sequence=['#351c75'])

    fig.update_layout(
        title=f'Distance to Employment Centres. Average: {(data["DIS"].mean()):.2f}',
        xaxis_title='Weighted Distance to 5 Boston Employment Centres',
        yaxis_title='Number of Homes',
        bargap=0.1,
        showlegend=False  
    )

    st.plotly_chart(fig)

    st.write("- A majority of homes are closer to employment centers in Boston.")
    st.write("- On average, a home is about 3.8 miles from an employment center.")

