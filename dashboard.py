import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Section a: Display Benchmark Results
def display_benchmark_results():
    # Load benchmark results
    benchmark_results = pd.read_csv('benchmark_results.csv')

    # Display benchmark results
    st.title('Benchmark Results')
    st.write(benchmark_results)

# Section b: Display Price Prediction Models
def display_price_predictions():
    # Load price prediction data
    price_predictions = pd.read_csv('stock_predictions.csv')

    # Print the columns to debug
    st.write("Columns in price_predictions:", price_predictions.columns)

    # Select company ticker
    ticker = st.selectbox('Select Company Ticker', price_predictions['ticker'].unique())

    # Filter data for selected ticker
    ticker_data = price_predictions[price_predictions['ticker'] == ticker]

    # Plot price predictions
    fig, ax = plt.subplots()
    ax.plot(ticker_data['date'], ticker_data['actual_price'], label='Actual Price')
    ax.plot(ticker_data['date'], ticker_data['predicted_price'], label='Predicted Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    # Display plot
    st.pyplot(fig)

# Main function to run the Streamlit app
def main():
    st.sidebar.title("Dashboard Sections")
    section = st.sidebar.radio("Select Section", ("Benchmark Results", "Price Predictions"))

    if section == "Benchmark Results":
        display_benchmark_results()
    elif section == "Price Predictions":
        display_price_predictions()

# Run the Streamlit app
if __name__ == "__main__":
    main()