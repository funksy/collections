<script setup>
import Title from "./Title.vue";
import NavLinks from "./NavLinks.vue";
</script>

<template>
  <nav class="nav-bar">
    <Title />
    <NavLinks />
  </nav>
</template>

<style>
.nav-bar {
  place-self: center;
  display: flex;
  flex-direction: row;
  flex: none;
  justify-content: space-between;
  width: 100%;
  height: 10rem;
  max-width: 72rem;
  border: 4px solid skyblue;
}
</style>
