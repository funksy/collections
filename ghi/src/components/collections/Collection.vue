<script setup>
import { defineModel } from 'vue';
import router from '../../router';

const collection = defineModel()
</script>

<template>
  <div class="collection-wrapper" @click="router.push(`/collections/${collection.id}`)">
    <h1 class="collection-name">{{ collection.name }}</h1>
    <h2>Fields: {{ collection.fields.length }}</h2>
  </div>
</template>

<style>
.collection-wrapper {
  margin: 20px;
  padding: 10px;  
  border: 2px solid orange;
  border-radius: 4px;
  width: 12rem;
  cursor: pointer;
}

.collection-wrapper:hover {
  transform: scale(1.01);
  box-shadow: 5px 5px 5px 0px rgba(0, 0, 0, 0.25);
}

.collection-name {
  text-transform: uppercase;
  font-weight: bold;
}
</style>