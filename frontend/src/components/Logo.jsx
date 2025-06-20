import React from 'react';

const Logo = ({ imageSrc = "logo.png", text = "Onyx", highlightText = "XR", className = "" }) => {
  return (
    <div className="flex items-center gap-1">
        <img src="/logo.png" alt="Logo" className="h-8 md:h-10 w-auto" />
        <div className="text-lg md:text-xl font-bold text-gray-800">Onyx<span className='text-gradient'>XR</span></div>
    </div>
  );
};

export default Logo; 