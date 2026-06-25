import streamlit as st
from fuctions.plot import plot_history

st.title('Stocks History')
st.write('Look the stock valeus')

ticker =st.sidebar.text_input (
    'Choose the ticker: ',
    value = 'NVDA'
)

fig = plot_history(ticker)
st.plotly_chart(fig)