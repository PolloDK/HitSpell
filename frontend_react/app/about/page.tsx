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
            <li><strong>Extracción de características de audio</strong>:</li>
            <li>Predice su potencial de convertirse en hit.</li>
            <li>Entrega recomendaciones personalizadas para mejorarla.</li>
          </ol>

        </div>
      </main>
    </>
  );
}
