<template>
  <div>
    <div style="text-align: right">
      <el-button type="primary" @click="showProjectModal" style="margin-bottom: 10px">Создать проект</el-button>
    </div>
    <project-form />
    <project-grid />
  </div>
</template>

<script>
import ProjectGrid from "@/components/project/ProjectGrid";
import ProjectForm from "@/components/project/ProjectForm";

export default {
  components: {
    ProjectGrid,
    ProjectForm
  },
  methods: {
    showProjectModal(){
      this.$store.commit('project/SET_STATE', {isCreateModalVisible: true})
    }
  }
}
</script>

<style>
</style>
