"use client";

import {
  FaWaveSquare, FaMusic, FaHeartbeat, FaClock, FaCompactDisc, FaVolumeUp,
} from "react-icons/fa";
import {
  GiSoundWaves, GiMusicalNotes, GiSpeaker,
} from "react-icons/gi";
import {
  MdGraphicEq, MdSpeed,
} from "react-icons/md";
import {
  TbDeviceAnalytics, TbMoodHappy, TbMoodSad, TbMoodNervous, TbChevronDown, TbChevronUp,
} from "react-icons/tb";
import type { ReactNode } from "react";
import { useState } from "react";
import * as Tooltip from "@radix-ui/react-tooltip";

type Props = {
  features: Record<string, any>;
};

const iconMap: Record<string, () => ReactNode> = {
  genre: () => <FaMusic />,
  duration_ms: () => <FaClock />,
  high_danceability_value: () => <FaHeartbeat />,
  high_gender_value: () => <GiSpeaker />,
  high_mood_acoustic_value: () => <GiSoundWaves />,
  high_mood_aggressive_value: () => <TbMoodNervous />,
  high_mood_electronic_value: () => <MdGraphicEq />,
  high_mood_happy_value: () => <TbMoodHappy />,
  high_mood_party_value: () => <FaWaveSquare />,
  high_mood_relaxed_value: () => <FaVolumeUp />,
  high_mood_sad_value: () => <TbMoodSad />,
  high_moods_mirex_value: () => <GiMusicalNotes />,
  high_timbre_value: () => <FaCompactDisc />,
  high_tonal_atonal_value: () => <MdSpeed />,
  high_voice_instrumental_value: () => <GiSpeaker />,
  low_average_loudness: () => <FaVolumeUp />,
  low_dynamic_complexity: () => <TbDeviceAnalytics />,
  low_bpm: () => <FaHeartbeat />,
  audio_sample_rate: () => <MdSpeed />,
  audio_codec: () => <FaCompactDisc />,
  audio_bit_rate: () => <TbDeviceAnalytics />,
  audio_downmix: () => <GiSpeaker />,
  audio_lossless: () => <FaCompactDisc />,
  low_key_key: () => <FaMusic />,
  low_key_scale: () => <GiSoundWaves />,
  low_chords_key: () => <GiMusicalNotes />,
  low_tuning_frequency: () => <MdSpeed />,
  low_onset_rate: () => <GiSoundWaves />,
};

