import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('Water Temperature')


DATA_URL = ('c:/temp/waterquality.csv')
#Temp_COLUMN = DATA_URL['WaterTemp']

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #data[Temp_COLUMN] = pd.to_datetime(data[Temp_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
     st.subheader('Raw data')
     st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data['pH'])
st.bar_chart(hist_values)

value_counts = data['WaterTemp'].value_counts()
st.write("### Water Temperature Pie Chart")
fig, ax = plt.subplots()
ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)