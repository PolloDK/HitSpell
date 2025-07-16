"use client";

import { motion } from "framer-motion";
import { FaUpload, FaBrain, FaMagic, FaClipboardCheck } from "react-icons/fa";

const steps = [
  {
    icon: <FaUpload className="text-pink-400 text-4xl" />,
    title: "Sube tu canción",
    description: "Carga un archivo de audio y deja que la magia comience.",
  },
  {
    icon: <FaBrain className="text-blue-400 text-4xl" />,
    title: "Analizamos con IA",
    description: "Extraemos y procesamos decenas de características acústicas.",
  },
  {
    icon: <FaMagic className="text-purple-400 text-4xl" />,
    title: "Estimamos su potencial",
    description: "Nuestro modelo predice la probabilidad de que tu canción sea un hit.",
  },
  {
    icon: <FaClipboardCheck className="text-green-400 text-4xl" />,
    title: "Te damos recomendaciones",
    description: "Recibe consejos personalizados para mejorar tu canción.",
  },
];

export default function HowItWorksSection() {
  return (
    <section className="py-12 px-4 text-white">
      <h2 className="text-center text-white text-3xl md:text-4xl font-bold mb-2">
        ¿Cómo funciona HitSpell?
      </h2>
      <p className="text-center text-zinc-400 text-base md:text-lg mb-8">
        Un viaje en 4 pasos para desatar el poder oculto de tu canción
      </p>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 max-w-7xl mx-auto">
        {steps.map((step, index) => (
          <motion.div
            key={index}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            whileHover={{ scale: 1.05 }}
            transition={{
              type: "spring",
              stiffness: 300,
              damping: 20,
              duration: 0.05,
              delay: index * 0.1,
              ease: "easeOut",
            }}
            className="bg-zinc-900/90 rounded-2xl p-6 border border-white/10 shadow-md transition-all"
          >
            <div className="mb-4 flex justify-center">{step.icon}</div>
            <h3 className="text-xl font-semibold text-center mb-2">{step.title}</h3>
            <p className="text-sm text-center text-zinc-300">{step.description}</p>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
