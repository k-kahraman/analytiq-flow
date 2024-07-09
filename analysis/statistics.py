import pandas as pd
import numpy as np
import scipy.stats as stats
import streamlit as st
from utils.commons import detect_data_type

# Dictionary to map statistical analysis types to their respective functions
STAT_FUNCTIONS = {
    'Summary': lambda col: col.describe(),
    'Frequency': lambda col: col.value_counts(),
    'Mean': np.mean,
    'Median': np.median,
    'Mode': lambda col: col.mode().tolist(),
    'Standard Deviation': np.std,
    'Variance': np.var,
    'Normality Test': lambda col: stats.normaltest(col.dropna()),
    'Unique Values': lambda col: col.nunique(),
    'Top 5 Common Values': lambda col: col.value_counts().head(5),
    'Skewness': lambda col: col.skew(),
    'Text Length Summary': lambda col: col.dropna().apply(len).describe()
}


def perform_statistics(df: pd.DataFrame,
                       column: str,
                       stat_type: str,
                       visualize=False):
    """
    Perform selected statistical analysis on a DataFrame column and optionally visualize the results.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.
        column (str): The column to analyze.
        stat_type (str): The type of statistics to compute.
        visualize (bool): Whether to visualize the result.

    Returns:
        Any: The result of the statistical analysis or None if visualization is directly rendered.
    """
    if stat_type not in STAT_FUNCTIONS:
        st.error("Selected statistical analysis is not supported.")
        return None

    result = STAT_FUNCTIONS[stat_type](df[column])

    if visualize:
        visualize_data(df[column], result, stat_type)

    return result if not visualize else None


def visualize_data(column_data, result, stat_type):
    """
    Visualize the results of statistical analysis.

    Args:
        column_data (pd.Series): The data of the column to visualize.
        result (Any): The result of the statistical analysis.
        stat_type (str): The type of statistics to visualize.
    """
    if stat_type in ['Mean', 'Median', 'Standard Deviation', 'Variance']:
        st.bar_chart(column_data.dropna())
    elif stat_type in ['Frequency', 'Top 5 Common Values']:
        st.bar_chart(result)


def add_statistical_analysis(df: pd.DataFrame):
    st.write("### Statistical Analysis")
    if st.checkbox("Perform Statistical Analysis"):
        data_types = detect_data_type(df)
        column_to_analyze = st.selectbox("Select Column", df.columns)
        # Determine the appropriate analysis options based on the data type
        analysis_options = []
        if data_types[column_to_analyze] == 'numeric':
            analysis_options = [
                "Summary", "Mean", "Median", "Mode", "Standard Deviation",
                "Variance", "Normality Test", "Skewness"
            ]
        elif data_types[column_to_analyze] == 'categorical':
            analysis_options = ["Summary", "Frequency", "Top 5 Common Values"]
        elif data_types[column_to_analyze] == 'text':
            analysis_options = [
                "Text Length Summary", "Frequency", "Unique Values",
                "Top 5 Common Values"
            ]
        elif data_types[column_to_analyze] == 'datetime':
            analysis_options = ["Summary"]

        analysis_type = st.selectbox("Select the type of analysis",
                                     analysis_options)
        visualize = st.checkbox("Visualize Results")

        if st.button("Calculate"):
            with st.spinner("Calculating..."):
                result = perform_statistics(df, column_to_analyze,
                                            analysis_type, visualize)
                if result is not None:
                    st.write(
                        f"Results for {analysis_type} of {column_to_analyze}:")
                    st.write(result)
