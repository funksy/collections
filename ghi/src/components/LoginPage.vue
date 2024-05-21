<script setup>
import { ref } from "vue";
import { useUser } from "../store/UserStore";
import Toggle from "./common/Toggle.vue";

const userStore = useUser();
const loginUsername = ref(null);
const loginPassword = ref(null);
const signupUsername = ref(null);
const signupPassword = ref(null);
const signupPasswordConf = ref(null);
const errorMessage = ref(null);
const signup = ref(false);

const loginUser = async (e) => {
  e.preventDefault();
  if (loginUsername.value && loginPassword.value) {
    const response = await userStore.loginUser(
      loginUsername.value,
      loginPassword.value
    );
    if (response instanceof Error) {
      errorMessage.value = response.message;
    }
  } else {
    errorMessage.value = "please provide a username and password";
  }
};

const signupUser = async (e) => {
  e.preventDefault();
  if (
    signupUsername.value &&
    signupPassword.value &&
    signupPasswordConf.value &&
    signupPassword.value === signupPasswordConf.value
  ) {
    const response = await userStore.createUser(
      signupUsername.value,
      signupPassword.value
    );
    if (response instanceof Error) {
      errorMessage.value = response.message;
    } else {
      await userStore.loginUser(signupUsername.value, signupPassword.value);
    }
  } else if (signupPassword.value !== signupPasswordConf.value) {
    errorMessage.value = "password and password confirmation do not match";
  } else {
    errorMessage.value = "please fill out all fields";
  }
};
</script>

<template>
  <div class="login-page">
    <div class="login-form-wrapper">
      <Toggle
        class="signup-toggle"
        v-model="signup"
        option_a="Login"
        option_b="Sign Up"
      />
      <form
        v-if="!signup"
        class="login-form"
      >
        <input
          class="login-form-field"
          v-model="loginUsername"
          required
          placeholder="Username"
        />
        <input
          class="login-form-field"
          v-model="loginPassword"
          type="password"
          required
          placeholder="Password"
        />
        <button
          class="login-form-button"
          type="submit"
          @click="loginUser"
        >
          Login
        </button>
      </form>
      <form
        v-if="signup"
        class="login-form"
      >
        <input
          class="login-form-field"
          v-model="signupUsername"
          required
          placeholder="Username"
        />
        <input
          class="login-form-field"
          v-model="signupPassword"
          type="password"
          required
          placeholder="Password"
        />
        <input
          class="login-form-field"
          v-model="signupPasswordConf"
          type="password"
          required
          placeholder="Password Confirmation"
        />
        <button
          class="signup-form-button"
          type="submit"
          @click="signupUser"
        >
          Sign Up
        </button>
      </form>
      <p
        v-if="errorMessage"
        class="error-message"
      >
        {{ errorMessage }}
      </p>
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

.signup-toggle {
  place-self: center;
  margin: 8px;
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

.signup-form-button {
  place-self: center;
  margin: 8px;
  padding: 4px;
  border: 1px solid black;
  border-radius: 4px;
  width: 8rem;
  background: lightgray;
}
</style>
