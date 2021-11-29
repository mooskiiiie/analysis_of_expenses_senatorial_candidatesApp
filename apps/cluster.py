import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def app():

    code = """
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(df_scaled_ss)
    labels = kmeans.predict(df_scaled_ss)
    """
    code1 = """
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df_scaled_ss = scaler.fit_transform(df_final)
    """

    code3 = """
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()

    df_final.drop(columns = ['Cluster_Labels'], inplace = True)

    df_minmax = scaler.fit_transform(df_final)
    df_minmax = pd.DataFrame(df_minmax, index=df_final.index, columns=df_final.columns)

    df_minmax['Cluster_Labels'] = labels

    df_clusters = df_minmax.set_index("Cluster_Labels")
    df_clusters = df_clusters.groupby("Cluster_Labels").mean().reset_index()
    df_clusters
    """

    code4 = """
    from math import pi

    def make_spider( row, title, color):
 
    categories=list(df_clusters)[1:]
    N = len(categories)
 
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
 
    ax = plt.subplot(3,3,row+1, polar=True )
 
    ax.set_theta_offset(pi / 3.5)
    ax.set_theta_direction(-1)
    
    plt.xticks(angles[:-1], categories, color='grey', size=8)
 
    ax.set_rlabel_position(0)

    plt.yticks([-0.25, 0, 0.25, 0.5, 0.75, 1], [-0.25, 0, 0.25, 0.5,0.75, 1], color="grey", size=7) #formmscaled
    plt.ylim(-0.25,1)

    values=df_clusters.loc[row].drop('Cluster_Labels').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)
 
    plt.title(title, size=14, color=color, y=1.1)
    """

    code5 = """
    my_dpi=100
    plt.figure(figsize=(1200/my_dpi, 1200/my_dpi), dpi=my_dpi)
    plt.subplots_adjust(hspace=0.5)

    my_palette = plt.cm.get_cmap("Set2", len(df_clusters.index))

    for row in range(0, len(df_clusters.index)):
        make_spider(row=row, 
            title='Segment '+(df_clusters['Cluster_Labels'][row]).astype(str), 
            color=my_palette(row))
    
    plt.savefig('clusters.png', dpi = 300)
    plt.show()
    """
    
    header = st.container()
    body = st.container()
    image = Image.open('assets/cluster.png')

    df_senatorialvotes = pd.read_csv('data/2019-senatorial-votes.csv')
    df_candidatecamps = pd.read_csv('data/2019-candidate-campaigns.csv')
    merged = df_candidatecamps.merge(df_senatorialvotes, how='inner')

    with header:
        st.title('Cluster Analysis')
        st.markdown('In order for us to implement K-means clustering, we had to first identify what is the most optimized number of clusters.')
        st.markdown('Before implementing the algorithm, we first had to scale our data.')
        st.code(code1, language='python')

        st.markdown('After experimenting with different number of clusters, we have decided to set our K to 3 for this made the most sense based on our data.')
        st.code(code, language='python')

        st.markdown('Right after implementing the algorithm, the next step was to assign these clusters as Cluster Labels inside our working dataframe.')
        st.markdown('In order for us to perform a Radar Analysis on our current data, we first had to scale our data once again using MinMaxScaler')
        st.code(code3, language='python')

        st.markdown('All that was left to do is to plot the Radar Graph.')
        st.code(code4, language='python')
        st.code(code5, language='python')

        st.write("")
        st.write("")

        st.image(image, width=900)