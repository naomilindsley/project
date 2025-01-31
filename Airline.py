import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Set Streamlit page configuration
st.set_page_config(page_title="Airline Satisfaction Prediction", page_icon="✈️")

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis", "Extras"])

# Function to load data
# Data Preparation
st.title("Upload and Display Dataset")

uploaded_file = st.file_uploader("Upload your file (csv)", type=["csv"])
pd.read_csv(uploaded_file)
st.write("Uploaded file preview:")
# Home Page
# Home Page
if page == "Home":
    st.title("Airline Satisfaction Prediction Project ✈️")
    st.subheader("Welcome!")
    st.write(
        """
        The dataset used in this project is the "Airline Passenger Satisfaction" dataset.
        It contains information about airline passengers, including features such as flight distance,
        seat comfort, inflight entertainment, and more.
        """
    )
    
    st.subheader("Upload and Display an Image")
    uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"], key="image_uploader")
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

# Data Overview Page
if page == "Data Overview":
    st.title("Data Overview")
    

# Exploratory Data Analysis (EDA) Page
if page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis 📊")
    

 # Select Visualization Type
    st.subheader("Select a Visualization:")
    eda_type = st.multiselect("Choose visualization(s):", ["Histogram", "Box Plot", "Bar Plot"])

        # Histogram
if "Histogram" in eda_type:
            st.subheader("Histogram")
            selected_col = st.selectbox("Select a numerical column:", num_cols, key="histogram")
            if selected_col:
                st.plotly_chart(px.histogram(df, x=selected_col, title=f"Histogram of {selected_col}"))

        # Box Plot
if "Box Plot" in eda_type:
            st.subheader("Box Plot")
            y_col = st.selectbox("Select a column for Box Plot (y-axis):", num_cols, key="box_y")
            x_col = st.selectbox("Select a column for Box Plot (x-axis):", obj_cols, key="box_x")
            if y_col and x_col:
                st.plotly_chart(px.box(df, x=x_col, y=y_col, title=f"Box Plot: {y_col} vs {x_col}", color=x_col))

        # Bar Plot
if "Bar Plot" in eda_type:
            st.subheader("Bar Plot")
            x_col = st.selectbox("Select x-axis (categorical):", obj_cols, key="bar_x")
            y_col = st.selectbox("Select y-axis (numerical):", num_cols, key="bar_y")
            if x_col and y_col:
                st.plotly_chart(px.bar(df, x=x_col, y=y_col, title=f"Bar Plot: {y_col} by {x_col}", color=x_col))
else:
        st.warning("Please upload a dataset to perform EDA.")

# Extras Page
if page == "Extras":
    st.title("Useful Information")
    st.subheader("Airline Demand-Supply Imbalance is Good for Revenue, Tough on Customer Experience, Says J.D. Power")
    st.write(
        '''
        [Link to the article](https://www.jdpower.com/business/press-releases/2023-north-america-airline-satisfaction-study)
        '''
    )
