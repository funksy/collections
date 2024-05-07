<script setup>
import { ref } from 'vue';
import { useUser } from '../../store/UserStore';
import CollectionField from './CollectionField.vue'
import router from '../../router';

const userStore = useUser()
const username = userStore.userData.username
const token = userStore.token.access_token
const API = import.meta.env.VITE_API_HOST

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
  } else {
    console.log('no form name')
  }
  let formFields = true
  for (const field of collectionData.value.fields) {
    if (!field.name || !field.data_type) {
      formFields = false
      console.log('something about fields failed')
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
  if (formValidation()) {
    const collectionsUrl = API + `/${username}/collections`
    const body = JSON.stringify(collectionData.value)
    const fetchConfig = {
      method: 'post',
      body: body,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
      }
    }
    const response = await fetch(collectionsUrl, fetchConfig)
    if (response.ok) {
      const data = await response.json()
      router.push(`/collections/${data.id}`)
    }
  } else {
    errorMessage.value = "Please ensure all fields are completed"
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
        <ul class="new-collection-fields" v-for="(_, index) in collectionData.fields">
          <CollectionField
            v-model="collectionData.fields[index]"
            :index="index"
          />
        </ul>
        <button
          type="button"
          class="new-collection-add-field-button"
          @click="addField"
        >
          Add Field
        </button>
        <button
          type="button"
          class="new-collection-remove-field-button"
          @click="removeField"
          v-if="collectionData.fields.length > 1"
        >
          Remove Field
        </button>
        <button
          type="submit"
          class="collection-create-button"
          @click="createCollection"
        >
          Create Collection
        </button>
        <p
          v-if="errorMessage"
          class="error-message"
        >
          {{ errorMessage }}
        </p>
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
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 16px;
}

.new-collection-fields {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
  margin-bottom: 8px;
  padding: 8px;
  border: 1px solid orange;
}

.new-collection-remove-field-button {
  place-self: center;
  width: 6rem;
  margin: 4px;
  padding: 2px;
  border: 1px solid red;
  border-radius: 4px;
  background-color: lightgray;
  font-size: smaller;
  box-shadow: 1px 1px 1px 0px rgba(0, 0, 0, 0.25);
}

.new-collection-remove-field-button:hover {
  transform: scale(1.01);
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}

.new-collection-add-field-button {
  place-self: center;
  width: 6rem;
  margin: 4px;
  padding: 2px;
  border: 1px solid black;
  border-radius: 4px;
  background-color: lightgray;
  font-size: smaller;
  box-shadow: 1px 1px 1px 0px rgba(0, 0, 0, 0.25);
}

.new-collection-add-field-button:hover {
  transform: scale(1.01);
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}

.collection-create-button {
  place-self: center;
  width: 10rem;
  margin-top: 16px;
  padding: 8px;
  border: 2px solid green;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}

.collection-create-button:hover {
  transform: scale(1.01);
  box-shadow: 4px 4px 4px 0px rgba(0, 0, 0, 0.25);
}

.error-message {
  place-self: center;
  color: red;
  font-weight: bold;
  margin: 8px;
  text-transform: lowercase;
}
</style>