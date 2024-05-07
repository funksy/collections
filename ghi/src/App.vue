<script setup>
import router from "./router";
import { useUser } from "./store/UserStore";
import NavBar from "./components/nav/NavBar.vue";
import NavTree from "./components/nav/NavTree.vue";

const userStore = useUser();

if (!userStore.isLoggedIn) {
  router.push("/login");
}
</script>

<template>
  <div class="app-wrapper">
    <NavBar />
    <NavTree />
    <RouterView />
  </div>
</template>

<style>
.app-wrapper {
  display: flex;
  flex-direction: column;
  width: 100dvw;
  height: 100dvh;
}
</style>
