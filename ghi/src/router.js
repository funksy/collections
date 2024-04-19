import { createWebHistory, createRouter } from "vue-router";

import MainPage from "./components/MainPage.vue";
import LoginPage from "./components/LoginPage.vue";
import Logout from "./components/Logout.vue"

const routes = [
    {path: '/', component: MainPage},
    {path: '/login', component: LoginPage},
    {path: '/logout', component: Logout},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router