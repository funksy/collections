import { defineStore } from "pinia";

const API_HOST = import.meta.env.VITE_API_HOST
const collectionsUrl = API_HOST + '/collections'


export const useCollection = defineStore('collections', {
    state: () => ({
        collections: []
    }),

    actions: {
        async getMyCollections(token) {
            const fetchConfig = {
                method: 'get',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                }
            }
            const response = await fetch(`${collectionsUrl}/me`, fetchConfig)
            if (response.ok) {
                const data = await response.json()
                this.collections = data.collections
            }
        }
    }
})
