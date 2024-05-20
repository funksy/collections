<script setup>
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import router from "../../router";
import { getItems } from "../../functions/items";
import { useUser } from "../../store/UserStore";
import Item from "./Item.vue";

const userStore = useUser();
const { username, access_token } = storeToRefs(userStore);
const route = useRoute();
const collection_id = route.params.collection_id;

const items = ref(null);

onMounted(async () => {
  items.value = await getItems(username, collection_id, access_token);
});
</script>

<template>
  <div class="items-page-wrapper">
    <div class="items">
      <template v-if="items">
        <div v-for="(_, index) in items">
          <Item v-model="items[index]" />
        </div>
      </template>
    </div>
    <button
      class="new-item-button"
      @click="router.push(`/collections/${collection_id}/items/new`)"
    >
      Add Item
    </button>
  </div>
</template>

<style>
.items-page-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.items {
  place-self: center;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
}

.new-item-button {
  place-self: center;
  width: 10rem;
  margin: 16px;
  padding: 8px;
  border: 2px solid green;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
}

.new-item-button:hover {
  transform: scale(1.01);
  box-shadow: 4px 4px 4px 0px rgba(0, 0, 0, 0.25);
}
</style>
