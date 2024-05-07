<script setup>
import { ref, defineProps, defineModel } from "vue";
import DataTypeDropdown from "../common/DataTypeDropdown.vue";

const collectionFields = defineModel();
const dropdownOptions = ref([
  {
    display: "String",
    val: "str",
  },
  {
    display: "Number",
    val: "int",
  },
  {
    display: "True/False",
    val: "bool",
  },
]);
</script>

<template class="collection-fields-wrapper">
  <form class="collection-fields-form">
    <input
      id="collection-field-name"
      class="collection-field-name"
      v-model="collectionFields.name"
      placeholder="Field name"
      required
    />
    <DataTypeDropdown
      id="collection-data-type"
      :options="dropdownOptions"
      :placeholder="'Field Data Type'"
      v-model="collectionFields.data_type"
    />
    <div class="required-checkbox-wrapper">
      <input
        id="required-checkbox"
        class="required-checkbox-button"
        type="checkbox"
        v-model="collectionFields.required"
      />
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

.collection-field-name {
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
