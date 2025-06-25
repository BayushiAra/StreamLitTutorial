import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
from datetime import time, datetime

#if "role" not in st.session_state:
#    st.session_state.role = None

settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
demo1page = st.Page("SubDemo1.py", title="SubDemo 1", icon=":material/settings:")
demo2page = st.Page("SubDemo2.py", title="SubDemo 2", icon=":material/settings:")

demo1_btn = st.button('Demo1 Page')
demo2_btn = st.button('Demo2 Page')




# Example 1
st.write('Hello, *World!* :sunglasses:')

# Example 2
st.write(1234)

# Example 3
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10,20,30,40]
})
st.write(df)

# Example 4
st.write('Below is a Dataframe:', df, 'Above is a Dataframe.')

# Example 5 
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a','b','c'])
c = alt.Chart(df2).mark_circle().encode(x='a',y='b',size='c', color='c', tooltip=['a','b','c'])
st.write(c)

st.subheader('Range Slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))

st.write('values:', values)

st.subheader('Range time slider')
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11,30), time(12,45)))

st.write("You're scheduled for: ", appointment)