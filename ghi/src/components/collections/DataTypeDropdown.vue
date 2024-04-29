<script setup>
import {
  ref,
  defineProps,
  defineModel,
  onMounted,
  onBeforeUnmount 
} from 'vue';

const dataType = defineModel()
const props = defineProps(['options'])
const selectedOption = ref(null)
const isDropdownVisible = ref(false)
const dropdown = ref(null)

const toggleOptionSelect = (option) => {
  dataType.value = option
  selectedOption.value = option
  // emit('update: modelValue', option)
  isDropdownVisible.value = false
}

const closeDropdown = (element) => {
  if (!dropdown.value.contains(element.target)) {
    isDropdownVisible.value = false
  }
}

onMounted(() => {
  window.addEventListener('click', closeDropdown)
})

onBeforeUnmount(() => {
  window.removeEventListener('click', closeDropdown)
})
</script>

<template>
    <div class="dropdown-wrapper" ref="dropdown">
      <div
        class="dropdown-selected-option"
        @focus="isDropdownVisible = true"
        tabindex="0"
      >
        <span v-if="selectedOption">
          {{ selectedOption }}
        </span>
        <span v-else v-bind:style="{opacity: 0.5}">
          Field data type
        </span>
      </div>
      <div
        class="options-wrapper"
        v-if="isDropdownVisible"
      >
        <div
          class="option"
          v-for="(option, index) in options"
          :key="index"
          @click="toggleOptionSelect(option)"
        >
          {{ option.name || option }}
        </div>
      </div>
    </div>
</template>

<style>
.dropdown-wrapper {
  cursor: pointer;
  width: 100%;
}

.dropdown-selected-option {
  margin: 8px;
  padding: 8px;
  border: solid 1px black;
  border-radius: 4px;
}

.options-wrapper {
  position: relative;
  margin: 8px;
  margin-top: -4px;
}

.option:hover {
  background: #dddddd;
}

.option {
  margin-top: -1px;
  padding: 8px;
  border: solid 1px black;
}

.option:first-of-type {
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}

.option:last-of-type {
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
}
</style>