import axios from "axios";

const BASE_URL = import.meta.env.VITE_REACT_APP_API || "http://localhost:8000";

console.log("API Base URL:", BASE_URL);

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
