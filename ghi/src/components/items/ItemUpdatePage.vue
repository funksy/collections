<script setup>
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { getCollection } from "../../functions/collections";
import { getItem, updateItem } from "../../functions/items";
import { useUser } from "../../store/UserStore";
import ItemField from "./ItemField.vue";
import router from "../../router";

const userStore = useUser();
const { username, access_token } = storeToRefs(userStore);
const route = useRoute();
const collection_id = route.params.collection_id;
const item_id = route.params.item_id;

const itemData = ref(null);
const collectionData = ref(null);
const errorMessage = ref(null);

const formValidation = () => {
  let formName = false;
  if (itemData.value.name) {
    formName = true;
  }
  let formFields = true;
  for (const field of itemData.value.fields) {
    if (!field.val) {
      formFields = false;
    }
  }
  return formName && formFields;
};

const sendUpdate = async (e) => {
  e.preventDefault();
  if (formValidation()) {
    const result = await updateItem(
      username.value,
      collection_id,
      item_id,
      itemData.value,
      access_token.value
    );
    if (result) {
      router.push(`/collections/${collection_id}/items/${item_id}`);
    } else {
      errorMessage.value = "Something went wrong.  Please try again";
    }
  } else {
    errorMessage.value = "Please ensure all fields are completed";
  }
};

const resetItem = async () => {
  itemData.value = await getItem(
    username.value,
    collection_id,
    item_id,
    access_token.value
  );
};

onMounted(async () => {
  itemData.value = await getItem(
    username.value,
    collection_id,
    item_id,
    access_token.value
  );
  collectionData.value = await getCollection(
    username.value,
    collection_id,
    access_token.value
  );
});
</script>

<template>
  <div class="update-item-page">
    <h1 v-if="!itemData || !collectionData">Loading...</h1>
    <div
      class="update-item-form-wrapper"
      v-else
    >
      <h1 class="update-item-header">{{ itemData.name }}</h1>
      <form class="update-item-form">
        <h1 class="update-item-fields-header">Item Fields</h1>
        <ul
          class="update-item-fields"
          v-for="(_, index) in itemData.fields"
        >
          <itemField
            v-model="itemData.fields[index]"
            :fieldDataType="collectionData.fields[index].data_type"
          />
        </ul>
        <button
          type="button"
          class="reset-item-button"
          @click="resetItem"
        >
          Reset Data
        </button>
        <button
          type="submit"
          class="item-update-button"
          @click="sendUpdate"
        >
          Update item
        </button>
        <p
          v-if="errorMessage"
          class="error-message"
        >
          {{ errorMessage }}
        </p>
      </form>
    </div>
  </div>
</template>

<style>
.update-item-page {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.update-item-form-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 24rem;
  border: 4px solid blue;
  margin: 8px;
  padding: 8px;
}

.update-item-header {
  text-align: center;
  font-weight: bold;
  font-size: xx-large;
}

.update-item-form {
  display: flex;
  flex-direction: column;
}

.update-item-name {
  margin: 8px;
  padding: 8px;
  border: 1px solid black;
  border-radius: 4px;
}

.update-item-fields-header {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 16px;
}

.update-item-fields {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
  margin-bottom: 8px;
  padding: 8px;
  border: 1px solid orange;
}

.reset-item-button {
  place-self: center;
  width: 10rem;
  margin-top: 16px;
  padding: 8px;
  border: 2px solid orange;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}

.reset-item-button:hover {
  transform: scale(1.01);
  box-shadow: 4px 4px 4px 0px rgba(0, 0, 0, 0.25);
}

.item-update-button {
  place-self: center;
  width: 10rem;
  margin-top: 16px;
  padding: 8px;
  border: 2px solid green;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}

.item-update-button:hover {
  transform: scale(1.01);
  box-shadow: 4px 4px 4px 0px rgba(0, 0, 0, 0.25);
}

.error-message {
  place-self: center;
  color: red;
  font-weight: bold;
  margin: 8px;
  text-transform: lowercase;
}
</style>
