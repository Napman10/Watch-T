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
          <el-button icon="el-icon-search" style="margin-left: 10px" type="success" @click="filterProjects">Поиск</el-button>
        </el-form-item>
        <el-form-item v-if="meAdmin()" style="float: right">
          <el-button icon="el-icon-document-add" type="primary" @click="showProjectModal" style="margin-bottom: 10px">Создать проект</el-button>
        </el-form-item>
      </el-form>
        <el-table
            :data="projects"
            style="width: 300px"
            @cell-click="openProject"
        >
            <el-table-column prop="short_name" width="100" />
            <el-table-column prop="header"  width="200" />
        </el-table>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import {meCreator, meAdmin} from "@/utils/indentMe";
export default {
    data() {
        return { form: {}};
    },
    computed: {
        ...mapGetters('project', ['projects', 'isCreateModalVisible']),
    },
    methods: {
      openProject(cell){
        const id = cell.id;
        this.$store.dispatch('project/getProject', id);
        this.$router.push({'name': 'project', params: {projectId: id}});
      },
      filterProjects(){
        this.$store.dispatch('project/getProjects', this.form);
      }, meCreator, meAdmin,
      showProjectModal(){
        this.$store.commit('project/SET_STATE', {isCreateModalVisible: true})
      }
    },
    mounted() {
        this.$store.dispatch('project/getProjects');
    }
};
</script>

<style>
</style>