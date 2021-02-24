<template>
    <el-dialog title="Редактировать комментарий" :visible="editCommentModalVisible" :before-close="closeModal">
        <el-form :model="form" ref="editCommentForm" :rules="rules">

            <el-form-item prop="text">
                <el-input v-model="form.text"></el-input>
            </el-form-item>

        </el-form>

        <div slot="footer">
            <el-button @click="closeModal">Закрыть</el-button>
            <el-button @click="submit" type="primary">Изменить</el-button>
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
                text: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    },
                    {
                        max: 255,
                        message: 'Не больше 255 символов'
                    }
                ],
            }
        };
    },
    computed: {
        ...mapGetters('issue', ['editCommentModalVisible', 'comment', 'issue'])
    },
    methods: {
        submit() {
            this.$refs['editCommentForm'].validate((valid) => {
                if (valid) {
                    const payload = Object.assign({id: this.comment.id, issue_id: this.issue.id},
                        {text: this.form.text})
                    this.$store.dispatch('issue/editComment', payload);
                    this.form = {};
                    this.$store.commit('issue/SET_STATE', { editCommentModalVisible: false });
                }
            });
        },
        closeModal() {
            this.$store.commit('issue/SET_STATE', { editCommentModalVisible: false });
            this.form = {};
        },
    }
};
</script>

<style></style>