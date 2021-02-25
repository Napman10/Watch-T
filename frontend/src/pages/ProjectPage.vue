<template>
  <div>
    <h2>{{project.short_name}}</h2>
    <h2>{{project.header}}</h2>
    {{project.description}}
    <div style="text-align: right">
        <el-button type="primary" @click="showIssueProjectDescModal" style="margin-bottom: 10px">Отнаследовать задачу</el-button>
    </div>
  <desc-project-issue-form/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import DescProjectIssueForm from "@/components/issue/DescProjectIssueForm";

export default {
  data() {
        return {
            projectId: this.$route.params.projectId
        };
    },
  components: {
    DescProjectIssueForm
  },
  computed: {
        ...mapGetters('project', ['project']),
        ...mapGetters('issue', ['descProjectIssueModalVisible'])
    },
  methods: {
    showIssueProjectDescModal() {
      this.$store.dispatch('user/getUsers');
      this.$store.commit('issue/SET_STATE', {descProjectIssueModalVisible: true});
    }
  },
   mounted() {
        this.$store.dispatch('project/getProject', this.projectId);
    }
}
</script>

<style scoped>

</style>