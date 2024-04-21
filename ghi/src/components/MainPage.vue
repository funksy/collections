<script setup>
import router from '../router';
import { ref } from 'vue';
import { useUser } from '../store/UserStore';
import { useCollection } from '../store/CollectionStore';

const userStore = useUser()
const collectionStore = useCollection()

if (!userStore.isLoggedIn) {
  router.push('/login')
}
</script>

<template>
  <div className="main-page self-center flex flex-col w-full h-full max-w-6xl border-4 border-red-500">
    <button @click="collectionStore.getCollections(userStore.token.access_token)">Get Collections</button>
    <ul v-if="collectionStore.collections">
      <li v-for="collection in collectionStore.collections">
        {{ collection.name }}
      </li>
    </ul>
  </div>
</template>
