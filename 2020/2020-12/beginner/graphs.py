import streamlit as st
import pandas as pd
import numpy as np
import math

STEPS=1000
funcs = {'y=x**2': (lambda x: x**2, -2, 2),
         'y=sin(x)': (math.sin, -2*math.pi, 2*math.pi),
         'y = e ** (x/-8) * cos(x)':
         (lambda x: (math.e**(x/-8))*math.cos(x), 0, 10)}

st.title("Graphs")
option = st.selectbox('Which function do you want to plot?',
                      list(funcs.keys()))
if option:
    f, low, high = funcs[option]
    x = list(np.arange(low, high, (high-low)/STEPS))
    y = [f(v) for v in x]
    df = pd.DataFrame(zip(x, y), columns=['x','y'])
    df = df.set_index('x')
    st.line_chart(df)
