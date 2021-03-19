<template>
  <div>
    <h2>{{project.short_name}}</h2>
    <h2>{{project.header}}</h2>
    {{project.description}}
    <div style="text-align: right">
        <el-button type="primary" @click="showIssueProjectDescModal" style="margin-bottom: 10px">Отнаследовать задачу</el-button>
    </div>
    <div style="text-align: right">
      <el-button type="primary" @click="showAssignModal" style="margin-bottom: 10px">Назначить пользователя</el-button>
    </div>
  <desc-project-issue-form/>
  <assign-user-form/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import DescProjectIssueForm from "@/components/issue/DescProjectIssueForm";
import AssignUserForm from "@/components/project/AssignUserForm";

export default {
  data() {
        return {
            projectId: this.$route.params.projectId
        };
    },
  components: {
    DescProjectIssueForm,
    AssignUserForm
  },
  computed: {
        ...mapGetters('project', ['project', 'isAssignModalVisible']),
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
    }
  },
   mounted() {
        this.$store.dispatch('project/getProject', this.projectId);
    }
}
</script>

<style scoped>

</style>