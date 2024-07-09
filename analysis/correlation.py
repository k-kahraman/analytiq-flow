import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils.commons import detect_data_type


def analyze_correlation(df: pd.DataFrame, columns: list):
    """
    Analyze the correlation between selected numerical columns in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.
        columns (list): List of column names to include in the correlation analysis.

    Returns:
        pd.DataFrame: A DataFrame containing the correlation matrix.
    """
    if len(columns) < 2:
        st.error(
            "Please select at least two numerical columns for correlation analysis."
        )
        return None

    try:
        # Compute the correlation matrix
        correlation_matrix = df[columns].corr()
        return correlation_matrix
    except Exception as e:
        st.error(f"Error calculating correlation: {e}")
        return None


def add_correlation_analysis(df: pd.DataFrame):
    """
    Adds UI elements to perform correlation analysis and visualize the results.

    Args:
        df (pd.DataFrame): The DataFrame from which to compute correlations.
    """
    if st.checkbox("Perform Correlation Analysis"):
        # Filter only numeric columns for correlation analysis
        numeric_columns = df.select_dtypes(include='number').columns
        selected_columns = st.multiselect(
            "Select columns to calculate correlation", numeric_columns)

        if selected_columns and len(selected_columns) > 1:
            if st.button("Show Correlation Matrix"):
                with st.spinner("Calculating..."):
                    correlation_result = analyze_correlation(
                        df, selected_columns)
                    if correlation_result is not None:
                        st.write("Correlation Matrix:")
                        st.dataframe(correlation_result)
                        visualize_correlation_matrix(correlation_result)


def visualize_correlation_matrix(correlation_matrix):
    """
    Visualize the correlation matrix using a heatmap.

    Args:
        correlation_matrix (pd.DataFrame): The correlation matrix to visualize.
    """
    fig, ax = plt.subplots()
    sns.heatmap(correlation_matrix,
                annot=True,
                fmt=".2f",
                cmap='coolwarm',
                ax=ax)
    plt.title('Correlation Matrix')
    st.pyplot(fig)


def add_correlation_analysis(df: pd.DataFrame):
    st.write("### Correlation Analysis")
    if st.checkbox("Perform Correlation Analysis"):
        data_types = detect_data_type(df)
        numeric_columns = [
            col for col, dtype in data_types.items() if dtype == 'numeric'
        ]
        selected_columns = st.multiselect(
            "Select columns to calculate correlation", numeric_columns)

        if len(selected_columns) > 1:
            if st.button("Show Correlation Matrix"):
                with st.spinner("Calculating..."):
                    correlation_result = analyze_correlation(
                        df, selected_columns)
                    if correlation_result is not None:
                        st.write("Correlation Matrix:")
                        st.dataframe(correlation_result)
