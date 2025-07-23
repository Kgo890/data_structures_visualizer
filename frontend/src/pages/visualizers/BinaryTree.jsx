import React, { useState, useEffect } from "react";
import api from '../../components/axios';
import {
  Container,
  Typography,
  Box,
  Button,
  TextField,
} from "@mui/material";
import { TransformWrapper, TransformComponent } from "react-zoom-pan-pinch";

export default function BinaryTreeVisualizer() {
  const [input, setInput] = useState("");
  const [treeStructure, setTreeStructure] = useState(null);
  const [history, setHistory] = useState([]);
  const [reverseSteps, setReverseSteps] = useState([]);
  const [stepIndex, setStepIndex] = useState(null);


  useEffect(() => {
    fetchTreeStructure();
  }, []);

  async function fetchTreeStructure() {
    try {
      const response = await api.get("/binary-tree/tree-structure");
      setTreeStructure(response.data);
    } catch (error) {
      console.error("Error fetching tree structure:", error);
    }
  }

  async function insert() {
    try {
      await api.post("/binary-tree/insert", { value: input });
      setHistory((prev) => [...prev, `Insert: ${input}`]);
      setInput("");
      fetchTreeStructure();
    } catch (error) {
      console.error("Insert failed:", error);
    }
  }

  async function deleteNode() {
    try {
      const value = parseInt(input);
      await api.delete("/binary-tree", { params: { value } });
      setHistory((prev) => [...prev, `Delete: ${value}`]);
      setInput("");
      fetchTreeStructure();
    } catch (error) {
      console.error("Delete failed:", error);
    }
  }

  async function inOrder() {
    try {
      const response = await api.get("/binary-tree/in_order-traverse");
      const { steps } = response.data;
      animateTraversal(steps, "In-Order");
    } catch (error) {
      console.error("In-Order traversal failed:", error);
    }
  }

  async function preOrder() {
    try {
      const response = await api.get("/binary-tree/pre_order-traverse");
      const { steps } = response.data;
      animateTraversal(steps, "Pre-Order");
    } catch (error) {
      console.error("Pre-Order traversal failed:", error);
    }
  }

  async function postOrder() {
    try {
      const response = await api.get("/binary-tree/post_order-traverse");
      const { steps } = response.data;
      animateTraversal(steps, "Post-Order");
    } catch (error) {
      console.error("Post-Order traversal failed:", error);
    }
  }

  async function checkBalance() {
    try {
      const res = await api.get("/binary-tree/is-balanced");
      setHistory((prev) => [...prev, `Balanced: ${res.data.balanced}`]);
    } catch (error) {
      console.error("Check balance failed:", error);
    }
  }

  async function getHeight() {
    try {
      const res = await api.get("/binary-tree/height");
      setHistory((prev) => [...prev, `Height: ${res.data.height}`]);
    } catch (error) {
      console.error("Get height failed:", error);
    }
  }

  async function getLeafCount() {
    try {
      const res = await api.get("/binary-tree/leaf-count");
      setHistory((prev) => [...prev, `Leaf Nodes: ${res.data.leaf_count}`]);
    } catch (error) {
      console.error("Get leaf count failed:", error);
    }
  }

  async function reset() {
    try {
      await api.get("/binary-tree/clear");
      setInput("");
      setStepIndex(null);
      setReverseSteps([]);
      setTreeStructure(null);
      setHistory((prev) => [...prev, "Reset: Binary Tree cleared"]);
    } catch (error) {
      console.error("Reset failed:", error);
    }
  }

  function animateTraversal(steps, type) {
    setReverseSteps(steps || []);
    setStepIndex(0);
    setHistory((prev) => [...prev, `${type} Traversal:`]);

    let index = 0;
    const interval = setInterval(() => {
      if (index >= steps.length) {
        clearInterval(interval);
        setTimeout(() => setStepIndex(null), 500);
        return;
      }

      const currentNode = steps[index];
      setHistory((prev) => [...prev, `Visit: ${currentNode}`]);
      setStepIndex(index);
      index++;
    }, 1000);
  }

  function renderTree(node, x = 600, y = 50, depth = 0, spacing = 180, levelGap = 80) {
    if (!node) return null;

    const children = [];
    const nodeGap = spacing / (depth + 1);
    const highlight = stepIndex !== null && reverseSteps[stepIndex] === node.value;

    if (node.left) {
      children.push(
        <>
          <line x1={x} y1={y} x2={x - nodeGap} y2={y + levelGap} stroke="#ccc" />
          {renderTree(node.left, x - nodeGap, y + levelGap, depth + 1)}
        </>
      );
    }

    if (node.right) {
      children.push(
        <>
          <line x1={x} y1={y} x2={x + nodeGap} y2={y + levelGap} stroke="#ccc" />
          {renderTree(node.right, x + nodeGap, y + levelGap, depth + 1)}
        </>
      );
    }

    return (
      <>
        {children}
        <circle
          cx={x}
          cy={y}
          r={highlight ? 24 : 20}
          fill={highlight ? "#00bcd4" : "#1976d2"}
          stroke={highlight ? "#0ff" : "none"}
          strokeWidth={highlight ? 3 : 0}
        />
        <text
          x={x}
          y={y + 5}
          textAnchor="middle"
          fill="white"
          fontSize="16"
          fontFamily="Arial"
        >
          {node.value}
        </text>
      </>
    );
  }

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Typography variant="h4" align="center" gutterBottom>
        Binary Tree Visualizer
      </Typography>

      {/* Controls */}
      <Box display="flex" flexDirection="column" alignItems="flex-start" gap={2} mb={4}>
        <Box display="flex" gap={2}>
          <TextField
            label="Enter value"
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <Button variant="contained" onClick={insert}>Insert</Button>
          <Button variant="contained" color="secondary" onClick={deleteNode}>Delete</Button>
          <Button variant="contained" color="error" onClick={reset}>Clear</Button>
        </Box>
        <Box display="flex" gap={2}>
          <Button variant="outlined" onClick={inOrder}>In-Order</Button>
          <Button variant="outlined" onClick={preOrder}>Pre-Order</Button>
          <Button variant="outlined" onClick={postOrder}>Post-Order</Button>
        </Box>
        <Box display="flex" gap={2}>
          <Button variant="outlined" onClick={checkBalance}>Is Balanced?</Button>
          <Button variant="outlined" onClick={getHeight}>Get Height</Button>
          <Button variant="outlined" onClick={getLeafCount}>Leaf Nodes</Button>
        </Box>
      </Box>

      {/* Visual Tree with Zoom/Pan */}
      <Box
        sx={{
          position: "relative",
          width: "100%",
          height: "500px",
          border: "1px solid #ccc",
          mb: 4,
        }}
      >
        <TransformWrapper>
          <TransformComponent>
            <svg width="1200" height="800">{renderTree(treeStructure)}</svg>
          </TransformComponent>
        </TransformWrapper>
      </Box>

      {/* Traversal History */}
      <Box p={2} bgcolor="#1e1e1e" borderRadius={2} sx={{ border: "1px solid #555" }}>
        <Typography variant="h6" color="white" gutterBottom>
          Traversal History
        </Typography>
        <Box display="flex" flexWrap="wrap" gap={1}>
          {history.map((entry, index) => (
            <Box
              key={index}
              px={2}
              py={1}
              bgcolor={
                entry.startsWith("Visit")
                  ? "#424242"
                  : entry.includes("Traversal")
                  ? "#1976d2"
                  : "#2e7d32"
              }
              color="white"
              borderRadius={1}
              fontSize="0.85rem"
            >
              {entry}
            </Box>
          ))}
        </Box>
      </Box>
    </Container>
  );
}
