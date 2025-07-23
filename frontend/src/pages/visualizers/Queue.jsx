import React, {useState, useEffect} from "react";
import api from '../../components/axios';
import { Container, Grid, Typography, Box, Button, TextField } from "@mui/material";
import { motion, AnimatePresence } from "framer-motion";

export default function QueueVisualizer() {

    const MAX_QUEUE_SIZE = 10;


    const [input, setInput] = useState("");
    const [queue, setQueue] = useState([]);
    const [history, setHistory] = useState([])
    const [peekIndex, setPeekIndex] = useState(null);



    useEffect(() => {
        getQueue();
    }, []);



    async function getQueue() {
      try {
        const response = await api.get("/queue/get-item");
        setQueue(response.data.message);
      } catch (error) {
        console.error("Error fetching Queue:", error);
      }
    }


    async function enqueueToQueue() {
      try {
        const response = await api.post("/queue/enqueue", { value: input });
        setHistory((prev) => [...prev, `Enqueue: ${input}`]);

        setQueue((prev) => [...prev, { id: Date.now(), value: input }]);
        setInput("");
      } catch (error) {
        console.error("Enqueue failed:", error);
      }
    }


    async function dequeueFromQueue() {
      try {
        const response = await api.delete("/queue/dequeue");
        const value = response.data.message;
        setHistory((prev) => [
          ...prev,
          `Dequeue: ${value}`
        ]);
        setQueue((prev) => prev.slice(1));
        setInput("");
      } catch (error) {
        console.error("Dequeue failed:", error);
      }
    }

    async function peek() {
      try {
        const response = await api.get('/queue/peek');
        const value = response.data.message;

        setHistory((prev) => [
          ...prev,
          value !== undefined
            ? `Peek: Element ${value} is at the head of the queue`
            : `Peek: The queue is empty`
        ]);

        if (queue.length > 0) {
          setPeekIndex(0);
          setTimeout(() => setPeekIndex(null), 1000);
        }

        setInput("");
        getQueue();
      } catch (error) {
        console.error("Peek failed:", error);
      }
    }


    async function is_empty() {
      try {
        const response = await api.get("/queue/empty");
        const sizeResponse = await api.get("/queue/size");
        const isEmpty = response.data.message;
        const size = sizeResponse.data.message;

        setHistory((prev) => [
        ...prev,
        isEmpty
        ? `Is-Empty: The queue is empty`
        : `Is-Empty: The queue is not empty having ${size} element(s)`
        ]);

        setInput("");
        getQueue();
      } catch (error) {
        console.error("Is-empty failed:", error);
      }
    }

    async function reset() {
      try {
        const response = await api.get("/queue/clear");
        setInput("");
        setQueue([]);
        setHistory((prev) => [
        ...prev,
        "Reset: Queue has been cleared"
        ]);

      } catch (error) {
        console.error("reset failed:", error);
      }
    }


    return (
      <Container>
        <Typography variant="h4" gutterBottom>Queue</Typography>
        <Grid container spacing={4}>
          {/* Controls */}
          <Grid item xs={12} md={4}>
            <Box mb={3} p={2} bgcolor="grey.600" borderRadius={2}>
              <Typography variant="h6" color="white">Queue Controls</Typography>
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
                  <Button
                    fullWidth
                    variant="contained"
                    onClick={enqueueToQueue}
                    disabled={queue.length >= MAX_QUEUE_SIZE}
                  >
                    Enqueue
                  </Button>
                </Grid>
                <Grid item xs={6}>
                  <Button fullWidth variant="contained" color="error" onClick={reset}>
                    Clear
                  </Button>
                </Grid>
                <Grid item xs={6}>
                  <Button fullWidth variant="contained" color="info" onClick={peek}>
                    Peek
                  </Button>
                </Grid>
                <Grid item xs={6}>
                  <Button fullWidth variant="contained" color="secondary" onClick={is_empty}>
                    Is-empty
                  </Button>
                </Grid>
                <Grid item xs={12}>
                  <Button fullWidth variant="contained" color="warning" onClick={dequeueFromQueue}>
                    Dequeue
                  </Button>
                </Grid>
              </Grid>
            </Box>

            {/* Operation History */}
            <Box p={2} bgcolor="grey.600" borderRadius={2}>
              <Typography variant="h6" color="white">Operation History</Typography>
              <Box mt={1}>
                {history.map((entry, idx) => (
                  <Typography key={idx} variant="body2" color="white">
                    • {entry}
                  </Typography>
                ))}
              </Box>
            </Box>
          </Grid>

          {/* Queue Display */}
          <Grid item xs={12} md={8}>
            <Box display="flex" flexDirection="column" alignItems="center">
              <Box width="100%" display="flex" justifyContent="space-between" px={2}>
                <Typography variant="subtitle1">Head ➝</Typography>
                <Typography variant="subtitle1">Tail ➝</Typography>
              </Box>
              <Box
                mt={2}
                display="flex"
                flexDirection="row"
                alignItems="center"
                justifyContent="flex-start"
                minHeight={150}
                width="100%"
                border={2}
                borderRadius={2}
                px={2}
                py={3}
              >
                <AnimatePresence>
                  {queue.map((item, index) => (
                    <motion.div
                      key={item.id}
                      initial={{ opacity: 0, y: -10 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: 10 }}
                      transition={{ duration: 0.3 }}
                    >
                      <Box
                        m={1}
                        px={2}
                        py={1}
                        bgcolor="grey.800"
                        color="white"
                        borderRadius={2}
                        textAlign="center"
                        boxShadow={peekIndex === index ? "0 0 10px 4px yellow" : ""}
                      >
                        {item.value}
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