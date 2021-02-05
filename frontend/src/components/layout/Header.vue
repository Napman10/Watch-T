<template>
    <header class="header">
        <router-link class="logo" to="/api/issue/list" exact>WatchT</router-link>
        <li class="cursor-pointer" @click="logout">Выйти</li>
    </header>
</template>

<script>
export default {
  name: "PageHeader",
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