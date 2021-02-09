<template>
  <div>
    <div style="text-align: right">
      <el-button type="primary" @click="showModal" style="margin-bottom: 10px">Новая задача</el-button>
    </div>
    <issue-grid />
  </div>
</template>

<script>
import IssueGrid from "@/components/issue/IssueGrid";
import IssueForm from "@/components/issue/IssueForm";
import { mapGetters } from 'vuex';

export default {
  components: {
    IssueGrid,
    IssueForm
  },
  methods: {
        showModal() {
            this.$store.commit('issue/SET_STATE', { isCreateModalVisible: true });
        }
    },
}
</script>

<style>
</style>
