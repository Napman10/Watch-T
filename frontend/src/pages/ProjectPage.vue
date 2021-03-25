<template>
  <div v-if="!unAssignedStuff">
    <div v-if="meCreator">
      <h2>{{project.short_name}}</h2>
      <h2>{{project.header}}</h2>
      {{project.description}}<br/>
      Затрачено времени {{tableMinutes(project)}}
      Открыт {{project.created_date}}
      <div style="text-align: right">
          <el-button type="primary" @click="showIssueProjectDescModal" style="margin-bottom: 10px">Отнаследовать задачу</el-button>
      </div>
      <div style="text-align: right">
        <el-button type="primary" @click="showAssignModal" style="margin-bottom: 10px">Назначить пользователя</el-button>
      </div>
      <div style="text-align: right">
        <el-button type="primary" @click="showUnAssignModal" style="margin-bottom: 10px">Отстранить пользователя</el-button>
      </div>
      <div v-if="meAdmin()" style="text-align: right">
        <el-button type="danger" @click="deleteMe" style="margin-bottom: 10px">Удалить проект</el-button>
      </div>
    <desc-project-issue-form/>
    <assign-user-form/>
    <un-assign-user-form/>
    </div>
    <div v-else>permission denied</div>
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

export default {
  data() {
        return {
            projectId: this.$route.params.projectId
        };
    },
  components: {
    DescProjectIssueForm,
    AssignUserForm,
    UnAssignUserForm
  },
  computed: {
        ...mapGetters('project', ['project', 'isAssignModalVisible', 'isUnAssignModalVisible', 'unAssignedStuff']),
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