const featureDescriptions: Record<string, string> = {
  genre: "Género musical asignado por el usuario para contextualizar el análisis.",
  duration_ms: "Duración total de la canción en milisegundos.",

  high_danceability_value: "Clasificación categórica sobre cuán bailable es la canción según modelos de aprendizaje automático.",
  high_danceability_probability: "Probabilidad de que la canción pertenezca a la categoría de bailabilidad detectada.",

  high_gender_value: "Clasificación predominante del género vocal percibido en la canción (masculino, femenino o neutro).",
  high_gender_probability: "Confianza del modelo en la clasificación de género vocal.",

  high_mood_acoustic_value: "Clasificación binaria sobre si la canción tiene características acústicas marcadas.",
  high_mood_acoustic_probability: "Probabilidad asociada a la clasificación de acústica.",

  high_mood_aggressive_value: "Indica si la canción tiene un carácter agresivo (e.g. ritmo fuerte, percusión intensa).",
  high_mood_aggressive_probability: "Probabilidad de que la canción sea percibida como agresiva.",

  high_mood_electronic_value: "Determina si la canción contiene elementos electrónicos predominantes.",
  high_mood_electronic_probability: "Probabilidad de que la canción pertenezca a la categoría electrónica.",

  high_mood_happy_value: "Clasificación sobre si la canción transmite emociones alegres o positivas.",
  high_mood_happy_probability: "Confianza en la clasificación emocional alegre.",

  high_mood_party_value: "Indica si la canción es adecuada para contextos festivos según sus características.",
  high_mood_party_probability: "Probabilidad asociada a la clasificación 'party'.",

  high_mood_relaxed_value: "Clasifica si la canción transmite una atmósfera relajada o calmada.",
  high_mood_relaxed_probability: "Confianza en la percepción de relajación.",

  high_mood_sad_value: "Clasificación emocional de tristeza detectada en la canción.",
  high_mood_sad_probability: "Probabilidad asociada a la categoría de tristeza.",

  high_moods_mirex_value: "Cluster emocional asignado según la taxonomía MIRex (ej. Cluster1 a Cluster5).",
  high_moods_mirex_probability: "Probabilidad de pertenencia al cluster emocional detectado.",

  high_timbre_value: "Clasificación de timbre predominante: brillante, oscuro, o intermedio.",
  high_timbre_probability: "Confianza en la clasificación del timbre detectado.",

  high_tonal_atonal_value: "Determina si la canción tiene una estructura tonal clara o es atonal.",
  high_tonal_atonal_probability: "Probabilidad de que el análisis tonal coincida con la categoría detectada.",

  high_voice_instrumental_value: "Indica si la canción tiene voz humana predominante o es puramente instrumental.",
  high_voice_instrumental_probability: "Confianza del modelo en esta clasificación.",

  low_average_loudness: "Volumen promedio del archivo de audio en LUFS (Loudness Units Full Scale).",
  low_dynamic_complexity: "Medida de variabilidad en la dinámica (volumen) de la canción.",

  low_mfcc_mean_0: "Coeficiente MFCC 0 (energía del espectro), promedio en el tiempo.",
  low_mfcc_mean_1: "Coeficiente MFCC 1, promedio en el tiempo.",
  low_mfcc_mean_2: "Coeficiente MFCC 2, relacionado con la envolvente espectral.",
  low_mfcc_mean_3: "Coeficiente MFCC 3, información de forma espectral.",
  low_mfcc_mean_4: "Coeficiente MFCC 4, detalles finos de timbre.",
  low_mfcc_mean_5: "Coeficiente MFCC 5.",
  low_mfcc_mean_6: "Coeficiente MFCC 6.",
  low_mfcc_mean_7: "Coeficiente MFCC 7.",
  low_mfcc_mean_8: "Coeficiente MFCC 8.",
  low_mfcc_mean_9: "Coeficiente MFCC 9.",
  low_mfcc_mean_10: "Coeficiente MFCC 10.",
  low_mfcc_mean_11: "Coeficiente MFCC 11.",
  low_mfcc_mean_12: "Coeficiente MFCC 12.",

  low_bpm: "Velocidad de la canción en beats por minuto (tempo estimado).",
  low_beats_count: "Cantidad total de pulsos o beats detectados en la canción.",

  low_key_key: "Tónica musical (nota base) detectada en la canción (ej: C, D#, F).",
  low_key_scale: "Tipo de escala detectada (mayor, menor u otra).",
  low_key_strength: "Confianza en la detección de la tonalidad principal.",

  low_chords_key: "Tónica predominante en la progresión de acordes detectada.",
  low_chords_scale: "Tipo de escala usada en los acordes (mayor o menor).",
  low_chords_changes_rate: "Frecuencia de cambio de acordes en la canción (transiciones por segundo).",

  low_tuning_frequency: "Frecuencia base de afinación en Hz (ej: 440 Hz para estándar).",
  low_danceability: "Medida continua de cuán bailable es la canción basada en ritmo y repetición.",
  low_onset_rate: "Frecuencia de aparición de nuevos sonidos o eventos sonoros por segundo.",

  audio_sample_rate: "Frecuencia de muestreo del archivo (Hz), indica la calidad de grabación.",
  audio_analysis_sample_rate: "Frecuencia de muestreo usada internamente para el análisis.",
  audio_codec: "Formato de codificación de audio (ej. pcm_s24le, mp3, etc.).",
  audio_bit_rate: "Tasa de bits del archivo, representa su calidad (bits por segundo).",
  audio_equal_loudness: "Ajuste para igualar la percepción de volumen entre sonidos.",
  audio_length: "Duración total del audio en segundos.",
  audio_md5_encoded: "Hash MD5 del contenido de audio, usado para identificación única.",
  audio_replay_gain: "Valor utilizado para normalizar el volumen entre distintas pistas.",
  audio_downmix: "Tipo de mezcla (mono, estéreo o combinado).",
  audio_lossless: "Indica si el archivo fue comprimido sin pérdida de calidad (true/false)."
};


