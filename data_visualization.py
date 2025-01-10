
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot sales trends
def plot_sales_trends(sales_data):
    sales_data.plot(x='Date', y='Sales', kind='line', title='Sales Trends')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.show()

# Example usage
if __name__ == "__main__":
    sales_data = pd.DataFrame({
        'Date': ['2023-01-01', '2023-02-01', '2023-03-01'],
        'Sales': [5000, 7000, 8000]
    })
    plot_sales_trends(sales_data)
