import { createRouter, createWebHistory } from 'vue-router';
import MainTab from '../views/MainTab.vue';
import ToolsTab from '../views/ToolsTab.vue';
import SensorsTab from '../views/SensorsTab.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/main' },
    { path: '/main', name: 'main', component: MainTab },
    { path: '/tools', name: 'tools', component: ToolsTab },
    { path: '/sensors', name: 'sensors', component: SensorsTab },
  ]
});

export default router;
