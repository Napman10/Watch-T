<template>
    <div>
        <el-table
            :data="issues"
            style="width: 100%"
        >
            <el-table-column prop="short_name" width="50" />
            <el-table-column prop="header"  width="400" />
            <el-table-column prop="project"  width="400" />
            <el-table-column prop="author"  width="250" />
            <el-table-column prop="executor" min-width="150" />
            <el-table-column prop="priority" min-width="150" />
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
        ...mapGetters('issue', ['issues']),
    },
    methods: {
    },
    mounted() {
        this.$store.dispatch('issue/getIssues');
    }
};
</script>

<style>
</style>