import pandas as pd

def clean_data(input_filename: str, output_filename: str)->pd.DataFrame: 
    df = pd.read_csv(f'Dataset/{input_filename}')
    df = df.dropna()
    df = df.drop_duplicates()
    release_year = []
    release_month = []
    for x in df.index: 
        if df.loc[x, 'budget'] <= 0 or df.loc[x, 'revenue'] <= 0: 
            df.drop(x, inplace=True)
        else: 
            date_str: str = df.loc[x, 'release_date']
            date: list = date_str.split("-")
            release_year.append(date[0])
            release_month.append(date[1])
    df['release_year'] = release_year
    df['release_month'] = release_month
    df.to_csv(f'Dataset/{output_filename}')

if __name__=="__main__": 
    archivo = "popular_10000_movies_tmdb.csv"
    df = clean_data(archivo)
    print(df)