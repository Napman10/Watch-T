<template>
    <header class="header">
        <router-link class="logo" to="issues/" exact>WatchT</router-link>
<!--        <ul class="userInfo">-->
<!--            <li class="cursor-pointer" @click="changeMo">{{ currentMo.name }}</li>-->
<!--            <li>{{ userFullName }}</li>-->
<!--            <li class="cursor-pointer" @click="logout">Выйти</li>-->
<!--        </ul>-->
    </header>
</template>

<script>
export default {
name: "Headerp"
}
</script>

<style scoped>
.header {
    background: #44c8f3;
    padding: 25px 15px;
    margin-bottom: 8px;
}
</style>