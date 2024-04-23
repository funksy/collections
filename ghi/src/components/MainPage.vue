<script setup>
import router from '../router';
import { ref, onMounted } from 'vue';
import { useUser } from '../store/UserStore';
import { useCollection } from '../store/CollectionStore';
import { storeToRefs } from 'pinia';

const userStore = useUser()
const collectionStore = useCollection()
const { collections } = storeToRefs(collectionStore)

onMounted(() => {
  collectionStore.getCollections(userStore.token.access_token)
})

if (!userStore.isLoggedIn) {
  router.push('/login')
}
</script>

<template>
  <div className="main-page self-center flex flex-col w-full h-full max-w-6xl border-4 border-red-500">
    <!-- <button @click="collectionStore.getCollections(userStore.token.access_token)">Get Collections</button> -->
    <ul v-if="collections">
      <li v-for="collection in collections">
        {{ collection.name }}
      </li>
    </ul>
  </div>
</template>
