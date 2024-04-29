import { createWebHistory, createRouter } from "vue-router"

import LoginPage from "./components/LoginPage.vue"
import LogoutPage from "./components/LogoutPage.vue"
import CollectionsPage from "./components/collections/CollectionsPage.vue"
import NewCollectionPage from "./components/collections/NewCollectionPage.vue"
import CollectionDetailsPage from "./components/collections/CollectionDetailsPage.vue"
import CollectionUpdatePage from "./components/collections/CollectionUpdatePage.vue"

const routes = [
    {path: '/', component: CollectionsPage},
    {path: '/login', component: LoginPage},
    {path: '/logout', component: LogoutPage},
    {path: '/collections/new', component: NewCollectionPage},
    {path: '/collections/:collection_id', component: CollectionDetailsPage},
    {oath: '/collections/:collection_id', component: CollectionUpdatePage}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router