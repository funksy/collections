<script setup>
import { defineProps, defineModel } from "vue";
import { useRoute } from "vue-router";
import router from "../../router";

const item = defineModel();
const route = useRoute();
const collection_id = route.params.collection_id;
</script>

<template>
  <div
    class="item-wrapper"
    @click="router.push(`/collections/${collection_id}/items/${item.id}`)"
  >
    <h1 class="item-name">{{ item.name }}</h1>
    <h2>Fields: {{ item.fields.length }}</h2>
  </div>
</template>

<style>
.item-wrapper {
  margin: 20px;
  padding: 10px;
  border: 2px solid orange;
  border-radius: 4px;
  width: 12rem;
  cursor: pointer;
}

.item-wrapper:hover {
  transform: scale(1.01);
  box-shadow: 5px 5px 5px 0px rgba(0, 0, 0, 0.25);
}

.item-name {
  text-transform: uppercase;
  font-weight: bold;
}
</style>
