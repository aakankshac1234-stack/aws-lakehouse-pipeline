import pandas as pd
from src.transformations import transform_data

def test_revenue_calculation():
    df = pd.DataFrame({
        "quantity": [2],
        "price": [10]
    })

    result = transform_data(df)

    assert result["revenue"][0] == 20
