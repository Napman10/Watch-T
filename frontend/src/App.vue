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
body {
    margin: 0;
    padding: 0;
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
</style>
