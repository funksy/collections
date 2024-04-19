<script setup>
import router from './router';
import { watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useUser } from './store/UserStore'
import NavBar from './components/nav/NavBar.vue'

const userStore = useUser()
const { isLoggedIn } = storeToRefs(userStore)

watch(isLoggedIn, () => {
  if (isLoggedIn.value) {
    router.push('/')
  } else {
    router.push('/login')
  }
})

</script>

<template>
  <div className="flex flex-col w-dvh h-dvh bg-slate-200">
    <NavBar />
    <p>
      <strong>Current route path:</strong> {{ $route.fullPath }}
    </p>
    <RouterView />
  </div>
</template>./components/MainPage.vue