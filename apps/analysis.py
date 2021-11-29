import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def app():
    header = st.container()
    body = st.container()
    image = Image.open('assets/g1.png')
    image2 = Image.open('assets/g2.png')
    image3 = Image.open('assets/g3.png')
    

    df_senatorialvotes = pd.read_csv('data/2019-senatorial-votes.csv')
    df_candidatecamps = pd.read_csv('data/2019-candidate-campaigns.csv')
    #merged = df_candidatecamps.merge(df_senatorialvotes, how='inner')

    with header:
        st.header('Exploratory Data Analysis')

    with body:
        st.subheader('Insight on candidate demographics')
        st.markdown('First, We classified candidates accdg to those who invested in their political campaigns (spenders), and those who did not spend any money on campaigns (non-spenders) ')
        st.image(image, width=300)
        st.markdown('- All candidates who won the 2019 senatorial elections invested in their political campaigns (spenders)')
        st.markdown('- However, some candidates did not have any financial support to utilize in their campaigns.  (non-spenders)')

        st.subheader('2019 Top Election Candidate Spenders')
        st.image(image2, width=600)
        st.markdown('- As you can see in this graph, 6 out of 12 won among the top spenders.')

        st.subheader('Insight on candidate spendings')
        st.image(image3, width=500)
        st.markdown('- 11 out of 12 of the winning candidates invested mainly political ads')
        st.markdown('- But does spending relate to candidate victory?')

