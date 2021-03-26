<template>
    <el-dialog title="Сменить пароль" :visible="isChangePasswordVisible" :before-close="closeModal">
        <el-form :model="form" ref="changePasswordForm" :rules=rules>
            <el-form-item label="Пароль" prop="password">
                <el-input type="password" v-model="form.password" autocomplete="off"></el-input>
            </el-form-item>

            <el-form-item label="Подтвердите пароль" prop="password2">
                <el-input type="password" v-model="form.password2" autocomplete="off"></el-input>
            </el-form-item>
        </el-form>

        <div slot="footer">
            <el-button @click="closeModal">Закрыть</el-button>
            <el-button @click="clearForm">Очистить</el-button>
            <el-button @click="submit" type="primary">Сохранить</el-button>
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
            password: [
              {
                max: 128,
                message: 'Не больше 128 символов'
              },
              {
                min: 8,
                message: 'Не менее 8 символов'
              }
            ],
            password2: [
              {
                validator: this.validatePassword
              }
            ],
          },
        };
    },
    computed: {
        ...mapGetters('user', ['isChangePasswordVisible', 'user']),
    },
    methods: {
      validatePassword(rule, value, callback) {
            if (value !== this.form.password && this.form.password) {
                return callback(new Error('Пароли не совпадают'));
            } else {
                callback();
            }
        },
        submit() {
            this.$refs['changePasswordForm'].validate((valid) => {
                if (valid) {
                  const payload = Object.assign(this.form, {id: this.user.id});
                  this.$store.dispatch('user/editUser', payload);
                  this.form = {};
                }
            });
        },
        closeModal() {
            this.$store.commit('user/SET_STATE', { isChangePasswordVisible: false });
        },
        clearForm(){
            this.form = {}
        }
    }
};
</script>

<style></style>