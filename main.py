import streamlit as st
import streamlit_folium
import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
from multiapp import MultiApp
from apps import home, links, methods, info, conclusion, cluster, analysis
warnings.filterwarnings('ignore')

app = MultiApp()

app.add_app('Introduction', home.app)
app.add_app('Data Information', info.app)
app.add_app('Methodology', methods.app)
app.add_app('Exploratory Data Analysis', analysis.app)
app.add_app('Cluster Analysis', cluster.app)
app.add_app('Conclusion & Recommendations', conclusion.app)
app.add_app('Resources', links.app)



app.run()