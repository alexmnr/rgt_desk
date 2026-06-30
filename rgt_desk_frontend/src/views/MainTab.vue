<script setup>
import { useStore } from '../stores/store';
import Container from '../components/Container.vue';
import ToggleSwitch from '../components/ToggleSwitch.vue';

const store = useStore();
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
