import streamlit as st
import numpy as np
import pandas as pd
import math

st.title("Graphs")

def square(x):
    return x**2

def exp_dec(x):
    return math.e ** (x/-8) * math.cos(x)

x = []
for loop in np.arange(-2, 2.1, .1):
    x.append(loop)
y = [square(v) for v in x]
df = pd.DataFrame(zip(x, y), columns=['x', 'y'])
df = df.set_index('x')
st.line_chart(df)

x = []
for loop in np.arange(-2*math.pi, 2*math.pi, .1):
    x.append(loop)
y = [math.sin(v) for v in x]
df = pd.DataFrame(zip(x, y), columns=['x', 'y'])
df = df.set_index('x')
st.line_chart(df)

x = []
for loop in np.arange(0, 10, .1):
    x.append(loop)
y = [exp_dec(v) for v in x]
df = pd.DataFrame(zip(x, y), columns=['x', 'y'])
df = df.set_index('x')
st.line_chart(df)

