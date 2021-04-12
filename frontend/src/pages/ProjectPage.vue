<template>
  <div v-if="!unAssignedStuff">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>О проекте {{project.short_name}}</span>
          </div>
          <div class="text item">
            Проект: {{project.header}}
          </div>
          <div class="text item">
            Открыт {{project.created_date}}
          </div>
          <div class="text item">
            Затрачено времени {{tableMinutes(project)}}
          </div>
          <div class="text item">
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
          </div>
        </el-card>
      </el-col>
      <el-col id="description" :span="8">
        {{project.description}}
      </el-col>
    </el-row>
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
#description{
  width: 600px;
  word-wrap: break-word;
  margin-top: 10px;
  color: white;
}
</style>