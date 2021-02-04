import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
window.Vuex = Vuex;

import auth from './modules/auth';
import issue from './modules/issue';

let store = new Vuex.Store({
    modules: {
        auth,
        issue
    }
});

export default store;