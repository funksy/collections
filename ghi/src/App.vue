<script setup>
import router from "./router";
import Cookies from "js-cookie";
import { useUser } from "./store/UserStore";
import NavBar from "./components/nav/NavBar.vue";
import NavTree from "./components/nav/NavTree.vue";

const userStore = useUser();
const cookies = Cookies.get("access_token");

if (!cookies) {
  router.push("/login");
} else {
  userStore.loginUserWithToken();
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
