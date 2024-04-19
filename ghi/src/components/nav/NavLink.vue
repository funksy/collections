<script setup>
defineProps(['name', 'path'])
</script>

<template>
  <div className="nav-link m-4">
    <span>{{ name }}</span>
  </div>
</template>