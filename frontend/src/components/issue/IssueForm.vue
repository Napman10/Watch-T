<template>
    <el-dialog title="Новое задание" :visible="isCreateModalVisible" :before-close="closeModal">
        <el-form :model="form" ref="issueForm" :rules="rules">
            <el-form-item label="Короткое название" prop="shortName">
                <el-input v-model="form.shortName"></el-input>
            </el-form-item>

            <el-form-item label="Заголовок" prop="model">
                <el-input v-model="form.header"></el-input>
            </el-form-item>

        </el-form>

        <div slot="footer">
            <el-button @click="closeModal">Закрыть</el-button>
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
                shortName: [
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
    },
    methods: {
        submit() {
            //this.form.moId = this.currentMo.id;
            this.$refs['issueForm'].validate((valid) => {
                if (valid) {
                    this.$store.dispatch('issue/addIssue', this.form);
                }
            });
        },
        closeModal() {
            this.$store.commit('issue/SET_STATE', { isCreateModalVisible: false });
        }
    }
};
</script>

<style></style>