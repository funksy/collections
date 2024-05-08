<script setup>
import { ref, computed, watch } from "vue";
import { useRoute } from "vue-router";
import { useUser } from "../../store/UserStore";
import NavLink from "./NavLink.vue";

const userStore = useUser();
const username = userStore.userData.username;
const token = userStore.token.access_token;
const API = import.meta.env.VITE_API_HOST;
const route = useRoute();
const collection = ref({ name: null, path: null });
const item = ref({ name: null, path: null });

const routeParams = computed(() => {
  return route.params;
});

watch(routeParams, async () => {
  if ("collection_id" in routeParams.value) {
    getCollection(routeParams.value.collection_id);
  } else {
    collection.value = { name: null, path: null };
  }
  if ("item_id" in routeParams.value) {
    getItem(routeParams.value.item_id, routeParams.value.collection_id);
  } else {
    item.value = { name: null, path: null };
  }
});

const getCollection = async (collection_id) => {
  const collectionUrl = API + `/${username}/collections/${collection_id}`;
  const fetchConfig = {
    method: "get",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(collectionUrl, fetchConfig);
  if (response.ok) {
    const data = await response.json();
    collection.value = {
      name: data.name,
      path: `/collections/${collection_id}/items`,
    };
  }
};

const getItem = async (item_id, collection_id) => {
  const itemUrl =
    API + `/${username}/collections/${collection_id}/items/${item_id}`;
  const fetchConfig = {
    method: "get",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(itemUrl, fetchConfig);
  if (response.ok) {
    const data = await response.json();
    item.value = {
      name: data.name,
      path: `/collections/${collection_id}/items/${item_id}`,
    };
  }
};
</script>

<template>
  <div class="nav-tree">
    <div>
      <NavLink
        class="nav-tree-link"
        name="My Collections"
        path="/"
      />
    </div>
    <div v-if="collection.name">
      <NavLink
        class="nav-tree-link"
        :name="collection.name"
        :path="collection.path"
      />
    </div>
    <div v-if="item.name">
      <NavLink
        class="nav-tree-link"
        :name="item.name"
        :path="item.path"
      />
    </div>
  </div>
</template>

<style>
.nav-tree {
  display: flex;
  flex-direction: row;
  width: 100%;
  max-width: 72rem;
}

.nav-tree-link {
  font-weight: bold;
  text-transform: uppercase;
  text-decoration: underline;
}
</style>
