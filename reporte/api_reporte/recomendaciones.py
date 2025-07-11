import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
MODO = 1 #1:prueba (canciones propias)      2:real (con nuevo input)
RUTA_FULL_FEATURES = 'features_full_final.csv'

client = OpenAI(api_key = API_KEY)

def filtrar_features(df:pd.DataFrame | pd.Series) -> pd.DataFrame | pd.Series:
    """Funcion que filtra los features que posiblemente iran al prompt"""
    ritmo_energia = [
        'low_bpm', 'low_onset_rate', 'low_danceability',
        'low_dynamic_complexity', 'low_average_loudness', 'high_danceability_probability'
    ]
    tonalidad = [
        'low_key_strength', 'low_chords_changes_rate'
    ]
    mfccs = [f'low_mfcc_mean_{i}' for i in range(13)]
    moods = [
        'high_mood_acoustic_probability',
        'high_mood_aggressive_probability',
        'high_mood_happy_probability',
        'high_mood_party_probability',
        'high_mood_relaxed_probability',
        'high_mood_sad_probability'
    ]
    columnas = ['genre'] + ritmo_energia + tonalidad + mfccs + moods
    return df[columnas].copy()

def obtener_genero(nueva_cancion:pd.Series) -> str:
    """Función que dependiendo el modo, retorna el género de la nueva canción a analizar"""
    if MODO == 1:
        return nueva_cancion['genre']
    else:
        genero = input("Ingresa el género de la canción:")
        return genero

def promedio_genero(df_filtrado:pd.DataFrame, genero:str) -> pd.Series:
    """Funcion que calcula los promedios en base al genero"""
    return df_filtrado[df_filtrado['genre'] == genero].mean(numeric_only=True)

def comparar_cancion_con_promedio(nueva_cancion:pd.Series, promedio_genero:pd.Series) -> dict:
    """Función que calcula y retorna las diferencias de los valores de las features de la nueva canción con el promedio de su género"""
    if MODO == 1:
        nueva_cancion.drop(['genre'], inplace=True)
    diferencias = {}
    for feature in nueva_cancion.index:
        valor_actual = nueva_cancion[feature]
        valor_referencia = promedio_genero[feature]
        diferencias[feature] = round(float(valor_actual-valor_referencia),3)
    return diferencias

def generar_prompt(genero:str, diferencias:dict, nueva_cancion:pd.Series, promedio_genero:pd.Series, porcentaje_umbral:float=0.05) -> str:
    """Función que genera el prompt para pasarse a la api de open ai"""
    sugerencias = []

    for feature, diferencia in diferencias.items():
        val_actual = nueva_cancion[feature]
        val_prom = promedio_genero[feature]

        umbral = abs(val_prom * porcentaje_umbral) if val_prom != 0 else porcentaje_umbral

        if abs(diferencia) > umbral:
            if diferencia < 0:
                sugerencias.append(
                    f"- '{feature}': el valor actual es {val_actual:.2f}, mientras que el promedio del género es {val_prom:.2f}. Está por debajo del promedio; podrías intentar incrementarlo.")
            else:
                sugerencias.append(
                    f"- '{feature}': el valor actual es {val_actual:.2f}, mientras que el promedio del género es {val_prom:.2f}. Está por encima del promedio; podrías ajustarlo.")

    if not sugerencias:
        sugerencias.append("Los valores están bastante alineados con el promedio del género.")

    prompt = f"Tengo una canción del género {genero}. Estas son las diferencias respecto al promedio de las canciones más populares del mismo género:\n\n"
    prompt += "\n".join(sugerencias)
    prompt += "\n\nDame recomendaciones musicales para mejorar esta canción"
    prompt += "\nLos nombres de las features vienen en inglés, pero la respuesta debe ser todo en castellano."

    return prompt

def obtener_recomendacion(prompt:str) -> str:
    """Función que en base al promtp, obtiene las recomendaciones de open ai"""
    response = client.chat.completions.create(
        model='gpt-4.1-mini',
        messages=[
            {"role": "system", "content": "Eres una app de música que brinda consejos claros y útiles sobre cómo mejorar una canción según sus características."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    datos = filtrar_features(pd.read_csv(RUTA_FULL_FEATURES))       #Leer datos y filtrar
    datos.dropna(inplace=True)
    nueva_cancion = datos.sample(n=1).squeeze()                     #Para prueba usamos una muestra del mismo dataset
    genero = obtener_genero(nueva_cancion)
    promedio_genero_nueva_cancion = promedio_genero(datos, genero)
    diferencias = comparar_cancion_con_promedio(nueva_cancion, promedio_genero_nueva_cancion)
    prompt = generar_prompt(genero, diferencias, nueva_cancion, promedio_genero_nueva_cancion)
    recomendacion = obtener_recomendacion(prompt)
    print(recomendacion)
