import { defineStore } from "pinia";
import { mande } from 'mande'

const API_HOST = import.meta.env.VITE_API_HOST
const collectionsApi = mande(API_HOST + '/collections')


export const useCollection = defineStore('collections', {
    state: () => ({
        collections: []
    }),

    actions: {
        async getCollections(token) {
            collectionsApi.options.headers.Authorization = 'Bearer ' + token
            this.collections = await collectionsApi.get()
        }
    }
})
