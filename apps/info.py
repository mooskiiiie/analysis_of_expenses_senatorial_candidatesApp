import streamlit as st
import pandas as pd

def app():

    @st.cache
    def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    df = pd.read_csv('data/spend-social_df.csv')    
    csv = convert_df(df)
    header = st.container()
    columns = st.container()
    column1, column2, column3 = st.columns(3)
    

    with header:
        st.title('Data Information')
        st.subheader('Data')
        st.markdown('''
        The data used for the analysis is a merged dataset from the 2019-candidate-campaigns
        and 2019-senatorial-votes datasets.
        ''')
        st.dataframe(df)
        convert_df(df)
        st.download_button(
            label="Download dataset",
            data=csv,
            file_name='data/spend-social_df.csv',
            mime='text/csv',
        )

    with columns:
        st.subheader('Columns')
        with column1:
            st.markdown('Candidate')
            st.caption('This columns shows all the senatorial candidates in 2019')
            st.markdown('Votes')
            st.caption('This column refers to the sum of votes per candidate')
            st.markdown('Total Expenditures')
            st.caption('This column refers to the total expenses per candidate')
            st.markdown('Travel Expenses')
            st.caption('This column refers to the travel expenses per candidate')
            st.markdown('Compensation of campaigners')
            st.caption('Amount of money compensated for campaigners')
            st.markdown('Communications')
            st.caption('Communication expenses')
            st.markdown('Stationary, printing, and distribution')
            st.caption('Amount of expenses for printing, etc.')
        
        with column2:
            st.markdown('Employment of poll watchers')
            st.caption('Expenses for poll watchers')
            st.markdown('Rent, maintenance, etc.')
            st.caption('Expenses on rent, etc.')
            st.markdown('Political meetings and rallies')
            st.caption('Expenses for political meetings')
            st.markdown('Pol ads')
            st.caption('Total expenses on political advertisements')
            st.markdown('Employment of counsel')
            st.caption('Expenses for counsel employment')
            st.markdown('Copying and classifying list of voters')
            st.caption('Expenses on copying list of voters')
            st.markdown('Printing of sample ballots')
            st.caption('Expenses on the printing of sample ballots')
        
        with column3:
            st.markdown('Facebook - number of candidate posts')
            st.caption('Total number of Facebook posts from the candidate')
            st.markdown('Facebook - total comments')
            st.caption('Total number of comments on candidate\'s posts')
            st.markdown('Facebook - total shares')
            st.caption('Total number of candidate\'s posts\'s shares')
            st.markdown('Facebook - total reactions')
            st.caption('Total number of reactions on candidate\'s posts')
            st.markdown('win')
            st.caption('Indicates if the candidate won or lost')