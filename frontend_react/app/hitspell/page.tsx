"use client";

import { useState } from "react";
import { useDropzone } from "react-dropzone";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Button } from "@/components/ui/button";
import { motion, AnimatePresence } from "framer-motion";
import Navbar from "../../components/Navbar";
import PopularidadCard from "../../components/PopularidadCard";
import RecomendacionReport from "../../components/RecomendacionReport";

const genres = ["rock", "pop", "electronic", "classical", "hip hop", "jazz", "house", "country", "blues", "punk", "r&b", "techno", "reggae", "funk", "latin", "disco"];

export default function Hitspell() {
  const [genre, setGenre] = useState("");
  const [fileName, setFileName] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [alert, setAlert] = useState("");
  const [analyzing, setAnalyzing] = useState(false);
  const [stageText, setStageText] = useState("");
  const [features, setFeatures] = useState<any>(null);
  const [popularityScore, setPopularityScore] = useState<number | null>(null);
  const [recomendacionTexto, setRecomendacionTexto] = useState<string | null>(null);

  const uploadToAPI = async (file: File): Promise<string | null> => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("/api/upload", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Falló el upload");

      const { fileName } = await res.json();
      return fileName;
    } catch (err) {
      console.error("Error subiendo archivo:", err);
      return null;
    }
  };

  const simulateUpload = () => {
    setUploading(true);
    setProgress(0);
    const interval = setInterval(() => {
      setProgress((prev) => {
        if (prev >= 100) {
          clearInterval(interval);
          setUploading(false);
          return 100;
        }
        return prev + 25;
      });
    }, 80);
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: {
      "audio/wav": [],
      "audio/mpeg": [], // MIME type para .mp3
    },
    multiple: false,
    maxSize: 200 * 1024 * 1024,
    onDrop: (acceptedFiles) => {
      setAlert("");
      if (acceptedFiles.length > 0) {
        const f = acceptedFiles[0];
        const ext = f.name.split(".").pop()?.toLowerCase();
        if (ext === "wav" || ext === "mp3") {
          setFile(f);
          setFileName(f.name);
          simulateUpload();
        } else {
          setAlert("❌ El archivo debe ser .wav o .mp3");
        }
      }
    },
  });

