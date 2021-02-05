<template>
    <div>
        <el-form :model="form" ref="loginForm" label-position="top" :rules="rules" @keyup.native.enter="submit">
            <el-form-item label="Имя пользователя" prop="username">
                <el-input v-model="form.username" clearable></el-input>
            </el-form-item>
            <el-form-item label="Пароль" prop="password">
                <el-input type="password" v-model="form.password" clearable></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" style="text-align: center">
            <el-button @click="submit" type="primary">Войти</el-button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {},
            rules: {
                username: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    }
                ],
                password: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    }
                ]
            }
        };
    },
    computed: {},
    methods: {
        submit() {
            this.$refs['loginForm'].validate((valid) => {
                if (valid) {
                    const loading = this.$loading({ lock: true });
                    this.$store.dispatch('auth/login', this.form).then(loading.close());
                }
            });
        },
        validatePassword(rule, value, callback) {
            if (value === '') {
                callback(new Error('Please input the password'));
            } else {
                if (this.ruleForm.checkPass !== '') {
                    this.$refs.ruleForm.validateField('checkPass');
                }
                callback();
            }
        }
    }
};
</script>