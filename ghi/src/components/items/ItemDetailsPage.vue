<script setup>
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { deleteItem, getItem } from "../../functions/items";
import router from "../../router";
import { useUser } from "../../store/UserStore";

const userStore = useUser();
const { username, access_token } = storeToRefs(userStore);
const route = useRoute();
const collection_id = route.params.collection_id;
const item_id = route.params.item_id;

const item = ref(null);
const errorMessage = ref(null);

onMounted(async () => {
  item.value = await getItem(
    username.value,
    collection_id,
    item_id,
    access_token.value
  );
});

const requestDelete = async () => {
  const response = await deleteItem(
    username.value,
    collection_id,
    item_id,
    access_token.value
  );
  if (response.result) {
    router.push(`/collections/${collection_id}/items`);
  } else {
    errorMessage.value = response.error;
  }
};
</script>

<template>
  <template v-if="item">
    <div class="item-details-page">
      <div class="item-details-wrapper">
        <div class="item-details-name">
          <h1>{{ item.name }}</h1>
        </div>
        <div class="item-details-actions">
          <button
            class="item-details-update-button"
            @click="
              router.push(
                `/collections/${collection_id}/items/${item_id}/update`
              )
            "
          >
            Update Item
          </button>
          <button
            class="item-details-delete-button"
            @click="requestDelete"
          >
            Delete Item
          </button>
        </div>
        <div
          class="item-details-fields"
          v-for="field in item.fields"
        >
          <div class="item-details-field-wrapper">
            <h2 class="item-details-field-name">
              {{ field.name }}:
              <span class="item-details-field-value">{{ field.val }}</span>
            </h2>
          </div>
        </div>
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
.item-details-page {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.item-details-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 24rem;
  border: 4px solid blue;
  margin: 8px;
  padding: 8px;
}

.item-details-name {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 8px;
  text-transform: uppercase;
}

.item-details-fields {
  display: flex;
  flex-direction: column;
  border: 2px solid orange;
  border-radius: 4px;
  margin: 16px;
  padding: 8px;
}

.item-details-field-wrapper {
  display: inline;
}
.item-details-field-name {
  margin: 8px;
  font-weight: bold;
  text-transform: uppercase;
}

.item-details-field-value {
  margin: 8px;
  font-weight: 400;
  text-transform: capitalize;
}

.item-details-actions {
  display: flex;
  flex-direction: row;
  place-self: center;
}

.item-details-update-button {
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

.item-details-update-button:hover {
  transform: scale(1.01);
  box-shadow: 4px 4px 4px 0px rgba(0, 0, 0, 0.25);
}

.item-details-delete-button {
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

.item-details-delete-button:hover {
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
