<template>
    <header class="header">
        <router-link class="logo" to='/' exact>WatchT</router-link>
        <router-link to='/issues' exact>Задачи</router-link>
        <router-link to='/projects' exact>Проекты</router-link>
        <menu class="userInfo">
            <li>{{ username }}</li>
            <li class="cursor-pointer" @click="logout">Выйти</li>
        </menu>
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
            this.$store.dispatch('auth/logout');
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
.cursor-pointer {
    color: white;
    cursor: pointer;
}
</style>