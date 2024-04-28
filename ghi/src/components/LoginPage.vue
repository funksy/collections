<script setup>
import { ref } from 'vue';
import { useUser } from '../store/UserStore'

const userStore = useUser()
const username = ref(null)
const password = ref(null)
const errorMessage = ref(null)

async function loginUser(e) {
  e.preventDefault()
  if (username.value && password.value) {
    const response = await userStore.loginUser(username.value, password.value)
    if (response instanceof Error) {
      errorMessage.value = response.message
    }
  } else {
    errorMessage.value = "please provide a username and password"
  }
  
}
</script>

<template>
  <div class="login-page">
    <div class="login-form-wrapper">
      <h1 class="login-form-header">Login</h1>
      <form class="login-form">
        <input
          class="login-form-field"
          v-model="username"
          required
          placeholder="Username"
        />
        <input
          class="login-form-field"
          v-model="password"
          type="password"
          required
          placeholder="Password"
        />
        <button
          class="login-form-button"
          type="submit"
          @click="loginUser">
            Login
          </button>
      </form>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<style>
.login-page {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.login-form-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 24rem;
  border: 4px solid blue;
  margin: 5px;
}

.login-form-header {
  text-align: center;
  font-weight: bold;
}

.error-message {
  place-self: center;
  color: red;
  font-weight: bold;
  margin: 8px;
  text-transform: lowercase;
}

.login-form {
  margin: 5px;
  display: flex;
  flex-direction: column;
}

.login-form-field {
  place-self: center;
  margin: 8px;
  padding: 4px;
  border: 1px solid black;
  border-radius: 4px;
}

.login-form-button {
  place-self: center;
  margin: 8px;
  padding: 4px;
  border: 1px solid black;
  border-radius: 4px;
  width: 8rem;
  background: lightgray;
}
</style>