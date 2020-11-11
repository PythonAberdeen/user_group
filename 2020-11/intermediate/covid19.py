#!/usr/bin/env python
# coding: utf-8

# ### COVID-19
# * Explore covid19 data
# * Thanks to John Hopkins University for providing the data https://github.com/CSSEGISandData/COVID-19
#

# In[1]:


# essential libraries
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
from matplotlib import pyplot as plt
import plotly.graph_objects as go
from fbprophet import Prophet
import pycountry
import plotly.express as px
import plotly.io as pio
from functools import reduce
from plotly.subplots import make_subplots
import streamlit as st


# read and prepare the data
@st.cache
def load_prepare_data():
    # time seriese data
    url1 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    url2 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
    url3 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
    url4 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-07-2020.csv"

    df_confirmed = pd.read_csv(url1)
    df_deaths = pd.read_csv(url2)
    df_recovered = pd.read_csv(url3)

    # this file should have the latest figures
    df = pd.read_csv(url4, parse_dates=['Last_Update'])
    # rename some columns
    df_confirmed.rename(columns={'Country/Region': 'Country'}, inplace=True)
    df_recovered.rename(columns={'Country/Region': 'Country'}, inplace=True)
    df_deaths.rename(columns={'Country/Region': 'Country'}, inplace=True)
    df.rename(columns={'Last_Update': 'Date'}, inplace=True)
    df.rename(columns={'Country_Region': 'Country'}, inplace=True)
    # Work out confirmed, deaths and recovered cases
    df_confirmed = df_confirmed.reset_index(drop=True)
    # reshape the data frames
    cols_list = df_confirmed.columns.to_list()[:4]
    dates_list = df_confirmed.columns.to_list()[4:]
    # tidy data df_confirmed
    df_confirmedM = pd.melt(df_confirmed, id_vars=cols_list, value_vars=dates_list, var_name='Date',
                            value_name='Confirmed')
    cols_list = df_deaths.columns.to_list()[:4]
    dates_list = df_deaths.columns.to_list()[4:]
    # tidy data df_deaths
    df_deathsM = pd.melt(df_deaths, id_vars=cols_list, value_vars=dates_list, var_name='Date',
                         value_name='Deaths')
    # Recovered
    cols_list = df_recovered.columns.to_list()[:4]
    dates_list = df_recovered.columns.to_list()[4:]

    # dates_list
    # and finally tidy data df_recovered
    df_recoveredM = pd.melt(df_recovered, id_vars=cols_list, value_vars=dates_list, var_name='Date',
                            value_name='Recovered')
    # Merege the three time series into one
    df_all = [df_confirmedM, df_deathsM, df_recoveredM]
    covid19 = reduce(
        lambda left, right: pd.merge(left, right, on=cols_list + ['Date'], how='outer'), df_all)
    # covid19.head()
    # Tidy the df again: Rows to be represented by state, country, lat, long, and date
    df_covid19 = covid19.copy()
    cols_ids = df_covid19.columns[:5]

    cases = ['Confirmed', 'Deaths', 'Recovered']
    df_covid19 = pd.melt(df_covid19, id_vars=cols_ids, value_vars=cases, var_name='Cases',
                         value_name='Count')
    df_covid19['Date'] = pd.to_datetime(df_covid19['Date'], format='%m/%d/%y', errors='raise')
    df_covid19['Week'] = df_covid19['Date'].dt.strftime('%W')
    # df_covid19.head()
    covid19['Active'] = covid19['Confirmed'] - covid19['Deaths']
    # change the datatype for timedate
    covid19['Date'] = pd.to_datetime(covid19['Date'])

    return covid19


