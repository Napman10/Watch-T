<template>
  <el-dialog title="Назначить сотрудника" :visible="isAssignModalVisible" :before-close="closeModal">
    <el-form :model="form" ref="assignUserForm" :rules="rules">

      <el-form-item label="Пользователь" prop="user">
        <el-select v-model="form.user"
                   clearable placeholder="Назначьте пользователя">
          <el-option
              v-for="item in [{username: 'Не назначено'}].concat(users)"
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
    ...mapGetters('issue', ['isAssignModalVisible', 'issue']),
    ...mapGetters('user', ['users'])
  },
  methods: {
    submit() {
      this.$refs['assignUserForm'].validate((valid) => {
        if (valid) {
          const data = Object.assign(this.form, {id: this.issue.id});
          this.$store.dispatch('issue/assignUser', data);
          this.$store.dispatch('issue/getIssue', this.issue.id);
          this.form = {};
        }
      });
    },
    closeModal() {
      this.form = {};
      this.$store.commit('issue/SET_STATE', {isAssignModalVisible: false});
    }
  }
};
</script>

<style></style>