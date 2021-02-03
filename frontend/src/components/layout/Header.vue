<template>
    <header class="header">
        <router-link class="logo" to="/api/issue/" exact>WatchT</router-link>
<!--        <ul class="userInfo">-->
<!--            <li class="cursor-pointer" @click="changeMo">{{ currentMo.name }}</li>-->
<!--            <li>{{ userFullName }}</li>-->
<!--            <li class="cursor-pointer" @click="logout">Выйти</li>-->
<!--        </ul>-->
    </header>
</template>

<script>
export default {
name: "PageHeader"
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