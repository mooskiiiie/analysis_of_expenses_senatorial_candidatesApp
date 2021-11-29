import streamlit as st
from PIL import Image

def app():

    header = st.container()
    body = st.container()
    image = Image.open('assets/b.png')

    with header:
        st.title('Conclusion/Recommendation Page')

    with body:
        st.subheader('Public Funding and Rules')

        st.markdown('To even the playing field, goverment funding can be provided to candidates. In Germany, parties receive funding in proportion to the votes they received.')
        st.image(image)
        st.markdown(""" 
        As seen, donations barely comprise 10% of the contributions. It is uncertain how much candidates in the Philippines are funded by the donors, but the Philippine Center for Independent Journalism(PCIJ) has said that candidates are backed by only a few donors.
        """)

        st.subheader('Spending Limits')
        st.markdown('A study conducted in the 2020 mayoral elections in Brazil showed positive results when spending limits. Mayors were limited to about 900k pesos in spending; scaled down depending on the demographics of regions. As a rule, the limit was set at 70% of the highest spender of the previous election.')
        st.markdown('This increased competitiveness and reduced reelection rates with donations. This also reduced the overspending and wealthy donations [5]')

        st.subheader('Final Recommendations')
        st.markdown('It is important to note that these measures are tailor fitted to these countries. The Philippines has to figure out its own blend of election policies and checks. ')
        st.markdown('''
        In summary, the Philippines should fine tune and consider the following methods to democratize elections and lower campaign spending:

        - Government funding
        - Political ad air time allocation
        - Spending limits
        ''')

