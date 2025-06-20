import React from "react";
import './index.css';
import Logo from './components/Logo';
import Sidebar from './components/Sidebar';

const App = () => {
  return (
    <div>
      <header>
        <nav className="nav">
          <Logo />
        </nav>
      </header>
      <div className="flex">
        <Sidebar />
        <main className="flex-1 p-6">
          <h1>Welcome to OnyxXR!</h1>
        </main>
      </div>
    </div>
  );
};

export default App;