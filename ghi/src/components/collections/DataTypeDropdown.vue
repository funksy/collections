<script setup>
import {
  ref,
  computed,
  defineProps,
  defineEmits,
  onMounted,
  onBeforeUnmount 
} from 'vue';

const props = defineProps({
  options: {
    type: Array,
    required: true
  },
  modelValue: {
    default: null
  }
})
const emit = defineEmits(['update: modelValue'])
const selectedOption = ref(null)
const mappedSelectedOption = computed(() => {
  return (selectedOption.value?.name || selectedOption.value) || 'Field data type'
})
const isDropdownVisible = ref(false)
const dropdown = ref(null)

const toggleOptionSelect = (option) => {
  selectedOption.value = option
  emit('update: modelValue', option)
  closeDropdown()
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
    <div class="dropdown-wrapper">
      <div
        class="dropdown-selected-option"
        @focus="isDropdownVisible = true"
        ref="dropdown"
        tabindex="0"
      >
        <span v-bind:style="!selectedOption ? {opacity: 0.5} : {opacity: 1}">
          {{ mappedSelectedOption }}
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