const handleAnalyze = async () => {
  setAlert("");

  if (!genre || !file || !fileName) {
    setAlert("⚠️ Debes seleccionar un género y subir una canción válida (.wav)");
    return;
  }

  // 🔄 Limpiar resultados anteriores
  setPopularityScore(null);
  setRecomendacionTexto("");
  setFeatures(null);

  setAnalyzing(true);
  setStageText("Analizando patrones de energía...");

  const texts = [
    "Analizando tempo y ritmo...",
    "Extrayendo texturas musicales...",
    "Detectando emociones y ánimos...",
    "Analizando tonalidades, timbres y estructura tonal...",
    "Ajustando el hechizo musical...",
  ];

  let idx = 0;
  const interval = setInterval(() => {
    setStageText(texts[idx]);
    idx++;
    if (idx >= texts.length) clearInterval(interval);
  }, 20000);

  try {
    // Subir audio
    const uploadedFileName = await uploadToAPI(file);
    if (!uploadedFileName) {
      throw new Error("❌ No se pudo subir el archivo.");
    }

    // Paso 1: Extracción de features
    setStageText("🎧 Analizando características de la canción...");
    const featuresResponse = await fetch("/api/proxy-feature", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ filename: uploadedFileName }),
    });

    if (!featuresResponse.ok) {
      throw new Error("❌ Error durante la extracción de features.");
    }

    const features = await featuresResponse.json();
    const featuresWithGenre = { genre, ...features };
    setFeatures(featuresWithGenre);

    // Paso 2: Predicción de popularidad
    setStageText("🔮 Prediciendo popularidad...");
    let Popularity: number | null = null;

    try {
      const popularityRes = await fetch("/api/proxy-predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(featuresWithGenre),
      });

      if (!popularityRes.ok) throw new Error("Respuesta no válida desde la API de popularidad");

      const json = await popularityRes.json();
      Popularity = json.Popularity ?? json.popularity ?? null;

      if (typeof Popularity === "number") {
        setStageText(`✅ Popularidad estimada: ${Popularity.toFixed(2)} / 100`);
        setPopularityScore(Popularity);
      }
    } catch (popErr) {
      console.warn("⚠️ Falló la predicción de popularidad:", popErr);
      setAlert("⚠️ Falló la predicción de popularidad.");
    }

    // Paso 3: Recomendación
    setStageText("💡 Generando recomendaciones...");
    try {
      const recomendationRes = await fetch("/api/proxy-recommendation", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(featuresWithGenre),
      });

      if (!recomendationRes.ok) throw new Error();

      const { recomendacion: rec } = await recomendationRes.json();
      const recFinal = rec.replace(/del género string/g, `del género ${genre}`);
      setRecomendacionTexto(recFinal);
    } catch (recErr) {
      console.warn("⚠️ Falló la generación de la recomendación:", recErr);
      setAlert("⚠️ Falló la generación de la recomendación.");
    }

    if (Popularity !== null) {
      setStageText(`✅ Popularidad estimada: ${Popularity.toFixed(2)} / 100`);
    }
  } catch (err: any) {
    console.error("❌ Error general:", err);
    setAlert(err.message || "❌ Error de conexión durante el análisis.");
  } finally {
    clearInterval(interval);
    setAnalyzing(false);
  }
};



  return (
    <>
      <Navbar />
      <main className="min-h-screen px-4 pt-32 pb-12 max-w-4xl mx-auto text-white">
        <motion.h1
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-3xl font-bold mb-6 text-center"
        >
          Sube tu canción
        </motion.h1>

        {alert && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mb-4 px-4 py-3 rounded-lg bg-gradient-to-r from-pink-600 to-fuchsia-700 text-white shadow-lg text-sm text-center"
          >
            {alert}
          </motion.div>
        )}

        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="mb-8"
        >
          <Label className="mb-2 block text-white">Selecciona el género</Label>
          <Select onValueChange={setGenre}>
            <SelectTrigger className="w-60 bg-zinc-900 border border-zinc-700 text-white">
              <SelectValue placeholder="Elige un género..." />
            </SelectTrigger>
            <SelectContent className="bg-zinc-900 text-white">
              {genres.map((g) => (
                <SelectItem key={g} value={g}>{g.charAt(0).toUpperCase() + g.slice(1)}</SelectItem>
              ))}
            </SelectContent>
          </Select>
        </motion.div>

        <motion.div
          whileHover={{ scale: 1.02 }}
          {...(getRootProps() as any)}
          className={`border-2 border-dashed rounded-xl p-8 text-center transition-all duration-300 cursor-pointer ${
            isDragActive ? "border-pink-500 bg-zinc-800" : "border-zinc-700"
          }`}
        >
          <input {...getInputProps()} />

          <p className="text-sm text-white/70 mb-4">
            Sube tu archivo <strong>.wav</strong> o <strong>.mp3</strong>
          </p>

          <AnimatePresence>
            {!fileName && (
              <motion.p
                key="placeholder"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="text-white/80"
              >
                {isDragActive
                  ? "Suelta el archivo aquí..."
                  : "Arrastra tu canción aquí o haz clic para subir"}
              </motion.p>
            )}

            {uploading && (
              <motion.p
                key="uploading"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="text-pink-400 font-semibold"
              >
                🎵 Subiendo archivo...
              </motion.p>
            )}
          </AnimatePresence>

          {!uploading && fileName && !analyzing && (
            <motion.p
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="mt-4 text-green-400 text-center font-semibold"
            >
              ✅ Archivo cargado: {fileName}
            </motion.p>
          )}
        </motion.div>

        <AnimatePresence>
          {uploading && (
            <motion.div
              key="progressbar"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="mt-6 w-full"
            >
              <div className="w-full bg-zinc-700 h-4 rounded-full overflow-hidden">
                <motion.div
                  initial={{ width: 0 }}
                  animate={{ width: `${progress}%` }}
                  transition={{ ease: "easeOut", duration: 0.3 }}
                  className="bg-pink-500 h-full rounded-full"
                />
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {!analyzing && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6 }}
            className="mt-10 flex justify-center"
          >
            <Button
              onClick={handleAnalyze}
              className="text-lg px-8 py-5 bg-gradient-to-r from-pink-500 to-fuchsia-700 text-white shadow-xl rounded-2xl transition-all duration-500 transform hover:scale-105 hover:shadow-pink-500/50 cursor-pointer"
            >
              🔮 Analizar canción
            </Button>
          </motion.div>
        )}

        {popularityScore !== null && (
          <PopularidadCard popularity={popularityScore} />
        )}

        {recomendacionTexto && (
          <RecomendacionReport recomendacion={recomendacionTexto} />
        )}

        {analyzing && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mt-10 text-center"
          >
            <img src="/HIT.gif" alt="Analizando..." className="mx-auto w-40 h-40 mb-4" />
            <p className="text-pink-300 font-medium animate-pulse">{stageText}</p>
            <div className="w-full bg-zinc-700 h-4 rounded-full mt-6 overflow-hidden">
              <motion.div
                initial={{ width: 0 }}
                animate={{ width: `100%` }}
                transition={{ duration: 120, ease: "linear" }}
                className="bg-pink-500 h-full"
              />
            </div>
          </motion.div>
        )}
      </main>
    </>
  );
}
