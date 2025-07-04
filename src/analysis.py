import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np   

plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 16
sns.set_palette("viridis")
sns.set_style("whitegrid") 


def plot_cart_abandon_rate(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Cart_Abandonment_Rate_PCT'], marker='o', linestyle='-', color='skyblue')
    plt.title('E-commerce Cart Abandonment Rate in Turkey (2023-2024)')
    plt.xlabel('Date')
    plt.ylabel('Cart Abandonment Rate (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def analyze_data_quality(df):
    print("\n--- Data Quality Check ---")
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nGeneral Statistics:")
    print(df.describe())
    print("\nUnique Values for Categorical Columns:")
    for col in df.select_dtypes(include='object').columns:
        print(f"- {col}: {df[col].unique()}")

def analyze_time_series_metrics(df):
    print("\n--- Time Series Analysis of Key Metrics ---")
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 18))

    axes[0].plot(df['Date'], df['Total_Transactions'], marker='o', linestyle='-', color='orange')
    axes[0].set_title('Total Online Transactions (2023-2024)')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Transaction Count')
    axes[0].grid(True)

    axes[1].plot(df['Date'], df['Average_Cart_Value_TL'], marker='o', linestyle='-', color='green')
    axes[1].set_title('Average Cart Value (TL) (2023-2024)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Average Cart Value (TL)')
    axes[1].grid(True)

    axes[2].plot(df['Date'], df['Credit_Card_Share_PCT'], marker='o', linestyle='-', label='Credit Card Share (%)', color='purple')
    axes[2].plot(df['Date'], df['Cash_On_Delivery_Share_PCT'], marker='o', linestyle='-', label='Cash on Delivery Share (%)', color='brown')
    axes[2].set_title('Payment Method Shares (2023-2024)')
    axes[2].set_xlabel('Date')
    axes[2].set_ylabel('Share (%)')
    axes[2].legend()
    axes[2].grid(True)

    plt.tight_layout()
    plt.show()

def analyze_sector_performance(df):
    print("\n--- Sector Performance Analysis ---")
    sector_summary = df.groupby('Top_Selling_Sector').agg(
        Avg_Abandon_Rate=('Cart_Abandonment_Rate_PCT', 'mean'),
        Avg_Cart_Value=('Average_Cart_Value_TL', 'mean'),
        Avg_Transaction_Count=('Total_Transactions', 'mean'), 
        Avg_Sales_Share=('Sector_Sales_Share_PCT', 'mean') 
    ).sort_values(by='Avg_Abandon_Rate', ascending=False)

    print("\nAverage Metrics by Sector:")
    print(sector_summary)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))
    axes = axes.flatten() 

    sns.barplot(x=sector_summary.index, y=sector_summary['Avg_Abandon_Rate'], ax=axes[0])
    axes[0].set_title('Average Cart Abandonment Rate by Sector')
    axes[0].set_xlabel('Sector')
    axes[0].set_ylabel('Avg. Abandon Rate (%)')
    axes[0].tick_params(axis='x', rotation=45, ha='right')

    sns.barplot(x=sector_summary.index, y=sector_summary['Avg_Cart_Value'], ax=axes[1])
    axes[1].set_title('Average Cart Value by Sector')
    axes[1].set_xlabel('Sector')
    axes[1].set_ylabel('Avg. Cart Value (TL)')
    axes[1].tick_params(axis='x', rotation=45, ha='right')

    sns.barplot(x=sector_summary.index, y=sector_summary['Avg_Transaction_Count'], ax=axes[2])
    axes[2].set_title('Average Transaction Count by Sector')
    axes[2].set_xlabel('Sector')
    axes[2].set_ylabel('Avg. Transaction Count')
    axes[2].tick_params(axis='x', rotation=45, ha='right')
    
    sns.barplot(x=sector_summary.index, y=sector_summary['Avg_Sales_Share'], ax=axes[3])
    axes[3].set_title('Average Sales Share by Sector')
    axes[3].set_xlabel('Sector')
    axes[3].set_ylabel('Avg. Sales Share (%)')
    axes[3].tick_params(axis='x', rotation=45, ha='right')

    plt.tight_layout()
    plt.show()

def analyze_payment_method_impact(df):
    print("\n--- Analysis of Payment Method Impact on Cart Abandonment ---")
    
    numerical_cols = ['Cart_Abandonment_Rate_PCT', 'Average_Cart_Value_TL',
                      'Credit_Card_Share_PCT', 'Cash_On_Delivery_Share_PCT',
                      'Total_Transactions', 'Sector_Sales_Share_PCT'] 
    
    available_numerical_cols = [col for col in numerical_cols if col in df.columns]
    
    correlation_matrix = df[available_numerical_cols].corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Correlation Matrix of Numerical Variables')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

    sns.scatterplot(x='Credit_Card_Share_PCT', y='Cart_Abandonment_Rate_PCT', data=df, ax=axes[0])
    axes[0].set_title('Credit Card Share vs. Cart Abandonment Rate')
    axes[0].set_xlabel('Credit Card Share (%)')
    axes[0].set_ylabel('Cart Abandonment Rate (%)')
    axes[0].grid(True)

    sns.scatterplot(x='Cash_On_Delivery_Share_PCT', y='Cart_Abandonment_Rate_PCT', data=df, ax=axes[1])
    axes[1].set_title('Cash on Delivery Share vs. Cart Abandonment Rate')
    axes[1].set_xlabel('Cash on Delivery Share (%)')
    axes[1].set_ylabel('Cart Abandonment Rate (%)')
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

def analyze_average_cart_value(df):
    print("\n--- Average Cart Value Analysis ---")
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Average_Cart_Value_TL'], kde=True, bins=10) 
    plt.title('Distribution of Average Cart Value')
    plt.xlabel('Average Cart Value (TL)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Average_Cart_Value_TL', y='Cart_Abandonment_Rate_PCT', data=df)
    plt.title('Average Cart Value vs. Cart Abandonment Rate')
    plt.xlabel('Average Cart Value (TL)')
    plt.ylabel('Cart Abandonment Rate (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def run_all_analysis(df):
    print("\n--- Comprehensive EDA Started ---")

    analyze_data_quality(df)
    
    print("\n--- Cart Abandonment Rate Time Series Analysis ---")
    plot_cart_abandon_rate(df)

    analyze_time_series_metrics(df) 

    analyze_sector_performance(df)

    analyze_payment_method_impact(df)

    analyze_average_cart_value(df)

    print("\n--- Comprehensive EDA Completed ---")