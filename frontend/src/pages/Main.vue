<template>
    <div>
        <header-page></header-page>
        <main class="main">
            <router-view></router-view>
        </main>
    </div>
</template>

<script>
import HeaderPage from '@/components/layout/Header';
export default {
    components: { HeaderPage }
};
</script>

<style scoped>
* {
    box-sizing: border-box;
}
.main {
    margin-left: calc(20% + 10px);
    margin-right: 10px;
}
</style>