import pandas as pd

def clean_data(filename: str)->pd.DataFrame: 
    df = pd.read_csv(filename)
    df = df.dropna()
    df = df.drop_duplicates()
    for x in df.index: 
        if df.loc[x, 'budget'] <= 0 or df.loc[x, 'revenue'] <= 0: 
            df.drop(x, inplace=True)
    return df

def test_df()->pd.DataFrame: 
    technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","PySpark","Spark"],
    'Fee' :[20000,25000,26000,22000,24000,35000],
    'Duration':['30day','40days','35days','40days','60days','60days'],
    'Discount':[1000,2300,1200,2500,2000,2000]
              }
    df = pd.DataFrame(technologies)
    return df

if __name__=="__main__": 
    archivo = "popular_10000_movies_tmdb.csv"
    df = clean_data(archivo)
    print(df)