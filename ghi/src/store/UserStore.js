import { defineStore } from "pinia";

const API_HOST = import.meta.env.VITE_API_HOST
const tokenUrl = API_HOST + '/token'
const usersUrl = API_HOST + '/users'

export const useUser = defineStore('users', {
    state: () => ({
        userData: null,
        token: null,
        isLoggedIn: false
    }),

    actions: {
        async createUser(username, password) {
            const fetchConfig = {
                method: 'post',
                body: JSON.stringify({username: username, password: password}),
                headers: {'Content-Type': 'application/json'}
            }
            const response = await fetch(usersUrl, fetchConfig)
            if (response.ok) {
                this.userData = await response.json()
            }
        },
        async loginUser(username, password) {
            const tokenUrl = API_HOST + '/token'
            const body = JSON.stringify(
                `grant_type=&username=${username}&password=${password}&scope=&client_id=&client_secret=`
            )
            const fetchConfig = {
                method: 'post',
                body: body,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }
            const response = await fetch(tokenUrl, fetchConfig)
            if (response.ok) {
                this.token = await response.json()
                this.isLoggedIn = true
                await this.getUserData(username)
            }
        },
        async getUserData(username) {
            const fetchConfig = {
                method: 'get',
                headers: {'Content-Type': 'application/json'}
            }
            const response = await fetch(`${usersUrl}/${username}`, fetchConfig)
            if (response.ok) {
                this.userData = await response.json()
            }
        },        
        logoutUser() {
            this.token = null
            this.isLoggedIn = false
            this.userData = null
        },
        
    }
})