def top_countries_by_cases_by_date(top=30, least=False, byDate='28.01.2020', cases='Confirmed',
                                   title='28.03.2020'):
    # The code below should generate similar barplot to the one generated above using df

    temp = covid19.copy()
    temp['Date'] = pd.to_datetime(temp['Date']).dt.date

    mask = (temp['Date'] < byDate)
    temp = temp.loc[mask]

    temp = temp.groupby(['Country', 'Date'], as_index=False).agg(
        {'Confirmed': 'sum', 'Deaths': 'sum',
         'Active': 'sum', 'Recovered': 'sum'})

    temp = temp.groupby('Country')['Confirmed', 'Deaths', 'Recovered', 'Active'].max().reset_index()
    temp = temp.sort_values(by=cases, ascending=False)
    temp = temp.reset_index(drop=True)

    if least == True:
        temp = temp[:top]
    else:
        x = temp.shape[0]
        x = x - top
        temp = temp[x:]

    if cases == 'Confirmed':
        colors = 'rgb(26, 30, 250)'
    elif cases == 'Deaths':
        colors = 'rgb(255, 60, 30)'
    else:
        colors = 'rgb(100, 255, 150)'
    # colors = ['deepskyblue',] * 5
    # colors[3] = 'crimson'

    fig = go.Figure(data=[go.Bar(
        x=temp['Country'],
        y=temp[cases],
        text=temp[cases],
        marker_color=colors
        # marker_color=colors # marker color can be a single color value or an iterable
    )])
    # byDate.strftime("%A %d. %B %Y")
    # byDate.strftime("%d/%m/%y")
    # fig.update_layout(showlegend=False)

    fig.update_layout(template='plotly_white')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_yaxes(title_text="Number of Cases", hoverformat=".3f")
    fig.update_layout(
        title_text="Number of " + cases + " Cases: Top " + str(top) + ' Countries ' + title,
        title_x=0.5)
    return (fig)


# call the function to read and prepare data
covid19 = load_prepare_data()
# st.write(covid19.head())
byDate = pd.to_datetime(max(covid19['Date']))

# get min and max date from the data
start_date_df = pd.to_datetime(min(covid19['Date']))
end_date_df = pd.to_datetime(max(covid19['Date']))

#### streamlit code #####################

# create a nice title  use st.markdown(...)

st.markdown(
    "<h1 style='text-align: left; color: red;'>Aberdeen Python User Group Meeting (Nov-2020)</h1>",
    unsafe_allow_html=True)
# add an entry message if needed
msg_intro = '<br>A demo using streamlit. It loads covid19 related data, and '
msg_intro = msg_intro + 'show top n countries in the number of confirmed cases, deaths, or recovered cases.'
msg_intro = msg_intro + 'Data is extracted from John Hopkins University' + ' ' + ' [Github Repository](https://github.com/CSSEGISandData/COVID-19)'
msg_intro = msg_intro + ' and last updated on <b>' + str(
    pd.to_datetime(max(covid19['Date'])).strftime("%d-%m-%y")) + '</b>'
msg_intro = msg_intro + '. <p>Code for full example availble at [https://github.com/heyad/covid19World](https://github.com/heyad/covid19World)'

msg_intro = msg_intro + '<span style="color:gray"><b></b></span><br><br>'
st.markdown(msg_intro, True)

# create input fields (widgets)
# hint for date use data_input(), numbers number_input(), list of choices selectbox(...) and so on

start_date = st.sidebar.date_input('Enter start date', start_date_df) # create date_input on the side bar
end_date = st.sidebar.date_input('Enter end date',  end_date_df) # create date_input on the side bar
number_s = st.sidebar.number_input('Enter number of countries', min_value=1, max_value=30, value=10)# create number_input on the side bar (for to n countries)
cases_type = st.sidebar.selectbox('Case type', ['Confirmed', 'Deaths', 'Recovered']) # use selectbox to create choices to show either Confirmed, Deaths, or Recovered cases

# call the function top_countries_by_cases_by_date suing the user's input data
fig = top_countries_by_cases_by_date(number_s, True, end_date, cases_type,
                                     ' by ' + str(end_date.strftime("%d/%m/%y")))
# plot the diagram
st.plotly_chart(fig)

