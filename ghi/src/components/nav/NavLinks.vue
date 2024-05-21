<script setup>
import { storeToRefs } from "pinia";
import NavLink from "./NavLink.vue";
import { useUser } from "../../store/UserStore";

const userStore = useUser();
const { isLoggedIn } = storeToRefs(userStore);
</script>

<template>
  <div class="nav-links">
    <NavLink
      v-if="!isLoggedIn"
      name="Login"
      path="/login"
    />
    <NavLink
      v-if="isLoggedIn"
      name="Main"
      path="/"
    />
    <button
      v-if="isLoggedIn"
      @click="userStore.logoutUser"
      style="margin: 16px"
    >
      Logout
    </button>
  </div>
</template>

<style>
.nav-links {
  align-items: center;
  display: flex;
  flex-direction: row;
}
</style>
