<template>
    <el-dialog :title="this.isEdit === true ? `Редактирование пользователя` : `Регистрация пользователя`" :visible="isCreateModalVisible" :before-close="closeModal">
        <el-form :model="form" ref="userForm" :rules="this.isEdit ? rulesEdit : rulesCreate">

            <el-form-item label="Никнейм" prop="username">
                <el-input v-model="form.username"></el-input>
            </el-form-item>

            <el-form-item label="Имя" prop="first_name">
                <el-input v-model="form.first_name"></el-input>
            </el-form-item>

            <el-form-item label="Фамилия" prop="last_name">
                <el-input v-model="form.last_name"></el-input>
            </el-form-item>

            <el-form-item label="Email" prop="email">
                <el-input v-model="form.email"></el-input>
            </el-form-item>

            <el-form-item v-if="!this.isEdit" label="Пароль" prop="password">
                <el-input type="password" v-model="form.password" autocomplete="off"></el-input>
            </el-form-item>

            <el-form-item v-if="!this.isEdit" label="Подтвердите пароль" prop="password2">
                <el-input type="password" v-model="form.password2" autocomplete="off"></el-input>
            </el-form-item>

            <el-form-item label="Роль">
                <el-select v-model="form.role"  :value="this.user.role" clearable placeholder="Выберите роль">
                    <el-option :value="0" label="Гость" />
                    <el-option :value="1" label="Разработчик" />
                    <el-option :value="2" label="Аналитик" />
                    <el-option :value="3" label="Тимлид" />
                    <el-option :value="4" label="Администратор" />
                </el-select>
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
            rulesCreate: {
                username: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    },
                    {
                        max: 150,
                        message: 'Не больше 150 символов'
                    }
                ],
                password: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    },
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
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    },
                    {
                        validator: this.validatePassword
                    }
                ],
                first_name: [
                    {
                        max: 30,
                        message: 'Не больше 30 символов'
                    }
                ],
                last_name: [
                    {
                        max: 150,
                        message: 'Не больше 150 символов'
                    }
                ],
                email: [
                    {
                        required: true,
                        message: 'Поле обязательно для заполнения'
                    },
                    {
                        max: 254,
                        message: 'Не больше 254 символов'
                    }
                ],
            },
          rulesEdit: {
            username: [
              {
                max: 150,
                message: 'Не больше 150 символов'
              }
            ],
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
            first_name: [
              {
                max: 30,
                message: 'Не больше 30 символов'
              }
            ],
            last_name: [
              {
                max: 150,
                message: 'Не больше 150 символов'
              }
            ],
            email: [
              {
                max: 254,
                message: 'Не больше 254 символов'
              }
            ],
          },
        };
    },
    computed: {
        ...mapGetters('user', ['isCreateModalVisible', 'isEdit', 'user']),
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
            this.$refs['userForm'].validate((valid) => {
                if (valid) {
                    if (this.isEdit) {
                      const payload = Object.assign(this.form, {id: this.user.id});
                      this.$store.dispatch('user/editUser', payload);
                    } else {
                      this.$store.dispatch('user/addUser', this.form);
                    }
                    this.form = {};
                }
            });
        },
        closeModal() {
            this.$store.commit('user/SET_STATE', { isCreateModalVisible: false });
        },
        clearForm(){
            this.form = {}
        }
    }
};
</script>

<style></style>