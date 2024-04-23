<script setup>
defineProps(['collection'])
</script>

<template>
  <div className="nav-link m-4">
    <RouterLink v-bind:to="path">{{ name }}</RouterLink>
  </div>
</template>