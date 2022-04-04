import streamlit as st
import pandas as pd

st.image('Figura_data-science.png', width = 400)
st.sidebar.image('Figura_data-science.png', use_column_width = 'always') 

st.header('Aula 7 - Dia 05/04/2022')

st.markdown('# Meu Web App ')


dados = pd.read_csv('prof-dados-resumido.csv')

st.write(dados)

var = st.sidebar.selectbox('Selecione uma variável', ['Idade', 'Profissão'])

ms = dados['Salário'].groupby(dados[var]).mean()

st.write(ms)
st.table(dados.describe())

variaveis = dados.columns.tolist()

var1 = st.sidebar.selectbox('Selecioe uma variável', variaveis)

plot = dados['Salário'].groupby(dados[var1]).mean().plot(kind = 'barh')
st.pyplot(plot.figure)

