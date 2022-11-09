
def rem_digits(df,column_name):
    df[column_name] = df[column_name].str.replace('\d+', '')
    return df

def rem_dot(df,column_name):
    df[column_name] = df[column_name].str.replace('.', '')
    return df

def rem_xa0(df,column_name):
    df[column_name] = df[column_name].str.replace('\xa0', ',')
    return df

def rem_double_coma(df,column_name):
    df[column_name] = df[column_name].str.replace(',,', ',')
    return df

def rem_slash(df,column_name):
    df[column_name] = df[column_name].str.replace('-', '')
    return df
