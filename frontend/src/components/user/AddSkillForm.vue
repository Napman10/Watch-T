<template>
  <el-dialog title="Добавить навык" :visible="isAddSkillvisible" :before-close="closeModal">
    <el-form :model="form" ref="addSkillForm" :rules="rules">

      <el-form-item label="Навык" prop="skill">
        <el-select v-model="form.skill">
          <el-option
              v-for="item in skills"
              :key="item.typo"
              :value="['Frontend', 'Backend', 'DevOps', 'Mobile', 'DB', 'SysAdmin'][item.typo]">
          </el-option>
        </el-select>
      </el-form-item>

    </el-form>

    <div slot="footer">
      <el-button @click="submit" type="primary">Добавить</el-button>
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
        skill: [
          {
            required: true,
            message: 'Поле обязательно для заполнения'
          }
        ]
      }
    };
  },
  computed: {
    ...mapGetters('user', ['isAddSkillvisible', 'user', 'skills']),
  },
  methods: {
    submit() {
      this.$refs['addSkillForm'].validate((valid) => {
        if (valid) {
          const payload = Object.assign(this.form, {id: this.user.id});
          this.$store.dispatch('user/editUser', payload);
          this.form = {};
        }
      });
    },
    closeModal() {
      this.form = {};
      this.$store.commit('user/SET_STATE', {isAddSkillvisible: false});
    }
  }
};
</script>

<style></style>