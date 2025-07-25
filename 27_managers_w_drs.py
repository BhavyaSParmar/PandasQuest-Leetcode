import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
     manager_counts = employee['managerId'].value_counts()
    
     qualifying_managers = manager_counts[manager_counts >= 5].index.tolist()
     result = employee[employee['id'].isin(qualifying_managers)][['name']]
     return result