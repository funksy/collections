import { defineStore } from "pinia";
import { mande } from 'mande'

const API_HOST = import.meta.env.VITE_API_HOST
const tokenApi = mande(API_HOST + '/token')
const usersApi = mande(API_HOST + '/users')

export const useUser = defineStore('users', {
    state: () => ({
        userData: null,
        token: null,
        isLoggedIn: false
    }),

    actions: {
        async createUser(username, password) {
            this.userData = await usersApi.post({username, password})
        },
        async loginUser(username, password) {
            const body = JSON.stringify(
                `grant_type=&username=${username}&password=${password}&scope=&client_id=&client_secret=`
            )
            try {
                this.token = await tokenApi.post('', body, {
                    headers: {"Content-Type": "application/x-www-form-urlencoded"}
                })
            } catch (error) {
                throw error
            }
            if (this.token) {
                this.userData = await usersApi.get(username)
                this.isLoggedIn = true
            }

        },
        logoutUser() {
            this.token = null
            this.isLoggedIn = false
            this.userData = null
        }
    }
})
