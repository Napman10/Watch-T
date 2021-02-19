<template>
  <div>
    <div style="text-align: right">
      <el-button type="primary" @click="showIssueModal" style="margin-bottom: 10px">Новая задача</el-button>
    </div>
    <issue-form />
    <issue-grid />
  </div>
</template>

<script>
import IssueGrid from "@/components/issue/IssueGrid";
import IssueForm from "@/components/issue/IssueForm";

export default {
  components: {
    IssueGrid,
    IssueForm
  },
  methods: {
        showIssueModal() {
            this.$store.dispatch('project/getProjects');
            this.$store.dispatch('user/getUsers');
            this.$store.commit('issue/SET_STATE', { isCreateModalVisible: true });
        }
    },
}
</script>

<style>
</style>
