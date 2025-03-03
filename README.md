# Stock_Prices_S-P_500
The purpose of this project is to combine research, benchmarking and coding using the provided time-series dataset of stock prices for S&amp;P 500 companies

# 1. Storing and Retrieving Data

### Objective:
Decide whether to store the data in CSV or Parquet format, considering compression schemes, and justify your choice at scales 1x, 10x, and 100x.

## 1.1. Research CSV vs. Parquet
- **CSV:** Simple, human-readable, but less efficient in terms of storage and query performance, especially for large datasets.
- **Parquet:** Columnar storage format, highly efficient for read-heavy operations, supports compression, and is optimized for big data processing.

### Load the CSV Dataset
First, let's load the CSV dataset into a Pandas DataFrame.

### Convert CSV to Parquet
Next, let's convert the dataset to Parquet format. Parquet is a columnar storage format that is highly efficient for large datasets.
- **engine='pyarrow':** PyArrow is a fast and efficient library for working with Parquet files.
- **compression='snappy':** Snappy is a popular compression scheme that balances speed and compression ratio.

## 1.2. Benchmarking
Now, let's benchmark the performance of CSV and Parquet formats at 1x, 10x, and 100x scales.

### Compare Measure Time
Measure the time taken to read and write the data.

#### 1x Scale (Original Dataset)

#### 10x Scale (Simulate 10x Data)
To simulate a 10x larger dataset, concatenate the dataset with itself 10 times.

#### 100x Scale (Simulate 100x Data)
Similarly, a 100x larger dataset was simulated by concatenating the data set 100 times.

### Compare Storage Size
Compare the file sizes of CSV and Parquet files at each scale.

## 1.3. Analysis of Results

### Load Times
- **1x Scale:** Parquet is **faster** than CSV.
- **10x Scale:** Parquet is **faster** than CSV.
- **100x Scale:** Parquet is **faster** than CSV.

**Key Insight:** As the dataset size increases, Parquet consistently outperforms CSV in terms of load times. The performance gap becomes more significant at larger scales (10x and 100x).

### File Sizes
- **1x Scale:** Parquet is **smaller** than CSV.
- **10x Scale:** Parquet is **smaller** than CSV.
- **100x Scale:** Parquet is **smaller** than CSV.

**Key Insight:** Parquet files are significantly smaller than CSV files at all scales. This is due to Parquet's columnar storage format and efficient compression (e.g., Snappy).

## 1.4. Recommendation
Based on the benchmarking results, here’s the recommendation:

- **For small datasets (1x):** Parquet is recommended for its speed and efficiency, but CSV is acceptable if simplicity is a priority.
- **For medium to large datasets (10x and 100x):** Parquet is the clear winner due to its superior performance in both load times and storage efficiency.

# 2. Manipulating, Analyzing Data, and Building Models

### Objective:
Compare the performance of Pandas and Polars for data manipulation and analysis, and build prediction models using technical indicators.

### Dataset Details
The dataset has 7 columns with 619,040 rows. Here's a breakdown of its key features:
- **Target Variable:** close (closing price of a company's stock).
- **Numerical Features:** open, high, low, and volume.
- **Categorical Features:** date, and name.

### Handle Missing Values
Handling missing values is an important step before proceeding with any analysis or modelling.

Based on the Dataset Details output, it seems there are:
- 11 missing values in **open**
- 8 missing values in **high**
- 8 missing values in **low**

So because the number of missing values is small, we can **drop** those rows.

## 2.1. Compare Pandas vs. Polars
We’ll compare the performance of Pandas and Polars for data manipulation tasks. As we will see later, **Polars is a faster** alternative to Pandas, especially for large datasets.
- Perform common data manipulation tasks (e.g., filtering, grouping, aggregating) using both Pandas and Polars.
- Measure the time taken for each operation.

### Filtering Data

### Grouping and Aggregating

## 2.2. Technical Indicators
Technical indicators are essential for analyzing stock prices. Now that the data is clean, we will calculate 4 technical indicators such as Moving Average (MA), Relative Strength Index (RSI), Moving Average Converge Divergence (MACD), Bollinger Bands; and we will add them as new columns to the dataframe.

Let’s calculate these indicators for each stock (grouped by **name**).

### Moving Average (MA)

### Relative Strength Index (RSI)

### Moving Average Convergence Divergence (MACD)

### Bollinger Bands

#### Add Indicators to the dataframe

## 2.3 Build Prediction Models
Now, let’s build prediction models (Linear Regression, Random Forest) to forecast the next day's closing price. We’ll use an 80-20 train-test split and evaluate the models using **RMSE (Root Mean Squared Error)**.

#### Handling missing

### Models: Linear Regression & Random Forest
We’ll use the technical indicators (**MA**, **RSI**, **MACD**, **MACD_Signal**, **Bollinger_Mid**, **Bollinger_Upper**, **Bollinger_Lower**) as features and the **close** price as the target.

#### Analysis of Models
- **Linear Regression:**
    - The RMSE of **0.826** indicates that, on average, the model's predictions are off by approximately 0.834 units from the actual closing prices.
    - This is a reasonable performance for a simple model like Linear Regression.

- **Random Forest:**
    - The RMSE of **0.854** is slightly higher than that of Linear Regression, which is unexpected because Random Forest is typically more powerful and flexible.
    - This could be due to **Underfitting**: The model may not have enough trees (**n_estimators=100**) to capture the complexity of the data.
 
# 3. Creating a Visual Dashboard
### Objective:
Research and compare dashboarding libraries (e.g., Streamlit, Dash, Reflex) and create a dashboard to display benchmark results and price predictions.

### Saving Predictions and Benchmark Results

## Dashboards A) & B)
- To disaply tha dashboard we must open anaconda promt and then run this:
    - **streamlit run dashboard.py**
