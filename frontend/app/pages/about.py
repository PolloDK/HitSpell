import streamlit as st

def show_about():
    st.markdown("<h2 style='color:#f72585'>🎧 Sobre el proyecto</h2>", unsafe_allow_html=True)
    st.markdown("""
    Este proyecto utiliza inteligencia artificial para analizar canciones a partir de sus características acústicas extraídas directamente del audio.
    A través de modelos entrenados con decenas de miles de canciones, estimamos el potencial de popularidad de una pista y entregamos sugerencias específicas para mejorar su impacto.

    El análisis se basa en variables acústicas y perceptuales obtenidas mediante extracción automática.
    A continuación se explican sus principales componentes:
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📂 Variables", unsafe_allow_html=True)

    st.markdown("""
**🎼 `genre`**
Representa el género al que apunta la canción (ej: rock, pop, electrónica). Esta variable la define el artista.

**⏱️ `duration_ms`**
Duración total del audio en milisegundos.

---

### 🎶 Carácter y emociones (`high_...` variables)

**🕺 `high_danceability_value` / `high_danceability_probability`**
Indica qué tan bailable es la canción. Puede influir en su capacidad para funcionar en fiestas o contextos sociales.

**👩‍🎤 `high_gender_value` / `high_gender_probability`**
Clasificación subjetiva del timbre de la voz: femenina o masculina. No representa género real, sino la percepción auditiva.

**🎻 `high_mood_acoustic_value` / `high_mood_acoustic_probability`**
Mide si la canción suena más acústica (instrumentos reales) o no (electrónica, digital).

**💥 `high_mood_aggressive_value` / `high_mood_aggressive_probability`**
Captura cuán intensa o agresiva es la canción en su energía o dinámica.

**🎛️ `high_mood_electronic_value` / `high_mood_electronic_probability`**
Refleja si tiene una producción basada en sonidos electrónicos.

**😊 `high_mood_happy_value` / `high_mood_happy_probability`**
Indica si la canción transmite felicidad o positividad.

**🎉 `high_mood_party_value` / `high_mood_party_probability`**
Evalúa si la canción se asocia a un contexto de fiesta o celebración.

**😌 `high_mood_relaxed_value` / `high_mood_relaxed_probability`**
Mide si la canción evoca calma o una atmósfera relajada.

**😢 `high_mood_sad_value` / `high_mood_sad_probability`**
Estima el nivel de melancolía o tristeza en la música.

**🎯 `high_moods_mirex_value` / `high_moods_mirex_probability`**
Clasificación general emocional basada en clústeres musicales definidos por MIR (Music Information Retrieval).

**🔆 `high_timbre_value` / `high_timbre_probability`**
Describe el color del sonido: puede ser brillante, oscuro, metálico, etc.

**🎼 `high_tonal_atonal_value` / `high_tonal_atonal_probability`**
Indica si la canción tiene una estructura tonal clara (como en la música popular) o no (atonalidad, como en experimental).

**🎙️ `high_voice_instrumental_value` / `high_voice_instrumental_probability`**
Define si la pista es vocal, instrumental o mixta.

---

### 🎛️ Parámetros técnicos (`low_...`, `audio_...`)

**🔊 `low_average_loudness`**
Sonoridad promedio de la canción. Afecta cómo se percibe el volumen general.

**📈 `low_dynamic_complexity`**
Variedad de dinámicas dentro de la canción (pasajes suaves vs fuertes).

**🎚️ `low_mfcc_mean_0` a `low_mfcc_mean_12`**
Coeficientes cepstrales que capturan textura, timbre y propiedades frecuenciales. Se usan comúnmente en procesamiento de audio.

**🎧 `audio_sample_rate` / `audio_analysis_sample_rate`**
Frecuencia de muestreo del audio, medida en Hz.

**🔒 `audio_codec` / `audio_bit_rate` / `audio_lossless`**
Información técnica de compresión del archivo. Afecta calidad sonora.

**🎛️ `audio_equal_loudness` / `audio_replay_gain`**
Relacionados con ajustes de percepción de volumen.

**🧪 `audio_md5_encoded`**
Identificador único del archivo (hash), usado para trazabilidad.

**🎛️ `audio_downmix`**
Describe si el audio fue convertido de estéreo a mono, o es una mezcla de canales.

---

### 🎵 Elementos musicales

**🎵 `low_key_key` / `low_key_scale` / `low_key_strength`**
Tonalidad, modo (mayor/menor) y fuerza con que se detecta dicha tonalidad.

**🎹 `low_chords_key` / `low_chords_scale` / `low_chords_changes_rate`**
Progresión de acordes y cuán frecuentemente cambian. Cambios rápidos dan sensación de complejidad.

**🎶 `low_tuning_frequency`**
Frecuencia base de afinación (ej: 440 Hz). Algunas canciones usan valores alternativos (como 432 Hz) por estilo.

**💃 `low_danceability`**
Índice técnico de qué tan bailable es la canción, calculado directamente del ritmo y dinámica.

**⚡ `low_onset_rate`**
Frecuencia con que aparecen nuevos sonidos. Más alto = más eventos rítmicos.

**🕐 `low_bpm` / `low_beats_count`**
Velocidad del pulso musical (beats por minuto) y número de pulsos detectados en toda la canción.
""", unsafe_allow_html=True)
