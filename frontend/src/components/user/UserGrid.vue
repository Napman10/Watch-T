<template>
    <div>
      <el-form
            v-model="form"
            :inline="true"
            @submit.native.prevent="filterUsers"
            @keyup.native.enter="filterUsers"
            label-position="top"
        >

            <el-form-item>
                <el-select v-model="form.role" @change="filterUsers" clearable placeholder="Роль">
                    <el-option :value="0" label="Гость" />
                    <el-option :value="1" label="Разработчик" />
                    <el-option :value="2" label="Проектный менеджер" />
                    <el-option :value="3" label="Тимлид" />
                    <el-option :value="4" label="Администратор" />
                </el-select>
            </el-form-item>

            <el-form-item>
                <el-input v-model="form.somename" clearable placeholder="Поиск..." />
            </el-form-item>

            <el-form-item>
                <el-button icon="el-icon-search" style="margin-left: 10px" type="success" @click="filterUsers">Поиск</el-button>
            </el-form-item>

            <el-form-item v-if="meAdmin()" style="float: right">
              <el-button icon="el-icon-user" type="primary" @click="showUserModal" style="margin-bottom: 10px">Создать пользователя</el-button>
            </el-form-item>
        </el-form>

        <el-table
            :data="users"
            style="width: 700px"
            @cell-click="openUser"
        >
            <el-table-column prop="username" width="200" />
            <el-table-column prop="first_name" width="100" />
            <el-table-column prop="last_name" width="200" />
            <el-table-column prop="role" :formatter="printRole" width="200" />
        </el-table>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import {meAdmin} from "@/utils/indentMe";

export default {
    data() {
        return { form: {} };
    },
    computed: {
        ...mapGetters('user', ['users']),
    },
    methods: {
      filterUsers(){
        this.$store.dispatch('user/getUsers', this.form)
      },
      printRole(row){
        const roles = ['Гость', 'Разработчик', 'Проектный менеджер', 'Тимлид', 'Администратор']
        return roles[row.role]
      },
      openUser(cell){
        const id = cell.id
        this.$store.dispatch('user/getUser', id);
        this.$router.push({'name': 'user', params: {userId: id}})
      },
      showUserModal() {
        this.$store.commit('user/SET_STATE', { isCreateModalVisible: true, isEdit: false });
      },
      meAdmin
    },
    mounted() {
        this.$store.dispatch('user/getUsers');
    }
};
</script>

<style>
</style>