"use client";

import Link from "next/link";
import { FaGithub } from "react-icons/fa";

const Footer = () => {
  return (
    <footer className="bg-zinc-900 text-zinc-400 pt-10 pb-4 border-t border-zinc-800 w-full">
      <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center md:items-start gap-6">
        {/* Logo + Navegación horizontal */}
        <div className="flex items-start gap-10">
          {/* Logo */}
          <img src="/HITSPELL.svg" alt="Hitspell Logo" className="h-8 w-auto" />

          {/* Navegación vertical al lado del logo */}
          <nav className="flex flex-col gap-2 text-sm">
            <Link href="/" className="hover:text-pink-400 transition-colors">Inicio</Link>
            <Link href="/about" className="hover:text-pink-400 transition-colors">Sobre</Link>
            <Link href="/upload" className="hover:text-pink-400 transition-colors">Subir Canción</Link>
          </nav>
        </div>

        {/* GitHub */}
        <a
          href="https://github.com/PolloDK/Hitanalyzer"
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center gap-2 text-sm hover:text-pink-400 transition-colors mt-2 md:mt-0"
        >
          <FaGithub size={20} />
          Repositorio
        </a>
      </div>

      {/* Derechos reservados */}
      <div className="mt-8 text-center text-xs text-zinc-500">
        © {new Date().getFullYear()} HitSpell. Todos los derechos reservados.
      </div>
    </footer>
  );
};

export default Footer;
