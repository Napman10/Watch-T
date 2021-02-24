<template>
  <div>
    <h2>{{issue.short_name}}</h2>
    <h5>{{issue.project}}</h5>
    <h2>{{issue.header}}</h2>
    <h5>{{issue.description}}</h5>
    <h5>Автор: {{issue.author}}</h5>
    <h5>Исполнитель: {{executorOrNull(issue)}} </h5>
    <h5>Статус: {{issue.status}} </h5>
    <h5>Приоритет: {{issue.priority}} </h5>
    <h5>Оценка: {{parseFromMinutes(issue.want_minutes)}} </h5>
    <h5>Затрачено: {{parseFromMinutes(issue.got_minutes)}} </h5>
    <h2>Комментарии</h2>
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
      v-model="form"
      :inline="true"
      @submit.native.prevent="addComment"
      @keyup.native.enter="addComment"
      label-position="top">
      <el-form-item label="Комментарий">
        <el-input type="textarea" v-model="form.text"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="addComment">Отправить</el-button>
      </el-form-item>
    </el-form>
    <comment-edit-form/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import CommentEditForm from "@/components/issue/CommentEditForm";

export default {
  data() {
        return {
            issueId: this.$route.params.issueId,
            form: {}
        };
    },
  computed: {
        ...mapGetters('issue', ['issue', 'comments', 'editCommentModalVisible']),
    },
  components: {
    CommentEditForm
  },
  methods: {
    addComment(){
      if (this.form.text) {
        const obj = {issue_id: this.issueId};
        const payload = Object.assign(obj, this.form);
        this.$store.dispatch('issue/addComment', payload);
        this.form = {};
      }
    },
    isEdited(row){
      if (row.edited){
        return row.text + (" (ред).");
      }
      return row.text;
    },
    executorOrNull(issue){
      if (issue.executor !== ''){
        return issue.executor;
      }
      else {
        return "Нет исполнителя";
      }
    },
    div(val, by){
      return (val - val % by) / by;
    },
    parseFromMinutes(minutes){
      const toHour = 60;
      const toDay = toHour * 8;
      const toWeek = toDay * 5;

      const weeks = this.div(minutes, toWeek);
      minutes -= weeks * toWeek;

      const days = this.div(minutes, toDay);
      minutes -= days * toDay;

      const hours = this.div(minutes, toHour);
      minutes -= hours * toHour;

      var result = "";
      if (weeks !== 0){
        result += weeks + 'н ';
      }
      if (days !== 0) {
        result += days + 'д ';
      }
      if (hours !== 0){
        result += hours + 'ч ';
      }
      if (minutes !== 0) {
        result += minutes + 'м ';
      }
      if (result === ""){
        return "-";
      }
      else {
        return result;
      }
    },
    deleteComment(row){
      this.$store.commit('issue/SET_STATE', { comment: row });
      this.$store.dispatch('issue/deleteComment', {id: row.id, issue_id: this.issueId});
    },
    callEditComment(row){
      this.$store.commit('issue/SET_STATE', { comment: row });
      this.$store.commit('issue/SET_STATE', { editCommentModalVisible: true });
    }
  },
   mounted() {
        this.$store.dispatch('issue/getIssue', this.issueId);
    }
}
</script>

<style scoped>

</style>