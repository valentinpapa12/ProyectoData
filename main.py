from fastapi import FastAPI
import pandas as pd

#Cargamos el dataset que previamente limpiamos
df = pd.read_csv("data4.csv")

app = FastAPI()
    

#Consulta 1
#Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

@app.get("/get_word_count/{plataforma}/{keyword}")
async def get_word_count(plataforma: str, keyword: str):
    if plataforma == "amazon":
        #Filtramos por la primera letra del id
        df_filtro = df[df["id"].str.startswith("a")]
        #Buscamos la palabra clave en el titulo y contamos todos los registros
        cuenta = df_filtro["title"].str.contains(keyword).sum()
        return {"plataforma": plataforma, "keyword": keyword, "cantidad": int(cuenta)}
        
    #Hacemos lo mismo para las demás plataformas
    if plataforma == "disney":
        df_filtro = df[df["id"].str.startswith("d")]
        cuenta = df_filtro["title"].str.contains(keyword).sum()
        return {"plataforma": plataforma, "keyword": keyword, "cantidad": int(cuenta)}
    if plataforma == "hulu":
        df_filtro = df[df["id"].str.startswith("h")]
        cuenta = df_filtro["title"].str.contains(keyword).sum()
        return {"plataforma": plataforma, "keyword": keyword, "cantidad": int(cuenta)}
    if plataforma == "netflix":
        df_filtro = df[df["id"].str.startswith("n")]
        cuenta = df_filtro["title"].str.contains(keyword).sum()
        return {"plataforma": plataforma, "keyword": keyword, "cantidad": int(cuenta)}
    
    
#Consulta 2
#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

@app.get("/get_score_count/{plataforma}/{puntaje}/{anio}")
async def get_score_count(plataforma: str, puntaje: int, anio: int):
    if plataforma == "amazon":
        #Filtramos por la primera letra del id
        df_filtro = df[df["id"].str.startswith("a")]
        #Ahora filtramos por tipo de contenido (pelicula)
        df_filtro = df_filtro[df_filtro["duration_type"] == "min"]
        #Filtramos por el puntaje
        df_filtro = df_filtro[df_filtro["score"] > puntaje]
        #Filtramos por año
        df_filtro = df_filtro[df_filtro["release_year"] == anio]
        #Contamos la cantidad de peliculas
        cuenta = df_filtro["id"].count()
        return {"plataforma": plataforma, "puntaje": int(puntaje), "cantidad": int(cuenta)}
    
    #Hacemos lo mismo para las demás plataformas
    if plataforma == "disney":
        df_filtro = df[df["id"].str.startswith("d")]
        df_filtro = df_filtro[df_filtro["duration_type"] == "min"]
        df_filtro = df_filtro[df_filtro["score"] > puntaje]
        df_filtro = df_filtro[df_filtro["release_year"] == anio]
        cuenta = df_filtro["id"].count()
        return {"plataforma": plataforma, "puntaje": int(puntaje), "cantidad": int(cuenta)}
    if plataforma == "hulu":
        df_filtro = df[df["id"].str.startswith("h")]
        df_filtro = df_filtro[df_filtro["duration_type"] == "min"]
        df_filtro = df_filtro[df_filtro["score"] > puntaje]
        df_filtro = df_filtro[df_filtro["release_year"] == anio]
        cuenta = df_filtro["id"].count()
        return {"plataforma": plataforma, "puntaje": int(puntaje), "cantidad": int(cuenta)}
    if plataforma == "netflix":
        df_filtro = df[df["id"].str.startswith("n")]
        df_filtro = df_filtro[df_filtro["duration_type"] == "min"]
        df_filtro = df_filtro[df_filtro["score"] > puntaje]
        df_filtro = df_filtro[df_filtro["release_year"] == anio]
        cuenta = df_filtro["id"].count()
        return {"plataforma": plataforma, "puntaje": int(puntaje), "cantidad": int(cuenta)}
    
#Consulta 3
#Película que más duró según año, plataforma y tipo de duración

@app.get("/get_longest/{plataforma}/{anio}/{tipo_duracion}")
async def get_longest(plataforma: str, anio: int, tipo_duracion: str):
    if plataforma == "amazon":
        #Filtramos por la primera letra del id
        df_filtro = df[df["id"].str.startswith("a")]
        #Filtramos por tipo de duración (película o serie)
        df_filtro = df_filtro[df_filtro["duration_type"] == tipo_duracion]
        #Filtramos por el año
        df_filtro = df_filtro[df_filtro["release_year"] == anio]
        #Ordenamos de mayor a menor por duración
        df_filtro = df_filtro.sort_values(by="duration_int", ascending=False)
        longest = df_filtro["title"].iloc[0]
        duracion = df_filtro["duration_int"].iloc[0]
        return {
                "plataforma": plataforma, "longest": str(longest), 
                "duracion": int(duracion), "tipo_duracion": tipo_duracion
                }
    
    #Hacemos lo mismo con las demás plataformas
    if plataforma == "disney":
        df_filtro = df[df["id"].str.startswith("d")]
        df_filtro = df_filtro[df_filtro["duration_type"] == tipo_duracion]
        df_filtro = df_filtro[df_filtro["release_year"] == anio]
        df_filtro = df_filtro.sort_values(by="duration_int", ascending=False)
        longest = df_filtro["title"].iloc[0]
        duracion = df_filtro["duration_int"].iloc[0]
        return {
                "plataforma": plataforma, "longest": str(longest), 
                "duracion": int(duracion), "tipo_duracion": tipo_duracion
                }
    if plataforma == "hulu":
        df_filtro = df[df["id"].str.startswith("h")]
        df_filtro = df_filtro[df_filtro["duration_type"] == tipo_duracion]
        df_filtro = df_filtro[df_filtro["release_year"] == anio]
        df_filtro = df_filtro.sort_values(by="duration_int", ascending=False)
        longest = df_filtro["title"].iloc[0]
        duracion = df_filtro["duration_int"].iloc[0]
        return {
                "plataforma": plataforma, "longest": str(longest), 
                "duracion": int(duracion), "tipo_duracion": tipo_duracion
                }
    if plataforma == "netflix":
        df_filtro = df[df["id"].str.startswith("n")]
        df_filtro = df_filtro[df_filtro["duration_type"] == tipo_duracion]
        df_filtro = df_filtro[df_filtro["release_year"] == anio]
        df_filtro = df_filtro.sort_values(by="duration_int", ascending=False)
        longest = df_filtro["title"].iloc[0]
        duracion = df_filtro["duration_int"].iloc[0]
        return {
                "plataforma": plataforma, "longest": str(longest), 
                "duracion": int(duracion), "tipo_duracion": tipo_duracion
                }
        

#Consulta 4
#Cantidad de series y películas por rating

@app.get("/get_rating_count/{rating}")
async def get_rating_count(rating: str):
    #Filtramos el dataframe por rating
    df_filtro = df[df["rating"] == rating]
    cuenta = df_filtro["id"].count()
    return {"rating": rating, "cantidad": int(cuenta)}