<script setup>
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import router from "../../router";
import { getCollections } from "../../functions/collections";
import { useUser } from "../../store/UserStore";
import Collection from "./Collection.vue";

const userStore = useUser();
const { username, access_token } = storeToRefs(userStore);

const collections = ref(null);

onMounted(async () => {
  collections.value = await getCollections(username.value, access_token.value);
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
