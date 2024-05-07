<script setup>
import { ref, onMounted } from "vue";
import router from "../../router";
import { useUser } from "../../store/UserStore";
import Collection from "./Collection.vue";

const userStore = useUser();
const username = userStore.userData.username;
const token = userStore.token.access_token;
const API = import.meta.env.VITE_API_HOST;

const collections = ref(null);

onMounted(async () => {
  const collectionsUrl = API + `/${username}/collections`;
  const fetchConfig = {
    method: "get",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(collectionsUrl, fetchConfig);
  if (response.ok) {
    const data = await response.json();
    collections.value = data.collections;
  }
});
</script>

<template>
  <div class="collections-page-wrapper">
    <div class="collections">
      <template v-if="collections">
        <div v-for="(_, index) in collections">
          <Collection v-model="collections[index]" />
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
  border: 2px solid green;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}

.new-collection-button:hover {
  transform: scale(1.01);
  box-shadow: 4px 4px 4px 0px rgba(0, 0, 0, 0.25);
}
</style>
