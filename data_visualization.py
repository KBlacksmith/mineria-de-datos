import pandas as pd
import os
import matplotlib.pyplot as plt

def visualize_data(): 
    if not os.path.exists('img'): 
        os.mkdir('img')

    result = pd.read_csv('Dataset/releases_by_year.csv')
    result = result.groupby('release_year')['id'].aggregate('sum')
    result.plot(kind='bar', xlabel='Año de lanzamiento', ylabel='Cantidad de películas', title='Películas más populares')
    plt.savefig("img/number_of_movies_by_release_year.png")
    plt.show()

    plt.cla()
    result = pd.read_csv('Dataset/number_of_movies_by_genre.csv')
    result = result.groupby('genres')['count'].aggregate('sum')
    result.plot(kind='pie', y='Cantidad de Juegos', autopct='%1.0f%%')
    plt.savefig('img/number_of_movies_by_genre.png')
    plt.show()