<script setup>
import { ref } from 'vue';
import { useUser } from '../store/UserStore'

const userStore = useUser()
const username = ref('')
const password = ref('')
const errorMessage = ref('')

function loginUser(e) {
  e.preventDefault()
  userStore.loginUser(username.value, password.value)
}
</script>

<template>
  <div className="login-page self-center flex flex-col w-full h-full max-w-6xl border-4 border-red-500">
    <div className="login-form self-center flex flex-col w-96 border-4 border-blue-800">
      <h1 className="text-center">Login</h1>
      <p v-if="errorMessage" className="text-red-500 font-bold">{{ errorMessage }}</p>
      <form>
        <div>
          <input
            v-model="username"
            placeholder="Username"
          />
        </div>
        <div>
          <input
            v-model="password"
            type="password"
            required
            placeholder="Password"
          />
        </div>
        <button @click="loginUser">Login</button>
      </form>
    </div>
  </div>
</template>
