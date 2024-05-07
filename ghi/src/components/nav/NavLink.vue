<script setup>
defineProps(["name", "path"]);
</script>

<template>
  <div class="nav-link">
    <RouterLink v-bind:to="path">{{ name }}</RouterLink>
  </div>
</template>

<style>
.nav-link {
  margin: 16px;
}
</style>
