import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { useState } from "react";

import Home from "./pages/Home";
import StackVisualizer from "./pages/visualizers/Stack";
import SearchAppBar from "./components/AppBar";

function App() {
  const [searchQuery, setSearchQuery] = useState("");

  return (
    <BrowserRouter>
      <SearchAppBar searchQuery={searchQuery} setSearchQuery={setSearchQuery} />
      <Routes>
        <Route path="/" element={<Home searchQuery={searchQuery} />} />
        <Route path="/stack" element={<StackVisualizer />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
