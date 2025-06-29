import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

def drop_columns(df, cols_to_drop):
    return df.drop(columns=cols_to_drop)

def fill_missing_values(df):
        if 'duration_ms' in df.columns:
            df['duration_ms'] = df['duration_ms'].fillna(df['duration_ms'].median())
        if 'audio_sample_rate' in df.columns:
            df['audio_sample_rate'] = df['audio_sample_rate'].fillna(df['audio_sample_rate'].mode()[0])
        return df

def scale_minmax(df, columns_to_scale):
    scaler = MinMaxScaler()
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
    return df

def encode_binary_column(df, column, positive_val='danceable', negative_val='not_danceable'):
    df[column + '_encoded'] = df[column].map({positive_val: 1, negative_val: 0})
    return df.drop(columns=[column])

def encode_binary_multiple(df, binary_map):
    for col, mapping in binary_map.items():
        df[col] = df[col].map(mapping).fillna(0).astype(int)
    return df

def one_hot_encode(df, cols):
    return pd.get_dummies(df, columns=cols, drop_first=True)

def frequency_encode(df, cols):
    for col in cols:
        freq_map = df[col].value_counts().to_dict()
        df[col] = df[col].map(freq_map)
    return df

def final_cleanup(df):
    if 'release_date' in df.columns:
        df['release_year'] = df['release_date'].dt.year
        df['release_year'].fillna(df['release_year'].median(), inplace=True)
        df.drop(columns='release_date', inplace=True)

    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].median())

    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mode()[0])

    return df

def scale_standard(df):
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

def preprocess_features(df: pd.DataFrame) -> pd.DataFrame:
    df = drop_columns(df, ['audio_md5_encoded'])
    #Fill null values
    df_fill_missing_values = fill_missing_values(df)
    #Scale with MinMaxScaler to numeric values
    df_scale_minmax = scale_minmax(df_fill_missing_values, ['duration_ms'])
    #Encode binary values
    df_encode = encode_binary_column(df_scale_minmax, 'high_danceability_value', 'danceable', 'not_danceable')
    binary_map = {
    'high_gender_value': {'female': 1, 'male': 0},
    'high_mood_acoustic_value': {'acoustic': 1, 'not_acoustic': 0},
    'high_mood_aggressive_value': {'aggressive': 1, 'not_aggressive': 0},
    'high_mood_electronic_value': {'electronic': 1, 'not_electronic': 0},
    'high_mood_happy_value': {'happy': 1, 'not_happy': 0},
    'high_mood_party_value': {'party': 1, 'not_party': 0},
    'high_mood_relaxed_value': {'relaxed': 1, 'not_relaxed': 0},
    'high_mood_sad_value': {'sad': 1, 'not_sad': 0},
    'high_timbre_value': {'bright': 1, 'dark': 0},
    'high_tonal_atonal_value': {'tonal': 1, 'atonal': 0},
    'high_voice_instrumental_value': {'voice': 1, 'instrumental': 0},
    'audio_downmix': {'mix': 1, 'left': 0},
    'low_key_scale': {'major': 1, 'minor': 0},
    'low_chords_scale': {'major': 1, 'minor': 0}
    }
    df_encode_multiple = encode_binary_multiple(df_encode, binary_map)
    
    df_encode_multiple_hot_encode = one_hot_encode(df_encode_multiple, ['high_moods_mirex_value'])
    
    #Frecuency encoding for medium cardinality columns
    medium_card_cols = [
    'audio_codec', 'low_key_key', 'low_chords_key'
    ]
    df_frequency_encode = frequency_encode(df_encode_multiple_hot_encode, medium_card_cols)
    #Remainig clean
    df_final_preview = final_cleanup(df_frequency_encode)
    #Final Scaling
    df = scale_standard(df_final_preview)
    df = df.fillna(df.mean(numeric_only=True))
    return df

    
    
    