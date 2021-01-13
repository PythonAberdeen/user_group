import streamlit as st
import pandas as pd

from check_env_log import parse_log

log_file = st.file_uploader("Upload log file")

if log_file is not None:
    data = [e for e in parse_log(log_file.readlines())]
    df = pd.DataFrame(data, columns=['time', 'voltage', 'current', 'power',
                                 'inlet_temp', 'local_temp', 'core_temp'])
    df = df.set_index('time')
 
    st.title("Power")
    
    st.line_chart(df[['voltage', 'current', 'power']])

    st.title("Temperatures")
    st.line_chart(df[['inlet_temp', 'local_temp', 'core_temp']])

    st.write(df.describe())
