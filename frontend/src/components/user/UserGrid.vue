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
                    <el-option :value="2" label="Аналитик" />
                    <el-option :value="3" label="Тимлид" />
                    <el-option :value="4" label="Администратор" />
                </el-select>
            </el-form-item>

            <el-form-item>
                <el-input v-model="form.somename" clearable placeholder="Поиск..." />
            </el-form-item>

            <el-form-item>
                <el-button style="margin-left: 10px" type="success" @click="filterUsers">Поиск</el-button>
            </el-form-item>
        </el-form>
        <el-table
            :data="users"
            style="width: 100%"
        >
            <el-table-column prop="user" width="50" />
            <el-table-column prop="role"  width="400" />
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
        ...mapGetters('user', ['users']),
    },
    methods: {
      filterUsers(){
        this.$store.dispatch('user/getUsers', this.form)
      }
    },
    mounted() {
        this.$store.dispatch('user/getUsers');
    }
};
</script>

<style>
</style>