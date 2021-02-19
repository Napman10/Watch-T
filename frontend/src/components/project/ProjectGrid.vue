<template>
    <div>
        <el-table
            :data="projects"
            style="width: 100%"
            @cell-click="openProject"
        >
            <el-table-column prop="short_name" width="100" />
            <el-table-column prop="header"  width="400" />
        </el-table>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    data() {
        return { form: {} };
    },
    computed: {
        ...mapGetters('project', ['projects']),
    },
    methods: {
      openProject(cell){
        const id = cell.id;
        this.$store.dispatch('project/getProject', id);
        this.$router.push({'name': 'project', params: {projectId: id}});
      }
    },
    mounted() {
        this.$store.dispatch('project/getProjects');
    }
};
</script>

<style>
</style>