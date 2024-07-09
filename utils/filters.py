import pandas as pd
import streamlit as st
from pandas.api.types import is_numeric_dtype, is_datetime64_any_dtype, is_categorical_dtype, is_string_dtype


def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df

    df = df.copy()
    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                filter_values = st.multiselect(f"Values for {column}",
                                               options=df[column].unique(),
                                               default=list(
                                                   df[column].unique()))
                df = df[df[column].isin(filter_values)]
            elif is_numeric_dtype(df[column]):
                min_val, max_val = df[column].min(), df[column].max()
                min_select, max_select = st.slider(
                    "Select range for " + column, min_val, max_val,
                    (min_val, max_val))
                df = df[(df[column] >= min_select)
                        & (df[column] <= max_select)]
            elif is_datetime64_any_dtype(df[column]):
                start_date, end_date = df[column].min(), df[column].max()
                start_select, end_select = st.date_input(
                    "Select date range for " + column, [start_date, end_date])
                df = df[(df[column] >= pd.to_datetime(start_select))
                        & (df[column] <= pd.to_datetime(end_select))]
            else:  # Add support for text and other data types that are neither numeric nor datetime
                text_values = st.text_input(
                    f"Enter text to filter for {column}")
                if text_values:
                    df = df[df[column].str.contains(text_values, na=False)]

    return df
