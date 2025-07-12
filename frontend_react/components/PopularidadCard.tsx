"use client";

import React from "react";

type Props = {
  popularity: number;
};

const PopularidadCard: React.FC<Props> = ({ popularity }) => {
  return (
    <div className="bg-gradient-to-r from-purple-600 to-pink-500 shadow-lg rounded-xl p-6 mt-6 transition-transform transform hover:scale-105 w-full text-center text-white mb-6">
      <h2 className="text-2xl font-bold mb-2">🌟 Popularidad Estimada</h2>
      <p className="text-5xl font-extrabold tracking-wide">
        {popularity.toFixed(2)} / 100
      </p>
    </div>
  );
};

export default PopularidadCard;
