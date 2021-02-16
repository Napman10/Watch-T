<template>
  <div>
    <div style="text-align: right">
      <el-button type="primary" @click="showUserModal" style="margin-bottom: 10px">Создать пользователя</el-button>
    </div>
    <user-form />
    <user-grid />
  </div>
</template>

<script>
import UserGrid from "@/components/user/UserGrid";
import UserForm from "@/components/user/UserForm";

export default {
  components: {
    UserGrid,
    UserForm
  },
  methods: {
        showUserModal() {
            this.$store.commit('user/SET_STATE', { isCreateModalVisible: true });
        }
    },
}
</script>

<style>
</style>
