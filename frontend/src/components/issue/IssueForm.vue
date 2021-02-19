<template>
    <el-dialog title="Новое задание" :visible="isCreateModalVisible" :before-close="closeModal">
        <el-form :model="form" ref="issueForm" :rules="rules">
            <el-form-item label="Короткое название" prop="short_name">
                <el-input v-model="form.short_name"></el-input>
            </el-form-item>

            <el-form-item label="Заголовок" prop="header">
                <el-input v-model="form.header"></el-input>
            </el-form-item>

            <el-form-item label="Проект" prop="project_name">
                <el-select v-model="form.project_name"
                  clearable placeholder="Выберите проект">
                  <el-option
                    v-for="item in projects"
                    :key="item.short_name"
                    :value="item.short_name">
                  </el-option>
                </el-select>
            </el-form-item>

            <el-form-item label="Выполнит" prop="executor_username">
                <el-select v-model="form.executor_username"
                  clearable placeholder="Выберите исполнителя">
                  <el-option
                    v-for="item in users"
                    :key="item.username"
                    :value="item.username">
                  </el-option>
                </el-select>
            </el-form-item>

            <el-form-item label="Оценка" prop="want_time">
                <el-input
                placeholder=""
                v-model="form.want_time"
                clearable>
              </el-input>
            </el-form-item>

            <el-form-item label="Приоритет" prop="priority">
                <el-select v-model="form.priority" clearable placeholder="Приоритет">
                    <el-option :value="0" label="Низкий" />
                    <el-option :value="1" label="Обычный" />
                    <el-option :value="2" label="Высокий" />
                    <el-option :value="3" label="Критический" />
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

                project_name: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    }
                ],

                want_time: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    }
                ],

                priority: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    }
                ]
            }
        };
    },
    computed: {
        ...mapGetters('issue', ['isCreateModalVisible']),
        ...mapGetters('project', ['projects']),
        ...mapGetters('user', ['users'])
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
        }
    }
};
</script>

<style></style>