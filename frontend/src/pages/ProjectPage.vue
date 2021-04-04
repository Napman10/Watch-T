<template>
  <div v-if="!unAssignedStuff">
      <h2>{{project.short_name}}</h2>
      <h2>{{project.header}}</h2>
      {{project.description}}<br/>
      Затрачено времени {{tableMinutes(project)}}
      Открыт {{project.created_date}}
      <div v-if="meCreator()">
        <el-dropdown trigger="click">
        <span class="el-dropdown-link">
          Действия<i class="el-icon-arrow-down el-icon--right"></i>
        </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item @click.native="showIssueProjectDescModal()" icon="el-icon-document-copy">Отнаследовать задачу</el-dropdown-item>
            <el-dropdown-item @click.native="showAssignModal()" icon="el-icon-user">Назначить пользователя</el-dropdown-item>
            <el-dropdown-item @click.native="showUnAssignModal()" icon="el-icon-user-solid">Отстранить пользователя</el-dropdown-item>
            <div v-if="meAdmin()">
              <el-dropdown-item @click.native="editMe()" icon="el-icon-edit">Редактировать проект</el-dropdown-item>
              <el-dropdown-item @click.native="deleteMe()" icon="el-icon-error">Удалить проект</el-dropdown-item>
            </div>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    <desc-project-issue-form/>
    <assign-user-form/>
    <un-assign-user-form/>
    <project-edit-form/>
  </div>
  <div v-else>
    Вы не назначены на этот проект
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import DescProjectIssueForm from "@/components/issue/DescProjectIssueForm";
import AssignUserForm from "@/components/project/AssignUserForm";
import UnAssignUserForm from "@/components/project/UnAssignUserForm";
import {meCreator, meAdmin} from "@/utils/indentMe";
import {minutesToText} from "@/utils/transfer";
import ProjectEditForm from "@/components/project/ProjectEditForm";

export default {
  data() {
        return {
            projectId: this.$route.params.projectId
        };
    },
  components: {
    DescProjectIssueForm,
    AssignUserForm,
    UnAssignUserForm,
    ProjectEditForm
  },
  computed: {
        ...mapGetters('project', ['project', 'isAssignModalVisible', 'isEditModalVisible','isUnAssignModalVisible', 'unAssignedStuff']),
        ...mapGetters('issue', ['descProjectIssueModalVisible'])
    },
  methods: {
    showIssueProjectDescModal() {
      this.$store.dispatch('user/getUsers', {project_id: this.project.id});
      this.$store.commit('issue/SET_STATE', {descProjectIssueModalVisible: true});
    },
    showAssignModal() {
      this.$store.dispatch('user/getUsers', {project_id: this.project.id, exclude: true});
      this.$store.commit('project/SET_STATE', {isAssignModalVisible: true});
    },
    showUnAssignModal() {
      this.$store.dispatch('user/getUsers', {project_id: this.project.id});
      this.$store.commit('project/SET_STATE', {isUnAssignModalVisible: true});
    },

    editMe() {
      this.$store.commit('project/SET_STATE', {isEditModalVisible: true});
    },
    deleteMe() {
      let run = confirm('Вы уверены, что хотите удалить проект?');
      if (run) {
        let run2 = confirm('Все подзадачи будут так же удалены');
        if (run2) {
          this.$store.dispatch('project/deleteProject', {id: this.project.id});
          this.$router.push({'name': 'projects'});
          this.$store.commit('project/SET_STATE', { project: {} });
        }
      }
    }, meAdmin, meCreator,
    tableMinutes(row) {
      const result = minutesToText(row.tracked_minutes);
      if (result === "-") return "0м";
      return result;
    },
  },
   mounted() {
        this.$store.dispatch('project/getProject', this.projectId);
    }
}
</script>

<style scoped>

</style>