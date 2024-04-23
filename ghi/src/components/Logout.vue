<script setup>
import router from '../router';
import { useCollection } from '../store/CollectionStore';
import { useUser } from '../store/UserStore'

const collectionStore = useCollection()
const userStore = useUser()

collectionStore.$reset()
userStore.$reset()
router.push('/login')
</script>

<template>

</template>
