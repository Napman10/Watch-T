<template>
  <div>
    <h2>{{issue.short_name}}</h2>
    <h2>{{issue.header}}</h2>
    {{issue.description}}
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  data() {
        return {
            issueId: this.$route.params.issueId
        };
    },
  computed: {
        ...mapGetters('issue', ['issue']),
    },
   mounted() {
        this.$store.dispatch('issue/getIssue', this.issueId);
    }
}
</script>

<style scoped>

</style>