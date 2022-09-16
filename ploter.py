import plotly.express as px
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
def scatter(data):
    x_list=list(range(1,len(data)+2))

    data['x_list']=x_list


    fig=px.scatter(x=x_list,y=data)
    return fig


def scatter_comp(data,data2,cut):
    if cut=="no":
        x_list = list(range(1, len(data) + 2))
        x_list2 = list(range(1, len(data2) + 2))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_list, y=data,
                                 mode='markers',
                                 name='Nieprawidłowe'))
        fig.add_trace(go.Scatter(x=x_list2, y=data2,
                                 mode='markers',
                                 name='Prawidłowe'))
        return fig
    if cut=="yes":
        x_list2 = list(range(1, len(data2) + 2))
        x_list = list(range(1, len(data2) + 52))
        fig = go.Figure()
        data = data.iloc[100:]
        fig.add_trace(go.Scatter(x=x_list, y=data,
                                 mode='markers',
                                 name='Nieprawidłowe'))
        fig.add_trace(go.Scatter(x=x_list2, y=data2,
                                 mode='markers',
                                 name='Prawidłowe'))
        return fig