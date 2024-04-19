<script setup>
import NavLink from './NavLink.vue';
</script>

<template>
  <div className="nav-links self-center flex flex-row">
    <NavLink name="Main" path="/"/>
    <NavLink name="Login" path="login"/>
    <NavLink name="Logout" path="logout"/>
  </div>
</template>