def validate_data(df):
    required_columns = [
        "order_id",
        "customer_id",
        "quantity",
        "price"
    ]

    missing = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )
