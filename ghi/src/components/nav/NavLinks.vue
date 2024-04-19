<script setup>
import NavLink from './NavLink.vue';
</script>

<template>
  <div className="nav-links self-center flex flex-row">
    <NavLink name="Collections" path="/collections"/>
    <NavLink name="Items" path="/items"/>
    <NavLink name="Users" path="/users"/>
  </div>
</template>