<template>
  <div>
    <h2>{{issue.short_name}}</h2>
    <h2>{{issue.header}}</h2>
    {{issue.description}}
    <h5>Проект: {{issue.project}}</h5>
    <h5>Автор: {{issue.author}}</h5>
    <h5>Исполнитель: {{executorOrNull(issue)}} </h5>
    <h5>Статус: {{issue.status}} </h5>
    <h5>Приоритет: {{issue.priority}} </h5>
    <h5>Оценка: {{timeToText(issue.want_minutes)}} </h5>
    <h5>Затрачено: {{timeToText(issue.got_minutes)}} </h5>
    <h5>Родительская задача: {{parentOrNull(issue)}}</h5>
    <div style="text-align: right">
      <el-button type="primary" @click="showIssueDescModal" style="margin-bottom: 10px">Отнаследовать задачу</el-button>
    </div>
    <el-tabs type="card">
      <el-tab-pane label="Комментарии">
        <el-table
            :data="comments"
            style="width: 100%"
        >
          <el-table-column prop="author" width="100" />
          <el-table-column prop="datetime"  width="300" />
          <el-table-column :formatter="isEdited" prop="text" width="400" />
          <el-table-column align="right">
            <template slot-scope="scope">
              <el-button
                  size="mini"
                  @click="callEditComment(scope.row)">Edit</el-button>
              <el-button
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
                clearable placeholder="Комментарий...">
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
          <el-table-column align="right">
            <template slot-scope="scope">
              <el-button
                  size="mini"
                  type="danger"
                  @click="deleteTrack(scope.row)">Delete</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-form
            v-model="trackForm"
            :inline="true"
            @submit.native.prevent="addTrack"
            @keyup.native.enter="addTrack"
            label-position="top"
        >
          <el-form-item label="Добавить время">
            <el-input v-model="trackForm.minutes" clearable placeholder="Затраченное время"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="addTrack">Затратить время</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="История">Role</el-tab-pane>
    </el-tabs>
    <comment-edit-form/>
    <desc-issue-form/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import CommentEditForm from "@/components/issue/CommentEditForm";
import DescIssueForm from "@/components/issue/DescIssueForm";
import { minutesToText } from "@/utils/transfer";

export default {
  data() {
        return {
            issueId: this.$route.params.issueId,
            commentForm: {},
            trackForm: {}
        };
    },
  computed: {
        ...mapGetters('issue', ['issue', 'comments', 'tracks', 'editCommentModalVisible', 'descIssueModalVisible']),
    },
  components: {
    CommentEditForm,
    DescIssueForm
  },
  methods: {
    addComment(){
      if (this.commentForm.text) {
        const obj = {issue_id: this.issueId};
        const payload = Object.assign(obj, this.commentForm);
        this.$store.dispatch('issue/addComment', payload);
        this.commentForm = {};
      }
    },
    addTrack(){
      if (this.trackForm.minutes) {
        const obj = {issue_id: this.issueId};
        const payload = Object.assign(obj, this.trackForm);
        this.$store.dispatch('issue/addTrack', payload);
        this.trackForm = {};
      }
    },
    isEdited(row){
      if (row.edited){
        return row.text + (" (ред).");
      }
      return row.text;
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
      this.$store.dispatch('issue/deleteComment', {id: row.id, issue_id: this.issueId});
    },
    callEditComment(row){
      this.$store.commit('issue/SET_STATE', { comment: row });
      this.$store.commit('issue/SET_STATE', { editCommentModalVisible: true });
    },
    deleteTrack(row){
      this.$store.commit('issue/SET_STATE', {track: row});
      this.$store.dispatch('issue/deleteTrack', {id: row.id, issue_id: this.issueId});
    },
    showIssueDescModal(){
      this.$store.dispatch('user/getUsers');
      this.$store.commit('issue/SET_STATE', {descIssueModalVisible: true})
    }
  },
   mounted() {
        this.$store.dispatch('issue/getIssue', this.issueId);
    }
}
</script>

<style scoped>

</style>