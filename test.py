
import streamlit as st
import pandas as pd

file = './data.csv'

df = pd.read_csv(file)

edited_df = st.data_editor(df, num_rows='dynamic')
