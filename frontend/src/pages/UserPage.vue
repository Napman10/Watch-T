<template>
  <div>
    <el-avatar :size="150" :src="user.photo"></el-avatar>
    <h2>{{user.first_name}}</h2>
    <h2>{{user.last_name}}</h2>
    <div style="text-align: right">
      <el-button type="primary" @click="callEditUser" style="margin-bottom: 10px">Редактировать пользователя</el-button>
    </div>
    <user-form/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import UserForm from "../components/user/UserForm";

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
    }
  },
   mounted() {
        this.$store.dispatch('user/getUser', this.userId);
    }
}
</script>

<style scoped>

</style>