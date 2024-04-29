<script setup>
import router from '../../router';
import { ref, onMounted } from 'vue';
import { useUser } from '../../store/UserStore';
import Collection from './Collection.vue';

const collections = ref(null)
const userStore = useUser()
const deletedCollection = ref('test')


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
  <div class="collections-page-wrapper">
    <div class="collections">
      <template v-if="collections">
        <div v-for="collection in collections">
          <Collection
            :collection="collection"
          />
        </div>
      </template>
    </div>
    <button
      class="new-collection-button"
      @click="router.push('/collections/new')"
    >
      Create Collection
    </button>
  </div>
</template>

<style>
.collections-page-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.collections {
  place-self: center;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
}

.new-collection-button {
  place-self: center;
  width: 10rem;
  margin: 16px;
  padding: 8px;
  border: 1px solid black;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
}
</style>