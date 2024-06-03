import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Analisis de desempeño de los colaboradores') 
st.header('Dashboard')
st.text('Se analizaron los colaboradores de la empresa Clue ') 

st.sidebar.image("sunlogo.jpeg")
st.sidebar.markdown("##")

empleados = pd.read_csv('employeed.csv')
#buscar los encabezados del csv
bdempleados = empleados[["name_employee","birth_date","age","gender","marital_status","hiring_date","position","salary","performance_score","last_performance_date","average_work_hours","satisfaction_level","absences"]]

#Control para seleccionar el genero del empleado
Select_gen = st.radio("Seleccionar genero", bdempleados['gender'].unique()) 
st.write("Seleccionar género:", Select_gen) 

#Control para seleccionar un rango del puntuaje
Select_performance = st.radio("Seleccionar puntaje de desempeño", bdempleados['performance_score'].unique()) 
st.write("Seleccionar puntaje:", Select_performance)

#Control deslizante para seleccionar el estado civil
seleccion_edoCivil = st.selectbox("Selección del estado civil del empleado",  bdempleados['marital_status'].unique()) 

#Grafica de la distribución de los puntuaje de desempeño
df_selection=bdempleados.query("gender == @gender & performance_score == @performance_score & marital_status == @marital_status")

#Grafica para visualizar las horas
avg_hours_gender=(
    df_selection.groupby(by=['gender']).sum()
[['average_work_hours']].sort_values(by="average_work_hours"))

fig_hours_gender=px.bar(avg_hours_gender,
                        x=avg_hours_gender.index,
                        y="average_work_hours", 
                        orientation="v",
                        title="Average Worked Hours by Gender",
                        labels=dict(average_work_hours="Total Worked Hours", gender="Gender"),
                        color_discrete_sequence=["#7ECBB4"],
                        template="plotly_white")

fig_hours_gender.update_layout(plot_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig_hours_gender)



