import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

t = np.linspace(0, 0.05, 1000)
v = 200*np.sqrt(2)*np.sin(2*np.pi*60*t)

fig1 = go.Figure(data=go.Scatter(x=t, y=v))
fig2, ax = plt.subplots()
ax.plot(t, v)

st.markdown("# Primeira Etapa - WebApp")
st.markdown("## Gráfico da Função 200√2.sin(2.π.60.t)")
st.markdown("Este é o gráfico de uma função senoidal")
st.plotly_chart(fig1)

ttt = np.linspace(0, 0.05, 1000)
vvv = (200*np.sqrt(2)*np.sin(2*np.pi*60*t)) ** 2

fig1 = go.Figure(data=go.Scatter(x=ttt, y=vvv))
fig2, ax = plt.subplots()
ax.plot(ttt, vvv)

st.markdown('## Gráfico da Função (200√2.sin(2.π.60.t))²')
st.markdown(" Este é o gráfico de uma função senoidal")
st.plotly_chart(fig1)
