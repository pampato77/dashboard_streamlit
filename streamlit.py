import pandas as pd 
import streamlit as st
from PIL import Image
from bokeh.plotting import figure

st.title('Analisis de desempeño de los colaboradores') 
st.header('Dashboard')
st.text('Se analizaron los colaboradores de la empresa Clue ') 

image = Image.open('sunlogo.jpeg')
st.image(image, caption='SoftSun')

empleados = pd.read_csv('employeed.csv')
#buscar los encabezados del csv
bdempleados = empleados[["name_employee","birth_date","age","gender","marital_status","hiring_date","position","salary","performance_score","last_performance_date","average_work_hours","satisfaction_level","absences"]]

#Control para seleccionar el genero del empleado
Select_gen = st.radio("Seleccionar genero", bdempleados['gender'].unique()) 
#st.write("Seleccionar género:", Select_gen) 

#Control para seleccionar un rango del puntuaje
#Select_performance = st.radio("Seleccionar puntaje de desempeño", bdempleados['performance_score'].unique()) 
#st.write("Seleccionar puntaje:", Select_performance)

#Control deslizante para seleccionar el estado civil
#seleccion_edoCivil = st.selectbox("Selección del estado civil del empleado",  bdempleados['marital_status'].unique()) 

#Grafica de puntuaje de desempeño
#p=figure()
#p.circle(x='performance_score', y='position',
#        source=df,
#         size=10, color='green')

#p.title.text ='Puntuaje de desempeño'
#p.xaxis.axis_label = 'performance_score'
#p.yaxis.axis_label = 'position'

#st.bokeh_chart(p, use_container_width=True)
#st.altair_chart(c, use_container_width=True)
