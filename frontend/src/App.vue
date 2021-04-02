<template>
  <div id="app" v-if="token">
    <router-view></router-view>
  </div>
    <div class="login" v-else>
        <h3 style="text-align: center">Вход в систему</h3>
        <login-form></login-form>
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
}
body {
    margin: 0;
    padding: 0;
    background-color: var(--main-bg-color);
}

.login {
    margin-left: auto;
    margin-right: auto;
    margin-top: 12%;
    padding: 16px;
    border: 2px solid #4f2aa3;
    width: 350px;
    border-radius: 5%;
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
.el-form-item__label, .el-dialog__title {
  color: white;
}
/*.el_table__header table, thead, tr, th, .row, col, colgroup{*/
/*  background-color: var(--main-bg-color);*/
/*}*/

</style>
