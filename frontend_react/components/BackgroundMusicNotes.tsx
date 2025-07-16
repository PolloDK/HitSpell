"use client";

import { useEffect, useState } from "react";

const NUM_NOTES = 300;
const musicSymbols = ["♪", "♩", "♫", "♬", "𝅘𝅥𝅮", "𝅘𝅥"];

const getRandom = (min: number, max: number) =>
  Math.random() * (max - min) + min;

export default function BackgroundMusicNotes() {
  const [notes, setNotes] = useState<
    {
      id: number;
      top: number;
      left: number;
      delay: number;
      duration: number;
      size: number;
      symbol: string;
    }[]
  >([]);

  useEffect(() => {
    const generatedNotes = Array.from({ length: NUM_NOTES }, (_, i) => ({
      id: i,
      top: getRandom(-100, 0), // empiezan fuera de pantalla
      left: getRandom(0, 100),
      delay: getRandom(0, 5),
      duration: getRandom(8, 20),
      size: getRandom(14, 26),
      symbol: musicSymbols[Math.floor(Math.random() * musicSymbols.length)],
    }));
    setNotes(generatedNotes);
  }, []);

  return (
    <div className="absolute inset-0 overflow-hidden z-0 pointer-events-none">
      <style jsx>{`
        @keyframes fall {
          0% {
            transform: translateY(-100vh);
          }
          100% {
            transform: translateY(120vh);
          }
        }
        .falling {
          animation-name: fall;
          animation-timing-function: linear;
          animation-iteration-count: infinite;
        }
      `}</style>

      {notes.map((note) => (
        <div
          key={note.id}
          className="absolute text-white opacity-18 falling"
          style={{
            top: `${note.top}%`,
            left: `${note.left}%`,
            animationDelay: `${note.delay}s`,
            animationDuration: `${note.duration}s`,
            fontSize: `${note.size}px`,
          }}
        >
          {note.symbol}
        </div>
      ))}
    </div>
  );
}
