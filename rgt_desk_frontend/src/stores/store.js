import { defineStore } from 'pinia';
import api from '../services/api';

export const useStore = defineStore('store', {
  state: () => ({
    status: {
      "ur20": "unknown",
      "nex10": "unknown",
      "rgt_manager": "unknown",
      "foxglove_bridge": "unknown",
    },
    configs: {
      ur20: {
        use_mock_hardware: false,
      },
      nex10: {
        use_mock_hardware: false,
        use_ft_sensor: true,
      }
    },
    pollingInterval: null
  }),
  actions: {
    async fetchStatus() {
      try {
        const response = await api.getStatus();
        this.status = response.data;
      } catch (error) {
        console.error("Failed to fetch status from backend:", error);
      }
    },
    
    startPolling() {
      if (!this.pollingInterval) {
        this.fetchStatus(); // Fetch immediately on start
        this.pollingInterval = setInterval(this.fetchStatus, 1000);
      }
    },
    
    stopPolling() {
      if (this.pollingInterval) {
        clearInterval(this.pollingInterval);
        this.pollingInterval = null;
      }
    },
    
    async startService(id, configData = this.configs[id] || {}) {
      console.log(`Starting service: ${id}`, configData);
      try {
        await api.startProcess(id, configData);
      } catch (error) {
        console.error(`Failed to start process ${id}:`, error);
        this.status[id] = 'unknown';
      }
    },
    
    async stopService(id) {
      console.log(`Stopping service: ${id}`);
      try {
        await api.stopProcess(id);
      } catch (error) {
        console.error(`Failed to stop process ${id}:`, error);
        this.status[id] = 'unknown';
      }
    },
  }
});
