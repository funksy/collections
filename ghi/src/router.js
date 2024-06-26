import { createWebHistory, createRouter } from "vue-router";

import LoginPage from "./components/LoginPage.vue";

import CollectionsPage from "./components/collections/CollectionsPage.vue";
import CollectionDetailsPage from "./components/collections/CollectionDetailsPage.vue";
import NewCollectionPage from "./components/collections/NewCollectionPage.vue";
import CollectionUpdatePage from "./components/collections/CollectionUpdatePage.vue";

import ItemsPage from "./components/items/ItemsPage.vue";
import ItemDetailsPage from "./components/items/ItemDetailsPage.vue";
import NewItemPage from "./components/items/NewItemPage.vue";
import ItemUpdatePage from "./components/items/ItemUpdatePage.vue";

const routes = [
  { path: "/login", component: LoginPage },

  { path: "/", component: CollectionsPage },
  { path: "/collections/:collection_id", component: CollectionDetailsPage },
  { path: "/collections/new", component: NewCollectionPage },
  {
    path: "/collections/:collection_id/update",
    component: CollectionUpdatePage,
  },

  { path: "/collections/:collection_id/items", component: ItemsPage },
  {
    path: "/collections/:collection_id/items/:item_id",
    component: ItemDetailsPage,
  },
  { path: "/collections/:collection_id/items/new", component: NewItemPage },
  {
    path: "/collections/:collection_id/items/:item_id/update",
    component: ItemUpdatePage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
