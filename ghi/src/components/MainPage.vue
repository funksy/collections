<script setup>
import router from '../router';
import { useUser } from '../store/UserStore';

const userStore = useUser()

if (!userStore.isLoggedIn) {
  router.push('/login')
}
</script>

<template>
  <div className="main-page self-center flex flex-col w-full h-full max-w-6xl border-4 border-red-500">

  </div>
</template>