import streamlit as st
import pandas as pd
from data_loader import load_data
from utils.filters import filter_dataframe
from analysis.statistics import add_statistical_analysis
from analysis.correlation import add_correlation_analysis


def main():
    st.title("AnalytiqFlow: Your Interactive Data Analysis Tool")

    # File upload section
    uploaded_file = st.file_uploader("Upload your CSV or Excel file",
                                     type=['csv', 'xlsx', 'xls'])
    if uploaded_file is not None:
        # Load and display the data
        df = load_data(uploaded_file)
        if not df.empty:
            st.write("### Uploaded Data")
            st.dataframe(df.head())

            # Allow users to filter the dataframe
            st.write("### Filter Data")
            df_filtered = filter_dataframe(df)
            if not df_filtered.empty:
                st.write("Filtered Data:")
                st.dataframe(df_filtered)

                # Add sections for statistical and correlation analysis
                add_statistical_analysis(df_filtered)
                add_correlation_analysis(df_filtered)


if __name__ == "__main__":
    main()
