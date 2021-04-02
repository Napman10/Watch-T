<template>
  <el-dialog title="Редактировать проект" :visible="isEditModalVisible" :before-close="closeModal">
    <el-form :model="form" ref="projectForm" :rules="rules">

      <el-form-item label="Короткое название" prop="short_name">
        <el-input v-model="form.short_name"></el-input>
      </el-form-item>

      <el-form-item label="Заголовок" prop="header">
        <el-input v-model="form.header"></el-input>
      </el-form-item>

      <el-form-item label="Описание" prop="description">
        <el-input v-model="form.description"></el-input>
      </el-form-item>

    </el-form>

    <div slot="footer">
      <el-button @click="closeModal">Закрыть</el-button>
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
        short_name: [
          {
            max: 16,
            message: 'Не больше 16 символов'
          }
        ],
        header: [
          {
            max: 65,
            message: 'Не больше 65 символов'
          }
        ],
        description: [
          {
            max: 255,
            message: 'Не больше 255 символов'
          }
        ],
      }
    };
  },
  computed: {
    ...mapGetters('project', ['isEditModalVisible', 'project']),
  },
  methods: {
    submit() {
      this.$refs['projectForm'].validate((valid) => {
        if (valid) {
          const payload = Object.assign(this.form, {id: this.project.id});
          this.$store.dispatch('project/editProject', payload);
          this.form = {};
        }
      });
    },
    closeModal() {
      this.$store.commit('project/SET_STATE', { isEditModalVisible: false });
    },
    clearForm(){
      this.form = {}
    }
  }
};
</script>

<style></style>