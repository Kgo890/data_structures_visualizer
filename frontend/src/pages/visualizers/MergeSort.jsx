import React, { useState } from "react";
import api from '../../components/axios';
import {
  Container,
  Typography,
  Box,
  Button,
  TextField,
  Slider,
} from "@mui/material";
import { motion } from "framer-motion";

export default function MergeSortVisualizer() {
  const [input, setInput] = useState("");
  const [array, setArray] = useState([]);
  const [steps, setSteps] = useState([]);
  const [stepIndex, setStepIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [history, setHistory] = useState([]);


  function handleInputChange(e) {
    setInput(e.target.value);
  }

  async function startSort() {
    try {
      const nums = input.split(",").map((n) => parseInt(n.trim()));
      const response = await api.post("/sort", {
        algorithm: "merge",
        value: nums,
      });

      setArray(nums);
      setSteps(response.data.steps || []);
      setStepIndex(0);
      setHistory([`Original: [${nums.join(", ")}]`]);
      setPlaying(true);
    } catch (error) {
      console.error("Merge sort failed:", error);
    }
  }

  // Step through animation
  React.useEffect(() => {
    if (!playing || stepIndex >= steps.length) {
      setPlaying(false);
      return;
    }

    const interval = setInterval(() => {
      setArray(steps[stepIndex]);
      setStepIndex((prev) => prev + 1);
      setHistory((prev) => [
        ...prev,
        `Step ${stepIndex + 1}: [${steps[stepIndex].join(", ")}]`,
      ]);
    }, 800);

    return () => clearInterval(interval);
  }, [playing, stepIndex]);

  function reset() {
    setInput("");
    setArray([]);
    setSteps([]);
    setStepIndex(0);
    setPlaying(false);
    setHistory([]);
  }

  return (
    <Container maxWidth="md" sx={{ mt: 4 }}>
      <Typography variant="h4" align="center" gutterBottom>
        Merge Sort Visualizer
      </Typography>

      {/* Controls */}
      <Box display="flex" gap={2} mb={3}>
        <TextField
          label="Enter numbers (comma-separated)"
          value={input}
          onChange={handleInputChange}
          fullWidth
        />
        <Button variant="contained" onClick={startSort}>
          Sort
        </Button>
        <Button variant="contained" color="error" onClick={reset}>
          Reset
        </Button>
      </Box>

      {/* Visual Array */}
      <Box
        display="flex"
        justifyContent="center"
        alignItems="flex-end"
        gap={1}
        height={200}
        border="1px solid #ccc"
        mb={3}
      >
        {array.map((val, i) => (
          <motion.div
            key={i}
            initial={{ scaleY: 1 }}
            animate={{ scaleY: 1 }}
            style={{
              background: "#1976d2",
              color: "white",
              width: 30,
              height: val * 5,
              display: "flex",
              justifyContent: "center",
              alignItems: "flex-end",
              fontSize: "0.75rem",
              borderRadius: 4,
            }}
          >
            {val}
          </motion.div>
        ))}
      </Box>

      {/* Step History */}
      <Box p={2} bgcolor="#1e1e1e" borderRadius={2} sx={{ border: "1px solid #555" }}>
        <Typography variant="h6" color="white" gutterBottom>
          Sorting Steps
        </Typography>
        <Box display="flex" flexDirection="column" gap={1} maxHeight={200} overflow="auto">
          {history.map((line, index) => (
            <Box
              key={index}
              px={2}
              py={1}
              bgcolor="#2e7d32"
              color="white"
              borderRadius={1}
              fontSize="0.85rem"
            >
              {line}
            </Box>
          ))}
        </Box>
      </Box>
    </Container>
  );
}
