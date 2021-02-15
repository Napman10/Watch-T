import api from '@/api';
import {SET_STATE, setState} from '@/store/helpers';
import { showErrorNotify } from '@/utils';


export default {
    namespaced: true,
    state: {
        token: localStorage.getItem("token")
    },

    getters: {
        token: (state) => state.token,
    },

    mutations: {
        SET_STATE,
        setState,
    },

    actions: {
        async login({ commit }, params) {
            try {
                const result = await api.login(params);
                localStorage.setItem("token", result.auth_token );
                setState(commit, { token: result.auth_token });
                window.location.reload();
            } catch (e) {
                showErrorNotify("Неправильные данные входа");
            }
        },
        async logout({commit}, params){
            try {
                await api.logout(params);
                setState(commit, { token: null});
                localStorage.removeItem('token');
            } catch (e) {
                showErrorNotify(e);
            }
        }
    }
};