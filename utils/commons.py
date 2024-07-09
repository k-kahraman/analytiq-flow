import pandas as pd
from pandas.api.types import is_numeric_dtype, is_datetime64_any_dtype, is_categorical_dtype


def detect_data_type(df: pd.DataFrame):
    """
    Detects and returns the data types of columns in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.

    Returns:
        dict: A dictionary mapping column names to their detected data type.
    """
    data_types = {}
    for column in df.columns:
        if is_numeric_dtype(df[column]):
            data_types[column] = 'numeric'
        elif is_datetime64_any_dtype(df[column]):
            data_types[column] = 'datetime'
        elif is_categorical_dtype(df[column]):
            data_types[column] = 'categorical'
        else:
            data_types[column] = 'text'
    return data_types


def convert_dates(df: pd.DataFrame, columns: list):
    """
    Convert columns in a DataFrame to datetime, ignoring errors.

    Args:
        df (pd.DataFrame): The DataFrame containing the columns to convert.
        columns (list): A list of column names to convert to datetime.

    Returns:
        pd.DataFrame: The DataFrame with converted columns.
    """
    for column in columns:
        try:
            df[column] = pd.to_datetime(df[column], errors='ignore')
        except Exception as e:
            print(f"Failed to convert {column} to datetime: {e}")
    return df
