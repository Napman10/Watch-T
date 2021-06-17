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
                <el-button icon="el-icon-search" style="margin-left: 10px" type="success" @click="filterIssues">Поиск</el-button>
            </el-form-item>
        </el-form>
        <el-table
            :data="issues"
            style="width: 1200px"
            @cell-click="openIssue"
            :row-class-name="tableRow"
        >
            <el-table-column prop="short_name" label="Задание" width="150" />
            <el-table-column prop="header"  width="400" />
            <el-table-column prop="project.name"  label="Проект" width="200" />
            <el-table-column prop="author"  label="Составил" width="150" />
            <el-table-column prop="executor" label="Выполняет" width="150" />
            <el-table-column prop="priority" label="Приоритет" width="150" />
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
      },
      openIssue(cell){
        const id = cell.id;
        this.$store.dispatch('issue/getIssue', id);
        this.$router.push({'name': 'issue', params: {issueId: id}});
      },
      tableRow({row}) {
        if (row.status === 'Готово') return 'done';
        else return '';
      }
    },
    mounted() {
        this.$store.dispatch('issue/getIssues');
    }
};
</script>

<style>
.el-table .done {
  text-decoration: line-through;
  color: gray;
}
</style>