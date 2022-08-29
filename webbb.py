import streamlit as st
import numpy as np
import plotly.graph_objects as go

t = np.linspace(0, 0.05, 1000)
v = 220*np.sqrt(2)*np.sin(2*np.pi*60*t)
c = (220*np.sqrt(2)*np.sin(2*np.pi*60*t))*2

fig1 = go.Figure(data=go.Scatter(x=t, y=v))
fig2 = go.Figure(data=go.Scatter(x=t, y=c))


st.markdown("# Tarefa Primeira Etapa WebApp")
st.markdown("Gráfico 1")
st.markdown("## 200√2*sin(2π60t)")
st.plotly_chart(fig1)
st.markdown("Gráfico 2")
st.markdown("## [200√2*sin(2π60t)]²")
st.plotly_chart(fig2)
