import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

export const routes = [
    {
        path: '/',
        component: require('../pages/Main.vue').default,
        name: 'main',
        children: [
            {
                path: '',
                component: require('../pages/IssuePage').default,
                name: 'issues'
            },
            {
                path: 'issues',
                component: require('../pages/IssuePage').default,
                name: 'issues'
            },
            {
                path: 'login',
                component: require('../pages/LoginPage').default,
                name: 'login'
            },
            {
                path: 'projects',
                component: require('../pages/ProjectPage').default,
                name: 'projects'
            },
            {
                path: 'user/:userId',
                component: require('../pages/UserPage').default,
                name: 'user'
            },
            {
                path: 'users',
                component: require('../pages/UsersPage').default,
                name: 'users'
            }
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
