<script setup>
import { reactive } from 'vue';
import { useStore } from '../stores/store';
import Container from '../components/Container.vue';
import ToggleSwitch from '../components/ToggleSwitch.vue';

const store = useStore();
// handler functions
const handleStartUr20 = () => {store.startService('ur20', { ...ur20Config });};
const handleStartNex10 = () => {store.startService('nex10', { ...nex10Config });};

</script>

<template>
  <div class="grid grid-cols-2 grid-rows-2 p-3 gap-3 w-full h-full">
    <Container class="flex-1" title="UR 20" id="ur20" @start="() => store.startService('ur20')" @stop="() => store.stopService('ur20')">
      <ToggleSwitch 
        v-model="store.configs.ur20.use_mock_hardware" 
        label="Use Mock Hardware" 
      />
    </Container>

    <Container class="flex-1" title="Nex 10" id="nex10" @start="() => store.startService('nex10')" @stop="() => store.stopService('nex10')">
      <ToggleSwitch 
        v-model="store.configs.nex10.use_mock_hardware" 
        label="Use Mock Hardware" 
      />
      <ToggleSwitch 
        v-model="store.configs.nex10.use_ft_sensor" 
        label="Use FT Sensor" 
      />
    </Container>

    <Container class="flex-1" title="RGT Manager" id="rgt_manager" @start="() => store.startService('rgt_manager')" @stop="() => store.stopService('rgt_manager')"/>
    <Container class="flex-1" title="Foxglove Bridge" id="foxglove_bridge" @start="() => store.startService('foxglove_bridge')" @stop="() => store.stopService('foxglove_bridge')"/>
    
  </div>
</template>
