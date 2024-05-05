<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import router from '../../router';
import { useUser } from '../../store/UserStore';
import ItemField from './ItemField.vue'


const userStore = useUser()
const username = userStore.userData.username
const token = userStore.token.access_token
const API = import.meta.env.VITE_API_HOST
const route = useRoute()
const collection_id = route.params.collection_id

const itemData = ref({
  name: null,
  fields: []
})
const collection = ref(null)
const errorMessage = ref(null)

onMounted(async () => {
  const collectionUrl = API + `/${username}/collections/${collection_id}`
  const fetchConfig = {
    method: 'get',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token,
    }
  }
  const response = await fetch(collectionUrl, fetchConfig)
  if (response.ok) {
    const data = await response.json()
    collection.value = data
    for (const collectionField of collection.value.fields) {
      const formattedField = {
        name: collectionField.name,
        val: null
      }
      itemData.value.fields.push(formattedField)
    }
  }
})


// const formValidation = () => {
//   let formName = false
//   if (collectionData.value.name) {
//     formName = true
//   } else {
//     console.log('no form name')
//   }
//   let formFields = true
//   for (const field of collectionData.value.fields) {
//     if (!field.name || !field.data_type) {
//       formFields = false
//       console.log('something about fields failed')
//     }
//   }
//   return formName && formFields
// }

const createItem = async (e) => {
  e.preventDefault()
  if (
    // formValidation()
    true
  ) {
    const itemsUrl = API + `/${username}/collections/${collection_id}/items`
    const body = JSON.stringify(itemData.value)
    const fetchConfig = {
      method: 'post',
      body: body,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
      }
    }
    const response = await fetch(itemsUrl, fetchConfig)
    if (response.ok) {
      const data = await response.json()
      router.push(`/collections/${collection_id}/items/${data.id}`)
    }
  } else {
    errorMessage.value = "Please ensure all fields are completed"
  }
}
</script>

<template>
  <div class="new-item-page">
    <div class="new-item-form-wrapper">
      <h1 class="new-item-header">New Item</h1>
      <form class="new-item-form">
        <input
          class="new-item-name"
          v-model="itemData.name"
          placeholder="Item Name"
          required
        />
        <h1 class="new-item-fields-header">Item Fields</h1>
        <ul class="new-item-fields" v-if="collection" v-for="(_, index) in collection.fields">
          <ItemField
            :fieldDataType="collection.fields[index].data_type"
            v-model="itemData.fields[index]"
          />
        </ul>
        <button
          type="submit"
          class="item-create-button"
          @click="createItem"
        >
          Create Item
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
.new-item-page {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.new-item-form-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 24rem;
  border: 4px solid blue;
  margin: 8px;
  padding: 8px;
}

.new-item-header {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 8px;
}

.new-item-form {
  margin: 8px;
  display: flex;
  flex-direction: column;
}

.new-item-name {
  margin: 8px;
  padding: 8px;
  border: 1px solid black;
  border-radius: 4px;
}

.new-item-fields-header {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 16px;
}

.new-item-fields {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
  margin-bottom: 8px;
  padding: 8px;
  border: 1px solid orange;
}

.item-create-button {
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