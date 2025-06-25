import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from src.model.registry import load_model


def predict_from_input(model, input_dict):
    df = pd.DataFrame([input_dict])
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df[["Pclass", "Sex", "Age", "Fare"]] = df[["Pclass", "Sex", "Age", "Fare"]].astype(float)
    return model.predict(df)[0]


# ✅ CLI entry point
def main():
    model = load_model()
    sample = {
  "mbid": "c49650c9-bb57-4657-9061-f963f79d37ff",
  "title": "Мой рок-н-ролл",
  "artist": "Би-2",
  "genre": "rock",
  "year": 2015,
  "duration_ms": 405000.0,
  "high_danceability_value": "danceable",
  "high_danceability_probability": 0.7415766716,
  "high_gender_value": "female",
  "high_gender_probability": 0.980534613132,
  "high_genre_dortmund_value": "electronic",
  "high_genre_dortmund_probability": 0.999589502811,
  "high_genre_electronic_value": "trance",
  "high_genre_electronic_probability": 0.500469386578,
  "high_genre_rosamerica_value": "pop",
  "high_genre_rosamerica_probability": 0.654012680054,
  "high_genre_tzanetakis_value": "jaz",
  "high_genre_tzanetakis_probability": 0.316520601511,
  "high_ismir04_rhythm_value": "VienneseWaltz",
  "high_ismir04_rhythm_probability": 0.262205898762,
  "high_mood_acoustic_value": "not_acoustic",
  "high_mood_acoustic_probability": 0.529871344566,
  "high_mood_aggressive_value": "not_aggressive",
  "high_mood_aggressive_probability": 0.995502233505,
  "high_mood_electronic_value": "electronic",
  "high_mood_electronic_probability": 0.585565507412,
  "high_mood_happy_value": "not_happy",
  "high_mood_happy_probability": 0.794855237007,
  "high_mood_party_value": "not_party",
  "high_mood_party_probability": 0.620302379131,
  "high_mood_relaxed_value": "not_relaxed",
  "high_mood_relaxed_probability": 0.763528585434,
  "high_mood_sad_value": "not_sad",
  "high_mood_sad_probability": 0.523806273937,
  "high_moods_mirex_value": "Cluster3",
  "high_moods_mirex_probability": 0.386361151934,
  "high_timbre_value": "bright",
  "high_timbre_probability": 0.854395031929,
  "high_tonal_atonal_value": "tonal",
  "high_tonal_atonal_probability": 0.836964964867,
  "high_voice_instrumental_value": "instrumental",
  "high_voice_instrumental_probability": 0.900350928307,
  "low_average_loudness": 0.868578135967,
  "low_dynamic_complexity": 3.66314101219,
  "low_mfcc_mean_0": -651.651000977,
  "low_mfcc_mean_1": 113.907058716,
  "low_mfcc_mean_2": 12.2799434662,
  "low_mfcc_mean_3": 19.9522800446,
  "low_mfcc_mean_4": 9.54801654816,
  "low_mfcc_mean_5": 2.25168848038,
  "low_mfcc_mean_6": 2.61635088921,
  "low_mfcc_mean_7": 0.892470479012,
  "low_mfcc_mean_8": -0.450145632029,
  "low_mfcc_mean_9": -0.680565237999,
  "low_mfcc_mean_10": -3.51771330833,
  "low_mfcc_mean_11": -2.01388978958,
  "low_mfcc_mean_12": -0.909115970135,
  "audio_sample_rate": 44100.0,
  "audio_codec": "flac",
  "audio_bit_rate": 0,
  "audio_equal_loudness": 0.0,
  "audio_analysis_sample_rate": 44100.0,
  "audio_length": 405.386657715,
  "audio_md5_encoded": "b822e4f7e7c07deaf63a74f41ad32a3f",
  "audio_replay_gain": -12.9106311798,
  "audio_downmix": "mix",
  "audio_lossless": true,
  "low_key_key": "A",
  "low_key_scale": "minor",
  "low_key_strength": 0.660111248493,
  "low_chords_scale": "minor",
  "low_chords_changes_rate": 0.0429504066706,
  "low_chords_key": "A",
  "low_chords_number_rate": 0.00125987862702,
  "low_tuning_nontempered_energy_ratio": 0.746798217297,
  "low_tuning_frequency": 437.213165283,
  "low_tuning_diatonic_strength": 0.531847715378,
  "low_tuning_equal_tempered_deviation": 0.103362463415,
  "low_danceability": 1.06615579128,
  "low_onset_rate": 3.15730714798,
  "low_bpm": 119.776863098,
  "low_beats_count": 799.0
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
        return {"greeting": "Hello, welcome to Hitalyzer API v.1.1!"}

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
        mbid: str,
        title: str,
        artist: str,
        genre: str,
        year: int,
        duration_ms: float,
        high_danceability_value: str,
        high_danceability_probability: float,
        high_gender_value: str,
        high_gender_probability: float,
        high_genre_dortmund_value: str,
        high_genre_dortmund_probability: float,
        high_genre_electronic_value: str,
        high_genre_electronic_probability: float,
        high_genre_rosamerica_value: str,
        high_genre_rosamerica_probability: float,
        high_genre_tzanetakis_value: str,
        high_genre_tzanetakis_probability: float,
        high_ismir04_rhythm_value: str,
        high_ismir04_rhythm_probability: float,
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
        audio_sample_rate: float,
        audio_codec: str,
        audio_bit_rate: int,
        audio_equal_loudness: float,
        audio_analysis_sample_rate: float,
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
        low_chords_number_rate: float,
        low_tuning_nontempered_energy_ratio: float,
        low_tuning_frequency: float,
        low_tuning_diatonic_strength: float,
        low_tuning_equal_tempered_deviation: float,
        low_danceability: float,
        low_onset_rate: float,
        low_bpm: float,
        low_beats_count: float
        ):
        
# ✅ Only runs with `python -m src.api.api`
if __name__ == "__main__":
    main()
