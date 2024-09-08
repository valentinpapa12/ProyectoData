#Creo una función que automatice la limpieza de todos los datasets:
def limpieza_data(ruta):
    '''
    Se realiza una limpieza del dataset indicado.

    Esta función toma como argumento la ruta relativa del dataset y aplica
    las siguientes condiciones:

    1) Generar campo id.
    2) Los valores nulos del campo rating deberán reemplazarse por el string “G”.
    3) De haber fechas, deberán tener el formato AAAA-mm-dd.
    4) Los campos de texto deberán estar en minúsculas, sin excepciones.
    5) El campo duration debe convertirse en dos campos: duration_int y duration_type.

    Parámetros
    ----------
    ruta : str
        Ruta relativa del dataset en formato csv.
    
    Retorna
    ---------
    DataFrame
        El dataset transformado y limpio
    
    Ejemplo
    ---------
    df = limpieza_data("dataset.csv")
    df
        col1  col2
    0     1     3
    1     2     4
    '''
    
    import pandas as pd
    import datetime
    import numpy as np
    
    #Cargamos el dataset
    df = pd.read_csv(ruta, sep=",")
    
    #Generamos campo id (primera letra de plataforma y el propio show_id)
    df.insert(0, "id", ruta[60] + df["show_id"].values)

    #Reemplazamos valores nulos del campo rating con "G"
    df["rating"].fillna("G", inplace=True)

    #Formateamos el campo "date_added" con formato "AAAA-mm-dd"
    df["date_added"] = pd.to_datetime(df["date_added"], errors='coerce')

    #Convertir todos los campos de texto en minúsculas
    df["cast"] = df["cast"].astype('object') #Cambio el tipo de dato para evitar fallos

    columnas = ["type", "title", "director", "cast", "country", "listed_in", "description", "duration", "rating"]
    for columna in columnas:
        df[columna] = df[columna].str.lower()

    #A partir del campo "duration", crear 2 columnas. Una "duration_int" y otra "duration_type"
    lista_int = []
    lista_type = []
    
    for i in range(len(df)):
        
        #Filtramos valores nulos
        mask = df[df["duration"].isnull()]
        filtro = list(mask["id"].values)
        
        if df["id"][i] in filtro:
            lista_int.append(np.nan)
            lista_type.append(np.nan)
        else:
            lista_int.append(int(str(df["duration"][i]).split()[0]))
            lista_type.append(str(df["duration"][i]).split()[1])
    
    df["duration_int"] = lista_int
    df["duration_type"] = lista_type
    df["duration_int"] = df["duration_int"].astype('Int64') #Cambio el tipo de dato
    #Reemplazamos seasons por season en singular
    df["duration_type"].replace("seasons", "season", inplace=True)

    return df

#Limpiamos todos los datasets
df_amazon = limpieza_data("C:/Users/Administrador/Documents/Nueva carpeta (2)/Datasets/amazon_prime_titles_score.csv")
df_disney = limpieza_data("C:/Users/Administrador/Documents/Nueva carpeta (2)/Datasets/disney_plus_titles-score.csv")
df_hulu = limpieza_data("C:/Users/Administrador/Documents/Nueva carpeta (2)/Datasets/hulu_titles-score (2).csv")
df_netflix = limpieza_data("C:/Users/Administrador/Documents/Nueva carpeta (2)/Datasets/netflix_titles-score.csv")

#Concatenamos todos los dataframes para formar uno solo
import pandas as pd
df = pd.concat([df_amazon, df_disney, df_hulu, df_netflix])

#Exportamos el dataframe maestro a formato csv
df.to_csv("data.csv")
print("Ejecución Exitosa")

