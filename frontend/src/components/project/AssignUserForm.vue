<template>
  <el-dialog title="Назначить сотрудника" :visible="isAssignModalVisible" :before-close="closeModal">
    <el-form :model="form" ref="assignUserForm" :rules="rules">

      <el-form-item label="Пользователь" prop="user">
        <el-select v-model="form.user"
                   clearable placeholder="Назначьте пользователя">
          <el-option
              v-for="item in users"
              :key="item.username"
              :value="item.username">
          </el-option>
        </el-select>
      </el-form-item>

    </el-form>

    <div slot="footer">
      <el-button @click="submit" type="primary">Назначить</el-button>
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
    ...mapGetters('project', ['isAssignModalVisible', 'project']),
    ...mapGetters('user', ['users'])
  },
  methods: {
    submit() {
      this.$refs['assignUserForm'].validate((valid) => {
        if (valid) {
          const data = Object.assign(this.form, {project_id: this.project.id});
          this.$store.dispatch('project/assignUser', data);
          this.form = {};
        }
      });
    },
    closeModal() {
      this.$store.commit('project/SET_STATE', { isAssignModalVisible: false });
    },
    clearForm(){
      this.form = {}
    }
  }
};
</script>

<style></style>