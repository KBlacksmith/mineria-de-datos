import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def print_buffer(): 
    print("\n-------------------\n")

#Can group by
#Id, Title, Release date, genres, original language, vote_average, vote_count, popularity, budget, production companies, revenue, runtime
def analyze_data(dataset: str): 
    df: pd.DataFrame = pd.read_csv(f'Dataset/{dataset}')
    print(df.columns)
    
    result = df['genres'].aggregate('count')
    print(result)
    print("Combinaciones distintas de géneros: " + str(result))
    print_buffer()
    
    result = df.groupby('original_language')['id'].aggregate('count')
    print("Películas por idioma original: ")
    print(result)
    print_buffer()
    
    result = df.groupby('production_companies')['id'].aggregate('count')
    print("Compañías productoras: ")
    print(result)
    print_buffer()
    
    result = df['release_date'].aggregate(['min', 'max'])
    print(result)
    print("Fecha de estreno más antigua: " + str(result['min']))
    print("Fecha de estreno más reciente: " + str(result['max']))
    print_buffer()

    result = df['popularity'].aggregate(['average', 'min', 'max'])
    print(result)
    print("Popularidad más baja: " + str(result['min']))
    print("Popularidad más alta: " + str(result['max']))
    print("Popularidad promedio: " + str(round(result['average'], 2)))
    print_buffer()

    result = df['vote_average'].aggregate(['average', 'min', 'max'])
    print(result)
    print("Peor calificación: " + str(result['min']))
    print("Mejor calificación: " + str(result['max']))
    print("Calificación promedio: " + str(round(result['average'], 2)))
    print_buffer()

    result = df['budget'].aggregate(['average', 'max'])
    print(result)
    print("Presupuesto promedio: " + str(round(result['average'], 2)))
    print("Presupuesto más grande: " + str(result['max']))
    print_buffer()


    result = df['revenue'].aggregate(['average', 'min', 'max'])
    print("Ganancias promedio: " + str(round(result['average'], 2)))
    print("Menor ganancias: " + str(result['min']))
    print("Mayor ganancias: " + str(result['max']))
    print_buffer()

    result = df.groupby('release_year')['id'].aggregate('count')
    print(result)
    result.to_csv("Dataset/releases_by_year.csv")
    print_buffer()

    genres: dict = dict()
    result = df.groupby('genres')['id'].aggregate('count')
    print(result)
    print_buffer()
    
    for indx, value in result.items(): 
        values = str(indx).lstrip('[')
        values = values.rstrip(']')
        values = values.split(', ')
        for val in values: 
            val = val.strip('\'')
            if val not in genres: 
                genres[val] = 1
            else: 
                genres[val] += 1
    genre_list = list()
    genre_count = list()
    for genre, num in genres.items(): 
        genre_list.append(genre)
        genre_count.append(num)
    new_df = {
        "genres": genre_list, 
        "count": genre_count
    }
    new_df = pd.DataFrame(new_df)
    new_df = new_df.groupby('genres')['count'].aggregate('sum')
    new_df.to_csv('Dataset/number_of_movies_by_genre.csv')
    print_buffer()
