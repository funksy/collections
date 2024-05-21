<script setup>
const props = defineProps(["option_a", "option_b"]);
const toggleProp = defineModel();

const toggle = () => {
  toggleProp.value = !toggleProp.value;
};
</script>

<template>
  <label class="switch">
    <input
      type="checkbox"
      @click="toggle"
    />
    <span class="slider"></span>
    <div class="login-option">{{ props.option_a }}</div>
    <div class="signup-option">{{ props.option_b }}</div>
  </label>
</template>

<style>
/* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  cursor: pointer;
  width: 180px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: blue;
  -webkit-transition: 0.4s;
  transition: 0.4s;
  opacity: 60%;
  border-radius: 8px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 86px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 4px;
}

.login-option {
  position: absolute;
  width: 90px;
  top: 4px;
  left: 0px;
  text-align: center;
  font-weight: bold;
}

.signup-option {
  position: absolute;
  width: 90px;
  top: 4px;
  right: 0px;
  text-align: center;
  font-weight: bold;
}

input:checked + .slider {
  background-color: red;
  opacity: 60%;
}

input:focus + .slider {
  box-shadow: 0 0 1px blue;
}

input:checked + .slider:before {
  -webkit-transform: translateX(86px);
  -ms-transform: translateX(86px);
  transform: translateX(86px);
}
</style>
