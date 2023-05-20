#Libraries
import os
import pandas as pd

#My files
#1
import data_cleaning
#2
import data_analysis
#3
import data_visualization
#4
#5
import linear_regression
#6
#7
#8
import clustering
#9
import text_analysis

if __name__=="__main__": 
    dataset = "popular_10000_movies_tmdb.csv"
    clean_dataset = 'clean_popular_movies.csv'
    
    print("01 - Data Cleaning")
    
    
    if not os.path.exists("Dataset/clean_popular_movies.csv"): 
        data_cleaning.clean_data(dataset, clean_dataset)
    
    df = pd.read_csv(f'Dataset/{clean_dataset}')
    print(df.columns)
    
    print("02 - Data Analysis")
    data_analysis.analyze_data(clean_dataset)
    
    print("03 - Data Visualization")
    #data_visualization.visualize_data()
    
    print("04 - Statistic Test")
    
    print("05 - Linear Model")
    #linear_regression.get_linear_regressions()
    
    print("06 - Forecasting")
    
    print("07 - Data Classification")
    
    print("08 - Clustering")
    clustering.cluster(clean_dataset)
    
    print("09 - Text Analysis")
    #text_analysis.analyze_text()
