import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', 
  headers: {
    'Content-Type': 'application/json'
  }
});

export default {
  getStatus() {
    return apiClient.get('/status');
  },
  startProcess(name, params = {}) {
    return apiClient.post('/start', { name, params });
  },
  stopProcess(name) {
    return apiClient.post('/stop', { name });
  }
};
