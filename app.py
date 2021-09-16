#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Wed Sep 15 @author: alexandrebelli"""import requestsimport pandas as pdimport streamlit as stimport plotly.express as pximport osimport dotenvfrom dotenv import load_dotenvimport numpy as npdef datetime(x):    return np.array(x, dtype=np.datetime64)symbol = st.sidebar.text_input("Stock Symbol",'BA')st.title("Visualizing Stock's Closing Cost for - "+str(symbol))load_dotenv()CONSUMER_KEY = os.environ.get("Key")url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+str(symbol)+'&outputsize=full&apikey='+str(CONSUMER_KEY)+'&datatype=csv'data = pd.read_csv(url)print(data)data['timestamp'] = datetime(data['timestamp'])data2 = data.drop(columns=['open', 'high','low', 'volume'])data2['year'] = data2['timestamp'].dt.yeardata2['month'] = data2['timestamp'].dt.monthoption_year = np.unique(data2['year'].values)print(option_year)year = st.sidebar.selectbox("Select a year", option_year)option_month = data2['month'].valuesoption_month = np.unique(option_month)print(data2)month = st.sidebar.selectbox('Select a Month', option_month)data3 = data2.loc[(data2["year"] == year) & (data2["month"] == month)]#print(data3)fig = px.line(data3, x="timestamp", y="close", labels={                     "timestamp": "Date",                     "close": "Closing Cost"                 })st.plotly_chart(fig, use_container_width=True)