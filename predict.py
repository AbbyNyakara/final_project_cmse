import pandas as pd
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("boston.csv")

def estimate():
    st.subheader("Lets estimate what your property is worth.")
    st.image("https://media.istockphoto.com/id/1409298953/photo/real-estate-agents-shake-hands-after-the-signing-of-the-contract-agreement-is-complete.jpg?s=612x612&w=0&k=20&c=SFybbpGMB0wIoI0tJotFqptzAYK_mICVITNdQIXqnyc=")
    target = data['PRICE']
    features = data.drop('PRICE', axis=1)

    X_train, X_test, y_train, y_test = train_test_split(features, 
                                                        target, 
                                                        test_size=0.2, 
                                                        random_state=10)
    train_pct = 100*len(X_train)/len(features)
    test_pct = 100*X_test.shape[0]/features.shape[0]

    regr = LinearRegression()
    regr.fit(X_train, y_train)
    rsquared = regr.score(X_train, y_train)

    regr_coef = pd.DataFrame(data=regr.coef_, index=X_train.columns, columns=['Coefficient'])
    # Premium for having an extra room
    premium = regr_coef.loc['RM'].values[0] * 1000
    predicted_vals = regr.predict(X_train)
    residuals = (y_train - predicted_vals)

    new_target = np.log(data['PRICE']) # Use log prices
    features = data.drop('PRICE', axis=1)

    X_train, X_test, log_y_train, log_y_test = train_test_split(features, 
                                                        new_target, 
                                                        test_size=0.2, 
                                                        random_state=10)

    log_regr = LinearRegression()
    log_regr.fit(X_train, log_y_train)
    log_rsquared = log_regr.score(X_train, log_y_train)

    log_predictions = log_regr.predict(X_train)
    log_residuals = (log_y_train - log_predictions)
    df_coef = pd.DataFrame(data=log_regr.coef_, index=X_train.columns, columns=['coef'])

    features = data.drop(['PRICE'], axis=1)
    average_vals = features.mean().values
    property_stats = pd.DataFrame(data=average_vals.reshape(1, len(features.columns)), 
                                columns=features.columns)
    
    log_estimate = log_regr.predict(property_stats)[0]
    print(f'The log price estimate is ${log_estimate:.3}')

    # Convert Log Prices to Acutal Dollar Values
    dollar_est = np.e**log_estimate * 1000
    # or use
    dollar_est = np.exp(log_estimate) * 1000

    # Some selected proppoertires

    # Set up the page: 
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        option1 = st.selectbox(
            "Close to charles river",
            ("False","True"),
        )
    with col2:
        option2 = st.number_input("Number of rooms", value=1)
    with col3:
        option3 = st.number_input("Students/classroom", value=1)
    with col4:
        option4 = st.number_input("Distance from town", value=1)
    with col5:
        pollution = 0
        option5 = st.selectbox(
            "Level of pollution",
            ("Low","Average", "High"),
        )
        if option5 == "Low":
            pollution = 0.25
        elif option5 == "Average":
            pollution = 0.5
        else:
            pollution = 0.75
    with col6:
        poverty = 0
        option6 = st.selectbox(
            "Poverty Index of Area",
            ("Low","Average", "High"),
        )
        if option6 == "Low":
            poverty = 0.25
        elif option6 == "Average":
            poverty = 0.5
        else:
            poverty = 0.75

    next_to_river = option1
    nr_rooms = option2
    students_per_classroom = option3
    distance_to_town = option4
    pollution = data.NOX.quantile(q=pollution) 
    amount_of_poverty =  data.LSTAT.quantile(q=poverty) # low

    # Solution
    # Set Property Characteristics
    property_stats['RM'] = nr_rooms
    property_stats['PTRATIO'] = students_per_classroom
    property_stats['DIS'] = distance_to_town

    if next_to_river:
        property_stats['CHAS'] = 1
    else:
        property_stats['CHAS'] = 0

    property_stats['NOX'] = pollution
    property_stats['LSTAT'] = amount_of_poverty

    # Make prediction
    log_estimate = log_regr.predict(property_stats)[0]

    # Convert Log Prices to Acutal Dollar Values
    dollar_est = np.e**log_estimate * 1000

    st.markdown(
        f'''
            ### With the selected features, your property is worth ${dollar_est:.6}
        '''
    )

