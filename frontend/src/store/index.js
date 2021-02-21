import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
window.Vuex = Vuex;

import auth from './modules/auth';
import comment from "./modules/comment";
import issue from './modules/issue';
import project from './modules/project';
import user from './modules/user';

let store = new Vuex.Store( {
    modules: {
        auth,
        comment,
        issue,
        project,
        user
    }
});

export default store;