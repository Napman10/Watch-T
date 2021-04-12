<template>
  <div>
    <project-form />
    <project-grid />
  </div>
</template>

<script>
import ProjectGrid from "@/components/project/ProjectGrid";
import ProjectForm from "@/components/project/ProjectForm";
import {meCreator, meAdmin} from "@/utils/indentMe";

export default {
  components: {
    ProjectGrid,
    ProjectForm
  },
  methods: {
    showProjectModal(){
      this.$store.commit('project/SET_STATE', {isCreateModalVisible: true})
    }, meCreator, meAdmin
  }
}
</script>

<style>
</style>
