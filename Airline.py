import streamlit as st
import matplotlib as plt
import pandas as pd
import plotly.express as px
from PIL import Image
import seaborn as sns
import numpy as np
st.set_page_config(page_title="Airline Satisfaction Prediction", page_icon="airplane")
uploaded_file = st.file_uploader




page = st.sidebar.selectbox("Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis", "Extras"])
# Data Preparation
uploaded_file = st.sidebar.file_uploader("Upload your Starbucks Excel file", type=["xlsx", "xls"])
if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.sidebar.error("Error: Unable to read the uploaded file. Please upload a valid Excel file.")

# Home Page
if page == "Home":
    st.title("Airline Satisfaction Prediction Project ✈️")
    st.subheader("Upload and Display an Image")
    uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
    st.subheader("Welcome!")
    st.write(
        """
       The dataset used in this project is the "Airline Passenger Satisfaction" dataset, which can be downloaded from Kaggle here. For this project, you will specifically use the train.csv file. The dataset contains information about airline passengers, including features such as flight distance, seat comfort, inflight entertainment, and more.
        """
    )

# Data Overview Page
if page == "Data Overview":
    st.title("Data Overview")
    st.subheader("About the Dataset")
    st.write(
        """
        This dataset includes nutritional information for Starbucks beverages. You can view details like:
        -Gender: Gender of the passengers (Female, Male)

Customer Type: The customer type (Loyal customer, disloyal customer)

Age: The actual age of the passengers

Type of Travel: Purpose of the flight of the passengers (Personal Travel, Business Travel)

Class: Travel class in the plane of the passengers (Business, Eco, Eco Plus)

Flight distance: The flight distance of this journey

Inflight wifi service: Satisfaction level of the inflight wifi service (0:Not Applicable;1-5)

Departure/Arrival time convenient: Satisfaction level of Departure/Arrival time convenient

Ease of Online booking: Satisfaction level of online booking

Gate location: Satisfaction level of Gate location

Food and drink: Satisfaction level of Food and drink

Online boarding: Satisfaction level of online boarding

Seat comfort: Satisfaction level of Seat comfort

Inflight entertainment: Satisfaction level of inflight entertainment

On-board service: Satisfaction level of On-board service

Leg room service: Satisfaction level of Leg room service

Baggage handling: Satisfaction level of baggage handling

Check-in service: Satisfaction level of Check-in service

Inflight service: Satisfaction level of inflight service

Cleanliness: Satisfaction level of Cleanliness

Departure Delay in Minutes: Minutes delayed when departure

Arrival Delay in Minutes: Minutes delayed when Arrival

Satisfaction: Airline satisfaction level(Satisfaction, neutral or dissatisfaction)
        """
    )
    st.write("### Preview of the Dataset:")
    st.dataframe(df)
    st.write("### Summary Statistics:")
    st.write(df.describe())
    # Exploratory Data Analysis (EDA)
if page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis 📊")

    # Numeric and Categorical Columns
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    obj_cols = df.select_dtypes(include=["object"]).columns.tolist()

    # Select Visualization Type
    st.subheader("Select a Visualization:")
    eda_type = st.multiselect("Choose visualization(s):", ["Histogram", "Box Plot",  "Bar Plot"])

    # Histogram
    if "Histogram" in eda_type:
        st.subheader("Histogram")
        selected_col = st.selectbox("Select a numerical column:", num_cols)
        if selected_col:
            st.plotly_chart(px.histogram(df, x=selected_col, title=f"Histogram of {selected_col}", color='Beverage'))

    # Box Plot
    if "Box Plot" in eda_type:
        st.subheader("Box Plot")
        y_col = st.selectbox("Select a column for Box Plot (y-axis):", num_cols)
        x_col = st.selectbox("Select a column for Box Plot (x-axis):", obj_cols)
        if y_col and x_col:
            st.plotly_chart(px.box(df, x=x_col, y=y_col, title=f"Box Plot: {y_col} vs {x_col}", color=x_col))

   
    # Bar Plot
    if "Bar Plot" in eda_type:
        st.subheader("Bar Plot")
        x_col = st.selectbox("Select x-axis (categorical):", obj_cols, key="bar_x")
        y_col = st.selectbox("Select y-axis (numerical):", num_cols, key="bar_y")
        if x_col and y_col:
            st.plotly_chart(px.bar(df, x=x_col, y=y_col, title=f"Bar Plot: {y_col} by {x_col}", color=x_col))

# Extras Page
if page == "Extras":
    st.title("Useful Information")

    st.subheader("Upload and Display an Image")
    uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

    st.subheader("Airline Demand-Supply Imbalance is Good for Revenue, Tough on Customer Experience, Says J.D. Power")

   