<script setup>
import { useStore } from '../stores/store';
import ProcessContainer from '../components/ProcessContainer.vue';
import ServiceContainer from '../components/ServiceContainer.vue';
import DropdownMenu from '../components/DropdownMenu.vue';
const store = useStore();

const namespaces = [
  { label: 'None', value: '' },
  { label: 'ur20', value: 'ur20' },
  { label: 'nex10', value: 'nex10' }
];
</script>

<template>
  <div class="grid grid-cols-2 grid-rows-3 p-3 gap-3 w-full h-full">
    <ProcessContainer class="flex-1" title="Spacemouse" id="spacemouse" @start="() => store.startProcess('spacemouse')" @stop="() => store.stopProcess('spacemouse')">
      <DropdownMenu 
        v-model="store.configs.spacemouse.ns" 
        label="Namespace" 
        :options="namespaces" 
      />
    </ProcessContainer>
    <ServiceContainer class="flex-1" title="Home" id="home" @execute="() => store.executeService('home')">
      <DropdownMenu 
        v-model="store.configs.home.ns" 
        label="Namespace" 
        :options="namespaces" 
      />
    </ServiceContainer>
    <ServiceContainer class="flex-1" title="Park" id="park" @execute="() => store.executeService('park')">
      <DropdownMenu 
        v-model="store.configs.park.ns" 
        label="Namespace" 
        :options="namespaces" 
      />
    </ServiceContainer>
  </div>
</template>
