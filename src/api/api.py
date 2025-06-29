import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from src.model.registry import load_model
from src.model.preprocessor import preprocess_features
import pandas as pd

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', 1000)        # Set width to prevent line wrapping
pd.set_option('display.max_colwidth', None) # Show full content of each column


def predict_from_input(model, input_dict):
    df = pd.DataFrame([input_dict])
    X_processed = preprocess_features(df)
    #y_pred = model.predict(X_processed)
    #return model.predict(X_processed)[0]
    for col in X_processed.columns:
        print(col)
    #return X_processed.info()

# ✅ CLI entry point
def main():
    model = load_model()
    sample = {
        "duration_ms": 43784,
        "high_danceability_value": "not_danceable",
        "high_danceability_probability": 0.8201501369476318,
        "high_gender_value": "female",
        "high_gender_probability": 0.6024620532989502,
        "high_mood_acoustic_value": "non_acoustic",
        "high_mood_acoustic_probability": 0.5138947367668152,
        "high_mood_aggressive_value": "not_aggressive",
        "high_mood_aggressive_probability": 0.9516782760620117,
        "high_mood_electronic_value": "electronic",
        "high_mood_electronic_probability": 0.5055626034736633,
        "high_mood_happy_value": "non_happy",
        "high_mood_happy_probability": 0.9658797979354858,
        "high_mood_party_value": "non_party",
        "high_mood_party_probability": 0.953216552734375,
        "high_mood_relaxed_value": "relaxed",
        "high_mood_relaxed_probability": 0.9485642313957214,
        "high_mood_sad_value": "sad",
        "high_mood_sad_probability": 0.7622365951538086,
        "high_moods_mirex_value": "Cluster3",
        "high_moods_mirex_probability": 0.42989349365234375,
        "high_timbre_value": "bright",
        "high_timbre_probability": 0.5134698152542114,
        "high_tonal_atonal_value": "atonal",
        "high_tonal_atonal_probability": 0.8252235651016235,
        "high_voice_instrumental_value": "instrumental",
        "high_voice_instrumental_probability": 0.8899824619293213,
        "low_average_loudness": 12.39195411836107,
        "low_dynamic_complexity": 0.0,
        "low_mfcc_mean_0": -772.3985595703125,
        "low_mfcc_mean_1": 211.89645385742188,
        "low_mfcc_mean_2": -27.749265670776367,
        "low_mfcc_mean_3": -9.654556274414062,
        "low_mfcc_mean_4": 4.18579626083374,
        "low_mfcc_mean_5": 11.31861400604248,
        "low_mfcc_mean_6": -7.522047519683838,
        "low_mfcc_mean_7": -3.0000829696655273,
        "low_mfcc_mean_8": -1.4680936336517334,
        "low_mfcc_mean_9": 5.078001022338867,
        "low_mfcc_mean_10": -0.7559494376182556,
        "low_mfcc_mean_11": -3.4250376224517822,
        "low_mfcc_mean_12": -4.563534259796143,
        "audio_sample_rate": 44100,
        "audio_codec": "unknown",
        "audio_bit_rate": 0,
        "audio_equal_loudness": 0.0,
        "audio_analysis_sample_rate": 44100.0,
        "audio_length": 43.784444444444446,
        "audio_md5_encoded": "837d3d311f6d89121a901eed8625c7b9",
        "audio_replay_gain": 0.0005527925095520914,
        "audio_downmix": "unknown",
        "audio_lossless": False,
        "low_key_key": "A",
        "low_key_scale": "minor",
        "low_key_strength": 0.8386735320091248,
        "low_chords_scale": "major",
        "low_chords_changes_rate": 0.051906779408454895,
        "low_chords_key": "A",
        "low_tuning_frequency": 450.02447509765625,
        "low_danceability": 1.0621150732040405,
        "low_onset_rate": 3.088253974914551,
        "low_bpm": 153.72462463378906,
        "low_beats_count": 111
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
        
        input_data = {
             "duration_ms": duration_ms,
             "high_danceability_value": high_danceability_value,
             "high_danceability_probability": high_danceability_probability,
             "high_gender_value": high_gender_value,
             "high_gender_probability":high_gender_probability,
             "high_mood_acoustic_value": high_mood_acoustic_value,
             "high_mood_acoustic_probability":high_mood_acoustic_probability,
             "high_mood_aggressive_value": high_mood_aggressive_value,
             "high_mood_aggressive_probability": high_mood_aggressive_probability,
             "high_mood_electronic_value": high_mood_electronic_value,
             "high_mood_electronic_probability": high_mood_electronic_probability,
             "high_mood_happy_value": high_mood_happy_value,
             "high_mood_happy_probability": high_mood_happy_probability,
             "high_mood_party_value": high_mood_party_value,
             "high_mood_party_probability": high_mood_party_probability,
             "high_mood_relaxed_value": high_mood_relaxed_value,
             "high_mood_relaxed_probability": high_mood_relaxed_probability,
             "high_mood_sad_value": high_mood_sad_value,
             "high_mood_sad_probability": high_mood_sad_probability,
             "high_moods_mirex_value": high_moods_mirex_value,
             "high_moods_mirex_probability": high_moods_mirex_probability,
             "high_timbre_value": high_timbre_value,
             "high_timbre_probability": high_timbre_probability,
             "high_tonal_atonal_value": high_tonal_atonal_value,
             "high_tonal_atonal_probability": high_tonal_atonal_probability,
             "high_voice_instrumental_value": high_voice_instrumental_value,
             "high_voice_instrumental_probability": high_voice_instrumental_probability,
             "low_average_loudness": low_average_loudness,
             "low_dynamic_complexity": low_dynamic_complexity,
             "low_mfcc_mean_0": low_mfcc_mean_0,
             "low_mfcc_mean_1": low_mfcc_mean_1,
             "low_mfcc_mean_2": low_mfcc_mean_2,
             "low_mfcc_mean_3": low_mfcc_mean_3,
             "low_mfcc_mean_4": low_mfcc_mean_4,
             "low_mfcc_mean_5": low_mfcc_mean_5,
             "low_mfcc_mean_6": low_mfcc_mean_6,
             "low_mfcc_mean_7": low_mfcc_mean_7,
             "low_mfcc_mean_8": low_mfcc_mean_8,
             "low_mfcc_mean_9": low_mfcc_mean_9,
             "low_mfcc_mean_10": low_mfcc_mean_10,
             "low_mfcc_mean_11": low_mfcc_mean_11,
             "low_mfcc_mean_12": low_mfcc_mean_12,
             "audio_sample_rate": audio_sample_rate,
             "audio_codec": audio_codec,
             "audio_bit_rate": audio_bit_rate,
             "audio_equal_loudness": audio_equal_loudness,
             "audio_analysis_sample_rate": audio_analysis_sample_rate,
             "audio_length": audio_length,
             "audio_md5_encoded": audio_md5_encoded,
             "audio_replay_gain": audio_replay_gain,
             "audio_downmix": audio_downmix,
             "audio_lossless": audio_lossless,
             "low_key_key": low_key_key,
             "low_key_scale": low_key_scale,
             "low_key_strength": low_key_strength,
             "low_chords_scale": low_chords_scale,
             "low_chords_changes_rate": low_chords_changes_rate,
             "low_chords_key": low_chords_key,
             "low_tuning_frequency": low_tuning_frequency,
             "low_danceability": low_danceability,
             "low_onset_rate": low_onset_rate,
             "low_bpm": low_bpm,
             "low_beats_count": low_beats_count     
         }
        result = predict_from_input(model, input_data)
        return {"Popularity": int(result)}
    
    @app.get("/report")
    def report():
        pass
# ✅ Only runs with `python -m src.api.api`
if __name__ == "__main__":
    main()
