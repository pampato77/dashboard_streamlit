
import pandas as pd 
import streamlit as st

from PIL import Image


st.title('Analisis de desempeño de los colaboradores') 
st.header('Dashboard')
st.text('Se analizaron los colaboradores de la empresa Clue ') 

image = Image.open('sun.webp')
st.image(image, caption='Logo de empresa',width='400px')

empleados = pd.read_csv('employeed.csv')
#buscar los encabezados del csv
#bdempleados = empleados[["name_employee","birth_date","age","gender","marital_status","hiring_date","position","salary","performance_score","last_performance_date","average_work_hours","satisfaction_level","absences"]]
