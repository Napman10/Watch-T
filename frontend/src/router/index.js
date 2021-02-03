import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

export const routes = [
    {
        path: '/',
        component: require('../pages/Main.vue').default,
        name: 'main',
        children: [
        ]
    }
];

export default new VueRouter({
    linkActiveClass: 'active',
    base: process.env.BASE_URL,
    routes: routes,
    scrollBehavior() {
        return { x: 0, y: 0 };
    },
    mode: process.env.isDev ? 'hash' : 'history'
});
