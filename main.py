import streamlit as st
import plotly
import pandas as pd
import sklearn
import scipy
import reader
import ploter
table1=reader.csv_reader('loty1.csv')
table2=reader.csv_reader('loty2.csv')
st.write("witam")
column_selected=st.selectbox(
    'Select column',
    table1.columns
)
cut="no"
agree = st.checkbox('cut')

if agree:
    cut="yes"

#st.plotly_chart(ploter.scatter(table1[f"{column_selected}"]))
#st.plotly_chart(ploter.scatter(table2[f"{column_selected}"]))

st.plotly_chart(ploter.scatter_comp(table1[f"{column_selected}"],table2[f"{column_selected}"],cut))

