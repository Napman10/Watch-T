<template>
    <el-dialog title="Новое задание" :visible="descIssueModalVisible" :before-close="closeModal">
        <el-form :model="form" ref="issueForm" :rules="rules">
            <el-form-item label="Короткое название" prop="short_name">
                <el-input v-model="form.short_name"></el-input>
            </el-form-item>

            <el-form-item label="Заголовок" prop="header">
                <el-input v-model="form.header"></el-input>
            </el-form-item>

            <el-form-item label="Описание" prop="description">
              <el-input type="textarea" v-model="form.description"></el-input>
            </el-form-item>

            <el-form-item label="Тип" prop="typo">
              <el-select v-model="form.typo" clearable placeholder="Тип">
                <el-option :value="0" label="Frontend" />
                <el-option :value="1" label="Backend" />
                <el-option :value="2" label="DevOps" />
                <el-option :value="3" label="Mobile" />
                <el-option :value="4" label="DB" />
                <el-option :value="5" label="SysAdmin" />
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
                typo: [
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
                ],
                description: [
                  {
                    max: 255,
                    message: 'Не больше 65 символов'
                  }
                ]
            }
        };
    },
    computed: {
        ...mapGetters('issue', ['descIssueModalVisible', 'issue']),
        ...mapGetters('user', ['users'])
    },
    methods: {
        submit() {
            this.$refs['issueForm'].validate((valid) => {
                if (valid) {
                    const desc = {parent: this.issue.id, level: this.issue.level + 1, project_name: this.issue.project.name}
                    let payload = Object.assign(this.form, desc);
                    this.$store.dispatch('issue/addIssue', payload);
                    this.$store.commit('issue/SET_STATE', { descIssueModalVisible: false });
                    this.form = {};
                }
            });
        },
        closeModal() {
            this.$store.commit('issue/SET_STATE', { descIssueModalVisible: false });
        },
        clearForm(){
            this.form = {}
        }
    }
};
</script>

<style></style>