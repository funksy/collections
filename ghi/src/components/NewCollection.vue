<script setup>
import { ref } from 'vue';

const count = ref(0);
const types = ['text', 'number', 'boolean']

function increment() {
  count.value++
}

function decrement() {
  count.value--
}

function reset() {
  count.value = 0
}
</script>

<template>
  <div>
    <h1>New Collection</h1>
    <form>
      <ul className="list-image-none">
        <li>
          <input id="name"/>
          <label htmlFor="name"> Collection Name</label>
        </li>
        <li v-for="item in count">
          <input id="field-label"/>
          <label htmlFor="field-label">Field label</label>          
          <input id="field-type"/>
          <label htmlFor="field-type">Field type</label>
        </li>
      </ul>
    </form>
    <button @click="increment">
      Add a Field
    </button>
    <button @click="decrement">
      Remove a Field
    </button>
    <button @click="reset">
      Reset
    </button>
  </div>
</template>

