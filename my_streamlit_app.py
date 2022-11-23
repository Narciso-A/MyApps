import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

#link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_auto = pd.read_csv(link)

# Here we use "magic commands":
df_auto

# st.line_chart(df_weather['MAX_TEMPERATURE_C'])

viz_correlation = sns.heatmap(df_auto.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True),
								annot=True)

st.pyplot(viz_correlation.figure)

viz_correlation_0 = plt.hist(df_auto['weightlbs'])

st.pyplot(viz_correlation_0.figure)

