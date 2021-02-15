import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
window.Vuex = Vuex;

import auth from './modules/auth';
import issue from './modules/issue';
import project from './modules/project';
import user from './modules/user';

let store = new Vuex.Store({
    modules: {
        auth,
        issue,
        project,
        user
    }
});

export default store;