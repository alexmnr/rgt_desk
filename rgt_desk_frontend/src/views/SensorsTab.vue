<script setup>
import { useStore } from '../stores/store';
import ProcessContainer from '../components/ProcessContainer.vue';
//import ToggleSwitch from '../components/ToggleSwitch.vue';
const store = useStore();
</script>

<template>
  <div class="grid grid-cols-2 p-3 gap-3 w-full h-full">
    <div class="grid grid-cols-1 grid-rows-2 gap-3 w-full h-full">
      <ProcessContainer class="flex-1" title="Tool-Side Realsense" id="tool_side_realsense" @start="() => store.startProcess('tool_side_realsense')" @stop="() => store.stopProcess('tool_side_realsense')"/>
      <ProcessContainer class="flex-1" title="Bed-Side Realsense" id="bed_side_realsense" @start="() => store.startProcess('bed_side_realsense')" @stop="() => store.stopProcess('bed_side_realsense')"/>
    </div>
    <div class="grid grid-cols-1 grid-rows-3 gap-3 w-full h-full">
      <ProcessContainer class="flex-1" title="Gelsight" id="gelsight" @start="() => store.startProcess('gelsight')" @stop="() => store.stopProcess('gelsight')"/>
      <ProcessContainer class="flex-1" title="Thermal Camera" id="thermal_camera" @start="() => store.startProcess('thermal_camera')" @stop="() => store.stopProcess('thermal_camera')"/>
      <ProcessContainer class="flex-1" title="Audio Capture" id="audio_capture" @start="() => store.startProcess('audio_capture')" @stop="() => store.stopProcess('audio_capture')"/>
    </div>
  </div>
</template>
