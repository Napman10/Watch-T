<template>
  <div>
    <user-grid />
  </div>
</template>

<script>
import UserGrid from "@/components/user/UserGrid";

export default {
  components: {
    UserGrid
  },
  methods: {
        // showUserModal() {
        //     this.$store.commit('user/SET_STATE', { isCreateModalVisible: true });
        // }
    },
}
</script>

<style>
</style>
