import axios from 'axios';

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/", // Change this if your backend runs elsewhere
});

export default API;
