import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    
    if N <= len(distinct_salaries):
        result = distinct_salaries.iloc[N-1]
    else:
        result = None

    return pd.DataFrame({'getNthHighestSalary({})'.format(N): [result]})