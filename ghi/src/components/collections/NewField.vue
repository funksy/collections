<script setup>
import { ref, defineProps } from 'vue'
import DataTypeDropdown from './DataTypeDropdown.vue'

const props = defineProps(['numField'])
const numField = ref(props.numField)
const name = ref(null)
const dataTypes = ref(['int', 'string', 'bool'])
const dataType = ref('')
const required = ref(false)
</script>

<template>
  <form class="collection-fields-form">
    <input
      class="field-name"
      v-model="name"
      placeholder="Field Name"
    />
    <DataTypeDropdown :options="dataTypes"/>
    <div class="required-checkbox">
      <input class="required-checkbox-button" type="checkbox" v-model="required">
      <label class="required-checkbox-label" for="required-checkbox">Required?</label>
    </div>
  </form>
</template>

<style>
.collection-fields-form {
  display: flex;
  flex-direction: column;
}

.field-name {
  margin: 8px;
  padding: 4px;
  border: 1px solid black;
}

.required-checkbox {
  display: inline;
}

.required-checkbox-button {
  margin-left: 8px;
}

.required-checkbox-label {
  margin-left: 8px;
}
</style>