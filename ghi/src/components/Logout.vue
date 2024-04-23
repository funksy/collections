<script setup>
import router from '../router';
import { useUser } from '../store/UserStore'

const userStore = useUser()

userStore.logoutUser()
router.push('/login')
</script>

<template>

</template>
