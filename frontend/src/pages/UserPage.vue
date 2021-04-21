<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>О пользователе {{user.username}}</span>
          </div>
          <div class="text item">
            {{user.first_name}} {{user.last_name}} {{itsYou()}}
          </div>
          <div class="text item">
            Роль: {{['Гость', 'Разработчик', 'Проектный менеджер', 'Тимлид', 'Администратор'][user.role]}}
          </div>
          <div class="text item">
            Email: {{user.email}}
          </div>
          <div class="text item">
            Затратил времени: {{tableMinutes(user)}}
          </div>
          <div class="text item">
            Был добавлен в команду {{user.joined}}
          </div>
          <div class="text item">
            <div v-if="meAdmin() || itsMe()">
              <el-dropdown trigger="click">
                <span class="el-dropdown-link">
                  Действия<i class="el-icon-arrow-down el-icon--right"></i>
                </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item @click.native="callEditUser()" icon="el-icon-edit">Редактировать</el-dropdown-item>
                  <el-dropdown-item v-if="itsDev(this.user)" @click.native="addSkill()" icon="el-icon-edit">Добавить квалификацию</el-dropdown-item>
                  <el-dropdown-item @click.native="callChangePassUser()" icon="el-icon-lock">Сменить пароль</el-dropdown-item>
                  <el-dropdown-item @click.native="deleteMe()" icon="el-icon-error">Удалить</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <user-form/>
    <change-password-form/>
    <add-skill-form/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import UserForm from "../components/user/UserForm";
import ChangePasswordForm from "@/components/user/ChangePasswordForm";
import {meAdmin, itsDev} from "@/utils/indentMe";
import {minutesToText} from "@/utils/transfer";
import AddSkillForm from "../components/user/AddSkillForm";

export default {
  data() {
        return {
            userId: this.$route.params.userId
        };
    },
  computed: {
        ...mapGetters('user', ['user', 'isEdit', 'isCreateModalVisible',
          'isChangePasswordVisible', 'isAddSkillvisible']),
    },
  components: {
    UserForm,
    ChangePasswordForm,
    AddSkillForm
  },
  methods: {
    callEditUser(){
      this.$store.commit('user/SET_STATE', { isEdit: true, isCreateModalVisible: true });
    },
    callChangePassUser() {
      this.$store.commit('user/SET_STATE', { isChangePasswordVisible: true });
    },
    addSkill() {
      this.$store.dispatch('user/getSkills', {id: this.user.id})
      this.$store.commit('user/SET_STATE', {isAddSkillvisible: true})
    },
    deleteMe() {
      let run = confirm('Вы уверены, что хотите удалить пользователя?')
      if (run) {
        let run2 = true;
        let self = this.user.username === localStorage.getItem('myName');
        if (self) {
          run2 = confirm('Вы удаляете собственную страницу');
        }
        if (run2) {
          this.$store.dispatch('user/deleteUser', {id: this.user.id});
          if (self) {
            localStorage.removeItem('token');
            location.reload();
          }
          else {
            this.$router.push({'name': 'users'});
          }
          this.$store.commit('user/SET_STATE', { user: {} });
        }
      }
    }, meAdmin, itsDev,
    tableMinutes(row) {
      const result = minutesToText(row.tracked_minutes);
      if (result === "-") return "0м";
      return result;
    },
    itsMe() {
      const myName = localStorage.getItem('myName');
      const thisName = this.user.username;
      return myName === thisName;
    },
    itsYou(){
      if (this.itsMe()) return "(Это вы)";
      return "";
    }
  },
   mounted() {
        this.$store.dispatch('user/getUser', this.userId);
    }
}
</script>

<style scoped>

</style>