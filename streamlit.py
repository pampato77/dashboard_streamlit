
import pandas as pd 
import streamlit as st

from PIL import Image

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
rango = st.expander("Opción de rango de desempeño del empleado")  
seleccion_Rango = rango.slider( "Seleccionar el rango",  
Min_value = float(bdempleados['performance_score'].min()), 
max_value = float(bdempleados['performance_score'].max()) 
)  

# plasmar la barras deslizantes 
st.write(f"Rango de desempeño del empleado { rango}: { seleccion_Rango.shape[0]}") 

 #Control deslizante para seleccionar el estado civil
seleccion_edoCivil = st.selectbox("Selección del estado civil del empleado",  bdempleados['marital_status'].unique()) 




