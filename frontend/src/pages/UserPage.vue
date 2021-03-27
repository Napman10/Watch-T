<template>
  <div>
    <h2>{{user.first_name}}</h2>
    <h2>{{user.last_name}}</h2>
    {{itsYou()}}
    Затрачено времени {{tableMinutes(user)}}
    Был добавлен в команду {{user.joined}}
    <div v-if="meAdmin() || itsMe()">
      <div style="text-align: right">
        <el-button type="primary" @click="callEditUser" style="margin-bottom: 10px">Редактировать</el-button>
      </div>
      <div style="text-align: right">
        <el-button type="primary" @click="callChangePassUser" style="margin-bottom: 10px">Сменить пароль</el-button>
      </div>
      <div style="text-align: right">
        <el-button type="danger" @click="deleteMe" style="margin-bottom: 10px">Удалить</el-button>
      </div>
    </div>
    <user-form/>
    <change-password-form/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import UserForm from "../components/user/UserForm";
import ChangePasswordForm from "@/components/user/ChangePasswordForm";
import {meAdmin} from "@/utils/indentMe";
import {minutesToText} from "@/utils/transfer";

export default {
  data() {
        return {
            userId: this.$route.params.userId
        };
    },
  computed: {
        ...mapGetters('user', ['user', 'isEdit', 'isCreateModalVisible', 'isChangePasswordVisible']),
    },
  components: {
    UserForm,
    ChangePasswordForm
  },
  methods: {
    callEditUser(){
      this.$store.commit('user/SET_STATE', { isEdit: true, isCreateModalVisible: true });
    },
    callChangePassUser() {
      this.$store.commit('user/SET_STATE', { isChangePasswordVisible: true });
    },
    deleteMe() {
      let run = confirm('Вы уверены, что хотите удалить пользователя?')
      if (run) {
        let run2 = true;
        let self = this.user.username === localStorage.getItem('myName');
        if (self) {
          run2 = confirm('Вы удаляете собственную страницу');
        }
        if (run2) {
          this.$store.dispatch('user/deleteUser', {id: this.user.id});
          if (self) {
            localStorage.removeItem('token');
            location.reload();
          }
          else {
            this.$router.push({'name': 'users'});
          }
          this.$store.commit('user/SET_STATE', { user: {} });
        }

      }
    }, meAdmin,
    tableMinutes(row) {
      const result = minutesToText(row.tracked_minutes);
      if (result === "-") return "0м";
      return result;
    },
    itsMe() {
      const myName = localStorage.getItem('myName');
      const thisName = this.user.username;
      return myName === thisName;
    },
    itsYou(){
      if (this.itsMe()) return "(Это вы)";
      return "";
    }
  },
   mounted() {
        this.$store.dispatch('user/getUser', this.userId);
    }
}
</script>

<style scoped>

</style>