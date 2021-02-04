import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
window.Vuex = Vuex;

import issue from './modules/issue';

let store = new Vuex.Store({
    modules: {
        issue
    }
});

export default store;