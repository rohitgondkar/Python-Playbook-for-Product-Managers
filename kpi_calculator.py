
def calculate_churn_rate(customers_lost, total_customers):
    return (customers_lost / total_customers) * 100

def calculate_revenue_growth(current_revenue, previous_revenue):
    return ((current_revenue - previous_revenue) / previous_revenue) * 100

# Example usage
if __name__ == "__main__":
    churn_rate = calculate_churn_rate(50, 1000)
    revenue_growth = calculate_revenue_growth(12000, 10000)
    print(f"Churn Rate: {churn_rate:.2f}%")
    print(f"Revenue Growth: {revenue_growth:.2f}%")
