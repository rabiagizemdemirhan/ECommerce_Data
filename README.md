# E-commerce Cart Abandonment Rate Analysis (2023-2024)

## Project Overview  
This project aims to provide an in-depth analysis of cart abandonment rates, customer behaviors, and sales performance for a Turkish e-commerce platform during 2023 and 2024. The insights derived offer actionable recommendations to reduce cart abandonment and improve customer conversion rates.

## Technologies Used  
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

## Installation  
To set up the project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rabiagizemdemirhan/ECommerce_Data.git](https://github.com/rabiagizemdemirhan/ECommerce_Data.git)
    cd ECommerce_Data
    ```
2.  **Install required libraries:**
    First, ensure you have `pip` and `venv` (for virtual environments) installed.
    It is highly recommended to use a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    (Note: The `requirements.txt` file needs to be generated in the project's root directory using `pip freeze > requirements.txt` after installing all dependencies.)

## Usage

The primary way to explore this analysis is through the Jupyter Notebook, which contains all the code, outputs, and explanations.

1.  **Open the Jupyter Notebook:**
    Ensure you are in the project's root directory (`ECommerce_Data`) in your terminal and your virtual environment is activated. Then run:
    ```bash
    jupyter notebook src/e_commerce_abandonment_analysis.ipynb
    ```
    Once the notebook opens in your browser (or VS Code), run all cells sequentially from top to bottom.

2.  **Run the main analysis script (Alternative):**
    For a non-interactive execution, you can run the `main.py` script. This will execute the data loading, analysis functions, and display plots.
    ```bash
    python src/main.py
    ```

### Analysis Details:

The comprehensive exploratory data analysis (EDA) includes:

* **Data Quality Checks:** Assessment of missing values, data types, and general descriptive statistics.
* **Time Series Analysis:** Examination of trends and fluctuations in cart abandonment rate, total transactions, average cart value, and payment method shares over time.
* **Sector-wise Sales Performance Comparisons:** Comparative analysis of cart abandonment rates, average cart values, transaction counts, and sales shares across different top-selling sectors.
* **Impact of Payment Methods:** Investigation into the correlation and relationships between credit card share, bank transfer share, cash-on-delivery share, and the cart abandonment rate.
* **Distribution of Average Cart Value:** Analysis of the distribution of average cart value and its relationship to the abandonment rate.

## Dataset

The analysis is based on a simulated monthly e-commerce dataset containing the following features:

* `Date`: End of month date (datetime information).
* `Total_Transactions`: Total number of transactions.
* `Cart_Abandonment_Rate_PCT`: Cart abandonment rate (percentage).
* `Average_Cart_Value_TL`: Average cart value (Turkish Lira).
* `Credit_Card_Share_PCT`: Share of payments made by credit card (percentage).
* `Bank_Transfer_Share_PCT`: Share of payments made by bank transfer/EFT (percentage).
* `Cash_On_Delivery_Share_PCT`: Share of payments made by cash on delivery (percentage).
* `Top_Selling_Sector`: Sector with the highest sales for the given period (categorical).
* `Sector_Sales_Share_PCT`: Top-selling sector’s share of total sales (percentage).

## Functions

Key Python functions utilized and defined within the project:

* `load_data(path)`: Responsible for loading the CSV dataset and performing initial preprocessing, such as converting the 'Date' column to datetime objects.
* `plot_cart_abandon_rate(df)`: Visualizes the trend of the cart abandonment rate over time using a line plot.
* `analyze_data_quality(df)`: Provides insights into data integrity by reporting missing values, general statistical summaries, and unique categorical values.
* `analyze_time_series_metrics(df)`: Generates time series plots to analyze the temporal changes in total transaction counts, average cart values, and the percentage shares of different payment methods.
* `analyze_sector_performance(df)`: Conducts and visualizes a comparative analysis of key performance metrics (abandonment rate, cart value, transactions, sales share) across various e-commerce sectors.
* `analyze_payment_method_impact(df)`: Explores the correlation and potential relationships between the shares of different payment methods and the overall cart abandonment rate using correlation matrices and scatter plots.
* `analyze_average_cart_value(df)`: Analyzes the distribution of average cart values and investigates its relationship with the cart abandonment rate through histograms and scatter plots.
* `run_all_analysis(df)`: A master function that orchestrates the sequential execution of all defined data analysis and visualization steps, providing a comprehensive EDA report.

## Results

This project successfully reveals significant patterns and relationships within the e-commerce dataset. It identifies the influence of various factors, including payment methods and specific sectors, on cart abandonment rates. The detailed analysis provides valuable insights that can inform business strategies, particularly in optimizing conversion funnels and enhancing customer trust by understanding the dynamics of credit card and cash-on-delivery payments.

## Contribution

Feel free to fork the repository and submit pull requests or open issues. Suggestions and improvements are always welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.