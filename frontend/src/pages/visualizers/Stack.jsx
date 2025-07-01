import React, {useState, useEffect} from "react";
import axios from 'axios'
import { Container, Grid, Typography, Box, Button, TextField } from "@mui/material";
import { motion, AnimatePresence } from "framer-motion";

export default function StackVisualizer() {

    const MAX_STACK_SIZE = 10;


    const [input, setInput] = useState("");
    const [stack, setStack] = useState([]);
    const [history, setHistory] = useState([])
    const [peekIndex, setPeekIndex] = useState(null);


    const BASE_URL = "http://localhost:8000/stack"

    useEffect(() => {
        getStack();
    }, []);



    async function getStack() {
      try {
        const response = await axios.get(BASE_URL);
        setStack(response.data.message);
      } catch (error) {
        console.error("Error fetching stack:", error);
      }
    }


    async function pushToStack() {
      try {
        const response = await axios.post(BASE_URL, { value: input });
        setHistory((prev) => [...prev, `Push: ${input}`]);

        setStack((prev) => [...prev, { id: Date.now(), value: input }]);
        setInput("");
      } catch (error) {
        console.error("Push failed:", error);
      }
    }


    async function popToStack() {
      try {
        const response = await axios.delete(BASE_URL);
        const value = response.data.message;
        setHistory((prev) => [
          ...prev,
          `Pop: ${value}`
        ]);
        setStack((prev) => prev.slice(0, -1));
        setInput("");
      } catch (error) {
        console.error("Pop failed:", error);
      }
    }

    async function peek() {
      try {
        const response = await axios.get(BASE_URL + '/peek');
        const value = response.data.message;

        setHistory((prev) => [
          ...prev,
          value !== undefined
            ? `Peek: Element ${value} is at the top of the stack`
            : `Peek: The stack is empty`
        ]);

        if (stack.length > 0) {
          setPeekIndex(stack.length - 1);
          setTimeout(() => setPeekIndex(null), 1000);
        }

        setInput("");
        getStack();
      } catch (error) {
        console.error("Peek failed:", error);
      }
    }


    async function is_empty() {
      try {
        const response = await axios.get(BASE_URL + "/empty");
        const sizeResponse = await axios.get(BASE_URL + "/size");
        const isEmpty = response.data.message;
        const size = sizeResponse.data.message;

        setHistory((prev) => [
        ...prev,
        isEmpty
        ? `Is-Empty: The stack is empty`
        : `Is-Empty: The stack is not empty having ${size} element(s)`
        ]);

        setInput("");
        getStack();
      } catch (error) {
        console.error("Is-empty failed:", error);
      }
    }

    async function reset() {
      try {
        const response = await axios.get(BASE_URL+"/clear");
        setInput("");
        setStack([]);
        setHistory((prev) => [
        ...prev,
        "Reset: Stack has been cleared"
        ]);

      } catch (error) {
        console.error("reset failed:", error);
      }
    }




    return (
      <Container>
        <Typography variant="h4" gutterBottom>Stack</Typography>
        <Grid container spacing={4}>
          <Grid item xs={12} md={4}>
            <Box mb={3} p={2} bgcolor="grey.200" borderRadius={2}>
              <Typography variant="h6">Stack Controls</Typography>
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
                    onClick={() => {
                      if (stack.length >= MAX_STACK_SIZE) {
                        setHistory(prev => [...prev, "Push: Stack is full"]);
                        return;
                      }
                      pushToStack();
                    }}
                  >
                    Push
                  </Button>
                </Grid>
                <Grid item xs={6}>
                  <Button fullWidth variant="outlined" onClick={popToStack}>
                    Pop
                  </Button>
                </Grid>
                <Grid item xs={6}>
                  <Button fullWidth color="info" variant="contained" onClick={peek}>
                    Peek
                  </Button>
                </Grid>
                <Grid item xs={6}>
                  <Button fullWidth color="warning" variant="contained" onClick={is_empty}>
                    Is-Empty
                  </Button>
                </Grid>
                <Grid item xs={12}>
                  <Button fullWidth color="error" variant="contained" onClick={reset}>
                    Clear
                  </Button>
                </Grid>
              </Grid>
            </Box>
            <Box p={2} bgcolor="grey.200" borderRadius={2}>
              <Typography variant="h6">Operation History</Typography>
              <Box mt={1}>
                {history.map((entry, idx) => (
                  <Typography key={idx} variant="body2">• {entry}</Typography>
                ))}
              </Box>
            </Box>
          </Grid>

          <Grid item xs={12} md={8}>
            <Box
              display="flex"
              justifyContent="center"
              alignItems="flex-end"
              height={400}
              overflow="hidden"
              border={1}
              borderRadius={2}
              p={2}
            >
              <Box
                display="flex"
                flexDirection="column-reverse"
                justifyContent="flex-start"
                alignItems="center"
                width={150}
                height="100%"
                position="relative"
              >
                <AnimatePresence>
                  {stack.map((item, index) => {
                    const isBottom = index === 0;
                    const isPeeked = index === stack.length - 1 && peekIndex === index;

                    return (
                      <motion.div
                        key={item.id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -20 }}
                        transition={{ duration: 0.3 }}
                        style={{ width: '100%', height: `${100 / MAX_STACK_SIZE}%` }}
                      >
                        <motion.div
                          animate={isPeeked ? { scale: 1.1, backgroundColor: "#FFEB3B" } : {}}
                          transition={{ duration: 0.3 }}
                          style={{
                            backgroundColor: isPeeked ? "#1976d2" : "#424242",
                            color: "white",
                            width: "100%",
                            height: "100%",
                            borderRadius: isBottom ? '0 0 16px 16px' : '0',
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "center",
                            fontWeight: "bold"
                          }}
                        >
                          {item.value}
                        </motion.div>
                      </motion.div>
                    );
                  })}
                </AnimatePresence>
              </Box>
            </Box>
          </Grid>
        </Grid>
      </Container>
    );


}