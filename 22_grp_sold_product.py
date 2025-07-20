import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates(subset=["sell_date", "product"])
    
    grouped = activities.groupby("sell_date")["product"].apply(
        lambda x: ",".join(sorted(x))
    ).reset_index(name="products")
    grouped["num_sold"] = grouped["products"].apply(lambda x: len(x.split(",")))
    result = grouped[["sell_date", "num_sold", "products"]]
    result = result.sort_values("sell_date").reset_index(drop=True)
    
    return result