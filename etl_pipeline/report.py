import pandas as pd

def total_sales_amount(df):
    return df['TotalAmount'].sum()

def report_sales_by_region(df):
    return df.groupby('Region', as_index=False)['TotalAmount'].sum()

def report_sales_by_category(df):
    return df.groupby('Category', as_index=False)['TotalAmount'].sum()

def average_order_value(df):
    return df['TotalAmount'].mean()

def top_10_customers_by_purchase_volume(df):
    return (
        df.groupby("CustomerID", as_index=False)["Quantity"]
        .sum()
        .sort_values("Quantity", ascending=False)
        .head(10)
    )

def top_n_products_by_sale_revenue(df, n):
    return (
        df.groupby("ProductID", as_index=False)["TotalAmount"]
        .sum()
        .sort_values("TotalAmount", ascending=False)
        .head(n)
    )

def sales_by_salesrep(df):
    return (
        df.groupby('SalesRep', as_index=False)['TotalAmount']
        .sum()
        .sort_values('TotalAmount', ascending=False)
    )

def order_count_per_day(df):
    data = df.assign(OrderDate=pd.to_datetime(df['OrderDate']).dt.normalize())
    return (
        data.groupby('OrderDate', as_index=False)['Quantity']
        .count()
        .rename(columns={'Quantity': 'OrderCount'})
    )

def qty_sold_by_category(df):
    return (
        df.groupby('Category', as_index=False)['Quantity']
        .sum()
        .sort_values('Quantity', ascending=False)
    )

def avg_qty_per_order(df):
    return df['Quantity'].mean()

def top_performing_regions(df):
    return (
        df.groupby('Region', as_index=False)['TotalAmount']
        .sum()
        .sort_values('TotalAmount', ascending=False)
    )

def customer_wise_order_count(df):
    return (
        df.groupby('CustomerID', as_index=False)['OrderID']
        .count()
        .rename(columns={'OrderID': 'OrderCount'})
    )

def report_sales_trend_monthly(df):
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    return df.groupby(df['OrderDate'].dt.to_period('M'))['TotalAmount'].sum()

def run_report(df):
    return {
        "total_sales_amount": total_sales_amount(df),
        "report_sales_by_region": report_sales_by_region(df),
        "report_sales_by_category": report_sales_by_category(df),
        "averge_order_value": average_order_value(df),
        "top_10_customers_by_purchase_volume": top_10_customers_by_purchase_volume(df),
        "top_10_products_by_sale_revenue": top_n_products_by_sale_revenue(df, 10),
        "sales_by_salesrep": sales_by_salesrep(df),
        "order_count_per_day":order_count_per_day(df),
        "qty_sold_by_category": qty_sold_by_category(df),
        "avg_qty_per_order": avg_qty_per_order(df),
        "top_performing_regions": top_performing_regions(df),
        "customer_wise_order_count": customer_wise_order_count(df),
        "monthly_sales_trend": report_sales_trend_monthly(df)
    }