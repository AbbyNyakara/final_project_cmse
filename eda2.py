import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("boston.csv")

def dist_pol():
    st.subheader("1.Relationship between the distance and pollution")
    with sns.axes_style('darkgrid'):
        sns.jointplot(x=data['DIS'], 
                        y=data['NOX'], 
                        height=8, 
                        kind='scatter',
                        color='deeppink', 
                        joint_kws={'alpha':0.5})

    plt.show()
    st.markdown(
        '''
        We see that pollution goes down as we go further and further out of town. 
        However, even at the same distance of 2 miles 
        to employment centres, we can get very different levels of pollution. 
        By a distance of between 9 miles and 12 miles, we have very similar levels of pollution. 
        '''
    )

def income_popl():
    """
    The function explores how the proportion of low income population affects the
    prices of homes. 
    """
    st.subheader("2. How the percentage of low income population affects home prices")
    with sns.axes_style('darkgrid'):
        sns.jointplot(x=data.LSTAT, 
                        y=data.PRICE,
                        height=7, 
                        color='crimson',
                        joint_kws={'alpha':0.5})
    plt.show()
    st.markdown(
        """
        There is a clear inverse relationship between these two properties.
        - The highest priced houses are associated with a very small percentage of low income
        people.(Mayble because they cannot afford. )
        - When the percentage of population with a lower income exceeds 20%, the prices
        of the houses are pretty steady.
        - What this means, is that when the percentage is over 20%, then no matter the house, 
        the price will be on the lower side. 
        """
    )

def rooms_value():
    """
    How the number of rooms affects home value
    """
    st.subheader("3.How the number of rooms affects home value")
    with sns.axes_style('whitegrid'):
        sns.jointplot(x=data.RM, 
                        y=data.PRICE, 
                        height=7, 
                        color='darkblue',
                        joint_kws={'alpha':0.5})
    plt.show()
    st.markdown(
        """
        - Again, we see those homes at the $50,000 mark all lined up at the top of the chart. 
        - Perhaps there was some sort of cap or maximum value imposed during data collection. 
        - However, the general pattern is, the 
        """
    )