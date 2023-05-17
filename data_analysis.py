import pandas as pd
def analyze_data(df: pd.DataFrame): 
    print(df.columns)
    
    result = df['genres'].aggregate('count')
    #print("Combinaciones distintas de géneros: " + str(result))
    
    result = df.groupby('original_language')['id'].aggregate('count')
    #print("Películas por idioma original: ")
    #print(result)
    
    result = df.groupby('production_companies')['id'].aggregate('count')
    #print("Compañías productoras: ")
    #print(result)
    
    result = df['release_date'].aggregate(['min', 'max'])
    print("Fecha de estreno más antigua: " + str(result['min']))
    print("Fecha de estreno más reciente: " + str(result['max']))
    print("--------")

    result = df['popularity'].aggregate(['average', 'min', 'max'])
    #print("Índice de popularidad promedio: " + str(result))
    print("Popularidad más baja: " + str(result['min']))
    print("Popularidad más alta: " + str(result['max']))
    print("Popularidad promedio: " + str(round(result['average'], 2)))
    print("--------")

    result = df['vote_average'].aggregate(['average', 'min', 'max'])
    print("Peor calificación: " + str(result['min']))
    print("Mejor calificación: " + str(result['max']))
    print("Calificación promedio: " + str(round(result['average'], 2)))
    print("--------")

    result = df['budget'].aggregate(['average', 'max'])
    print("Presupuesto promedio: " + str(round(result['average'], 2)))
    print("Presupuesto más grande: " + str(result['max']))
    print("--------")


    result = df['revenue'].aggregate(['average', 'min', 'max'])
    print("Ganancias promedio: " + str(round(result['average'], 2)))
    print("Menor ganancias: " + str(result['min']))
    print("Mayor ganancias: " + str(result['max']))