function FeatureItem({ name, value }: { name: string; value: any }) {
  const label = name
    .replace(/_/g, " ")
    .replace(/^(high|low) /, "")
    .replace(/\b\w/g, (l) => l.toUpperCase());

  const Icon = iconMap[name]?.() ?? <TbDeviceAnalytics />;
  const description = featureDescriptions[name] ?? "Sin descripción disponible.";

  return (
    <Tooltip.Provider>
      <Tooltip.Root delayDuration={300}>
        <Tooltip.Trigger asChild>
          <div className="bg-zinc-800 p-2 rounded-xl shadow flex items-start gap-2 w-full h-full cursor-help hover:ring-1 hover:ring-indigo-400">
            <div className="text-lg text-indigo-400">{Icon}</div>
            <div>
              <div className="text-xs text-zinc-400 truncate max-w-[120px]">{label}</div>
              <div className="text-sm font-medium text-white truncate max-w-[120px]">
                {typeof value === "number" ? value.toFixed(3) : String(value)}
              </div>
            </div>
          </div>
        </Tooltip.Trigger>
        <Tooltip.Portal>
          <Tooltip.Content
            className="bg-zinc-900 text-white px-3 py-2 rounded-md text-sm max-w-xs shadow-md border border-zinc-700 z-50"
            side="top"
            sideOffset={6}
          >
            {description}
            <Tooltip.Arrow className="fill-zinc-900" />
          </Tooltip.Content>
        </Tooltip.Portal>
      </Tooltip.Root>
    </Tooltip.Provider>
  );
}

export default function AudioFeaturesDisplay({ features }: Props) {
  const [showAllHigh, setShowAllHigh] = useState(false);
  const [showAllLow, setShowAllLow] = useState(false);

  const highLevel = Object.keys(features)
    .filter((key) => key.startsWith("high_") && key.endsWith("_value"))
    .map((valueKey) => {
      const base = valueKey.replace("_value", "");
      const probKey = `${base}_probability`;
      return {
        base,
        valueKey,
        probKey,
        value: features[valueKey],
        probability: features[probKey] ?? null,
      };
  });

  const lowAndMeta = Object.entries(features).filter(([k]) => !k.startsWith("high_"));

  const visibleHigh = showAllHigh ? highLevel : highLevel.slice(0, 2);
  const visibleLow = showAllLow ? lowAndMeta : lowAndMeta.slice(0, 6);

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-10 p-4">
    {/* High-Level */}
    <div>
      <h2 className="text-xl font-bold mb-4 text-white flex items-center gap-2">
        <span className="text-blue-400 text-lg"></span> High-Level Features
      </h2>

      <div className="space-y-2">
        {visibleHigh.map(({ base, valueKey, probKey, value, probability }) => (
          <div key={base} className="grid grid-cols-2 gap-3">
            <FeatureItem name={valueKey} value={value} />
            {probability !== null && <FeatureItem name={probKey} value={probability} />}
          </div>
        ))}
      </div>

      {highLevel.length > 5 && (
        <button
          onClick={() => setShowAllHigh(!showAllHigh)}
          className="mt-4 text-indigo-400 hover:text-indigo-300 text-sm flex items-center gap-1"
        >
          {showAllHigh ? <>Ver menos <TbChevronUp /></> : <>Ver más <TbChevronDown /></>}
        </button>
      )}
    </div>


      {/* Low-Level + Metadata */}
      <div>
        <h2 className="text-xl font-bold mb-4 text-white flex items-center gap-2">
          <span className="text-green-400 text-lg"></span> Low-Level + Metadata
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-3">
          {visibleLow.map(([k, v]) => (
            <FeatureItem key={k} name={k} value={v} />
          ))}
        </div>
        {lowAndMeta.length > 5 && (
          <button
            onClick={() => setShowAllLow(!showAllLow)}
            className="mt-4 text-indigo-400 hover:text-indigo-300 text-sm flex items-center gap-1"
          >
            {showAllLow ? <>Ver menos <TbChevronUp /></> : <>Ver más <TbChevronDown /></>}
          </button>
        )}
      </div>
    </div>
  );
}
