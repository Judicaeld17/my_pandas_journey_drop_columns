# TASK: Create a function which receive a pandas dataframe and a column to drop as parameter and returns a datafrom without the dropped column.
import pandas as pd
def my_pandas_journey_drop_columns(df,col_to_drop):
    df=df.drop(col_to_drop,axis=1)
    return df
