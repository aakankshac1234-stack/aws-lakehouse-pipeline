import pandas as pd

def transform_data(df):
    df = df.drop_duplicates()

    df["order_date"] = pd.to_datetime(df["order_date"])

    df["revenue"] = df["quantity"] * df["price"]

    return df
