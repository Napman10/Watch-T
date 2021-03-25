<template>
  <div>
    <el-avatar :size="150" :src="user.photo"></el-avatar>
    <h2>{{user.first_name}}</h2>
    <h2>{{user.last_name}}</h2>
    Затрачено времени {{tableMinutes(user)}}
    Был добавлен в команду {{user.joined}}
    <div v-if="meAdmin()">
      <div style="text-align: right">
        <el-button type="primary" @click="callEditUser" style="margin-bottom: 10px">Редактировать пользователя</el-button>
      </div>
      <div style="text-align: right">
        <el-button type="danger" @click="deleteMe" style="margin-bottom: 10px">Удалить пользователя</el-button>
      </div>
    </div>
    <user-form/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import UserForm from "../components/user/UserForm";
import {meAdmin} from "@/utils/indentMe";
import {minutesToText} from "@/utils/transfer";

export default {
  data() {
        return {
            userId: this.$route.params.userId
        };
    },
  computed: {
        ...mapGetters('user', ['user', 'isEdit', 'isCreateModalVisible']),
    },
  components: {
    UserForm
  },
  methods: {
    callEditUser(){
      this.$store.commit('user/SET_STATE', { isEdit: true, isCreateModalVisible: true });
    },
    deleteMe() {
      let run = confirm('Вы уверены, что хотите удалить пользователя?')
      if (run) {
        this.$store.dispatch('user/deleteUser', {id: this.user.id});
        this.$router.push({'name': 'users'});
        this.$store.commit('user/SET_STATE', { user: {} });
      }
    }, meAdmin,
    tableMinutes(row) {
      const result = minutesToText(row.tracked_minutes);
      if (result === "-") return "0м";
      return result;
    },
  },
   mounted() {
        this.$store.dispatch('user/getUser', this.userId);
    }
}
</script>

<style scoped>

</style>