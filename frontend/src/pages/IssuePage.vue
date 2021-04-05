<template>
  <div v-if="!unAssignedStuff || meAdmin()">
    <el-row :gutter="20" style="color: white">
      <el-col :span="16">{{issue.short_name}}
        <h2>{{issue.header}}</h2>
        <div id="description">{{issue.description}}</div>
        <div v-if="children.length !== 0">
          <h5>Подзадачи: </h5>
          <ul>
            <li v-for="task in children">
              {{task.short_name}} - {{task.header}}
            </li>
          </ul>
        </div>
      </el-col>
      <el-col :span="8">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>О задаче {{issue.short_name}}</span>
          </div>
          <div class="text item">
            Проект: {{issue.project.name}}
          </div>
          <div class="text item">
            Автор: {{issue.author}}
          </div>
          <div class="text item">
            Исполнитель: {{executorOrNull(issue)}}
          </div>
          <div class="text item">
            Статус: {{issue.status}}
          </div>
          <div class="text item">
            Приоритет: {{issue.priority}}
          </div>
          <div class="text item">
            Оценка: {{timeToText(issue.want_minutes)}}
          </div>
          <div class="text item">
            Затрачено: {{timeToText(issue.got_minutes)}}
          </div>
          <div class="text item">
            Родительская задача: {{parentOrNull(issue)}}
          </div>
          <div class="text item">
            <div id="drops" v-if="meCreator()">
              <el-dropdown trigger="click">
                <span class="el-dropdown-link">
                  Действия<i class="el-icon-arrow-down el-icon--right"></i>
                </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item @click.native="showIssueDescModal()" icon="el-icon-document-copy">Отнаследовать задачу</el-dropdown-item>
                  <el-dropdown-item @click.native="assignUser()" icon="el-icon-user">Назначить сотрудника</el-dropdown-item>
                  <el-dropdown-item  v-if="isMyIssue()|| meCreator()" @click.native="changeStatus()" icon="el-icon-edit">Изменить статус</el-dropdown-item>
                  <el-dropdown-item @click.native="deleteMe()" icon="el-icon-error">Удалить задачу</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-row :gutter="20" style="margin-top: 100px">
      <el-tabs type="card">
        <el-tab-pane label="Комментарии">
          <div v-if="comments.length !== 0">
            <el-table
                :data="comments"
                style="width: 900px"
                :show-header="false"
            >
              <el-table-column prop="author" width="100" />
              <el-table-column prop="datetime"  width="300" />
              <el-table-column prop="text" width="400" />
              <el-table-column align="right">
                <template slot-scope="scope">
                  <i v-if="meAdmin()" class="el-icon-close" @click="deleteComment(scope.row)"></i>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <el-form
              v-model="commentForm"
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
          <div v-if="tracks.length !== 0">
            <el-table
                :data="tracks"
                style="width: 1000px"
                :show-header="false"
            >
              <el-table-column prop="executor" width="150"/>
              <el-table-column prop="datetime"  width="300" />
              <el-table-column prop="minutes" :formatter="tableMinutes" width="150"/>
              <el-table-column prop="text" wigth="300"/>
              <el-table-column align="right">
                <template slot-scope="scope">
                  <i v-if="meCreator()" class="el-icon-close" @click="deleteTrack(scope.row)"></i>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <el-form v-if="meExecutor()"
                   v-model="trackForm"
                   @submit.native.prevent="addTrack"
                   @keyup.native.enter="addTrack"
                   label-position="top"
          >
            <div v-if="canTrack(this.issue.executor)">
              <el-form-item label="Добавить время">
                <el-input style="width: 100px" v-model="trackForm.minutes" clearable placeholder="Время"></el-input>
              </el-form-item>
              <el-input
                  type="textarea"
                  v-model="trackForm.text"
                  clearable placeholder="Описание">
              </el-input>
              <el-form-item>
                <el-button style="margin-top: 20px" type="primary" @click="addTrack">Затратить время</el-button>
              </el-form-item>
            </div>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="История">
          <el-table
              :data="history"
              style="width: 700px"
              :show-header="false"
          >
            <el-table-column prop="datetime"  width="300" />
            <el-table-column prop="text" width="400" />
          </el-table>
        </el-tab-pane>
      </el-tabs>
    </el-row>
      <desc-issue-form/>
      <assign-user-form/>
      <change-issue-status-form/>
  </div>
  <div v-else>
    You do not have permission to watch this issue
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import DescIssueForm from "@/components/issue/DescIssueForm";
import AssignUserForm from "@/components/issue/AssignUserForm";
import { minutesToText } from "@/utils/transfer";
import {meCreator, meExecutor, meAdmin, meNotGuest, canTrack} from "@/utils/indentMe";
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
        ...mapGetters('issue', ['issue', 'comments', 'tracks', 'children', 'unAssignedStuff',
          'editCommentModalVisible', 'descIssueModalVisible', 'isStatusModalVisible', 'history'])
    },
  components: {
    DescIssueForm,
    AssignUserForm,
    ChangeIssueStatusForm
  },
  methods: {
    meCreator, meExecutor, meAdmin, meNotGuest, canTrack,
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
.box-card{
  float: right;
}
#description{
  width: 600px;
  word-wrap: break-word;
}
</style>