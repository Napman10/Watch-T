<template>
    <el-dialog title="Новое задание" :visible="isCreateModalVisible" :before-close="closeModal">
        <el-form :model="form" ref="issueForm" :rules="rules">
            <el-form-item label="Короткое название" prop="short_name">
                <el-input v-model="form.short_name"></el-input>
            </el-form-item>

            <el-form-item label="Заголовок" prop="header">
                <el-input v-model="form.header"></el-input>
            </el-form-item>

            <el-form-item label="Проект" prop="header">
                <el-select v-model="form.project_name"
                  multiple
                  filterable
                  remote
                  reserve-keyword
                  clearable placeholder="Проект"
                  :remote-method="getProjectsNames">
                  <el-option
                    v-for="item in prjNames"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
            </el-form-item>

        </el-form>

        <div slot="footer">
            <el-button @click="closeModal">Закрыть</el-button>
            <el-button @click="clearForm">Очистить</el-button>
            <el-button @click="submit" type="primary">Создать</el-button>
        </div>
    </el-dialog>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    data() {
        return {
            form: {},
            prjNames: [],
            rules: {
                short_name: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    },
                    {
                        max: 16,
                        message: 'Не больше 16 символов'
                    }
                ],
                header: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    },
                    {
                        max: 65,
                        message: 'Не больше 65 символов'
                    }
                ],
            }
        };
    },
    computed: {
        ...mapGetters('issue', ['isCreateModalVisible']),
        ...mapGetters('project', ['projects'])
    },
    methods: {
        submit() {
            this.$refs['issueForm'].validate((valid) => {
                if (valid) {
                    this.$store.dispatch('issue/addIssue', this.form);
                    this.form = {};
                }
            });
        },
        closeModal() {
            this.$store.commit('issue/SET_STATE', { isCreateModalVisible: false });
        },
        clearForm(){
            this.form = {}
        },
        getProjectsNames(query){
          this.$store.dispatch('project/getProjects', query)
          this.prjNames = this.projects
        }
    }
};
</script>

<style></style>