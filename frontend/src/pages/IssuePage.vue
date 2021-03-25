<template>
  <div>
    <h2>{{issue.short_name}}</h2>
    <h2>{{issue.header}}</h2>
    {{issue.description}}
    <h5>Проект: {{issue.project.name}}</h5>
    <h5>Автор: {{issue.author}}</h5>
    <h5>Исполнитель: {{executorOrNull(issue)}} </h5>
    <h5>Статус: {{issue.status}} </h5>
    <h5>Приоритет: {{issue.priority}} </h5>
    <h5>Оценка: {{timeToText(issue.want_minutes)}} </h5>
    <h5>Затрачено: {{timeToText(issue.got_minutes)}} </h5>
    <h5>Родительская задача: {{parentOrNull(issue)}}</h5>
    <div v-if="children.length !== 0">
      <h5>Подзадачи: </h5>
      <el-table
        :data="children"
        style="width: 100%"
        @cell-click="openIssue"
      >
        <el-table-column prop="short_name" width="100" />
        <el-table-column prop="header"  width="300" />
      </el-table>
    </div>
    <div v-if="meCreator()">
      <div style="text-align: right">
        <el-button type="primary" @click="showIssueDescModal" style="margin-bottom: 10px">Отнаследовать задачу</el-button>
      </div>
      <div style="text-align: right">
        <el-button type="danger" @click="deleteMe" style="margin-bottom: 10px">Удалить задачу</el-button>
      </div>
      <div style="text-align: right">
        <el-button type="primary" @click="assignUser">Назначить сотрудника</el-button>
      </div>
    </div>
    <div style="text-align: right" v-if="meCreator() || isMyIssue()">
        <el-button type="primary" @click="changeStatus">Изменить статус</el-button>
      </div>
    <el-tabs type="card">
      <el-tab-pane label="Комментарии">
        <el-table
            :data="comments"
            style="width: 100%"
        >
          <el-table-column prop="author" width="100" />
          <el-table-column prop="datetime"  width="300" />
          <el-table-column prop="text" width="400" />
          <el-table-column align="right">
            <template slot-scope="scope">
              <el-button v-if="meAdmin()"
                  size="mini"
                  type="danger"
                  @click="deleteComment(scope.row)">Delete</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-form
            v-model="commentForm"
            :inline="true"
            @submit.native.prevent="addComment"
            @keyup.native.enter="addComment"
            label-position="top">
          <el-form-item label="Комментарий">
            <el-input
                type="textarea"
                v-model="commentForm.text"
                clearable placeholder="Комментарий">
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="addComment">Отправить</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="Трекинг времени">
        <el-table
          :data="tracks"
          style="width: 100%"
        >
          <el-table-column prop="executor" width="150"/>
          <el-table-column prop="minutes" :formatter="tableMinutes" width="150"/>
          <el-table-column prop="text" wigth="300"/>
          <el-table-column align="right">
            <template slot-scope="scope">
              <el-button v-if="meAdmin()"
                  size="mini"
                  type="danger"
                  @click="deleteTrack(scope.row)">Delete</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-form v-if="meExecutor()"
            v-model="trackForm"
            :inline="true"
            @submit.native.prevent="addTrack"
            @keyup.native.enter="addTrack"
            label-position="top"
        >
          <el-form-item label="Добавить время">
            <el-input v-model="trackForm.minutes" clearable placeholder="Затраченное время"></el-input>
          </el-form-item>
          <el-input
              type="textarea"
              v-model="trackForm.text"
              clearable placeholder="Описание">
          </el-input>
          <el-form-item>
            <el-button type="primary" @click="addTrack">Затратить время</el-button>
          </el-form-item>

        </el-form>
      </el-tab-pane>
      <el-tab-pane label="История">Role</el-tab-pane>
    </el-tabs>
    <desc-issue-form/>
    <assign-user-form/>
    <change-issue-status-form/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import DescIssueForm from "@/components/issue/DescIssueForm";
import AssignUserForm from "@/components/issue/AssignUserForm";
import { minutesToText } from "@/utils/transfer";
import {meCreator, meExecutor, meAdmin} from "@/utils/indentMe";
import ChangeIssueStatusForm from "@/components/issue/ChangeIssueStatusForm";

export default {
  data() {
        return {
            issueId: this.$route.params.issueId,
            commentForm: {},
            trackForm: {}
        };
    },
  computed: {
        ...mapGetters('issue', ['issue', 'comments', 'tracks', 'children',
          'editCommentModalVisible', 'descIssueModalVisible', 'isStatusModalVisible'])
    },
  components: {
    DescIssueForm,
    AssignUserForm,
    ChangeIssueStatusForm
  },
  methods: {
    meCreator, meExecutor, meAdmin,
    isMyIssue() {
      const myName = localStorage.getItem('myName');
      return this.issue.executor === myName;
    },
    addComment(){
      if (this.commentForm.text) {
        const obj = {issue_id: this.issue.id};
        const payload = Object.assign(obj, this.commentForm);
        this.$store.dispatch('issue/addComment', payload);
        this.commentForm = {};
      }
    },
    addTrack(){
      if (this.trackForm.minutes) {
        const obj = {issue_id: this.issue.id};
        const payload = Object.assign(obj, this.trackForm);
        this.$store.dispatch('issue/addTrack', payload);
        this.trackForm = {};
      }
    },
    deleteMe() {
      let run = confirm('Вы уверены, что хотите удалить задачу? Все подзадачи будут так же удалены')
      if (run) {
        this.$store.dispatch('issue/deleteIssue', {id: this.issue.id});
        this.$router.push({'name': 'issues'});
        this.$store.commit('issue/SET_STATE', { issue: {} });
      }
    },
    timeToText(minutes) {
      return minutesToText(minutes);
    },
    tableMinutes(row) {
      return minutesToText(row.minutes);
    },
    executorOrNull(issue){
      if (issue.executor !== ''){
        return issue.executor;
      }
      else {
        return "Нет исполнителя";
      }
    },
    parentOrNull(issue){
      if (issue.parent !== ''){
        return issue.parent;
      }
      else {
        return '-';
      }
    },
    deleteComment(row){
      this.$store.commit('issue/SET_STATE', { comment: row });
      this.$store.dispatch('issue/deleteComment', {id: row.id, issue_id: this.issue.id});
    },
    deleteTrack(row){
      this.$store.commit('issue/SET_STATE', {track: row});
      this.$store.dispatch('issue/deleteTrack', {id: row.id, issue_id: this.issue.id});
    },
    showIssueDescModal(){
      this.$store.dispatch('user/getUsers', {project_id: this.issue.project.id});
      this.$store.commit('issue/SET_STATE', {descIssueModalVisible: true});
    },
    openIssue(cell){
      const id = cell.id;
      this.$store.dispatch('issue/getIssue', id);
      this.$router.push({'name': 'issue', params: {issueId: id}});
    },
    assignUser() {
      this.$store.dispatch('user/getUsers',
          {project_id: this.issue.project.id, dev: true});
      this.$store.commit('issue/SET_STATE', { isAssignModalVisible: true });
    },
    changeStatus() {
      this.$store.commit('issue/SET_STATE', { isStatusModalVisible: true });
      this.$store.dispatch('issue/getIssue', this.issueId);
    }
  },
   mounted() {
        this.$store.dispatch('issue/getIssue', this.issueId);
    }
}
</script>

<style scoped>

</style>