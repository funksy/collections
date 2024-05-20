<script setup>
import { ref, defineModel, onMounted } from "vue";
import { storeToRefs } from "pinia";
import router from "../../router";
import { getCollectionItemCount } from "../../functions/collections";
import { useUser } from "../../store/UserStore";

const userStore = useUser();
const { username, access_token } = storeToRefs(userStore);
const itemCount = ref(0);

const collection = defineModel();

onMounted(async () => {
  itemCount.value = await getCollectionItemCount(
    username.value,
    collection.value.id,
    access_token.value
  );
});
</script>

<template>
  <div class="collection-wrapper">
    <div
      class="collection-data"
      @click="router.push(`/collections/${collection.id}/items`)"
    >
      <h1 class="collection-data-name">{{ collection.name }}</h1>
      <h2 class="collection-data-entries">Entries: {{ itemCount }}</h2>
    </div>
    <button
      class="collection-data-button"
      @click="router.push(`/collections/${collection.id}`)"
    >
      Update/Delete Collection
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
  font-size: small;
  border: 1px solid black;
  border-radius: 4px;
}

.collection-data-button:hover {
  transform: scale(1.01);
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}
</style>
