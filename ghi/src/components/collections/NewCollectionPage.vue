<script setup>
import { ref } from 'vue';
import NewField from './NewField.vue'

const numFields = ref(1)
const name = ref('')

function addField() {
  numFields.value++
}
function removeField() {
  if (numFields.value > 1) {
    numFields.value--
  }
}
</script>

<template>
  <div class="new-collection-page">
    <div class="new-collection-form-wrapper">
      <h1 class="new-collection-header">New Collection</h1>
      <form class="new-collection-form">
        <input
          class="new-collection-name"
          v-model="name"
          placeholder="Collection Name"
        />
        <h1 class="new-collection-fields-header">Collection Fields</h1>
        <ul v-for="field in numFields">
          <NewField :numField="field" />
        </ul>
      </form>
      <button @click="addField">Add Field</button>
      <button @click="removeField">Remove Field</button>
    </div>
  </div>
</template>

<style>
.new-collection-page {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.new-collection-form-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 24rem;
  border: 4px solid blue;
  margin: 8px;
}

.new-collection-header {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 8px;
}

.new-collection-form {
  margin: 8px;
  display: flex;
  flex-direction: column;
}

.new-collection-name {
  margin: 8px;
  padding: 4px;
  border: 1px solid black;
}

.new-collection-fields-header {
  margin: 8px;
  text-align: center;
  font-weight: bold;
  font-size: larger;
}
</style>