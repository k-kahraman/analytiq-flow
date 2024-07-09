import pandas as pd
import streamlit as st


def load_data(uploaded_file) -> pd.DataFrame:
    """
    Load data from an uploaded file, automatically handling Excel and CSV files.

    Args:
        uploaded_file: The file uploaded by the user.

    Returns:
        A pandas DataFrame containing the loaded data.
    """
    # Try to detect the file type based on the file name
    file_name = uploaded_file.name
    if file_name.endswith('.csv'):
        return load_csv(uploaded_file)
    elif file_name.endswith(('.xlsx', '.xls')):
        return load_excel(uploaded_file)
    else:
        st.error("Unsupported file type. Please upload a CSV or Excel file.")
        return pd.DataFrame()


def load_csv(uploaded_file) -> pd.DataFrame:
    """
    Load data from a CSV file, handling potential issues with delimiters and encodings.

    Args:
        uploaded_file: The CSV file uploaded by the user.

    Returns:
        A pandas DataFrame.
    """
    try:
        # Attempt to read with common delimiters and encoding detection
        df = pd.read_csv(uploaded_file,
                         delimiter=None,
                         engine='python',
                         encoding='utf-8-sig')
    except Exception as e:
        st.error(f"Failed to load CSV file: {e}")
        return pd.DataFrame()
    return df


def load_excel(uploaded_file) -> pd.DataFrame:
    """
    Load data from an Excel file, managing different sheets if necessary.

    Args:
        uploaded_file: The Excel file uploaded by the user.

    Returns:
        A pandas DataFrame.
    """
    try:
        # Load the first sheet by default or let the user select a sheet
        xl = pd.ExcelFile(uploaded_file)
        if len(xl.sheet_names) > 1:
            sheet = st.selectbox('Select a sheet:', xl.sheet_names)
        else:
            sheet = xl.sheet_names[0]
        df = xl.parse(sheet)
    except Exception as e:
        st.error(f"Failed to load Excel file: {e}")
        return pd.DataFrame()
    return df
