import streamlit as st

def app():

    header = st.container()
    problem = st.container()
    objectives = st.container()

    with header:
        st.title('Analysis of Valuable Insights on Improving Philippine Elections Spending')
        st.markdown('''
        Election is one of the biggest manifestations of a democracy. With elections, politicians derive their power from the people. However, 
        it is also known that some politicians are not beholden to the people but to corporate interests. In the Philippines, known political 
        dynasties reign supreme in local and national elections. Its candidates are mostly funded by a few wealthy donors. [1] This is a problem 
        shared by democracies around the world. In the USA, politicians have been known to block climate and healthcare measures in opposition to popular support. [2]
        ''')

        st.markdown('**Are elections really democratic if there is money in politics?**')

    with problem:
        st.subheader('Problem Statement')
        st.markdown(''' 
        In the 2019 elections, 39% of senatorial candidates did not expend any money (non-spenders). However, none of them won a seat in the senate.
        Further, 89% of the funding of spender candidates are expended on political advertising. 
        
        As such, our group wanted to explore:
        ''')
        st.info('**What is the influence of campaign spending of senatorial candidates on the number of votes?**')

    with objectives:
        st.subheader('Objectives')
        st.markdown('- To investigate what is the influence of campaign spending of senatorial candidates on the number of votes')
        
      
            
    
    
