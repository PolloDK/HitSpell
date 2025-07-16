"use client";

import Image from "next/image";
import { useEffect, useRef } from "react";
import {
  Headphones,
  SlidersHorizontal,
  Music3,
  Brain,
} from "lucide-react";

const stats = [
  {
    icon: <Headphones className="w-7 h-7 text-pink-400" />,
    label: "110.000 canciones analizadas",
  },
  {
    icon: <SlidersHorizontal className="w-7 h-7 text-fuchsia-400" />,
    label: "82 características por pista",
  },
  {
    icon: <Music3 className="w-7 h-7 text-purple-400" />,
    label: "20 géneros musicales",
  },
  {
    icon: <Brain className="w-7 h-7 text-indigo-400" />,
    label: "Utilización de IA",
  },
];

const logos = [
  { src: "/logos/essentia_logo.svg", alt: "Essentia" },
  { src: "/logos/acousticbrainz.svg", alt: "AcousticBrainz" },
  { src: "/logos/spotify_logo.png", alt: "Spotify API" },
];

export default function BehindTheSpell() {
  const tickerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const ticker = tickerRef.current;
    if (!ticker) return;

    const animate = () => {
      ticker.scrollLeft += 0.5;
      if (ticker.scrollLeft >= ticker.scrollWidth / 2) {
        ticker.scrollLeft = 0;
      }
      requestAnimationFrame(animate);
    };

    animate();
  }, []);

  return (
    <section className="py-8 px-6 text-white text-center relative overflow-hidden">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-4xl font-extrabold text-zinc-100 mb-3 tracking-tight">
          Detrás del conjuro
        </h2>
        <p className="text-lg md:text-xl text-zinc-300 mb-12 max-w-3xl mx-auto">
          HitSpell combina ciencia de datos, procesamiento de audio digital e inteligencia artificial
          para analizar tu canción y predecir su potencial de éxito.
        </p>

        {/* Carrusel deslizante */}
        <div
          className="overflow-hidden whitespace-nowrap border-t border-b border-white/10 py-6 mb-16"
          ref={tickerRef}
        >
          <div className="inline-flex gap-10 px-4 animate-none">
            {[...stats, ...stats].map((item, i) => (
              <div
                key={i}
                className="bg-zinc-900/50 px-6 py-4 rounded-lg shadow-sm border border-zinc-800 min-w-[250px] inline-flex flex-col items-center justify-center"
              >
                {item.icon}
                <p className="text-base md:text-lg text-zinc-100 font-medium mt-3">
                  {item.label}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Logos institucionales */}
        <div className="flex flex-wrap justify-center items-center gap-10">
          {logos.map((logo, i) => (
            <Image
              key={i}
              src={logo.src}
              alt={logo.alt}
              width={130}
              height={130}
              className="opacity-80 hover:opacity-100 transition duration-200"
            />
          ))}
        </div>
      </div>
    </section>
  );
}
