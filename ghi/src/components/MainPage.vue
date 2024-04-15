<script setup>
  import Title from './Title.vue'
  import CollectionGrid from './CollectionGrid.vue'
  import NewCollection from './NewCollection.vue'

</script>

<template>
  <div className="main-page flex flex-col w-full h-full bg-red-300">
    <Title/>
    <NewCollection />
    <!-- <CollectionGrid /> -->
  </div>
</template>