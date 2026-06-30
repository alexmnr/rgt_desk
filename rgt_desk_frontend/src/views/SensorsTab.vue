<script setup>
import { useStore } from '../stores/store';
import Container from '../components/Container.vue';
//import ToggleSwitch from '../components/ToggleSwitch.vue';
const store = useStore();
</script>

<template>
  <div class="grid grid-cols-2 p-3 gap-3 w-full h-full">
    <div class="grid grid-cols-1 grid-rows-2 gap-3 w-full h-full">
      <Container class="flex-1" title="Tool-Side Realsense" id="tool_side_realsense" @start="() => store.startService('tool_side_realsense')" @stop="() => store.stopService('tool_side_realsense')"/>
      <Container class="flex-1" title="Bed-Side Realsense" id="bed_side_realsense" @start="() => store.startService('bed_side_realsense')" @stop="() => store.stopService('bed_side_realsense')"/>
    </div>
    <div class="grid grid-cols-1 grid-rows-3 gap-3 w-full h-full">
      <Container class="flex-1" title="Gelsight" id="gelsight" @start="() => store.startService('gelsight')" @stop="() => store.stopService('gelsight')"/>
      <Container class="flex-1" title="Thermal Camera" id="thermal_camera" @start="() => store.startService('thermal_camera')" @stop="() => store.stopService('thermal_camera')"/>
      <Container class="flex-1" title="Audio Capture" id="audio_capture" @start="() => store.startService('audio_capture')" @stop="() => store.stopService('audio_capture')"/>
    </div>
  </div>
</template>
