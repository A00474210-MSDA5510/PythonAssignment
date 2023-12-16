import streamlit as st
import pandas as pd
import plotly.express as px


def validate_csv_columns(df):
    # Check if the DataFrame has exactly two columns named 'name' and 'age'
    expected_columns = ['Name', 'Age']
    return all(column in df.columns for column in expected_columns) and len(df.columns) == 2


def main():
    st.title("CSV File Uploader and Viewer")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Validate columns
        if validate_csv_columns(df):
            # Display the DataFrame
            st.write("### Uploaded DataFrame:")
            st.write(df)

            # Plot histogram based on the 'age' column using Plotly
            st.write("### Age Histogram:")
            fig = px.histogram(df, x='Age', nbins=20, title='Age Histogram')
            st.plotly_chart(fig)

        else:
            st.error("Invalid CSV file! Please make sure the file has only 'name' and 'age' columns.")


if __name__ == "__main__":
    main()
