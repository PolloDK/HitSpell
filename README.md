# 🎧 HitSpell

**HitSpell** es un proyecto de análisis musical que utiliza inteligencia artificial para predecir la popularidad de una canción. A través de un proceso de extracción de características y un modelo de predicción, Hitspell te permite conocer el potencial de éxito de tus creaciones musicales, además de entregar un detallado análisis de las características de audio de tu canción y compararlas con el género musical al que apuntas.

El proyecto fue desarrollado como Proyecto Final para el **Bootcamp de Data Science e IA de Le Wagon**.

---

## 🚀 Demo

[Ver demo en producción]()

---

## 🧠 ¿Qué hace?

- 📂 Permite subir archivos `.mp3` o `.wav`
- 🎼 Extrae características acústicas con [Essentia](https://essentia.upf.edu/)
- 🎯 Predice la popularidad de la canción (0 a 100)
- 💡 Genera recomendaciones específicas para mejorar el impacto musical
- 🎛️ Muestra visualmente los atributos del track.

---

## 🛠️ Tecnologías utilizadas

Hitalyzer combina tecnologías de frontend, backend y análisis de audio para ofrecer un sistema inteligente de evaluación musical.

### 🎧 Audio Analysis

- **[Essentia](https://essentia.upf.edu/)**: librería de código abierto para análisis de audio desarrollada por el Music Technology Group de la Universidad Pompeu Fabra. Utilizada para extraer:
  - Características de bajo nivel como: BPM, tonalidad, acordes, frecuencia de afinación, etc.
  - Características de alto nivel como: mood, danceability, voice/instrumental, etc. Utilizando los modelos preentrenados con TensorFlow.

- **[AcousticBrainz](https://acousticbrainz.org/)**: base de datos pública utilizada como referencia para entrenar y validar características musicales. Contiene millones de características acústicas de canciones generados con Essentia.

- **[Spotify Web API](https://developer.spotify.com/documentation/web-api/)**: utilizada para obtener la popularidad global de la canción.

### 🧠 Inteligencia Artificial

- **Scikit-learn**: modelos supervisados entrenados para predecir la popularidad estimada de la canción, utilizando solo features acústicas y estructurales, sin depender de métricas sociales.

- **Python + FastAPI**: API ligera y rápida que procesa el audio, genera features, hace la predicción y devuelve recomendaciones personalizadas.

- **API Open AI**: para generar la recomendación mediante un prompt comparativo con las características de audio de la canción y el promedio de tendencias del género.

### 💻 Frontend

- **React (Next.js)**: para la interfaz.
- **Tailwind CSS**: para estilos y diseños.
- **Framer Motion**: para animaciones con el foco de mejorar la experiencia de usuario.

### ☁️ Infraestructura

- **Google Cloud Run**: despliegue del backend (FastAPI).
- **Google Cloud Storage**: almacenamiento temporal de archivos de audio subidos.

---

## Autores:

> Guillermo Herrera.
> Andrea Grain.
> Hildebrando Nuñez.
> Cesar Ramos.
> Cristián Rodríguez.
