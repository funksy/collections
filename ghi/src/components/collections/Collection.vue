<script setup>
import { ref, defineModel, onMounted } from 'vue';
import router from '../../router';
import { useUser } from '../../store/UserStore';
import { useRoute } from 'vue-router';

const userStore = useUser()
const username = userStore.userData.username
const token = userStore.token.access_token
const API = import.meta.env.VITE_API_HOST
const itemCount = ref(0)

const collection = defineModel()

onMounted(async () => {
  const itemsUrl = API + `/${username}/collections/${collection.value.id}/items/count`
  const fetchConfig = {
    method: 'get',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token,
    }
  }
  const response = await fetch(itemsUrl, fetchConfig)
  if (response.ok) {
      const data = await response.json()
      itemCount.value = data.count
  }
})
</script>

<template>
  <div class="collection-wrapper">
    <div class="collection-data" @click="router.push(`/collections/${collection.id}/items`)">
      <h1 class="collection-data-name">{{ collection.name }}</h1>
      <h2 class="collection-data-entries">Entries: {{ itemCount }}</h2>
    </div>
    <button
      class="collection-data-button"
      @click="router.push(`/collections/${collection.id}`)"
    >
      View/Update Collection Structure
    </button>
  </div>
</template>

<style>
.collection-wrapper {
  display: flex;
  flex-direction: column;
  margin: 20px;  
  width: 12rem;
}

.collection-data {
  display: flex;
  flex-direction: column;
  padding: 8px;
  width: 100%;
  height: 6rem;
  border: 2px solid orange;
  border-radius: 4px;
  cursor: pointer;
}

.collection-data:hover {
  transform: scale(1.01);
  box-shadow: 4px 4px 4px 0px rgba(0, 0, 0, 0.25);
}

.collection-data-name {
  margin-bottom: 28px;
  font-size: large;
  text-align: center;
  text-transform: uppercase;
  font-weight: bold;
}

.collection-data-entries {
  font-size: small;
}

.collection-data-button {
  place-self: center;
  width: 10rem;
  margin-top: 16px;
  padding: 2px;
  background-color: lightgray;
  font-size: x-small;
  border: 1px solid black;
  border-radius: 4px;
}

.collection-data-button:hover {
  transform: scale(1.01);
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}
</style>