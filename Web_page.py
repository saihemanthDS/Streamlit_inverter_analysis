import os

import streamlit as st
import pandas as pd
import numpy as np
import os
# st.write("Current directory:", os.getcwd())

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
# st.image("https://www.facebook.com/photo/?fbid=136141409173512&set=a.136141419173511", width = 200)

st.header(':green[Greenko Energy Pvt.Ltd]',divider = 'orange')

st.title("Solar Inverter Data Analysis")
st.write('This is the data available in the S3 File (Top 5 records)')

table = pd.read_json('90-1-Renewable-INVERTER-20241008230030.json')

table.set_index('TimeStamp',inplace = True)

st.dataframe(table.head(), use_container_width=True)

st.subheader('Total Energy Produced by the Inverter')
st.line_chart(table.groupby('Inverter')['ENG_TOTAL'].agg(np.max),x_label='Inverter', y_label='Total Energy')

st.subheader('Time V/s Soil loss')
st.line_chart(table,y = 'SOIL_LOSS',color = (255,0,0))

st.subheader('Breakdown Loss of the Inverter')
st.line_chart(table.groupby('Inverter')['BREAKDOWN_LOSS'].agg(np.sum),x_label='Inverter', y_label='Breakdown Loss',color = (128,0,0))

st.subheader('Inverter V/s Cabinet Temperature')
temp = table.groupby('Inverter')['CAB_TEMP'].agg(np.mean)
st.bar_chart(temp, x_label='Inverter', y_label='Cabinet Temperature')




# st.bar_chart(chart_data)
