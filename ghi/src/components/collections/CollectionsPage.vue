<script setup>
import router from '../../router';
import { ref, onMounted } from 'vue';
import { useUser } from '../../store/UserStore';
import Collection from './Collection.vue';

const userStore = useUser()
const collections = ref(null)

onMounted(async () => {
  const collectionsUrl = import.meta.env.VITE_API_HOST + '/collections'
  const fetchConfig = {
    method: 'get',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + userStore.token.access_token,
    }
  }
  const response = await fetch(`${collectionsUrl}/me`, fetchConfig)
  if (response.ok) {
      const data = await response.json()
      collections.value = data.collections
  }
})
</script>

<template>
  <div class="collections-page">
    <div v-if="collections" v-for="collection in collections">
      <Collection :collection="collection"/>
    </div>
  </div>
  <button @click="router.push('/collections/new')">Add New Collection</button>
</template>

<style>
.collections-page {
  place-self: center;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}
</style>