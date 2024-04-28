<script setup>
import { ref, computed } from 'vue';
import { useUser } from '../../store/UserStore';
import NewField from './NewField.vue'

const userStore = useUser()
const collectionData = ref({
  name: null,
  fields: [
    {
      name: null,
      data_type: null,
      required: false
    }
  ]
})
const errorMessage = ref(null)

const formValidation = () => {
  let formName = false
  if (collectionData.value.name) {
    formName = true
  }
  let formFields = true
  for (const field of collectionData.value.fields) {
    if (!field.name || !field.data_type) {
      formFields = false
    }
  }
  return formName && formFields
}

const addField = () => {
  collectionData.value.fields.push({
    name: null,
    data_type: null,
    required: false
  })
}
const removeField = () => {
  collectionData.value.fields.pop()
}

const createCollection = async (e) => {
  e.preventDefault()
  if (formValidation.value) {
    console.log('is this happening?')
    const collectionsUrl = import.meta.env.VITE_API_HOST + `/collections/${userStore.userData.username}`
    const body = JSON.stringify(collectionData.value)
    const fetchConfig = {
      method: 'post',
      body: body,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + userStore.token.access_token,
      }
    }
    const response = await fetch(collectionsUrl, fetchConfig)
    if (response.ok) {
      const data = await response.json()
      console.log(data)
    }
  } else {
    errorMessage.value = "Please ensure all fields are filled out"
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
          v-model="collectionData.name"
          placeholder="Collection Name"
          required
        />
        <h1 class="new-collection-fields-header">Collection Fields</h1>
        <ul v-for="(field, index) in collectionData.fields">
          <NewField
            v-model="collectionData.fields[index]"
            :index="index"
          />
        </ul>
        <button
          type="button"
          class="field-button"
          @click="addField"
        >
          Add Field
        </button>
        <button
          type="button"
          class="field-button"
          @click="removeField"
          v-if="collectionData.fields.length > 1"
        >
          Remove Field
        </button>
        <button
          type="submit"
          class="collection-submit-button"
          @click="createCollection"
        >
          Create Collection
        </button>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
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
  padding: 8px;
}

.new-collection-header {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 8px;
}

.new-collection-form {
  margin: 8px;
  margin-bottom: 4px;
  display: flex;
  flex-direction: column;
}

.new-collection-name {
  margin: 8px;
  padding: 8px;
  border: 1px solid black;
  border-radius: 4px;
}

.new-collection-fields-header {
  margin: 8px;
  text-align: center;
  font-weight: bold;
  font-size: larger;
}

.field-button {
  place-self: center;
  width: 6rem;
  margin: 4px;
  padding: 2px;
  border: 1px solid black;
  border-radius: 4px;
  background-color: lightgray;
  font-size: smaller;
}

.collection-submit-button {
  place-self: center;
  width: 10rem;
  margin: 8px;
  padding: 8px;
  border: 1px solid black;
  border-radius: 4px;
  background-color: green;
  font-weight: bold;
}

.error-message {
  place-self: center;
  color: red;
  font-weight: bold;
  margin: 8px;
  text-transform: lowercase;
}
</style>