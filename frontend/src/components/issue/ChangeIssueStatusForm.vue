<template>
  <el-dialog title="Изменить статус задачи" :visible="isStatusModalVisible" :before-close="closeModal">
    <el-form :model="form" ref="changeIssueStatusForm" :rules="rules">

      <el-form-item label="Статус" prop="status">
        <el-select v-model="form.status"
                   clearable placeholder="Статус">
              <el-option :value="0" label="Новая" />
              <el-option :value="1" label="Требуется уточнение" />
              <el-option :value="2" label="Назначена" />
              <el-option :value="3" label="В работе" />
              <el-option :value="4" label="Проверка" />
              <el-option :value="5" label="Готово" />
        </el-select>
      </el-form-item>

    </el-form>

    <div slot="footer">
      <el-button @click="submit" type="primary">Принять</el-button>
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
        status: [
          {
            required: true,
            message: 'Поле обязательно для заполнения'
          }
        ]
      }
    };
  },
  computed: {
    ...mapGetters('issue', ['isStatusModalVisible', 'issue'])
  },
  methods: {
    submit() {
      this.$refs['changeIssueStatusForm'].validate((valid) => {
        if (valid) {
          const data = Object.assign(this.form, {id: this.issue.id});
          this.$store.dispatch('issue/editIssue', data);
          this.form = {};
        }
      });
    },
    closeModal() {
      this.form = {};
      this.$store.commit('issue/SET_STATE', {isStatusModalVisible: false});
    }
  }
};
</script>

<style></style>