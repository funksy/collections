<script setup>
import Title from './Title.vue';
import NavLinks from './NavLinks.vue';
</script>

<template>
  <nav className="nav-bar self-center flex flex-row flex-0 justify-between w-full h-40 max-w-6xl border-4 border-sky-600">
    <Title/>
    <NavLinks />
  </nav>
</template>