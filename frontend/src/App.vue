<template>
  <div id="app" v-if="token">
    <router-view></router-view>
  </div>
  <div v-else>
    <h1>Добро пожаловать в Watch-T!</h1>
    <h3>Дипломная работа, выполненная студентом группы МО-416 Кашаповым Ильёй.</h3>
    <h5>При отсутствии учётной записи обратитесь к администратору по email: ilya.kashapov99@gmail.com</h5>
    <div class="login">
        <h3 style="text-align: center">Вход в систему</h3>
        <login-form></login-form>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import LoginForm from '@/components/login/LoginForm';

export default {
  name: 'App',
  components: {
    LoginForm
  },
  computed: {
    ...mapGetters('auth', ['token'])
  }
}
</script>

<style>
:root {
  --main-bg-color: #00345c;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
}

h1, h3, h5 {
  text-align:center;
  color: white;
}

body {
    margin: 0;
    padding: 0;
    background-color: var(--main-bg-color);
}

.login {
    margin-left: auto;
    margin-right: auto;
    margin-top: 5%;
    padding: 16px;
    border: 2px solid #FFDEAD;
    width: 350px;
    color: white;
    border-radius: 5%;
}

table {
  background: var(--main-bg-color);
}

.el-table__body tr:hover{
  color:black;
}
.el-table__body tr, th{
  background-color: var(--main-bg-color);
}
.el-dialog__header {
  background-color: #001729;
}
.el-dialog__body, .el-dialog__footer {
  background-color: #133E6B;
}
.el-table th, tr{
  background-color: var(--main-bg-color);
}
.el-tabs__item.is-active {
  color: #FFDEAD;
}
.el-form-item__label, .el-dialog__title, .el-table--fit, .el-tabs__item {
  color: white;
}
#main {
  margin-left: 100px;
  margin-right: 100px;
}

</style>
