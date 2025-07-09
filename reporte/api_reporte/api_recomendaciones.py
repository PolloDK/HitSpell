from recomendaciones import *
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

class Cancion(BaseModel):
    genre: str
    duration_ms: int
    high_danceability_value: str
    high_danceability_probability: float
    high_gender_value: str
    high_gender_probability: float
    high_mood_acoustic_value: str
    high_mood_acoustic_probability: float
    high_mood_aggressive_value: str
    high_mood_aggressive_probability: float
    high_mood_electronic_value: str
    high_mood_electronic_probability: float
    high_mood_happy_value: str
    high_mood_happy_probability: float
    high_mood_party_value: str
    high_mood_party_probability: float
    high_mood_relaxed_value: str
    high_mood_relaxed_probability: float
    high_mood_sad_value: str
    high_mood_sad_probability: float
    high_moods_mirex_value: str
    high_moods_mirex_probability: float
    high_timbre_value: str
    high_timbre_probability: float
    high_tonal_atonal_value: str
    high_tonal_atonal_probability: float
    high_voice_instrumental_value: str
    high_voice_instrumental_probability: float
    low_average_loudness: float
    low_dynamic_complexity: float
    low_mfcc_mean_0: float
    low_mfcc_mean_1: float
    low_mfcc_mean_2: float
    low_mfcc_mean_3: float
    low_mfcc_mean_4: float
    low_mfcc_mean_5: float
    low_mfcc_mean_6: float
    low_mfcc_mean_7: float
    low_mfcc_mean_8: float
    low_mfcc_mean_9: float
    low_mfcc_mean_10: float
    low_mfcc_mean_11: float
    low_mfcc_mean_12: float
    audio_sample_rate: float
    audio_codec: str
    audio_bit_rate: int
    audio_equal_loudness: float
    audio_analysis_sample_rate: float
    audio_length: float
    audio_md5_encoded: str
    audio_replay_gain: float
    audio_downmix: str
    audio_lossless: bool
    low_key_key: str
    low_key_scale: str
    low_key_strength: float
    low_chords_scale: str
    low_chords_changes_rate: float
    low_chords_key: str
    low_tuning_frequency: float
    low_danceability: float
    low_onset_rate: float
    low_bpm: float
    low_beats_count: int

app = FastAPI(debug=True)
app.state.datos = pd.read_csv('promedio_features.csv')

@app.post('/recomendar')
def dar_recomendacion(input:Cancion):
    datos = app.state.datos
    nueva_cancion = filtrar_features(pd.Series(input.model_dump()))
    genero = obtener_genero(nueva_cancion)
    promedio_genero_nueva_cancion = promedio_genero(datos, genero)
    diferencias = comparar_cancion_con_promedio(nueva_cancion,promedio_genero_nueva_cancion)
    prompt = generar_prompt(genero, diferencias, nueva_cancion, promedio_genero_nueva_cancion)
    recomendacion = obtener_recomendacion(prompt)
    return {'recomendacion': recomendacion}
