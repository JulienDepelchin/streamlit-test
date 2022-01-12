import streamlit as st
import pandas as pd

st.title("Test de l'application Streamlit")


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

st.header('Affichage de la dataframe')
df_cars

import seaborn as sns

viz_correlation = sns.heatmap(df_cars.corr(),
                              center=0,
                              cmap=sns.color_palette("vlag", as_cmap=True)
                              )

st.header('Analyse de corrélation avec un graphique')
st.pyplot(viz_correlation.figure)

import plotly.express as px

st.header("Analyse de corrélation et ajout d'un filtre")
Host_Country = st.selectbox('Sélectionnez un continent:', ('US.', 'Japan.', 'Europe.'))

fig = px.scatter(df_cars[df_cars["continent"].str.contains(f"{Host_Country}")], x="cubicinches", y="hp", size="cylinders",
				 log_x=True, size_max=10)
fig.show()



st.plotly_chart(fig, use_container_width=True)

st.header("Test avec un deuxième filtre")
Host_Cylinders = st.selectbox('Sélectionnez un nombre de cylindres:', (3, 4, 6, 8))
fig2 = px.scatter(df_cars[df_cars["cylinders"] == Host_Cylinders], x="cubicinches", y="mpg",
				 log_x=True, size_max=10)
fig.show()


st.plotly_chart(fig2, use_container_width=True)