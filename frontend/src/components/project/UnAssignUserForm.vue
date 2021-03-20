<template>
  <el-dialog title="Отстранить сотрудника" :visible="isUnAssignModalVisible" :before-close="closeModal">
    <el-form :model="form" ref="unAssignUserForm" :rules="rules">

      <el-form-item label="Пользователь" prop="user">
        <el-select v-model="form.user"
                   clearable placeholder="Отстраните пользователя">
          <el-option
              v-for="item in users"
              :key="item.username"
              :value="item.username">
          </el-option>
        </el-select>
      </el-form-item>

    </el-form>

    <div slot="footer">
      <el-button @click="submit" type="primary">Отстранить</el-button>
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
        user: [
          {
            required: true,
            message: 'Поле обязательно для заполнения'
          }
        ]
      }
    };
  },
  computed: {
    ...mapGetters('project', ['isUnAssignModalVisible', 'project']),
    ...mapGetters('user', ['users'])
  },
  methods: {
    submit() {
      this.$refs['unAssignUserForm'].validate((valid) => {
        if (valid) {
          const data = Object.assign(this.form, {project_id: this.project.id});
          this.$store.dispatch('project/unAssignUser', data);
          this.form = {};
        }
      });
    },
    closeModal() {
      this.form = {};
      this.$store.commit('project/SET_STATE', {isUnAssignModalVisible: false});
    }
  }
};
</script>

<style></style>