#making convert_job_skills accessible to all the notebooks
import ast
import pandas as pd
def convert_job_skills(x):
    '''Convert string to list'''
    try:
        if pd.notna(x):
            return ast.literal_eval(x)
        else:
            return x
    except (ValueError, SyntaxError):
        return x
