<template>
    <div>
        <page-header></page-header>
        <main class="main">
            <router-view></router-view>
        </main>
    </div>
</template>

<script>
import PageHeader from '@/components/layout/Header';
export default {
  components: { PageHeader }
}
</script>

<style scoped>
* {
    box-sizing: border-box;
}
.aside {
    width: 20%;
}
.main {
    margin-left: calc(20% + 10px);
    margin-right: 10px;
}
.left {
    float: left;
}
.clearfix {
    clear: both;
}
</style>