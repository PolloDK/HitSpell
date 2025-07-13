// app/page.tsx
"use client";

import Image from "next/image";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";
import Navbar from "../components/Navbar";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col ">
      <Navbar />

      <main className="flex-grow px-4 pt-24 pb-100">
        <div className="flex flex-col items-center justify-center max-w-4xl mx-auto text-center space-y-6 mt-10">
          <Image
            src="/HITSPELL.svg"
            alt="HitSpell Logo"
            width={320}
            height={100}
            className="mb-2"
          />

          <hr className="w-full border-t border-border" />

          <h2 className="text-2xl md:text-3xl font-bold text-white">
            HitSpell es un hechizo tecnológico diseñado
          </h2>

          <hr className="w-full pt-4 border-t border-border" />

          <p className="text-base md:text-lg text-white">
            Sube tu canción y deja que la magia ocurra: nuestra herramienta analiza sus elementos sonoros –tempo,
            ritmo, energía, texturas y emociones– y los compara con miles de éxitos musicales del mismo género.
            A través de un modelo entrenado con cientos de miles de canciones, HitSpell predice la probabilidad
            de que tu canción se convierta en hit a partir de sus características de audio.
          </p>
          <p className="text-base md:text-lg text-white">
            Pero no sólo se queda ahí. Como un oráculo musical, también te entrega recomendaciones concretas
            y personalizadas para afinar el hechizo: ajustes en tempo, mezcla, estructura o atmósfera emocional.
          </p>

          <motion.div
            whileHover={{
              scale: 1.05,
              boxShadow: "0 0 20px rgba(236, 72, 153, 0.6)",
            }}
            whileTap={{ scale: 0.95 }}
            transition={{ type: "spring", stiffness: 300 }}
            className="mt-6"
          >
            <Link href="/hitspell">
              <Button className="h-12 cursor-pointer text-lg px-6 py-4 bg-gradient-to-r from-pink-500 to-fuchsia-700 text-white shadow-md hover:shadow-pink-500/50 rounded-xl transition-all duration-300">
                ✨ Conjura tu próximo hit
              </Button>
            </Link>
          </motion.div>
        </div>
      </main>

      <Footer />
    </div>
  );
}
