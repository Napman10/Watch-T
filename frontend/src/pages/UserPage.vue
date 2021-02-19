<template>
  <div>
    <el-avatar :size="150" :src="user.photo"></el-avatar>
    <h2>{{user.first_name}}</h2>
    <h2>{{user.last_name}}</h2>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  data() {
        return {
            userId: this.$route.params.userId
        };
    },
  computed: {
        ...mapGetters('user', ['user']),
    },
   mounted() {
        this.$store.dispatch('user/getUser', this.userId);
    }
}
</script>

<style scoped>

</style>