import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
window.Vuex = Vuex;

let store = new Vuex.Store({
    modules: {
    }
});

export default store;