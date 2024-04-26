<script setup>
import { ref, defineProps } from 'vue'
import DataTypeDropdown from './DataTypeDropdown.vue'

const props = defineProps(['numField'])
const numField = ref(props.numField)
const fieldValues = ref({
  name: null,
  dataType: null,
  required: false
})
const dataTypes = ref([{
  name: 'Number',
  value: 'int'
  },
  {
  name: 'String',
  value: 'str'
  },
  {
  name: 'True/False',
  value: 'bool'
  },
])
</script>

<template class="collection-fields-wrapper">
  <h2 class="collection-fields-number">Field number: {{ numField }}</h2>
  <form class="collection-fields-form">
    <input
      id="field-name"
      class="field-name"
      v-model="fieldValues.name"
      placeholder="Field name"
    />
    <DataTypeDropdown
      id="data-type"
      :options="dataTypes"
      v-model="fieldValues.dataType"
    />
    <div class="required-checkbox-wrapper">
      <input id="required-checkbox" class="required-checkbox-button" type="checkbox" v-model="fieldValues.required">
      <label class="required-checkbox-label" for="required-checkbox">Field required?</label>
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
  margin-bottom: 32px;
}

.field-name {
  margin: 8px;
  padding: 8px;
  border: 1px solid black;
}

.required-checkbox-wrapper {
  display: inline;
}

.required-checkbox-button {
  margin: 8px;
}

.required-checkbox-label {
  margin-left: 8px;
}
</style>