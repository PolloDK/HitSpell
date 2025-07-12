"use client";

import React, { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";

type Props = {
  recomendacion: string;
};

const RecomendacionReport: React.FC<Props> = ({ recomendacion }) => {
  const [displayedText, setDisplayedText] = useState("");

  useEffect(() => {
    setDisplayedText("");
    if (!recomendacion) return;

    let index = 0;
    const interval = setInterval(() => {
      setDisplayedText((prev) => prev + recomendacion.charAt(index));
      index++;
      if (index >= recomendacion.length) clearInterval(interval);
    }, 5);

    return () => clearInterval(interval);
  }, [recomendacion]);

  return (
    <div className="flex justify-center mt-10">
      <div className="bg-zinc-900 border border-zinc-700 text-white rounded-xl px-10 py-8 shadow-inner min-h-[350px] w-full max-w-[1100px]">
        <h2 className="text-lg font-semibold mb-4 text-pink-500">📝 Recomendación</h2>
        <div className="text-white text-base leading-relaxed whitespace-pre-line">
          {displayedText.split("\n").map((line, index) => (
            <React.Fragment key={index}>
              {line}
              <br />
            </React.Fragment>
          ))}
        </div>
      </div>
    </div>
  );
};

export default RecomendacionReport;
