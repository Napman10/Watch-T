<template>
    <div>
      <el-form
            v-model="form"
            :inline="true"
            @submit.native.prevent="filterIssues"
            @keyup.native.enter="filterIssues"
            label-position="top"
        >

            <el-form-item>
                <el-select v-model="form.ownerrel" @change="filterIssues" clearable placeholder="">
                    <el-option :value="0" label="Все" />
                    <el-option :value="1" label="Назначенные на меня" />
                    <el-option :value="2" label="Назначенные мной" />
                    <el-option :value="3" label="Мои задачи" />
                </el-select>
            </el-form-item>

            <el-form-item>
                <el-input v-model="form.somename" clearable placeholder="Поиск..." />
            </el-form-item>

            <el-form-item>
                <el-select v-model="form.priority" @change="filterIssues" clearable placeholder="Приоритет">
                    <el-option :value="0" label="Низкий" />
                    <el-option :value="1" label="Обычный" />
                    <el-option :value="2" label="Высокий" />
                    <el-option :value="3" label="Критический" />
                </el-select>
            </el-form-item>

            <el-form-item>
                <el-select v-model="form.status" @change="filterIssues" clearable placeholder="Статус">
                    <el-option :value="0" label="Новая" />
                    <el-option :value="1" label="Требуется уточнение" />
                    <el-option :value="2" label="Назначена" />
                    <el-option :value="3" label="В работе" />
                    <el-option :value="4" label="Проверка" />
                    <el-option :value="5" label="Готово" />
                </el-select>
            </el-form-item>

            <el-form-item>
                <el-button style="margin-left: 10px" type="success" @click="filterIssues">Поиск</el-button>
            </el-form-item>
        </el-form>
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
      filterIssues(){
        this.$store.dispatch('issue/getIssues', this.form)
      }
    },
    mounted() {
        this.$store.dispatch('issue/getIssues');
    }
};
</script>

<style>
</style>