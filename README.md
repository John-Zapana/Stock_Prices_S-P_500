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
