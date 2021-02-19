<template>
  <div>
    <h2>{{project.short_name}}</h2>
    <h2>{{project.header}}</h2>
    {{project.description}}
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  data() {
        return {
            projectId: this.$route.params.projectId
        };
    },
  computed: {
        ...mapGetters('project', ['project']),
    },
   mounted() {
        this.$store.dispatch('project/getProject', this.projectId);
    }
}
</script>

<style scoped>

</style>