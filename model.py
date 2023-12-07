import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

data = pd.read_csv("boston.csv")

def model():
    st.subheader("Multivariable Linear Regression Model")

    target = data['PRICE']
    features = data.drop('PRICE', axis=1)

    # Create a slider to select the size of the training set
    training_size = st.slider("Select the size of the Training set - As a percentage of the entire dataset: ",
                              10, 90, 30)

    test_size = (100 - training_size) / 100

    X_train, X_test, y_train, y_test = train_test_split(features, 
                                                        target, 
                                                        test_size=test_size,
                                                        random_state=10)
    
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    rsquared = regr.score(X_train, y_train)

    st.write(f'Training data r-squared: {rsquared:.2}')

    # Predicted vals
    predicted_vals = regr.predict(X_train)

    # Calculate RMSE and MAE
    rmse = np.sqrt(mean_squared_error(y_train, predicted_vals))
    mae = mean_absolute_error(y_train, predicted_vals)

    st.write(f'Training data RMSE: {rmse:.2f}')
    st.write(f'Training data MAE: {mae:.2f}')

    predicted_vals = regr.predict(X_train)
    residuals = (y_train - predicted_vals)

    # Plot the figure
    fig, ax = plt.subplots()
    ax.scatter(x=y_train, y=predicted_vals, c='blue', alpha=0.6)
    ax.plot(y_train, y_train, color='red')
    ax.set_title(f'Actual vs Predicted Prices: $y _i$ vs $\hat y_i$', fontsize=17)
    ax.set_xlabel('Actual prices 000s $y _i$', fontsize=14)
    ax.set_ylabel('Predicted prices 000s $\hat y _i$', fontsize=14)

    # Show the plot using st.pyplot()
    st.pyplot(fig)

    # Plot the figure
    fig1, ax = plt.subplots(dpi=100)
    ax.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
    ax.set_title('Residuals vs Predicted Values', fontsize=17)
    ax.set_xlabel('Predicted Prices $\hat y _i$', fontsize=14)
    ax.set_ylabel('Residuals', fontsize=14)

    # Show the plot using st.pyplot()
    st.pyplot(fig1)

    fig3, ax = plt.subplots(dpi=100)
    sns.histplot(residuals, kde=True, color='indigo', ax=ax)
    ax.set_title(f'Residuals Distribution (Skew: {round(residuals.skew(), 2)}, Mean: {round(residuals.mean(), 2)})', fontsize=17)
    ax.set_xlabel('Residuals', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    st.pyplot(fig3)

    st.write("One of the options would be to change the lienar model entirely")
    st.write("Alternatively, i'll apply log transformation for the data to fit my model better.")

    st.subheader("Data Transformation - Log Transformation:")
    # Plot the figure
    fig4, ax = plt.subplots(dpi=100)
    sns.histplot(data['PRICE'], kde=True, color='green', ax=ax)
    ax.set_title(f'Distribution of Prices (Skew: {round(data["PRICE"].skew(), 3)})', fontsize=17)
    ax.set_xlabel('Prices', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)

    # Show the plot using st.pyplot()
    st.pyplot(fig4)

    y_log = np.log(data['PRICE'])


    # Plot the figure
    fig5, ax = plt.subplots(dpi=100)
    sns.histplot(y_log, kde=True, color='purple', ax=ax)
    ax.set_title(f'Log Prices Distribution (Skew: {round(y_log.skew(), 3)})', fontsize=17)
    ax.set_xlabel('Log Prices', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)

    # Show the plot using st.pyplot()
    st.pyplot(fig5)
    st.markdown(
        """
            The log prices have a skew that's closer to zero.
            This makes them a good candidate for use in our linear model. 
            Perhaps using log prices will improve our regression's r-squared and our model's residuals.
        """
    )

    # Plot the figure
    fig6, ax = plt.subplots(dpi=150)
    ax.scatter(data['PRICE'], y_log)
    ax.set_title('Mapping the Original Price to a Log Price', fontsize=17)
    ax.set_xlabel('Actual $ Price in 000s', fontsize=14)
    ax.set_ylabel('Log Price', fontsize=14)

    # Show the plot using st.pyplot()
    st.pyplot(fig6)

    st.subheader("Do regression using the log prices: ")

    new_target = np.log(data['PRICE']) # Use log prices
    features = data.drop('PRICE', axis=1)

    X_train, X_test, log_y_train, log_y_test = train_test_split(features, 
                                                    new_target, 
                                                    test_size=test_size, 
                                                    random_state=10)
    
    log_regr = LinearRegression()
    log_regr.fit(X_train, log_y_train)
    log_rsquared = log_regr.score(X_train, log_y_train)

    log_predictions = log_regr.predict(X_train)
    log_residuals = (log_y_train - log_predictions)

    st.subheader(f'Training data r-squared: {log_rsquared:.2}') 
    st.write("This shows an improvement with my model:")

        # Create a Streamlit app
    st.title("Distribution of Residuals")

    # Plot the figure for the log price model
    fig_log, ax_log = plt.subplots(dpi=100)
    sns.histplot(log_residuals, kde=True, color='navy', ax=ax_log)
    ax_log.set_title(f'Log Price Model Residuals (Skew: {round(log_residuals.skew(), 2)}, Mean: {round(log_residuals.mean(), 2)})', fontsize=17)
    ax_log.set_xlabel('Log Residuals', fontsize=14)
    ax_log.set_ylabel('Frequency', fontsize=14)

    # Show the plot for the log price model using st.pyplot()
    st.pyplot(fig_log)

    # Plot the figure for the original model
    fig_orig, ax_orig = plt.subplots(dpi=100)
    sns.histplot(residuals, kde=True, color='indigo', ax=ax_orig)
    ax_orig.set_title(f'Original Model Residuals (Skew: {round(residuals.skew(), 2)}, Mean: {round(residuals.mean(), 2)})', fontsize=17)
    ax_orig.set_xlabel('Original Residuals', fontsize=14)
    ax_orig.set_ylabel('Frequency', fontsize=14)

    # Show the plot for the original model using st.pyplot()
    st.pyplot(fig_orig)




    
