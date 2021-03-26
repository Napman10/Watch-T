<template>
    <div>
      <el-form
        v-model="form"
            :inline="true"
            @submit.native.prevent="filterProjects"
            @keyup.native.enter="filterProjects"
            label-position="top"
      >
        <el-form-item>
          <el-input v-model="form.somename" clearable placeholder="Поиск..." />
        </el-form-item>
        <el-form-item>
            <el-checkbox v-model="form.assigned">Доступные мне</el-checkbox>
        </el-form-item>
        <el-form-item>
          <el-button style="margin-left: 10px" type="success" @click="filterProjects">Поиск</el-button>
        </el-form-item>
      </el-form>
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
        return { form: {}};
    },
    computed: {
        ...mapGetters('project', ['projects']),
    },
    methods: {
      openProject(cell){
        const id = cell.id;
        this.$store.dispatch('project/getProject', id);
        this.$router.push({'name': 'project', params: {projectId: id}});
      },
      filterProjects(){
        this.$store.dispatch('project/getProjects', this.form);
      }
    },
    mounted() {
        this.$store.dispatch('project/getProjects');
    }
};
</script>

<style>
</style>