<script setup>
import router from '../../router';
const props = defineProps(['collection'])
</script>

<template>
  <div class="collection-wrapper" @click="router.push(`/collections/${props.collection.id}`)">
    <h1 class="collection-name">{{ props.collection.name }}</h1>
    <h2>Fields: {{ props.collection.fields.length }}</h2>
  </div>
</template>

<style>
.collection-wrapper {
  margin: 20px;
  padding: 10px;  
  border: 2px solid orange;
  width: 12rem;
}

.collection-name {
  text-transform: uppercase;
  font-weight: bold;
}
</style>