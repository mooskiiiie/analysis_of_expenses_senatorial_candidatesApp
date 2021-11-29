from enum import auto
import streamlit as st
from PIL import Image

def app():
    
    header = st.container()
    body = st.container()
    image = Image.open('assets/aaa.png')
    column1, column2, column3 = st.columns(3)
    column4, column5, column6 = st.columns(3)
    column1, column2, column3 = st.columns(3)

    with header:
        st.title('Methodology')

    with body:
        st.subheader('Step 1: Data Pre-Processing')
        st.markdown('''
        First, we had to consolidate, filter, and merge the datasets to make sure we have the right data.
        We then had to drop columns that weren't related to our objective.
        ''')
        st.image(image, width=45)
        
        st.subheader('Step 2: Data Wrangling')
        st.markdown('''
        In this step, we manipulated, sorted, and grouped the data to prepare for exploratory data analysis.
        ''')
        st.image(image, width=45)
        
        
        st.subheader('Step 3: Exploratory Data Analysis')
        st.markdown('''
        For our EDA, we did a correlation analysis to help us understand our features more
        in order to give way for Feature Engineering.
        ''')
        st.image(image, width=45)
        
        st.subheader('Step 4: Feature Engineering')
        st.markdown('''
        In this step, we selected the features that we would need in order to train the model.
        ''')
        st.image(image, width=45)

        st.subheader('Step 5: Modeling')
        st.markdown('''
        For modeling, we decided to do K-means clustering to answer our problem statement.
        ''')
        st.image(image, width=45)

        st.subheader('Step 6: Getting Insights')
        st.markdown('''
        In order to extract insights from our cluster analysis, we visualized our model through radar analysis.
        ''')
        
        