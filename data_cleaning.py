import pandas as pd

def clean_data(filename: str)->pd.DataFrame: 
    df = pd.read_csv(filename)
    df = df.dropna()
    return df

if __name__=="__main__": 
    archivo = "popular_10000_movies_tmdb.csv"
    df = clean_data(archivo)
    print(df)