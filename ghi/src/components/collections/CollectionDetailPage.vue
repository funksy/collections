<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useUser } from '../../store/UserStore';

const route = useRoute()
const collection_id = route.params.collection_id
const userStore = useUser()
const collection = ref(null)

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
</script>

<template>
  <div v-if="collection">
    <h1>{{ collection.name }}</h1>
    <ul>
      <li v-for="field in collection.fields">
        <ul>
          <li>{{ field.name }}</li>
          <li>{{ field.data_type }}</li>
          <li>{{ field.required }}</li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<style>

</style>