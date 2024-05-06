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
  <div class="collection-wrapper" @click="router.push(`/collections/${collection.id}`)">
    <h1 class="collection-name">{{ collection.name }}</h1>
    <h2>Entries: {{ itemCount }}</h2>
  </div>
</template>

<style>
.collection-wrapper {
  margin: 20px;
  padding: 10px;  
  border: 2px solid orange;
  border-radius: 4px;
  width: 12rem;
  cursor: pointer;
}

.collection-wrapper:hover {
  transform: scale(1.01);
  box-shadow: 5px 5px 5px 0px rgba(0, 0, 0, 0.25);
}

.collection-name {
  text-transform: uppercase;
  font-weight: bold;
}
</style>