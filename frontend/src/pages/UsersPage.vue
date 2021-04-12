<template>
  <div v-if="meAdmin()">
    <user-form />
    <user-grid />
  </div>
  <div v-else>
    no
  </div>
</template>

<script>
import UserGrid from "@/components/user/UserGrid";
import UserForm from "@/components/user/UserForm";
import {meAdmin} from "@/utils/indentMe";

export default {
  components: {
    UserGrid,
    UserForm
  },
  methods: {
        meAdmin
    },
}
</script>

<style>
</style>
