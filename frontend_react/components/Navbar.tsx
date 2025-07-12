// app/components/Navbar.tsx
"use client";

import Link from "next/link";
import Image from "next/image";
import { useState } from "react";
import { usePathname } from "next/navigation";
import { Menu, X } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

const navItems = [
  { label: "Home", href: "/" },
  { label: "About", href: "/about" },
  { label: "Hitspell", href: "/hitspell" }
];

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const pathname = usePathname();

  const isActive = (href: string) => pathname === href;

  return (
    <motion.nav
      className="fixed top-0 left-0 w-full z-50 bg-black text-white px-6 py-4 shadow-2xl backdrop-blur-xl"
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
    >
      <div className="flex justify-between items-center max-w-7xl mx-auto">
        <Link href="/">
          <Image
            src="/HITSPELL.svg"
            alt="Logo"
            width={160}
            height={40}
            priority
            className="transition-all hover:scale-105"
          />
        </Link>

        <div className="md:hidden">
          <button
            onClick={() => setIsOpen(!isOpen)}
            aria-label="Toggle menu"
            className="transition-transform duration-300"
          >
            {isOpen ? <X size={28} /> : <Menu size={28} />}
          </button>
        </div>

        <ul className="hidden md:flex gap-6 text-lg font-semibold">
          {navItems.map(({ label, href }) => (
            <li key={href}>
              <Link href={href}>
                <motion.span
                  className={`relative pb-1 inline-block transition-all duration-300 ${
                    isActive(href)
                      ? "text-pink-500 after:scale-x-100"
                      : "text-white hover:text-pink-400 after:scale-x-0"
                  } after:absolute after:left-0 after:-bottom-1 after:h-[2px] after:w-full after:bg-pink-500 after:transition-transform after:duration-300 after:origin-left`}
                >
                  {label}
                </motion.span>
              </Link>
            </li>
          ))}
        </ul>
      </div>

      <AnimatePresence>
        {isOpen && (
          <motion.ul
            className="md:hidden flex flex-col items-start bg-black text-white gap-4 mt-4 px-6 pb-6 rounded-b-xl"
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
          >
            {navItems.map(({ label, href }) => (
              <li key={href} className="w-full">
                <Link href={href} onClick={() => setIsOpen(false)}>
                  <motion.span
                    className={`block w-full py-2 transition-all duration-300 text-lg font-medium border-b-2 ${
                      isActive(href)
                        ? "text-pink-500 border-pink-500"
                        : "text-white border-transparent hover:text-pink-400 hover:border-pink-500"
                    }`}
                  >
                    {label}
                  </motion.span>
                </Link>
              </li>
            ))}
          </motion.ul>
        )}
      </AnimatePresence>
    </motion.nav>
  );
};

export default Navbar;
