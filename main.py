#Libraries
import pandas as pd

#My files
import data_cleaning

if __name__=="__main__": 
    dataset = "Dataset/popular_10000_movies_tmdb.csv"
    df: pd.DataFrame = data_cleaning.clean_data(dataset)
    print(df)