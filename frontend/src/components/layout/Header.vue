<template>
    <header class="header">
        <router-link class="logo" to='/' exact>WatchT</router-link>
        <router-link to='/issues' exact>Задачи</router-link>
        <router-link :to="meUserPath()" exact>Профиль</router-link>
        <router-link v-if="meCreator()" to='/projects' exact>Проекты</router-link>
        <router-link v-if="meAdmin()" to='/users' exact>Пользователи</router-link>
        <menu class="userInfo">
            <li class="cursor-pointer" @click="logout">Выйти</li>
        </menu>
    </header>
</template>

<script>
import {meAdmin, meCreator} from "@/utils/indentMe";

export default {
  name: "PageHeader",
  computed: {
    },
  methods: {
        logout() {
            this.$store.dispatch('auth/logout');
        },
        meAdmin, meCreator,
        meUserPath() {
          return "user/" + localStorage.getItem('myId');
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