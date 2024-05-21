import { defineStore } from "pinia";
import Cookies from "js-cookie";
import router from "../router";

const API = import.meta.env.VITE_API_HOST;
const tokenUrl = API + "/token";
const usersUrl = API + "/users";

export const useUser = defineStore("users", {
  state: () => ({
    userData: {
      id: null,
      username: null,
    },
    token: {
      access_token: null,
      token_type: null,
    },
    isLoggedIn: false,
  }),

  getters: {
    username: (state) => state.userData.username,
    access_token: (state) => state.token.access_token,
  },

  actions: {
    async createUser(username, password) {
      const fetchConfig = {
        method: "post",
        body: JSON.stringify({ username: username, password: password }),
        headers: { "Content-Type": "application/json" },
      };
      const response = await fetch(usersUrl, fetchConfig);
      if (response.ok) {
        this.userData = await response.json();
      } else {
        const error = await response.json();
        return new Error(error.detail);
      }
    },
    async loginUser(username, password) {
      const body = JSON.stringify(
        `grant_type=&username=${username}&password=${password}&scope=&client_id=&client_secret=`
      );
      const fetchConfig = {
        method: "post",
        body: body,
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      };
      const response = await fetch(tokenUrl, fetchConfig);
      if (response.ok) {
        this.token = await response.json();
        Cookies.set("access_token", this.token.access_token, { expires: 0.08 });
        await this.getUserData(username);
        this.isLoggedIn = true;
        router.push("/");
      } else {
        const error = await response.json();
        return new Error(error.detail);
      }
    },
    async loginUserWithToken() {
      const access_token = Cookies.get("access_token");
      const fetchConfig = {
        method: "get",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${access_token}`,
        },
      };
      const response = await fetch(`${tokenUrl}/current`, fetchConfig);
      if (response.ok) {
        const data = await response.json();
        this.userData = {
          id: data.id,
          username: data.username,
        };
        this.token = {
          access_token: access_token,
          token_type: "bearer",
        };
        this.isLoggedIn = true;
      }
    },
    logoutUser() {
      Cookies.remove("access_token");
      this.$state = resetState();
      router.push("/login");
    },
    async getUserData(username) {
      const fetchConfig = {
        method: "get",
        headers: { "Content-Type": "application/json" },
      };
      const response = await fetch(`${usersUrl}/${username}`, fetchConfig);
      if (response.ok) {
        this.userData = await response.json();
      }
    },
  },
});

const resetState = () => {
  return {
    userData: {
      id: null,
      username: null,
    },
    token: {
      access_token: null,
      token_type: null,
    },
    isLoggedIn: false,
  };
};
