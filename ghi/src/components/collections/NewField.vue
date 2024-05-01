<script setup>
import { ref, defineProps, defineModel } from 'vue'
import DataTypeDropdown from './DataTypeDropdown.vue'

const fieldValues = defineModel()
const props = defineProps(['index'])
const index = ref(props.index)
const dataTypes = ref(['Number', 'String', 'True/False'])
</script>

<template class="collection-fields-wrapper">
  <h2 class="collection-fields-number">Field number: {{ index + 1 }}</h2>
  <form class="collection-fields-form">
    <input
      id="field-name"
      class="field-name"
      v-model="fieldValues.name"
      placeholder="Field name"
      required
    />
    <DataTypeDropdown
      id="data-type"
      :options="dataTypes"
      v-model="fieldValues.data_type"
    />
    <div class="required-checkbox-wrapper">
      <input id="required-checkbox" class="required-checkbox-button" type="checkbox" v-model="fieldValues.required">
      <label class="required-checkbox-label">Field required?</label>
    </div>
  </form>
</template>

<style>
.collection-fields-number {
  margin: 8px;
  font-weight: bold;
}
.collection-fields-form {
  display: flex;
  flex-direction: column;
  margin-bottom: 8px;
}

.field-name {
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