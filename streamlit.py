
import pandas as pd 
import streamlit as st

from PIL import Image

base = pd.read_csv('employeed.csv)
st.title('Analisis de desempeño de los colaboradores') 
st.header('Dashboard')
st.text('Se analizaron los colaboradores de la empresa Clue ') 

image = Image.open('sun.webp')
st.image(image, caption='Logo de empresa')

