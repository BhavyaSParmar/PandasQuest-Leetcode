import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
     merged_df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('', '_dept'))

     max_salary_per_dept = merged_df.groupby('departmentId')['salary'].max().reset_index()
     max_salary_per_dept.rename(columns={'salary': 'max_salary'}, inplace=True)

     result = merged_df.merge(max_salary_per_dept, on='departmentId')
     result = result[result['salary'] == result['max_salary']]

     result = result[['name_dept', 'name', 'salary']]
     result.columns = ['Department', 'Employee', 'Salary']

     return result