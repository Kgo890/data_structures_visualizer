import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { useState } from "react";

import Home from "./pages/Home";
import StackVisualizer from "./pages/visualizers/Stack";
import QueueVisualizer from "./pages/visualizers/Queue";
import SinglyLinkedListVisualizer from "./pages/visualizers/SinglyLinkedList";
import DoubleLinkedListVisualizer from "./pages/visualizers/DoubleLinkedList";
import BinaryTreeVisualizer from "./pages/visualizers/BinaryTree";
import BubbleSortVisualizer from "./pages/visualizers/BubbleSort";
import SelectionSortVisualizer from "./pages/visualizers/SelectionSort";
import InsertionSortVisualizer from "./pages/visualizers/InsertionSort";
import MergeSortVisualizer from "./pages/visualizers/MergeSort";
import QuickSortVisualizer from "./pages/visualizers/QuickSort";
import SearchAppBar from "./components/AppBar";

function App() {
  const [searchQuery, setSearchQuery] = useState("");

  return (
    <BrowserRouter>
      <SearchAppBar searchQuery={searchQuery} setSearchQuery={setSearchQuery} />
      <Routes>
        <Route path="/" element={<Home searchQuery={searchQuery} />} />
        <Route path="/stack" element={<StackVisualizer />} />
        <Route path="/queue" element={<QueueVisualizer />} />
        <Route path="/singly-linked-list" element={<SinglyLinkedListVisualizer />} />
        <Route path="/double-linked-list" element={<DoubleLinkedListVisualizer />} />
        <Route path="/binary-tree" element={<BinaryTreeVisualizer />} />
        <Route path="/bubble-sort" element={<BubbleSortVisualizer />} />
        <Route path="/selection-sort" element={<SelectionSortVisualizer />} />
        <Route path="/insertion-sort" element={<InsertionSortVisualizer />} />
        <Route path="/merge-sort" element={<MergeSortVisualizer />} />
        <Route path="/quick-sort" element={<QuickSortVisualizer />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
