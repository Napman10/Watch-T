<template>
  <div>
    <h2>{{issue.short_name}}</h2>
    <h2>{{issue.header}}</h2>
    {{issue.description}}
    <h2>Комментарии</h2>
    <el-table
        :data="comments"
        style="width: 100%"
        >
      <el-table-column prop="author" width="100" />
      <el-table-column prop="datetime"  width="300" />
      <el-table-column prop="text" width="400" />
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
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  data() {
        return {
            issueId: this.$route.params.issueId,
            form: {}
        };
    },
  computed: {
        ...mapGetters('issue', ['issue', 'comments']),
    },
  methods: {
    addComment(){
      const obj = {issue_id: this.issueId};
      const payload = Object.assign(obj, this.form);
      this.$store.dispatch('issue/addComment', payload);
      this.form = {};
    }
  },
   mounted() {
        this.$store.dispatch('issue/getIssue', this.issueId);
    }
}
</script>

<style scoped>

</style>