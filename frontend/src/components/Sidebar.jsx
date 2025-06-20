import React from 'react';

const Sidebar = () => {
  return (
    <aside className="h-screen w-48 bg-gray-100 border-r flex flex-col py-4">
      <nav className="flex flex-col gap-2">
        <a href="#" className="px-4 py-2 hover:bg-gray-200 rounded">Home</a>
        <a href="#" className="px-4 py-2 hover:bg-gray-200 rounded">Profile</a>
        <a href="#" className="px-4 py-2 hover:bg-gray-200 rounded">Settings</a>
        <a href="#" className="px-4 py-2 hover:bg-gray-200 rounded">Logout</a>
      </nav>
    </aside>
  );
};

export default Sidebar; 