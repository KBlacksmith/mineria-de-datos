#Libraries
import os
import pandas as pd

#My files
import data_cleaning

import data_analysis

import data_visualization

import linear_regression

import forecasting

import classification

import clustering

import text_analysis

if __name__=="__main__": 
    dataset = "popular_10000_movies_tmdb.csv"
    clean_dataset = 'clean_popular_movies.csv'
    
    print("Data Cleaning")
    
    
    if not os.path.exists("Dataset/clean_popular_movies.csv"): 
        data_cleaning.clean_data(dataset, clean_dataset)
    
    df = pd.read_csv(f'Dataset/{clean_dataset}')
    print(df.columns)
    
    print("Data Analysis")
    #data_analysis.analyze_data(clean_dataset)
    
    print("Data Visualization")
    #data_visualization.visualize_data(clean_dataset)
    
    print("Statistic Test")
    
    print("Linear Model")
    #linear_regression.get_linear_regressions()
    
    print("Forecasting")
    #forecasting.forecasting()
    
    print("Data Classification")
    classification.classify()
    
    print("Clustering")
    clustering.cluster(clean_dataset)
    
    print("Text Analysis")
    text_analysis.analyze_text()
