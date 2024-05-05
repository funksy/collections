<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useUser } from '../../store/UserStore';
import ItemField from './ItemField.vue';
import router from '../../router';

const userStore = useUser()
const username = userStore.userData.username
const token = userStore.token.access_token
const API = import.meta.env.VITE_API_HOST
const route = useRoute()
const collection_id = route.params.collection_id
const item_id = route.params.item_id

const itemData = ref({
  name: null,
  fields: [
    {
      name: null,
      val: null
    }
  ]
})
const errorMessage = ref(null)

// const formValidation = () => {
//   let formName = false
//   if (collectionData.value.name) {
//     formName = true
//   }
//   let formFields = true
//   for (const field of collectionData.value.fields) {
//     if (!field.name || !field.data_type) {
//       formFields = false
//     }
//   }
//   return formName && formFields
// }

// const newField = () => {
//   collectionData.value.fields.push({
//     name: null,
//     data_type: null,
//     required: false
//   })
// }
// const removeField = (index) => {
//   collectionData.value.fields.splice(index, 1)
//   if (collectionData.value.fields.length < 1) {
//     newField()
//     minumumCollectionField.value = 'You must have at least 1 field defined'
//   }
// }

// const updateCollection = async (e) => {
//   e.preventDefault()
//   if (formValidation()) {
//     const collectionsUrl = API + `/${username}/collections/${collection_id}`
//     const body = JSON.stringify(collectionData.value)
//     const fetchConfig = {
//       method: 'put',
//       body: body,
//       headers: {
//         'Content-Type': 'application/json',
//         'Authorization': 'Bearer ' + token,
//       }
//     }
//     const response = await fetch(collectionsUrl, fetchConfig)
//     if (response.ok) {
//       // const data = await response.json()
//       router.push(`/collections/${collection_id}`)
//     }
//   } else {
//     errorMessage.value = "Please ensure all fields are completed"
//   }
// }

// const getCollection = async () => {
//   const collectionUrl = API + `/${username}/collections/${collection_id}`
//   const fetchConfig = {
//     method: 'get',
//     headers: {
//         'Content-Type': 'application/json',
//         'Authorization': 'Bearer ' + token,
//     }
//   }
//   const response = await fetch(`${collectionUrl}`, fetchConfig)
//   if (response.ok) {
//       const data = await response.json()
//       collectionData.value = {
//         name: data.name,
//         fields: data.fields
//       }
//   }
// }

// onMounted(async () => {
//   const collectionUrl = API + `/${username}/collections/${collection_id}`
//   const fetchConfig = {
//     method: 'get',
//     headers: {
//         'Content-Type': 'application/json',
//         'Authorization': 'Bearer ' + token,
//     }
//   }
//   const response = await fetch(`${collectionUrl}`, fetchConfig)
//   if (response.ok) {
//       const data = await response.json()
//       collectionData.value = {
//         name: data.name,
//         fields: data.fields
//       }
//   }
// })
</script>

<template>
  <div class="update-collection-page">
    <h1 v-if="!collectionData">Loading...</h1>
    <div class="update-collection-form-wrapper" v-else>
      <h1 class="update-collection-header">New Collection</h1>
      <form class="update-collection-form">
        <input
          class="update-collection-name"
          v-model="collectionData.name"
          placeholder="Collection Name"
          required
        />
        <h1 class="update-collection-fields-header">Collection Fields</h1>
        <p class="error-message" v-if="minumumCollectionField">{{ minumumCollectionField }}</p>
        <ul class="update-collection-fields" v-for="(field, index) in collectionData.fields">
          <CollectionField
            v-model="collectionData.fields[index]"
            :index="index"
          />
          <button
            type="button"
            class="remove-field-button"
            @click="removeField(index)"
          >
            Remove Field
          </button>
        </ul>
        <button
          type="button"
          class="add-field-button"
          @click="newField"
        >
          Add New Field
        </button>
        <button
          type="button"
          class="reset-fields-button"
          @click="getCollection"
        >
          Reset Fields
        </button>
        <button
          type="submit"
          class="collection-update-button"
          @click="updateCollection"
        >
          Update Collection
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
.update-collection-page {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.update-collection-form-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 24rem;
  border: 4px solid blue;
  margin: 8px;
  padding: 8px;
}

.update-collection-header {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 8px;
}

.update-collection-form {
  margin: 8px;
  display: flex;
  flex-direction: column;
}

.update-collection-name {
  margin: 8px;
  padding: 8px;
  border: 1px solid black;
  border-radius: 4px;
}

.update-collection-fields-header {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 16px;
}

.update-collection-fields {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
  margin-bottom: 8px;
  padding: 8px;
  border: 1px solid orange;
}

.remove-field-button {
  place-self: center;
  width: 6rem;
  margin: 4px;
  padding: 2px;
  border: 2px solid red;
  border-radius: 4px;
  background-color: lightgray;
  font-size: smaller;
}

.add-field-button {
  place-self: center;
  width: 6rem;
  margin: 4px;
  padding: 2px;
  border: 1px solid black;
  border-radius: 4px;
  background-color: lightgray;
  font-size: smaller;
}

.reset-fields-button {
  place-self: center;
  width: 10rem;
  margin-top: 16px;
  padding: 8px;
  border: 2px solid orange;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
}

.collection-update-button {
  place-self: center;
  width: 10rem;
  margin-top: 16px;
  padding: 8px;
  border: 2px solid green;
  border-radius: 4px;
  background-color: lightgray;
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