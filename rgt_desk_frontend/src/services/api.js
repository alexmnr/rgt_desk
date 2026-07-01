import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', 
  headers: {
    'Content-Type': 'application/json'
  }
});

export default {
  getStatus() {
    return apiClient.get('/get_status');
  },
  startProcess(name, params = {}) {
    return apiClient.post('/start_process', { name, params });
  },
  stopProcess(name) {
    return apiClient.post('/stop_process', { name });
  },
  executeService(name, params = {}) {
    return apiClient.post('/execute_service', { name, params });
  },
};
