import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

# Entetes
st.title('Cars')
st.sidebar.image('voiture_clip_art_gratuit_dessin.png')

# data !
link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_auto = pd.read_csv(link)

# Selection continent
continent_list = df_auto['continent'].unique()
countries = st.sidebar.multiselect(
	"Choix des continents", 
	continent_list, 
	continent_list[0]
	)

# Table 
df_auto_continent = df_auto[df_auto['continent'].isin(countries)]
st.write('Table des valeurs')
df_auto_continent

# Matrice corrletion
fig, ax = plt.subplots()
plt.title('Correlation')
ax = sns.heatmap(
	df_auto_continent.corr(), 
	center=0,
	cmap = sns.color_palette("vlag", as_cmap=True),
	annot=True
	)
st.pyplot(fig)
st.write('Poids et cylindrée évoluent dans le meme sens')

# Distribution poids
fig, ax = plt.subplots()
plt.title('Distribution')
ax = sns.histplot(data=df_auto_continent, x='weightlbs')
st.pyplot(fig)
st.write('Les Poids se repartissent de 1500 à 5000 lbs')

st.balloons()

