// app/page.tsx
"use client";

import Image from "next/image";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";
import Navbar from "../components/Navbar";
import Footer from "@/components/Footer";
import BackgroundMusicNotes from "@/components/BackgroundMusicNotes";
import HowItWorksSection from "@/components/HowItWorksSection";
import BehindTheSpell from "@/components/BehindTheSpell";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col relative overflow-hidden">
      <Navbar />

      <main className="flex-grow px-4 pt-24 pb-10 relative">
        {/* Background Notes - behind content */}
        <div className="absolute inset-0 -z-10 pointer-events-none">
          <BackgroundMusicNotes />
        </div>

        <div className="flex flex-col items-center justify-center max-w-4xl mx-auto text-center space-y-6 mt-10">
          <Image
            src="/HITSPELL.svg"
            alt="HitSpell Logo"
            width={320}
            height={100}
            className="mb-2"
          />

        <div className="text-white text-lg md:text-xl max-w-2xl">
        </div>

          <hr className="w-full border-t border-border" />

          <h2 className="text-2xl md:text-3xl font-bold text-white">
            Un conjuro digital que revela el potencial de tu canción
          </h2>

          <hr className="w-full pt-4 border-t border-border" />

          <p className="text-base md:text-lg text-white">
            Sube tu canción y deja que la magia ocurra: nuestra herramienta analiza sus elementos sonoros –tempo,
            ritmo, energía, texturas y emociones– y los compara con miles de éxitos musicales del mismo género.
          </p>
          <p className="text-base md:text-lg text-white">
            Como un oráculo musical, también te entrega recomendaciones concretas para afinar el hechizo:
            ajustes en tempo, mezcla, estructura o atmósfera emocional.
          </p>

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, ease: "easeOut" }}
            className="mt-10 w-full max-w-4xl rounded-2xl overflow-hidden shadow-2xl border border-white/10 backdrop-blur bg-white/5"
          >
            <video
              className="w-full h-auto"
              autoPlay
              muted
              loop
              playsInline
            >
              <source src="/demo_hitspell.mp4" type="video/mp4" />
              Tu navegador no soporta el video.
            </video>
          </motion.div>



          <HowItWorksSection />

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
              <Button className="h-14 cursor-pointer text-lg px-12 py-8 bg-gradient-to-r from-pink-500 to-fuchsia-700 text-white shadow-md hover:shadow-pink-500/50 rounded-xl transition-all duration-300">
                ✨ Conjura tu próximo hit
              </Button>
            </Link>
          </motion.div>

          <BehindTheSpell />
        </div>
      </main>

      <Footer />
    </div>
  );
}
