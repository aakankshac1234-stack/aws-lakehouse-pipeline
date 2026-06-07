from transformations import transform_data
from validations import validate_data
import pandas as pd

def main():
    df = pd.read_csv("data/sample_transactions.csv")

    validate_data(df)

    transformed_df = transform_data(df)

    transformed_df.to_csv(
        "data/processed_transactions.csv",
        index=False
    )

if __name__ == "__main__":
    main()
