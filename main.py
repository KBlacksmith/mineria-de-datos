#Libraries
import os
import pandas as pd

#My files
import data_cleaning
import data_analysis

if __name__=="__main__": 
    dataset = "Dataset/popular_10000_movies_tmdb.csv"
    print("01 - Data Cleaning")
    df: pd.DataFrame
    if os.path.exists("Dataset/clean_popular_movies.csv"): 
        df = pd.read_csv("Dataset/clean_popular_movies.csv")
    else: 
        df: pd.DataFrame = data_cleaning.clean_data(dataset)
        df.to_csv("Dataset/clean_popular_movies.csv")
    #df: pd.DataFrame = data_cleaning.test_df()
    print(df)
    print("02 - Data Analysis")
    data_analysis.analyze_data(df)