"use client";

import Navbar from "@/components/Navbar";
import { Heading3 } from "lucide-react";
import Image from "next/image";

export default function About() {
  return (
    <>
      <Navbar />
      <main className="px-4 pt-24">
        <div className="flex flex-col justify-center max-w-4xl mx-auto space-y-6 mt-10 text-white text-left">

          <Image
            src="/HITSPELL.svg"
            alt="HitSpell Logo"
            width={320}
            height={100}
            className="mb-2"
          />

          <h6 className="text-4xl font-bold pt-20">
            ¿Qué es Hitspell?
          </h6>

          <p className="text-base md:text-lg">
            <strong>Hitspell</strong> es un proyecto de análisis musical que utiliza inteligencia artificial para predecir la
            popularidad de una canción. A través de un proceso de extracción de características y un modelo de predicción,
            Hitspell te permite conocer el potencial de éxito de tus creaciones musicales, además de entregar un detallado análisis
            de las características de audio de tu canción y compararlas con el género musical que elijas.
          </p>

          <p className="text-base md:text-lg">
            El proyecto fue desarrollado como Proyecto Final para el <strong>Bootcamp de Data Science e IA de Le Wagon</strong>,
            por Guillermo Herrera, Andrea Grain, Hildebrando Nuñez, Cesar Ramos y Cristián Rodríguez.
          </p>

          <h6 className="text-4xl font-bold pt-16">
            Sobre el proyecto
          </h6>

          <p className="text-base md:text-lg">
            El proyecto se compone de tres secciones principales: la extracción de features de audio, la predicción de popularidad
            y la generación de una recomendación.
          </p>

          <ol className="list-decimal list-inside text-white text-lg mt-4 space-y-2">
            <li><strong>Extracción de características de audio</strong>: Se utilizó la librería de Essentia desarrollada por la Universitat Pompeu Fabra, Barcelona
            que permite extraer las características de audio de cualquier track dividida en dos principales grupo: las características low-level y las high-level.</li>
            Las características <strong>low-level</strong> son aquellas que se extraen directamente del audio, como el espectro de frecuencias, la tonalidad, los acordes, el ritmo, entre otras.
            Las características <strong>high-level</strong> son variables que buscan categorizar las canciones utilizando modelos de redes neuronales de TensorFlow para describir
            los sentimientos que se abordan en la canción, la energía, que tan buena para bailar es, entre otras.
            <li><strong>Predicción del potencial de convertirse en hit</strong>: con las características de audio extraídas se hace una predicción de la popularidad que podría llegar a tener
            únicamente utilizando las características de audio de la pista. Para ello se utilizó un modelo Light GBM entrenado con ~110.000 canciones
            de 20 géneros diferentes. La popularidad representa que tan popular es la canción actualmente en base al índice creado por Spotify, donde 0 representa que no es nada popular
            y 100 es la canción más popular del momento.</li>
            <li><strong> Generación de recomendaciones personalizadas</strong>: finalmente, HitSpell compara las características de audio de tu canción con el promedio de características de las
            canciones más populares dele género al que buscar apuntar. Con eso se genera una recomendación para que puedas comparar con las canciones en tendencia de ese género. </li>
          </ol>

          <h6 className="text-4xl font-bold pt-16">
            Diccionario de características de audio
          </h6>

          <div className="max-w-5xl mx-auto text-white space-y-12 py-16 px-4">
            <div>
              <h3 className="text-3xl font-bold mb-4">📂 Variables generales</h3>
              <ul className="space-y-4">
                <li>
                  <p><strong>🎼 <code>genre</code></strong> — Género definido por el artista (rock, pop, electrónica...).</p>
                </li>
                <li>
                  <p><strong>⏱️ <code>duration_ms</code></strong> — Duración del audio en milisegundos.</p>
                </li>
              </ul>
            </div>

            <div>
              <h3 className="text-3xl font-bold mb-4">🎶 Características <code>high-level</code></h3>
              <ul className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <li><p><strong>🕺 <code>high_danceability</code></strong> — Representa qué tan bailable es la canción, en base a los modelos entrenados de TensorFlow.</p></li>
                <li><p><strong>👩‍🎤 <code>high_gender</code></strong> — Timbre de voz percibido (femenino o masculino).</p></li>
                <li><p><strong>🎻 <code>high_mood_acoustic</code></strong> — Representa si la canción tiene un timbre/carácter más acústico/orgánico o digital.</p></li>
                <li><p><strong>💥 <code>high_mood_aggressive</code></strong> — Representa el estado de ánimo de agresividad como expresión en la pista.</p></li>
                <li><p><strong>🎛️ <code>high_mood_electronic</code></strong> — Representa la presencia de producción electrónica.</p></li>
                <li><p><strong>😊 <code>high_mood_happy</code></strong> — Representa el estado de ánimo de felicidad o positividad de la pista.</p></li>
                <li><p><strong>🎉 <code>high_mood_party</code></strong> — Representa el estado de ánimo de fiesta/celebración de la pista.</p></li>
                <li><p><strong>😌 <code>high_mood_relaxed</code></strong> — Representa el estado de ánimo de calma o relajación de la pista.</p></li>
                <li><p><strong>😢 <code>high_mood_sad</code></strong> — Representa el estado de ánimo de tristeza o melancolía de la pista.</p></li>
                <li><p><strong>🎯 <code>high_moods_mirex</code></strong> — Clúster emocional (MIR) que captura otras emociones.</p></li>
                <li><p><strong>🔆 <code>high_timbre</code></strong> — Representa el color del sonido (brillante, oscuro...).</p></li>
                <li><p><strong>🎼 <code>high_tonal_atonal</code></strong> — Representa si la pista tiene tonalidad clara o atonalidad.</p></li>
                <li><p><strong>🎙️ <code>high_voice_instrumental</code></strong> — Representa si es una pista mayoritariamente vocal, instrumental o mixto.</p></li>
              </ul>
            </div>

            <div>
              <h3 className="text-3xl font-bold mb-4">🎛️ Características <code>low-level</code></h3>
              <ul className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <li><p><strong>🔊 <code>low_average_loudness</code></strong> — Sonoridad promedio.</p></li>
                <li><p><strong>📈 <code>low_dynamic_complexity</code></strong> — Variación de dinámicas.</p></li>
                <li><p><strong>🎚️ <code>low_mfcc_mean_0–12</code></strong> — Textura/timbre frecuencial.</p></li>
                <li><p><strong>🎧 <code>audio_sample_rate</code></strong> — Frecuencia de muestreo (Hz).</p></li>
                <li><p><strong>🔒 <code>audio_codec</code>, <code>audio_bit_rate</code></strong> — Compresión/calidad.</p></li>
                <li><p><strong>🎛️ <code>audio_equal_loudness</code></strong> — Ajustes perceptivos de volumen.</p></li>
                <li><p><strong>🧪 <code>audio_md5_encoded</code></strong> — Identificador hash único.</p></li>
                <li><p><strong>🎛️ <code>audio_downmix</code></strong> — Conversión a mono o mezcla de canales.</p></li>
                <li><p><strong>🎵 <code>low_key_key</code>, <code>low_key_scale</code></strong> — Tonalidad y modo.</p></li>
                <li><p><strong>🎹 <code>low_chords_key</code>, <code>low_chords_changes_rate</code></strong> — Acordes y cambios.</p></li>
                <li><p><strong>🎶 <code>low_tuning_frequency</code></strong> — Frecuencia base (ej. 440Hz).</p></li>
                <li><p><strong>💃 <code>low_danceability</code></strong> — Índice técnico de bailable.</p></li>
                <li><p><strong>⚡ <code>low_onset_rate</code></strong> — Ritmo de aparición de eventos.</p></li>
                <li><p><strong>🕐 <code>low_bpm</code>, <code>low_beats_count</code></strong> — Velocidad del pulso musical.</p></li>
              </ul>
            </div>
          </div>


        </div>
      </main>
    </>
  );
}
