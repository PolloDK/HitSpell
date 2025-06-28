import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from src.model.registry import load_model
from src.model.preprocessor import *


def predict_from_input(model, input_dict):
    df = pd.DataFrame([input_dict])
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df[["Pclass", "Sex", "Age", "Fare"]] = df[["Pclass", "Sex", "Age", "Fare"]].astype(float)
    #X_processed = preprocess_features(X_pred)
    #y_pred = model.predict(X_processed)
    return model.predict(df)[0]


# ✅ CLI entry point
def main():
    model = load_model()
    sample = {
        "duration_ms": 0,
        "high_danceability_value": "",
        "high_danceability_probability": 0.0,
        "high_gender_value": "",
        "high_gender_probability": 0.0,
        "high_mood_acoustic_value": "",
        "high_mood_acoustic_probability": 0.0,
        "high_mood_aggressive_value": "",
        "high_mood_aggressive_probability": 0.0,
        "high_mood_electronic_value": "",
        "high_mood_electronic_probability": 0.0,
        "high_mood_happy_value": "",
        "high_mood_happy_probability": 0.0,
        "high_mood_party_value": "",
        "high_mood_party_probability": 0.0,
        "high_mood_relaxed_value": "",
        "high_mood_relaxed_probability": 0.0,
        "high_mood_sad_value": "",
        "high_mood_sad_probability": 0.0,
        "high_moods_mirex_value": "",
        "high_moods_mirex_probability": 0.0,
        "high_timbre_value": "",
        "high_timbre_probability": 0.0,
        "high_tonal_atonal_value": "",
        "high_tonal_atonal_probability": 0.0,
        "high_voice_instrumental_value": "",
        "high_voice_instrumental_probability": 0.0,
        "low_average_loudness": 0.0,
        "low_dynamic_complexity": 0.0,
        "low_mfcc_mean_0": 0.0,
        "low_mfcc_mean_1": 0.0,
        "low_mfcc_mean_2": 0.0,
        "low_mfcc_mean_3": 0.0,
        "low_mfcc_mean_4": 0.0,
        "low_mfcc_mean_5": 0.0,
        "low_mfcc_mean_6": 0.0,
        "low_mfcc_mean_7": 0.0,
        "low_mfcc_mean_8": 0.0,
        "low_mfcc_mean_9": 0.0,
        "low_mfcc_mean_10": 0.0,
        "low_mfcc_mean_11": 0.0,
        "low_mfcc_mean_12": 0.0,
        "audio_sample_rate": 0,
        "audio_codec": "",
        "audio_bit_rate": 0,
        "audio_equal_loudness": false,
        "audio_analysis_sample_rate": 0,
        "audio_length": 0.0,
        "audio_md5_encoded": "",
        "audio_replay_gain": 0.0,
        "audio_downmix": "",
        "audio_lossless": False,
        "low_key_key": "",
        "low_key_scale": "",
        "low_key_strength": 0.0,
        "low_chords_scale": "",
        "low_chords_changes_rate": 0.0,
        "low_chords_key": "",
        "low_tuning_frequency": 0.0,
        "low_danceability": 0.0,
        "low_onset_rate": 0.0,
        "low_bpm": 0.0,
        "low_beats_count": 0
        }
    result = predict_from_input(model, sample)
    print(f"🎯 PopularityRate: {result}")


# ✅ FastAPI app setup
if __name__ != "__main__":
    app = FastAPI(title="Hitalyzer - Song Popularity Predictor")
    model = load_model()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def root():
        return {"greeting": "Hello, welcome to Hitalyzer API v.1.1"}

    @app.get("/predict_popularity")
    # def predict_popularity(Pclass: str, Sex: str, Age: str, Fare: float):
    #     input_data = {
    #         "Pclass": Pclass,
    #         "Sex": Sex,
    #         "Age": Age,
    #         "Fare": Fare
    #     }
    #     result = predict_from_input(model, input_data)
    #     return {"SurviveRate": int(result)}
    def predict_popularity(
        duration_ms: int,
        high_danceability_value: str,
        high_danceability_probability: float,
        high_gender_value: str,
        high_gender_probability: float,
        high_mood_acoustic_value: str,
        high_mood_acoustic_probability: float,
        high_mood_aggressive_value: str,
        high_mood_aggressive_probability: float,
        high_mood_electronic_value: str,
        high_mood_electronic_probability: float,
        high_mood_happy_value: str,
        high_mood_happy_probability: float,
        high_mood_party_value: str,
        high_mood_party_probability: float,
        high_mood_relaxed_value: str,
        high_mood_relaxed_probability: float,
        high_mood_sad_value: str,
        high_mood_sad_probability: float,
        high_moods_mirex_value: str,
        high_moods_mirex_probability: float,
        high_timbre_value: str,
        high_timbre_probability: float,
        high_tonal_atonal_value: str,
        high_tonal_atonal_probability: float,
        high_voice_instrumental_value: str,
        high_voice_instrumental_probability: float,
        low_average_loudness: float,
        low_dynamic_complexity: float,
        low_mfcc_mean_0: float,
        low_mfcc_mean_1: float,
        low_mfcc_mean_2: float,
        low_mfcc_mean_3: float,
        low_mfcc_mean_4: float,
        low_mfcc_mean_5: float,
        low_mfcc_mean_6: float,
        low_mfcc_mean_7: float,
        low_mfcc_mean_8: float,
        low_mfcc_mean_9: float,
        low_mfcc_mean_10: float,
        low_mfcc_mean_11: float,
        low_mfcc_mean_12: float,
        audio_sample_rate: int,
        audio_codec: str,
        audio_bit_rate: int,
        audio_equal_loudness: bool,
        audio_analysis_sample_rate: int,
        audio_length: float,
        audio_md5_encoded: str,
        audio_replay_gain: float,
        audio_downmix: str,
        audio_lossless: bool,
        low_key_key: str,
        low_key_scale: str,
        low_key_strength: float,
        low_chords_scale: str,
        low_chords_changes_rate: float,
        low_chords_key: str,
        low_tuning_frequency: float,
        low_danceability: float,
        low_onset_rate: float,
        low_bpm: float,
        low_beats_count: int ):
        pass
    
    @app.get("/report")
    def report():
        pass
# ✅ Only runs with `python -m src.api.api`
if __name__ == "__main__":
    main()
