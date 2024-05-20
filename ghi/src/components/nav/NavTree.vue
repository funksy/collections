<script setup>
import { ref, computed, watch } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { getCollection } from "../../functions/collections";
import { getItem } from "../../functions/items";
import { useUser } from "../../store/UserStore";
import NavLink from "./NavLink.vue";

const userStore = useUser();
const { username, access_token } = storeToRefs(userStore);
const route = useRoute();
const collection = ref({ name: null, path: null });
const item = ref({ name: null, path: null });

const routeParams = computed(() => {
  return route.params;
});

watch(routeParams, async () => {
  if ("collection_id" in routeParams.value) {
    const collection_id = routeParams.value.collection_id;
    const data = await getCollection(
      username.value,
      collection_id,
      access_token.value
    );
    collection.value = {
      name: data.name,
      path: `/collections/${collection_id}/items`,
    };
  } else {
    collection.value = { name: null, path: null };
  }
  if ("item_id" in routeParams.value) {
    const collection_id = routeParams.value.collection_id;
    const item_id = routeParams.value.item_id;
    const data = await getItem(
      username.value,
      collection_id,
      item_id,
      access_token.value
    );
    item.value = {
      name: data.name,
      path: `/collections/${collection_id}/items/${item_id}`,
    };
  } else {
    item.value = { name: null, path: null };
  }
});
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
  place-self: center;
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
