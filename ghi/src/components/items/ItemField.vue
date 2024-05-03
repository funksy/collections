<script setup>
import { ref, defineProps, defineModel } from 'vue';
import DataTypeDropdown from '../common/DataTypeDropdown.vue'

const field = defineModel()
const props = defineProps(['fieldDataType'])
const dataType = props.fieldDataType
const dropdownOptions = ref([
  {
    display: 'True',
    val: true
  },
  {
    display: 'False',
    val: false
  }
])
</script>

<template>
  <h2 class="item-field-header">{{ field.name }}</h2>
  <form class="item-field-form">
    <input
      class="item-field-input-string"
      v-if="dataType === 'str'"
      type="text"
      v-model="field.val"
      placeholder="Please input your string"
    />
    <input
      class="item-field-input-number"
      v-if="dataType === 'int'"
      type="number"
      v-model="field.val"
      placeholder="Please input a number"
    />
    <DataTypeDropdown
      v-if="dataType === 'bool'"
      :options="dropdownOptions"
      :placeholder="'True/False?'"
      v-model="field.val"
    />
  </form>
</template>

<style>
.item-field-header {
  margin: 8px;
  font-weight: bold;
  text-transform: capitalize;
}

.item-field-form {
  display: flex;
  flex-direction: column;
  margin-bottom: 8px;
}

.item-field-input-string {
  margin: 8px;
  padding: 8px;
  border: 1px solid black;
  border-radius: 4px;
}

.item-field-input-number {
  margin: 8px;
  padding: 8px;
  border: 1px solid black;
  border-radius: 4px;
}

.required-checkbox-wrapper {
  display: inline;
}

.required-checkbox-button {
  margin: 8px;
  cursor: pointer;
}

.required-checkbox-label {
  margin-left: 8px;
}
</style>