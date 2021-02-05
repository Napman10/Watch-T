<template>
    <div>
        <el-table
            :data="projects"
            style="width: 100%"
        >
            <el-table-column prop="short_name" width="50" />
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
    },
    mounted() {
        this.$store.dispatch('project/getProjects');
    }
};
</script>

<style>
</style>