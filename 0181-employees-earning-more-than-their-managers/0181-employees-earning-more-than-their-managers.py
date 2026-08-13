import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    res=employee.merge(employee,left_on='managerId',right_on='id',how='left')
    filtered_df=res.query('salary_x>salary_y')
    result=pd.DataFrame({'Employee': filtered_df['name_x']})
    return result