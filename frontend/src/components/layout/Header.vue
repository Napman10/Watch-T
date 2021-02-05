<template>
    <header class="header">
        <router-link class="logo" to="/api/issue/list" exact>WatchT</router-link>
        <ul class="userInfo">
            <li>{{ username }}</li>
            <li class="cursor-pointer" @click="logout">Выйти</li>
        </ul>
    </header>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "PageHeader",
  computed: {
        ...mapGetters('auth', ['username'])
    },
  methods: {
        logout() {
            this.$store.commit('auth/LOG_OUT');
        }
    }
}
</script>

<style scoped>
.header {
    background: #412227;
    padding: 15px 15px;
    margin-bottom: 10px;
}
.logo {
    color: white;
    font-weight: bold;
    font-size: x-large;
    text-decoration: none;
}
</style>