import { defineStore } from "pinia";
import { mande } from 'mande'

const API_HOST = import.meta.env.VITE_API_HOST
const tokenApi = mande(API_HOST + '/token')
const userApi = mande(API_HOST + '/users')

export const useUserStore = defineStore('users', {
    state: () => ({
        userData: null,
    }),

    actions: {
        async createUser(username, password) {
            this.userData = await userApi.post({username, password})
        },
        async loginUser(username, password) {
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: JSON.stringify(
                    `grant_type=&username=${username}&password=${password}&scope=&client_id=&client_secret=`
                ),
            }
            const response = await fetch(API_HOST + '/token', requestOptions)
            this.userData = await response.json()
        }
    }
})