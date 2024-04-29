<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import router from '../../router';
import { useUser } from '../../store/UserStore';

const route = useRoute()
const collection_id = route.params.collection_id
const userStore = useUser()
const collection = ref(null)
const errorMessage = ref(null)

onMounted(async () => {
  const collectionUrl = import.meta.env.VITE_API_HOST + `/collections/${userStore.userData.username}/${collection_id}`
  const fetchConfig = {
    method: 'get',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + userStore.token.access_token,
    }
  }
  const response = await fetch(collectionUrl, fetchConfig)
  if (response.ok) {
    const data = await response.json()
    collection.value = data
  }
})

const deleteCollection = async () => {
  const collectionsUrl = import.meta.env.VITE_API_HOST + `/collections/${userStore.userData.username}/${collection_id}`
  const fetchConfig = {
    method: 'delete',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + userStore.token.access_token,
    }
  }
  const response = await fetch(collectionsUrl, fetchConfig)
  if (response.ok) {
    router.push('/')
  } else {
    const data = await response.json()
    errorMessage.value = data.detail
  }
}
</script>

<template>
  <template v-if="collection">
    <div class="collection-details-page">
      <div class="collection-details-wrapper">
        <div class="collection-details-name">
          <h1>{{ collection.name }}</h1>
        </div>
        <div
          class="collection-details-fields"
          v-for="field in collection.fields"
        >
          <h2 class="collection-details-field-name">{{ field.name }}</h2>
          <ul>
            <li class="collections-details-field-details">Data Type: {{ field.data_type }}</li>
            <li class="collections-details-field-details">Required: {{ field.required }}</li>
          </ul>
        </div>
      </div>
      <button
        class="collection-delete-button"
        @click="deleteCollection"
      >
        Delete Collection
      </button>
      <p
        class="error-message"
        v-if="errorMessage"
      >
        Error: {{ errorMessage }}
      </p>
    </div>
  </template>
</template>

<style>
.collection-details-page {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.collection-details-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 24rem;
  border: 4px solid blue;
  margin: 8px;
  padding: 8px;
}

.collection-details-name {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 8px;
}

.collection-details-fields {
  display: flex;
  flex-direction: column;
  border: 2px solid orange;
  border-radius: 4px;
  margin:16px;
  padding: 8px;
}

.collection-details-field-name {
  place-self: center;
  font-weight: bold;
  margin: 8px;
}

.collections-details-field-details {
  margin: 8px;
}

.collection-delete-button {
  place-self: center;
  width: 10rem;
  margin: 16px;
  padding: 8px;
  border: 1px solid black;
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