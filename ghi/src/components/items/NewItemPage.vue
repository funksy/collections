<script setup>
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import router from "../../router";
import { getCollection } from "../../functions/collections";
import { createItem } from "../../functions/items";
import { useUser } from "../../store/UserStore";
import ItemField from "./ItemField.vue";

const userStore = useUser();
const { username, access_token } = storeToRefs(userStore);
const route = useRoute();
const collection_id = route.params.collection_id;

const itemData = ref({
  name: null,
  fields: [],
});
const collection = ref(null);
const errorMessage = ref(null);

onMounted(async () => {
  collection.value = await getCollection(
    username.value,
    collection_id,
    access_token.value
  );
  for (const collectionField of collection.value.fields) {
    const formattedField = {
      name: collectionField.name,
      val: null,
    };
    itemData.value.fields.push(formattedField);
  }
});

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

const submitItem = async (e) => {
  e.preventDefault();
  if (formValidation()) {
    const response = await createItem(
      username.value,
      collection_id,
      itemData.value,
      access_token.value
    );
    if (response.status) {
      router.push(`/collections/${collection_id}/items/${response.item_id}`);
    } else {
      errorMessage.value = "Something went wrong.  Please try again";
    }
  } else {
    errorMessage.value = "Please ensure all fields are completed";
  }
};
</script>

<template>
  <div class="new-item-page">
    <div class="new-item-form-wrapper">
      <h1 class="new-item-header">New Item</h1>
      <form class="new-item-form">
        <input
          class="new-item-name"
          v-model="itemData.name"
          placeholder="Item Name"
          required
        />
        <h1 class="new-item-fields-header">Item Fields</h1>
        <ul
          class="new-item-fields"
          v-if="collection"
          v-for="(_, index) in collection.fields"
        >
          <ItemField
            :fieldDataType="collection.fields[index].data_type"
            v-model="itemData.fields[index]"
          />
        </ul>
        <button
          type="submit"
          class="item-create-button"
          @click="submitItem"
        >
          Create Item
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
.new-item-page {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 72rem;
  border: 4px solid red;
}

.new-item-form-wrapper {
  place-self: center;
  display: flex;
  flex-direction: column;
  width: 24rem;
  border: 4px solid blue;
  margin: 8px;
  padding: 8px;
}

.new-item-header {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 8px;
}

.new-item-form {
  margin: 8px;
  display: flex;
  flex-direction: column;
}

.new-item-name {
  margin: 8px;
  padding: 8px;
  border: 1px solid black;
  border-radius: 4px;
}

.new-item-fields-header {
  text-align: center;
  font-weight: bold;
  font-size: larger;
  margin: 16px;
}

.new-item-fields {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
  margin-bottom: 8px;
  padding: 8px;
  border: 1px solid orange;
}

.item-create-button {
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

.item-create-button:hover {
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
