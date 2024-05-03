import { defineStore } from "pinia";
import { useFetch } from '@vueuse/core'
import router from '../router';

const API = import.meta.env.VITE_API_HOST
const tokenUrl = API + '/token'
const usersUrl = API + '/users'

export const useUser = defineStore('users', {
    state: () => ({
        userData: {
            id: "66226cb581fcb111844470a5",
            username: 'john'
        },
        token: {
            access_token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2MjI2Y2I1ODFmY2IxMTE4NDQ0NzBhNSIsInVzZXJuYW1lIjoiam9obiJ9.qqQ3bZQTflFQAsMKHCfEiwSJShCwbZwzHkyOvIEbuiQ",
            token_type: 'bearer'
        },
        isLoggedIn: true
    }),

    getters: {
        userName: (state) => state.userData.username,
    },

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
                await this.getUserData(username)
                this.isLoggedIn = true
                router.push('/')
            } else {
                const error = await response.json()
                return new Error(error.detail)
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
    }
})
