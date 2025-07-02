import React, { useState, useEffect } from "react";
import axios from 'axios';
import { Container, Grid, Typography, Box, Button, TextField } from "@mui/material";
import { motion, AnimatePresence } from "framer-motion";

export default function SinglyLinkedListVisualizer() {
  const MAX_SINGLY_LINKED_LIST_SIZE = 10;

  const [input, setInput] = useState("");
  const [linkedList, setLinkedList] = useState([]);
  const [history, setHistory] = useState([]);
  const [reverseSteps, setReverseSteps] = useState([]);
  const [stepIndex, setStepIndex] = useState(null);

  const BASE_URL = "http://localhost:8000/singly-linked-list";

  useEffect(() => {
    getSinglyLinkedList();
  }, []);

  async function getSinglyLinkedList() {
    try {
      const response = await axios.get(BASE_URL + "/traverse");
      setLinkedList(response.data.message || []);
    } catch (error) {
      console.error("Error fetching list:", error);
      setLinkedList([])
    }
  }

  async function insertAtFront() {
    try {
      await axios.post(BASE_URL + "/add-head", { value: input });
      setHistory((prev) => [...prev, `Insert: ${input} at front`]);
      setInput("");
      getSinglyLinkedList();
    } catch (error) {
      console.error("Insert failed:", error);
    }
  }

  async function insertAtBack() {
    try {
      await axios.post(BASE_URL + "/add-tail", { value: input });
      setHistory((prev) => [...prev, `Insert: ${input} at back`]);
      setInput("");
      getSinglyLinkedList();
    } catch (error) {
      console.error("Insert failed:", error);
    }
  }

  async function deleteInFront() {
    try {
      const response = await axios.delete(BASE_URL + "/delete-front");
      const value = response.data.message;
      setHistory((prev) => [...prev, `Delete: ${value} from front`]);
      setInput("");
      getSinglyLinkedList();
    } catch (error) {
      console.error("Delete front failed:", error);
    }
  }

  async function deleteInBack() {
    try {
      const response = await axios.delete(BASE_URL + "/delete-back");
      const value = response.data.message;
      setHistory((prev) => [...prev, `Delete: ${value} from back`]);
      setInput("");
      getSinglyLinkedList();
    } catch (error) {
      console.error("Delete back failed:", error);
    }
  }

 async function reverse_list() {
  try {
    const response = await axios.get(BASE_URL + "/reverse");
    const { steps, current } = response.data;

    setReverseSteps(steps || []);
    setStepIndex(0);
    setHistory((prev) => [...prev, "Reverse List"]);

    let index = 0;
    const interval = setInterval(() => {
      if (index >= steps.length) {
        clearInterval(interval);


        if (Array.isArray(current)) {
          setLinkedList(current);
        } else {
          setLinkedList([]);
        }


        setTimeout(() => {
          setStepIndex(null);
        }, 300);
        return;
      }

      setStepIndex(index);
      index++;
    }, 1000);
  } catch (error) {
    console.error("Reverse failed:", error);
  }
}



  async function reset() {
    try {
      await axios.get(BASE_URL + "/clear");
      setInput("");
      setLinkedList([]);
      setStepIndex(null);
      setReverseSteps([]);
      setHistory((prev) => [...prev, "Reset: Singly Linked List cleared"]);
    } catch (error) {
      console.error("Reset failed:", error);
    }
  }

  return (
    <Container>
      <Typography variant="h4" gutterBottom>Singly Linked List</Typography>
      <Grid container spacing={4}>

        {/* Controls Section */}
        <Grid item xs={12} md={4}>
          <Box mb={3} p={2} bgcolor="grey.700" borderRadius={2}>
            <Typography variant="h6" color="white">Controls</Typography>
            <TextField
              label="Enter Value"
              variant="outlined"
              fullWidth
              value={input}
              onChange={(e) => setInput(e.target.value)}
              margin="normal"
            />
            <Grid container spacing={1}>
              <Grid item xs={6}>
                <Button fullWidth variant="contained" onClick={insertAtFront} disabled={(linkedList?.length || 0) >= MAX_SINGLY_LINKED_LIST_SIZE}>
                  Add Head
                </Button>
              </Grid>
              <Grid item xs={6}>
                <Button fullWidth variant="contained" onClick={insertAtBack} disabled={(linkedList?.length || 0)>= MAX_SINGLY_LINKED_LIST_SIZE}>
                  Add Tail
                </Button>
              </Grid>
              <Grid item xs={6}>
                <Button fullWidth variant="contained" color="error" onClick={deleteInFront}>
                  Delete Front
                </Button>
              </Grid>
              <Grid item xs={6}>
                <Button fullWidth variant="contained" color="error" onClick={deleteInBack}>
                  Delete Back
                </Button>
              </Grid>
              <Grid item xs={6}>
                <Button fullWidth variant="contained" color="secondary" onClick={reverse_list}>
                  Reverse
                </Button>
              </Grid>
              <Grid item xs={6}>
                <Button fullWidth variant="contained" color="warning" onClick={reset}>
                  Clear
                </Button>
              </Grid>
            </Grid>
          </Box>

          {/* History Panel */}
          <Box p={2} bgcolor="grey.700" borderRadius={2}>
            <Typography variant="h6" color="white">Operation History</Typography>
            <Box mt={1} sx={{ maxHeight: 200, overflowY: "auto" }}>
              {history.map((entry, idx) => (
                <Typography key={idx} variant="body2" color="white">
                  • {entry}
                </Typography>
              ))}
            </Box>
          </Box>
        </Grid>

        {/* Linked List Display */}
        <Grid item xs={12} md={8}>
          <Box display="flex" flexDirection="column" alignItems="center">
            <Typography variant="h6">Linked List</Typography>

            {/* Show Current/Next/Prev if in reverse mode */}
            {stepIndex !== null && reverseSteps[stepIndex] && (
              <Typography mt={1} fontWeight="bold">
                Current: {reverseSteps[stepIndex].current}{" "}
                Next: {reverseSteps[stepIndex].next ?? "null"}{" "}
                Prev: {reverseSteps[stepIndex].prev ?? "null"}
              </Typography>
            )}

            <Box
              mt={2}
              display="flex"
              alignItems="center"
              flexWrap="wrap"
              minHeight={120}
              border={2}
              borderRadius={2}
              p={2}
            >
              <AnimatePresence>
                {linkedList.map((value, index) => (
                  <motion.div
                    key={`${value}-${index}`}
                    initial={{ opacity: 0, y: -10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: 10 }}
                    transition={{ duration: 0.3 }}
                  >
                    <Box display="flex" alignItems="center" mr={2}>
                      <Box
                        px={2}
                        py={1}
                        bgcolor="grey.800"
                        color="white"
                        borderRadius={2}
                        boxShadow={
                          reverseSteps[stepIndex]?.current === value
                            ? "0 0 10px 4px yellow"
                            : ""
                        }
                        textAlign="center"
                      >
                        {value}
                      </Box>
                      {index !== linkedList.length - 1 && (
                        <Typography mx={1} fontSize={24}>➝</Typography>
                      )}
                    </Box>
                  </motion.div>
                ))}
              </AnimatePresence>
            </Box>
          </Box>
        </Grid>
      </Grid>
    </Container>
  );
}
