<template>
  <div id="app">
    <headerp></headerp>
  </div>
</template>

<script>
import Headerp from './components/layout/Header.vue'

export default {
  name: 'App',
  components: {
    Headerp
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
