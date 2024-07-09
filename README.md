# Analytiq Flow

Analytiq Flow is an interactive data analysis tool built with Streamlit and LangChain, designed to make data analysis accessible through natural language processing and interactive visualizations. Users can upload Excel or CSV files, filter and explore data, run statistical analyses, and use AI-driven LangChain integration to ask complex questions about their data.

## Features

- **Data Upload**: Supports CSV and Excel formats.
- **Data Filtering**: Dynamic filters based on column types.
- **Statistical Analysis**: Includes summaries, frequency counts, and more.
- **Correlation Analysis**: Visualize correlations between numerical data points.
- **LangChain Integration**: Perform advanced data analysis using natural language queries.
- **Secure Authentication**: Users can authenticate via API key or email-based OTP for using LangChain.

## Installation

Analytiq Flow uses Poetry for dependency management. To set up and run the project:

1. Clone the repository:
    `git clone https://github.com/k-kahraman/analytiq-flow.git`
2. Navigate to the project directory:
    `cd analytiq-flow`
3. Install dependencies using Poetry:
    `poetry install`
4. Run the application:
    `streamlit run main.py`

Ensure you have Python 3.10 installed on your machine to avoid any compatibility issues.

## Usage

After starting the application, follow the on-screen instructions to upload your data file and authenticate for advanced features. Use the interactive sidebar to navigate through various analysis features.

## Contributing

Contributions to AnalytiqFlow are welcome! Please read the CONTRIBUTING.md (WIP) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Thanks to OpenAI for providing the API powering the LangChain integration.
- Thanks to the Streamlit community for their continuous support and contributions.

## Contact

For support or queries, reach out to `kaan@kahraman.io`.
