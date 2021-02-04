<template>
  <div id="app">
    <page-header></page-header>
        <main class="main">
            <router-view></router-view>
        </main>
    <issue-grid></issue-grid>
  </div>
</template>

<script>
import PageHeader from "@/components/layout/Header";
import IssueGrid from "@/components/issue/IssueGrid";

export default {
  name: 'App',
  components: {
    PageHeader,
    IssueGrid
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
