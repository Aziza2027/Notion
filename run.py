import streamlit as st
import pandas as pd
st.set_page_config(layout="wide",page_title="Kanban - 2023",page_icon="🗓️",initial_sidebar_state="collapsed")
file = './data.csv'

df = pd.read_csv(file)
# print(df)

st.header('Aziza\'s 2023 Kanban :sunglasses:')

months = [
    "August",
    "September",
    "October",
    "November",
    "December",
    "June",
    "July",
    "May",
]

modification_container = st.container()

with modification_container:
    to_filter_columns = [st.selectbox("Choose month", ["All"]+months)]
    if to_filter_columns[0] =='All':
        to_filter_columns = months.copy()

height = (df.shape[0] + 1) * 35 + 3 

edited_df = st.data_editor(
    df[df.Month.isin(to_filter_columns)], 
    num_rows='dynamic',
    column_config={
        "Status": st.column_config.SelectboxColumn(
            "Status",
            help="The category of the app",
            width="medium",
            options=[
                "🟥🟥🟥",
                "🏆🏆🏆",
            ],
        ),
        "Month": st.column_config.SelectboxColumn(
            "Month",
            help="The category of the app",
            width="medium",
            options=months,
        )
    },

    use_container_width=True,
    )

def save_dataframe_to_csv():
    # Save the DataFrame to a CSV file
    if len(to_filter_columns) > 2:
        edited_df.to_csv(file, index=False)
        st.success("DataFrame saved")
    else:
        st.error("Oops! You did not choose all months.")

col1, col2 = st.columns([2, 1])

if col2.button("Save DataFrame to CSV"):
        save_dataframe_to_csv()





