<template>
  <el-menu
      :default-active="activeIndex2"
      id="nav"
      class="el-menu-demo"
      mode="horizontal"
      background-color="#6A5ACD"
      text-color="#fff"
      :router="true"
      active-text-color="#FFDEAD">
    <el-menu-item style="margin-left: 10px" index="/issues" :route="{ name: 'issues'}">Задачи</el-menu-item>
    <el-menu-item index="/projects" :route="{ name: 'projects'}">Проекты</el-menu-item>
    <el-menu-item v-if="meAdmin()" index="/users" :route="{ name: 'users'}">Пользователи</el-menu-item>
    <el-submenu style="position: absolute; right: .5em;" index="2">
      <template slot="title">Профиль</template>
      <el-menu-item index="/user" :route="{ path: 'user/'+myId()}">Мой профиль</el-menu-item>
      <el-menu-item index="/logout" @click="logout">Выйти</el-menu-item>
    </el-submenu>
  </el-menu>
</template>

<script>
import {meAdmin, meCreator} from "@/utils/indentMe";

export default {
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    };
  },
  name: "PageHeader",
  computed: {
    },
  methods: {
        logout() {
            this.$store.dispatch('auth/logout');
        },
        meAdmin, meCreator,
        myId() {
          return localStorage.getItem('myId');
        }
    }
}
</script>

<style scoped>
  #nav{
    margin-bottom: 10px
  }
</style>