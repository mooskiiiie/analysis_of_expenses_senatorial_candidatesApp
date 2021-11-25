import streamlit as st
import streamlit_folium
import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')


page_index = st.sidebar.radio('Navigation', ['Introduction', 'Methodology', 'Exploratory Data Analysis', 'Regression Analysis', 'Clustering Analysis'])


if page_index == 'Introduction':
    st.title('Introduction')

elif page_index == 'Methodology':
    st.title('Methodology')

elif page_index == 'Exploratory Data Analysis':
    st.title('Exploratory Data Analysis')

elif page_index == 'Regression Analysis':
    st.title('Regression Analysis')

elif page_index == 'Clustering Analysis':
    st.title('Clustering Analysis')

    