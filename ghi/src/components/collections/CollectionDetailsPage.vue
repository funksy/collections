<script setup>
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import router from "../../router";
import { getCollection, deleteCollection } from "../../functions/collections";
import { useUser } from "../../store/UserStore";

const userStore = useUser();
const { username, access_token } = storeToRefs(userStore);
const route = useRoute();
const collection_id = route.params.collection_id;

const collection = ref(null);
const errorMessage = ref(null);

onMounted(async () => {
  collection.value = await getCollection(
    username.value,
    collection_id,
    access_token.value
  );
});

const requestDelete = async () => {
  const response = await deleteCollection(
    username.value,
    collection_id,
    access_token.value
  );
  if (response.result) {
    router.push("/");
  } else {
    errorMessage.value = response.error;
  }
};
</script>

<template>
  <template v-if="collection">
    <div class="collection-details-page">
      <div class="collection-details-wrapper">
        <div class="collection-details-name">
          <h1>{{ collection.name }}</h1>
        </div>
        <div class="collection-details-actions">
          <button
            class="collection-details-update-button"
            @click="router.push(`/collections/${collection_id}/update`)"
          >
            Change Structure
          </button>
          <button
            class="collection-details-delete-button"
            @click="requestDelete"
          >
            Delete Collection
          </button>
        </div>
        <div
          class="collection-details-fields"
          v-for="field in collection.fields"
        >
          <h2 class="collection-details-field-name">{{ field.name }}</h2>
          <ul>
            <li class="collection-details-field-details">
              Data Type: {{ field.data_type }}
            </li>
            <li class="collection-details-field-details">
              Required: {{ field.required }}
            </li>
          </ul>
        </div>
        <button
          class="collection-items-button"
          @click="router.push(`/collections/${collection_id}/items`)"
        >
          View Items
        </button>
      </div>
      <p
        class="error-message"
        v-if="errorMessage"
      >
        Error: {{ errorMessage }}
      </p>
    </div>
  </template>
</template>

<style>
.collection-details-page {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.collection-details-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 24rem;
  border: 4px solid blue;
  margin: 8px;
  padding: 8px;
}

.collection-details-name {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 8px;
}

.collection-details-fields {
  display: flex;
  flex-direction: column;
  border: 2px solid orange;
  border-radius: 4px;
  margin: 16px;
  padding: 8px;
}

.collection-details-field-name {
  place-self: center;
  font-weight: bold;
  margin: 8px;
}

.collection-details-field-details {
  margin: 8px;
}

.collection-details-actions {
  display: flex;
  flex-direction: row;
  place-self: center;
}

.collection-details-update-button {
  place-self: center;
  width: 10rem;
  margin: 16px;
  padding: 8px;
  border: 1px solid green;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}

.collection-details-delete-button {
  place-self: center;
  width: 10rem;
  margin: 16px;
  padding: 8px;
  border: 1px solid red;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}

.collection-items-button {
  place-self: center;
  width: 10rem;
  margin: 16px;
  padding: 8px;
  border: 1px solid orange;
  border-radius: 4px;
  background-color: lightgray;
  font-weight: bold;
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
}

.collection-details-update-button:hover {
  transform: scale(1.01);
  box-shadow: 4px 4px 4px 0px rgba(0, 0, 0, 0.25);
}

.collection-details-delete-button:hover {
  transform: scale(1.01);
  box-shadow: 4px 4px 4px 0px rgba(0, 0, 0, 0.25);
}

.collection-items-button:hover {
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
