import pandas as pd
from datetime import date

def clean_data(input_filename: str, output_filename: str)->pd.DataFrame: 
    df = pd.read_csv(f'Dataset/{input_filename}')
    print(df)
    df = df.dropna()
    df = df.drop_duplicates()
    release_year = []
    release_month = []
    for x in df.index: 
        if df.loc[x, 'budget'] <= 0 or df.loc[x, 'revenue'] <= 0: 
            df.drop(x, inplace=True)
            continue

        release_date: list = df.loc[x, 'release_date'].split("-")
        release_year.append(release_date[0])
        release_month.append(release_date[1])

    df['release_year'] = release_year
    df['release_month'] = release_month
    print(df)
    df.to_csv(f'Dataset/{output_filename}')

if __name__=="__main__": 
    archivo = "popular_10000_movies_tmdb.csv"
    df = clean_data(archivo)
    print(df)