<script setup>
import { defineProps, ref } from 'vue';

const props = defineProps({
  options: {
    type: Array,
    required: true
  }
})
const selectedOption = ref(null)
</script>

<template>
    <div class="dropdown-wrapper">
      <div class="dropdown-selected-option">
        {{ selectedOption || "Please select a data type" }}
      </div>
      <div class="options-wrapper">
        <div
          class="option"
          v-for="(option, index) in options"
          :key="index"
        >
          {{ option }}
        </div>
      </div>
    </div>
</template>

<style>
.dropdown-wrapper {
  margin: 5px;
  padding: 16px;
  margin: 0 auto;
  cursor: pointer;
}

.dropdown-selected-option {
  padding: 8px;
  border: solid 1px black;
  box-sizing: border-box;
  margin-bottom: 4px;
}

.option:hover {
  background: #c5c5c5;
}

.option {
  padding: 8px;
  border: solid 1px black;
  box-sizing: border-box;
}
</style>